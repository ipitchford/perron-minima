#!/usr/bin/env python3
"""Independent symbolic and rational-interval reconstruction; imports no submitted algebra routines."""
import itertools,json,sys
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
def check(v,msg):
    if not v:raise ValueError(msg)

def orient(order):
    r={v:i for i,v in enumerate(order)};n=len(order)
    return sp.Matrix(n,n,lambda i,j:0 if i==j else 1 if r[i]<r[j] else -1)

def add(I,J):return I[0]+J[0],I[1]+J[1]
def mult(I,J):
    p=[x*y for x in I for y in J];return min(p),max(p)
def peval(p,var,I):
    v=(sp.Rational(0),sp.Rational(0))
    for c in sp.Poly(p,var).all_coeffs():v=add(mult(v,I),(c,c))
    return v

def main():
    ref=json.loads((ROOT/'reference_extensions.json').read_text())
    t,l=sp.symbols('t l'); b12,b13,b14,b23,b24,b34=sp.symbols('b12 b13 b14 b23 b24 b34');g=sp.symbols('g0:4')
    weights=sp.Matrix([[0,b12,b13,b14],[b12,0,b23,b24],[b13,b23,0,b34],[b14,b24,b34,0]])
    def matrix(order):
        S=orient(order);return sp.Matrix(4,4,lambda i,j:g[i] if i==j else weights[i,j]*(1+t*S[i,j]))
    P=matrix((0,1,2,3)).charpoly(l).as_expr();Q=matrix((0,2,1,3)).charpoly(l).as_expr()
    target=ref['four_cycle_coefficient']*t*t*(1-t*t)*b14*b23*(b12*b34-b13*b24)
    check(sp.expand(P-Q-target)==0,'symbolic tetrad characteristic difference')
    # All coefficients other than the constant are identical for every transitive order.
    base=sp.Poly(P,l).all_coeffs()[:-1]
    for order in itertools.permutations(range(4)):
        other=sp.Poly(matrix(order).charpoly(l).as_expr(),l).all_coeffs()[:-1]
        check(all(sp.expand(a-b)==0 for a,b in zip(base,other)),'four-point nonconstant coefficients')
    print('symbolic tetrads finished',file=sys.stderr,flush=True)
    # Exact local-minimum signs at every transitive vertex of the rational perturbation.
    eps=sp.Rational(ref['fragility_epsilon']);tv=sp.Rational(ref['fragility_t']);fields=[];margin=None
    for order in itertools.permutations(range(4)):
        S=orient(order);A=sp.Matrix(4,4,lambda i,j:0 if i==j else (1+eps if {i,j}=={0,1} else 1)*(1+tv*S[i,j]))
        pol=A.charpoly(l).as_expr();lo=sp.Rational(2);hi=sp.Rational(3)
        check(pol.subs(l,lo)<0<pol.subs(l,hi),'root bracket signs')
        cs=[x for x in sp.Poly(pol,l).all_coeffs() if x]
        check(sum(int(bool(a*b<0)) for a,b in zip(cs,cs[1:]))==1,'Descartes unique positive root')
        for _ in range(70):
            mid=(lo+hi)/2
            if pol.subs(l,mid)>0:hi=mid
            else:lo=mid
        J=(l*sp.eye(4)-A).adjugate();x=J*sp.ones(4,1);y=J.T*sp.ones(4,1)
        check(all(peval(a,l,(lo,hi))[0]>0 for a in list(x)+list(y)),'positive adjugate vectors')
        d=y.dot(x);dl,dh=peval(d,l,(lo,hi));check(dl>0,'positive Perron derivative denominator')
        slopes=[]
        for i,j in itertools.combinations(range(4),2):
            pair=1+eps if {i,j}=={0,1} else sp.Rational(1)
            numerator=sp.expand(tv*pair*S[i,j]*(y[i]*x[j]-y[j]*x[i]))
            nl,nh=peval(numerator,l,(lo,hi));check(nh<0,'strict signed derivative at box vertex')
            # Each true signed derivative is at most nh/dh < 0.
            lower_margin=-nh/dh;slopes.append(str(lower_margin))
            margin=lower_margin if margin is None else min(margin,lower_margin)
        fields.append({'order':list(order),'positive_root_interval':[str(lo),str(hi)],'lower_bounds_on_inward_coordinate_derivatives':slopes})
    print('local signs finished',file=sys.stderr,flush=True)
    # Differentiate one arbitrary summand, avoiding a gratuitously huge common denominator.
    m,gam=sp.symbols('m gamma');z=l-gam+m;den=z*z-t*t*m*m
    F=sp.atanh(t*m/z)
    check(sp.factor(sp.diff(F,l)+t*m/den)==0,'implicit lambda derivative summand')
    check(sp.factor(sp.diff(F,gam)-t*m/den)==0,'diagonal sensitivity summand')
    check(sp.factor(sp.diff(F,m)-t*(l-gam)/den)==0,'mass sensitivity summand')
    check(sp.factor(sp.diff(F,t)-m*z/den)==0,'coupling sensitivity summand')
    check(sp.simplify(sp.diff(sp.atanh(t),t)-1/(1-t*t))==0,'coupling target derivative')
    # Exact perturbed polynomial separation as a function of epsilon and t.
    e=sp.symbols('e')
    substitution={b12:1+e,b13:1,b14:1,b23:1,b24:1,b34:1,**{x:0 for x in g}}
    check(sp.factor((P-Q).subs(substitution)+4*e*t*t*(1-t*t))==0,'arbitrary-small perturbation separation')
    check(margin>sp.Rational(6927,100000),'published strict-gradient margin')
    records={'status':'PASS','strict_local_minimum_vertices':len(fields),'signed_coordinate_derivatives':6*len(fields),
      'minimum_certified_inward_derivative_lower_float':float(margin),'cases':fields,
      'scope':'exact interval signs at epsilon=1/100; arbitrary-small persistence is an analytic continuity argument'}
    (ROOT/'results'/'local_minima_intervals.json').write_text(json.dumps(records,indent=2,sort_keys=True)+'\n')
    summary={'status':'PASS','symbolic_four_point_orders':24,'universal_four_point_identity':True,'strict_local_vertices':24,'strict_coordinate_derivatives':144,'scalar_derivative_identities':5,'scope':'symbolic identities and exact interval certificates, not proof-assistant verification'}
    (ROOT/'results'/'new_symbolic.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n');print(json.dumps(summary,sort_keys=True))
if __name__=='__main__':main()
