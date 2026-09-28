#!/usr/bin/env python3
"""Content integrity and bounded proof-evidence replay. No assertion-based gates."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys,os,tempfile
ROOT=Path(__file__).resolve().parent

def manifest():
    records={}
    for line in (ROOT/'MANIFEST.sha256').read_text().splitlines():
        digest,name=line.split('  ',1);p=(ROOT/name).resolve()
        if not p.is_relative_to(ROOT.resolve()) or not p.is_file():raise ValueError('invalid manifest path: '+name)
        current=hashlib.sha256(p.read_bytes()).hexdigest()
        if current!=digest:raise ValueError('manifest mismatch: '+name)
        records[name]=digest
    return records

def run(args,out):
    before=manifest();env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1',EP_REPLAY_LOG_DIR=str(out))
    jobs=[['verify_public_reference.py']]
    if not args.smoke:
        jobs += [['verify_extensions.py'],['verify_new_symbolic.py'],['verify_manuscript.py'],['test_numerical_contract.py']]
        jobs += [['negative_controls.py','--part',x] for x in ['none','cycle','polynomial','robust']]
        if args.full:jobs += [['replay_sources.py','reviewed'],['replay_sources.py','referee']]
    rec=[]
    flags=['-OO'] if sys.flags.optimize==2 else ['-O'] if sys.flags.optimize==1 else []
    for j,job in enumerate(jobs):
        print('Running '+ ' '.join(job),file=sys.stderr,flush=True)
        p=subprocess.run([sys.executable,*flags,'code/'+job[0],*job[1:]],cwd=ROOT,env=env,capture_output=True,text=True,timeout=600)
        stem=str(j+1)+'_'+job[0].replace('.py','')
        (out/(stem+'.stdout')).write_text(p.stdout);(out/(stem+'.stderr')).write_text(p.stderr)
        if p.returncode:raise RuntimeError('job failed: '+' '.join(job)+'\n'+p.stderr+p.stdout)
        rec.append({'job':job,'returncode':0,'stdout_sha256':hashlib.sha256(p.stdout.encode()).hexdigest()})
    after=manifest()
    if before!=after:raise ValueError('integrity changed')
    result={'status':'PASS','mode':'smoke' if args.smoke else 'full' if args.full else 'default','manifested_files_before':len(before),'manifested_files_after':len(after),'jobs':rec,'scope':'deterministic identity/finite checks and scoped numerical reruns; not proof-assistant verification'}
    (out/'REPLAY_REPORT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps(result,sort_keys=True))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--full',action='store_true');ap.add_argument('--smoke',action='store_true');ap.add_argument('--out',type=Path);a=ap.parse_args()
    if a.out:
        out=a.out.resolve()
        if out.is_relative_to(ROOT.resolve()):raise ValueError('--out must be outside bundle')
        out.mkdir(parents=True,exist_ok=True);run(a,out)
    else:
        with tempfile.TemporaryDirectory(prefix='perron-replay-') as td:run(a,Path(td))
if __name__=='__main__':main()
