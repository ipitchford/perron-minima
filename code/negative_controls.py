#!/usr/bin/env python3
"""Proof-check corruption tests, independent of integrity checking."""
from pathlib import Path
import argparse,tempfile,shutil,json,subprocess,os,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]
def main():
    a=argparse.ArgumentParser();a.add_argument('--part',required=True,choices=['none','cycle','polynomial','robust']);args=a.parse_args()
    tests=[]
    with tempfile.TemporaryDirectory() as td:
        b=Path(td);(b/'code').mkdir()
        for n in ['core.py','verify_public_reference.py']:shutil.copy2(ROOT/'code'/n,b/'code'/n)
        shutil.copy2(ROOT/'replay.py',b/'replay.py')
        data=json.loads((ROOT/'reference_extensions.json').read_text())
        if args.part=='cycle':data['four_cycle_coefficient']=4
        if args.part=='polynomial':data['fragility_high_polynomial'][-1]='-1'
        if args.part=='robust':data['robust_Phi_at_one']='-1'
        (b/'reference_extensions.json').write_text(json.dumps(data))
        (b/'MANIFEST.sha256').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(b).as_posix()+'\n' for p in sorted(b.rglob('*')) if p.is_file()))
        for name,flags,opt in [('ordinary',[],None),('-O',['-O'],None),('-OO',['-OO'],None),('env1',[],'1'),('env2',[],'2')]:
            env=os.environ.copy();env.pop('PYTHONOPTIMIZE',None);env['PYTHONDONTWRITEBYTECODE']='1'
            if opt is not None:env['PYTHONOPTIMIZE']=opt
            for wrapper in [False,True]:
                command=[sys.executable,*flags,*(['replay.py','--smoke'] if wrapper else ['code/verify_public_reference.py'])]
                p=subprocess.run(command,cwd=b,env=env,capture_output=True,text=True,timeout=30)
                success=p.returncode==0
                if success!=(args.part=='none'):raise ValueError('unsafe acceptance in '+str((args.part,name,wrapper)))
                tests.append({'case':args.part,'mode':name,'wrapper':wrapper,'accepted':success})
    out={'status':'PASS','valid_acceptances':sum(t['accepted'] for t in tests),'invalid_rejections':sum(not t['accepted'] for t in tests),'cases':tests,'scope':'Three explicit mathematical corruptions, not exhaustive software validation'}
    (ROOT/'results'/('negative_'+args.part+'.json')).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:out[k] for k in ['status','valid_acceptances','invalid_rejections']},sort_keys=True))
if __name__=='__main__':main()
