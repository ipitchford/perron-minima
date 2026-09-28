"""Exact interfaces for robust factorised Perron optimisation.

Rational arithmetic only. No assertion is used for an acceptance condition.
The optimisation theorem concerns constant (not arbitrarily switching) matrices.
"""
from fractions import Fraction as F
from itertools import combinations
from core import require, minimum_bracket, poly_minimum

def parse_rational(x):
    require(not isinstance(x,bool) and isinstance(x,(str,int)), 'use integer or rational string, not a JSON float')
    return F(x)

def parse_vector(xs):
    require(isinstance(xs,list), 'expected a list')
    return [parse_rational(x) for x in xs]

def factorisation(b):
    n=len(b)
    require(n>=3 and all(len(r)==n for r in b),'requires square order at least three')
    b=[[F(x) for x in r] for r in b]
    require(all(b[i][j]==b[j][i]>0 for i in range(n) for j in range(i+1,n)), 'positive symmetric off-diagonal weights required')
    m0=b[0][1]*b[0][2]/b[1][2]
    m=[m0]+[b[0][i]**2/m0 for i in range(1,n)]
    failures=[]
    for i,j,k,l in combinations(range(n),4):
        terms=[b[i][j]*b[k][l], b[i][k]*b[j][l],b[i][l]*b[j][k]]
        if terms[0]!=terms[1] or terms[0]!=terms[2]:
            failures.append({'indices':[i,j,k,l],'products':list(map(str,terms))})
    exact=all(b[i][j]**2==m[i]*m[j] for i in range(n) for j in range(i+1,n))
    require(exact == (len(failures)==0), 'tetrad reconstruction mismatch')
    return {'factorised':exact,'candidate_squared_weights':list(map(str,m)), 'failed_tetrads':failures}

def robust_box(mlo,mhi,glo,ghi,tlo,thi,bits=90):
    n=len(mlo)
    require(n>=2 and all(len(v)==n for v in [mhi,glo,ghi]),'dimension mismatch')
    require(all(0<a<=b for a,b in zip(mlo,mhi)),'invalid positive mass intervals')
    require(all(0<=a<=b for a,b in zip(glo,ghi)),'invalid diagonal intervals')
    require(0<tlo<=thi<1,'requires 0<t_lower<=t_upper<1')
    lo,hi=minimum_bracket(mhi,ghi,tlo,bits)
    phi=poly_minimum(F(1),mhi,ghi,tlo)
    stable=max(ghi)<1 and phi>0
    return {'n':n,'scope':'a single fixed but unknown matrix from the parameter box; not arbitrary switching',
      'worst_corner':{'m':list(map(str,mhi)),'gamma':list(map(str,ghi)),'t':str(tlo)},
      'optimal_worst_case_perron_interval':[str(lo),str(hi)], 'Phi_at_one':str(phi),
      'robust_strict_stability':stable,'optimal_orders':'every fixed transitive order',
      'approximate_interval_for_reading':[float(lo),float(hi)]}

def approximate_factorisation(b,w):
    n=len(w)
    require(n>=2 and all(F(x)>0 for x in w),'positive weights required')
    require(len(b)==n and all(len(row)==n for row in b),'dimension mismatch')
    ratios=[]
    for i in range(n):
        for j in range(i+1,n):
            require(b[i][j]==b[j][i]>0,'positive symmetric weights required')
            z=F(b[i][j])/(F(w[i])*F(w[j]));ratios.extend([z,1/z])
    kappa=max([F(1),*ratios])
    return {'kappa':str(kappa),'guaranteed_approximation_factor':str(kappa*kappa),
      'scope':'any transitive orientation, fixed nonnegative diagonal and 0<t<1; factor not claimed sharp'}
