#!/usr/bin/env python3
"""Fast non-vacuous release gates, including publication-domain negative tests."""
import json,itertools
from pathlib import Path
from fractions import Fraction as F
from core import require,det,recover,BL,poly_minimum,Q
ROOT=Path(__file__).resolve().parents[1]
def orient(order):
    pos={v:i for i,v in enumerate(order)}
    return [[F(0 if i==j else 1 if pos[i]<pos[j] else -1) for j in range(4)] for i in range(4)]
def matrix(b,t,order):
    S=orient(order);return [[F(0) if i==j else b[i][j]*(1+t*S[i][j]) for j in range(4)] for i in range(4)]
def evalpoly(cs,x):
    a=F(0)
    for c in cs:a=a*x+F(c)
    return a

def main():
    r=json.loads((ROOT/'reference_extensions.json').read_text());e=F(r['fragility_epsilon']);t=F(r['fragility_t'])
    b=[[F(0) if i==j else 1+e if {i,j}=={0,1} else F(1) for j in range(4)] for i in range(4)]
    A=matrix(b,t,[0,1,2,3]);B=matrix(b,t,[0,2,1,3])
    require(det(A)-det(B)==r['four_cycle_coefficient']*e*t*t*(1-t*t),'incorrect four-cycle coefficient')
    for M,key in [(A,'fragility_high_polynomial'),(B,'fragility_low_polynomial')]:
        for x in [F(0),F(1),F(2),F(3),F(4)]:
            require(det([[x*F(i==j)-M[i][j] for j in range(4)] for i in range(4)])==evalpoly(r[key],x),'incorrect witness characteristic polynomial')
    v=poly_minimum(F(1),list(map(F,['1/3','2/3','1'])),list(map(F,['1/20','1/25','1/30'])),F(3,4))
    require(v==F(r['robust_Phi_at_one'])>0,'incorrect robust feasibility value')
    invalid=[(BL(2),F(1,2)),([[F(0)]*4 for _ in range(4)],F(1,10)),(BL(4),F(1,3))]
    for S,u in invalid:
        try:recover(S,u)
        except ValueError:pass
        else:raise ValueError('recovery domain gate accepted invalid input')
    print(json.dumps({'status':'PASS','exact_determinant_checks':11,'robust_sign_checks':1,'domain_rejections':3},sort_keys=True))
if __name__=='__main__':main()
