#!/usr/bin/env python3
"""Exact new checks, reconstructed by determinant expansion and rational arithmetic."""
import json,itertools,random,math
from pathlib import Path
from fractions import Fraction as F
from core import require,det,Q,BL,tournament,recover,permute,minimum_bracket,poly_minimum,weighted_matrix,perron_ratios,constants,resolvent,mv,switch
from extensions import factorisation,robust_box,approximate_factorisation
ROOT=Path(__file__).resolve().parents[1]
def write(n,x):
    p=ROOT/'results'/n;p.write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
def sign(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def charpoly(A):
    n=len(A);ans=[F(0)]*(n+1)
    for p in itertools.permutations(range(n)):
        prod=[F(sign(p))]
        for i,j in enumerate(p):prod=mul(prod,[-A[i][j],F(1)] if i==j else [-A[i][j]])
        for i,x in enumerate(prod):ans[i]+=x
    return list(reversed(ans))

def evaluate(cs,x):
    z=F(0)
    for c in cs:z=z*x+c
    return z

def bracket(cs,bits=80):
    lo=F(2);hi=F(3)
    require(evaluate(cs,lo)<0<evaluate(cs,hi),'witness root endpoints')
    require(sum(a*b<0 for a,b in zip([c for c in cs if c],[c for c in cs if c][1:]))==1,'witness unique positive root')
    for _ in range(bits):
        mid=(lo+hi)/2
        if evaluate(cs,mid)>0:hi=mid
        else:lo=mid
    return lo,hi

def ordermatrix(p):
    n=len(p);rank={j:i for i,j in enumerate(p)}
    return [[F(0 if i==j else 1 if rank[i]<rank[j] else -1) for j in range(n)] for i in range(n)]
def pairmatrix(b,g,t,p):
    S=ordermatrix(p);n=len(p)
    return [[g[i] if i==j else b[i][j]*(1+t*S[i][j]) for j in range(n)] for i in range(n)]

def main():
    ref=json.loads((ROOT/'reference_extensions.json').read_text());r=random.Random(928021)
    count=0
    for _ in range(24):
        b=[[F(0)]*4 for _ in range(4)]
        for i in range(4):
            for j in range(i+1,4):b[i][j]=b[j][i]=F(r.randrange(1,10),r.randrange(1,8))
        g=[F(r.randrange(0,6),5) for _ in range(4)];t=F(r.randrange(1,9),10)
        for p in itertools.permutations(range(4)):
            bp=[[b[i][j] for j in p] for i in p];gp=[g[i] for i in p]
            A=pairmatrix(bp,gp,t,(0,1,2,3));B=pairmatrix(bp,gp,t,(0,2,1,3))
            target=F(ref['four_cycle_coefficient'])*t*t*(1-t*t)*bp[0][3]*bp[1][2]*(bp[0][1]*bp[2][3]-bp[0][2]*bp[1][3])
            require(det(A)-det(B)==target,'four-cycle/tetrad identity');count+=1
    factcount=0
    for n in range(3,10):
        for _ in range(8):
            w=[F(r.randrange(1,11),r.randrange(1,9)) for i in range(n)]
            b=[[F(0) if i==j else w[i]*w[j] for j in range(n)] for i in range(n)]
            out=factorisation(b);require(out['factorised'],'factor reconstruction');require(list(map(F,out['candidate_squared_weights']))==[x*x for x in w],'squared weights')
            if n>=4:
                b[0][1]*=F(101,100);b[1][0]=b[0][1];require(not factorisation(b)['factorised'],'nonfactorisation detection')
            factcount+=1
    eps=F(ref['fragility_epsilon']);t=F(ref['fragility_t']);b=[[F(0) if i==j else 1+eps if {i,j}=={0,1} else F(1) for j in range(4)] for i in range(4)]
    polys={}; records=[]
    for p in itertools.permutations(range(4)):
        A=pairmatrix(b,[F(0)]*4,t,p);cs=charpoly(A)
        key='high' if p in [(0,1,2,3)] or cs==list(map(F,ref['fragility_high_polynomial'])) else 'low'
        require(cs==list(map(F,ref['fragility_'+key+'_polynomial'])),'fragility polynomial')
        polys.setdefault(key,{'coefficients':list(map(str,cs)),'count':0,'root_interval':list(map(str,bracket(cs)))});polys[key]['count']+=1
        records.append({'order':list(p),'class':key})
    require(F(polys['low']['root_interval'][1])<F(polys['high']['root_interval'][0]),'non-global spectral separation')
    box=json.loads((ROOT/'examples/robust_box.json').read_text())
    vectors=[[F(x) for x in box[k]] for k in ['m_lower','m_upper','gamma_lower','gamma_upper']]
    rob=robust_box(*vectors,F(box['t_lower']),F(box['t_upper']))
    require(rob['Phi_at_one']==ref['robust_Phi_at_one'] and rob['robust_strict_stability'],'robust reference')
    lo,hi=map(F,rob['optimal_worst_case_perron_interval']);corners=0
    for bits in itertools.product([0,1],repeat=7):
        m=[vectors[bits[i]][i] for i in range(3)];g=[vectors[2+bits[i+3]][i] for i in range(3)];tt=F(box['t_upper'] if bits[6] else box['t_lower'])
        l,h=minimum_bracket(m,g,tt,80)
        require(l<=hi,'box optimum below worst bound')
        # A positive-vector row-ratio enclosure checks actual transitive matrices.
        A=weighted_matrix(m,g,tt,Q(3));ra,rb=perron_ratios(A)
        require(ra<=h and rb>=l,'root versus independent positive test-vector interval')
        corners+=1
    approx=approximate_factorisation(b,[F(1)]*4)
    require(approx['kappa']=='101/100' and approx['guaranteed_approximation_factor']=='10201/10000','approximation certificate')
    S=tournament(6,int(ref['recovery_bits']));u=F(ref['recovery_u']);receipt=recover(S,u)
    mind=99;near=None
    for p in itertools.permutations(range(6)):
        B=permute(BL(6),p);dist=sum(S[i][j]!=B[i][j] for i in range(6) for j in range(i+1,6))
        if dist<mind:mind=dist;near=p
    require(receipt['edits_to_returned_BL']==ref['recovery_returned_distance'] and mind==ref['recovery_nearest_distance'],'non-nearest example')
    lam=F(receipt['lambda_BL']);tt=F(receipt['t']);A=[[1+tt*S[i][j] for j in range(6)] for i in range(6)];lb,ub=perron_ratios(A)
    require(lam-ub>=F(receipt['certified_deficit_lower']),'exact instance deficit')
    receipt.update(nearest_distance=mind,nearest_permutation=list(near),spectral_deficit_interval=[str(lam-ub),str(lam-lb)],uniform_bound_for_returned_distance=str(F(receipt['edit_coefficient'])*receipt['edits_to_returned_BL']),count_bound=receipt['backedges']+receipt['stable_swaps'])
    receipt['instance_edit_coefficient']=str(F(receipt['certified_deficit_lower'])/receipt['count_bound'])
    receipt['spectral_upper_to_instance_distance_floor']=int((lam-lb)/F(receipt['instance_edit_coefficient']))
    write('fragility_exact.json',{'polynomials':polys,'all_transitive_orders':records,'scope':'root separation exact; local-minimum gradient signs are independently checked by verify_new_symbolic.py'})
    write('robust_box_receipt.json',rob);write('recovery_example.json',receipt)
    summary={'status':'PASS','four_cycle_identities':count,'factorisation_cases':factcount,'fragility_transitive_polynomials':24,'robust_corners':corners,'nearest_recovery_permutations':720,'scope':'exact finite identities and examples; not a formal proof of the universal statements'}
    write('extensions_exact.json',summary);print(json.dumps(summary,sort_keys=True))
if __name__=='__main__':main()
