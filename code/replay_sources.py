#!/usr/bin/env python3
"""Re-run unchanged reviewed and referee sources in disposable workspaces."""
from pathlib import Path
import argparse,zipfile,tempfile,subprocess,os,sys,json,hashlib,math
from numerical_contract import compare_numerical
ROOT=Path(__file__).resolve().parents[1]
def check(v,m):
    if not v:raise ValueError(m)
def safe_extract(z,root):
    root=root.resolve()
    for info in z.infolist():
        target=(root/info.filename).resolve()
        check(target.is_relative_to(root),'unsafe archive path')
    z.extractall(root)
def main():
    p=argparse.ArgumentParser();p.add_argument('source',choices=['reviewed','referee']);a=p.parse_args()
    logroot=Path(os.environ.get('EP_REPLAY_LOG_DIR',str(ROOT/'logs')));logroot.mkdir(parents=True,exist_ok=True)
    env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
    with tempfile.TemporaryDirectory() as td:
        b=Path(td)
        name='resolvent_extensions_v0_1.zip' if a.source=='reviewed' else 'referee_checks_2026-09-28.zip'
        archive=ROOT/'provenance'/name
        with zipfile.ZipFile(archive) as z:safe_extract(z,b)
        if a.source=='reviewed':
            home=b/'resolvent_extensions_v0_1';before={p.relative_to(home).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (home/'results').glob('*.json')}
            flags=['-OO'] if sys.flags.optimize==2 else ['-O'] if sys.flags.optimize==1 else []
            run=subprocess.run([sys.executable,*flags,'replay.py'],cwd=home,env=env,capture_output=True,text=True,timeout=420)
            (logroot/'reviewed_full.stdout').write_text(run.stdout);(logroot/'reviewed_full.stderr').write_text(run.stderr)
            check(run.returncode==0,'reviewed replay failed')
            after={p.relative_to(home).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (home/'results').glob('*.json')}
            check(before==after,'reviewed deterministic result changed')
            rr=json.loads((home/'REPLAY_REPORT.json').read_text())
            original=json.loads((home/'results/numerical.json').read_text())
            numerical=subprocess.run([sys.executable,*flags,'code/numerical_checks.py'],cwd=home,env=env,capture_output=True,text=True,timeout=120)
            (logroot/'historical_numerical.stdout').write_text(numerical.stdout)
            (logroot/'historical_numerical.stderr').write_text(numerical.stderr)
            check(numerical.returncode==0,'historical numerical semantic checks failed')
            current=json.loads((home/'results/numerical.json').read_text())
            comparison=compare_numerical(original,current)
            (logroot/'historical_numerical_current.json').write_text(json.dumps(current,indent=2,sort_keys=True)+'\n')
            (logroot/'historical_numerical_comparison.json').write_text(json.dumps(comparison,indent=2,sort_keys=True)+'\n')
            result={'status':'PASS','source_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'exact_jobs':len(rr['jobs']),'numerical_jobs':1,'manifested_files':rr['manifested_files_before'],'exact_results_identical':True,'numerical_comparison':comparison,'source_scope':'Historical exact/default replay unchanged; numerical corroboration rerun separately with explicit tolerance. Nested earlier archives retained, not recursively replayed.'}
        else:
            home=b/'resolvent_referee_checks';before=json.loads((home/'independent_checks.json').read_text())
            flags=['-OO'] if sys.flags.optimize==2 else ['-O'] if sys.flags.optimize==1 else []
            run=subprocess.run([sys.executable,*flags,'independent_checks.py'],cwd=home,env=env,capture_output=True,text=True,timeout=420)
            (logroot/'referee.stdout').write_text(run.stdout);(logroot/'referee.stderr').write_text(run.stderr)
            check(run.returncode==0,'referee replay failed')
            now=json.loads((home/'independent_checks.json').read_text());(logroot/'referee_raw.json').write_text(json.dumps(now,indent=2,sort_keys=True)+'\n')
            elapsed=now.pop('elapsed_seconds');before.pop('elapsed_seconds')
            check(all(row['bound_violations']==row['repair_violations']==0 for row in now['all_six_vertex_tournaments']),'referee tournament violation')
            check(all(row['violations']==0 for row in now['continuous_box_grids']),'referee grid violation')
            check(now['exact_weighted_cospectrality']['status']=='PASS','referee exact polynomial check')
            # Retain any numerical differences rather than silently rewriting the referee record.
            changes=[]
            def compare(x,y,path=''):
                if isinstance(x,dict):
                    check(x.keys()==y.keys(),'referee schema changed')
                    for k in x:compare(x[k],y[k],path+'/'+k)
                elif isinstance(x,list):
                    check(len(x)==len(y),'referee array length')
                    for i,(u,v) in enumerate(zip(x,y)):compare(u,v,path+'/'+str(i))
                elif x!=y:
                    changes.append({'path':path,'original':x,'current':y})
            compare(before,now)
            (logroot/'referee_current.json').write_text(json.dumps(now,indent=2,sort_keys=True)+'\n')
            result={'status':'PASS','source_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'numerical_changes_excluding_elapsed':changes,'only_excluded_field':'elapsed_seconds; raw value retained in external replay log','tournament_parameter_cases':sum(x['tournaments'] for x in now['all_six_vertex_tournaments']),'repair_parameter_cases':sum(x['repair_cases'] for x in now['all_six_vertex_tournaments']),'exact_transitive_orders':now['exact_weighted_cospectrality']['orders_checked'],'box_grid_points':sum(x['points'] for x in now['continuous_box_grids'])}
        (logroot/('source_'+a.source+'.json')).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
