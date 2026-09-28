"""Portability contract for historical corroboration, not theorem validation.

The unchanged historical code enforces its own -1e-8 theorem sanity bound and
1e-59 high-precision root agreement. Here input identity remains exact, while
objective agreement permits 1e-10 relative/absolute error. Every changed field
is retained; no historical observation is overwritten.
"""
import math

def require(value,message):
    if not value:raise ValueError(message)

def compare_numerical(original,current):
    changes=[]
    def walk(a,b,p=''):
        require(type(a) is type(b),'type changed at '+p)
        if isinstance(a,dict):
            require(a.keys()==b.keys(),'schema changed at '+p)
            for k in a:walk(a[k],b[k],p+'/'+k)
        elif isinstance(a,list):
            require(len(a)==len(b),'length changed at '+p)
            for i,(x,y) in enumerate(zip(a,b)):walk(x,y,p+'/'+str(i))
        elif a!=b:changes.append({'path':p,'original':a,'current':b})
    walk(original,current)
    for k in ['seed','optimisation_attempts','successes','status','scope']:
        require(original[k]==current[k],'summary mismatch: '+k)
    require(len(current['trials'])==30 and current['successes']==30,'missing or failed optimisation')
    for a,b in zip(original['trials'],current['trials']):
        for k in ['n','m','gamma','t','initial','success']:
            require(a[k]==b[k],'changed numerical input/status: '+k)
        for k in ['objective','reference_root','deficit_above_minimum']:
            require(math.isfinite(b[k]),'nonfinite '+k)
            require(math.isclose(a[k],b[k],rel_tol=1e-10,abs_tol=1e-10),'numerical disagreement: '+k)
        require(all(math.isfinite(v) and -1<=v<=1 for v in b['result']),'invalid optimiser point')
        require(b['deficit_above_minimum']>=-1e-8,'negative theorem sanity gap')
    require([r['n'] for r in original['high_precision']]==[r['n'] for r in current['high_precision']],'high precision domain')
    return {'status':'PASS','seed_and_inputs_identical':True,'identical_trials':sum(a==b for a,b in zip(original['trials'],current['trials'])),'objective_rel_tol':1e-10,'objective_abs_tol':1e-10,'changes':changes,'scope':'Numerical corroboration only; historical exact results are checked separately.'}
