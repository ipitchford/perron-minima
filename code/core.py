"""Exact constructive resolvent calculations. No assertions authorise acceptance."""
from fractions import Fraction as F
from math import gcd, lcm

def require(p, message):
    if not p:
        raise ValueError(message)

def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def tr(A): return list(map(list,zip(*A)))
def mv(A,x): return [sum((a*b for a,b in zip(row,x)),F(0)) for row in A]
def mm(A,B): return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))
def inv(A):
    n=len(A); E=eye(n); B=[list(map(F,row))+E[i] for i,row in enumerate(A)]
    for j in range(n):
        p=next((i for i in range(j,n) if B[i][j]),None)
        require(p is not None,'singular matrix'); B[j],B[p]=B[p],B[j]
        v=B[j][j]; B[j]=[x/v for x in B[j]]
        for i in range(n):
            if i!=j:
                v=B[i][j]; B[i]=[x-v*y for x,y in zip(B[i],B[j])]
    return [row[n:] for row in B]

def det(A):
    B=[list(map(F,r)) for r in A]; n=len(B); ans=F(1)
    for j in range(n):
        k=next((i for i in range(j,n) if B[i][j]),None)
        if k is None:return F(0)
        if k!=j:B[k],B[j]=B[j],B[k];ans=-ans
        v=B[j][j];ans*=v
        for i in range(j+1,n):
            s=B[i][j]/v
            for k in range(j+1,n):B[i][k]-=s*B[j][k]
    return ans

def tournament(n,bits):
    A=[[F(0)]*n for _ in range(n)]; k=0
    for i in range(n):
        for j in range(i+1,n):
            v=F(1 if bits>>k&1 else -1);A[i][j]=v;A[j][i]=-v;k+=1
    return A

def Q(n):return [[F(0 if i==j else 1 if i<j else -1) for j in range(n)] for i in range(n)]
def switch(S,r):return [[r[i]*S[i][j]*r[j] for j in range(len(S))] for i in range(len(S))]
def BL(n):return switch(Q(n),[F((-1)**(i+1)) for i in range(n)])
def permute(S,p):return [[S[i][j] for j in p] for i in p]
def resolvent(S,u):return inv([[F(i==j)-u*S[i][j] for j in range(len(S))] for i in range(len(S))])
def validate(S,u):
    n=len(S);require(n>=2 and F(0)<u<F(1,n-1),'inadmissible u')
    require(all(len(r)==n for r in S),'nonsquare')
    require(all(S[i][j]==-S[j][i] and abs(S[i][j])<=1 for i in range(n) for j in range(n)),'not a skew box matrix')

def constants(n,u):
    q=(1-u)/(1+u); eta=1-(n-1)*u
    Fmin=(1-q**n)/(u*(1+q**n))
    a=4*u*u*eta*q**(n-2)/((1+u)**3*(1+q**n))
    B=(1+n*u)/(1+u)
    G=4*u*u*(F(3)/(1+u*u*(n-1)**2)-1)/B
    C=a*u*u/B
    return Fmin,a,B,G,C

def order_certificate(S,u):
    validate(S,u);n=len(S);x=mv(resolvent(S,u),[F(1)]*n)
    p=sorted(range(n),key=lambda i:(-x[i],i));xp=[x[i] for i in p];W=permute(S,p)
    y=mv(tr(resolvent(Q(n),u)),[F(1)]*n)
    pieces=[u*(1-W[i][j])*(y[j]*xp[i]-y[i]*xp[j]) for i in range(n) for j in range(i+1,n)]
    Fmin,a,B,G,C=constants(n,u);f=sum(x);cost=sum(1-W[i][j] for i in range(n) for j in range(i+1,n))
    require(min(x)>0,'positivity fails')
    require(f-Fmin==sum(pieces),'ordering identity fails')
    require(all(v>=0 for v in pieces),'negative summand')
    require(f-Fmin>=a*cost,'ordering lower bound fails')
    return p,cost,f, min(x),max(x)

def recover(S,u):
    validate(S,u);n=len(S)
    require(n>=4 and n%2==0,'requires even n>=4')
    require(all(abs(S[i][j])==1 for i in range(n) for j in range(i+1,n)),'not tournament')
    Fmin,a,B,G,C=constants(n,u); lam=F(n)-u*u*Fmin;t=u*lam
    require(0<t<=1,'u corresponds to parameter beyond t=1')
    x=mv(resolvent(S,u),[F(1)]*n);f=sum(x); lower=(lam-f)/max(x)
    r=mv(S,[F(1)]*n)
    if all(abs(v)==1 for v in r):
        W=switch(S,r);p,cost,fW,_,_=order_certificate(W,u);k=int(cost/2)
        rp=[r[i] for i in p]
        neg=[i for i in range(n) if rp[i]==-1];pos=[i for i in range(n) if rp[i]==1]
        alt=[j for pair in zip(neg,pos) for j in pair]
        swaps=sum(abs(v-2*j) for j,v in enumerate(neg))
        require(swaps<=k,'alternating repair exceeds k')
        order=[p[j] for j in alt];ideal=[[F(0)]*n for _ in range(n)]
        BLa=BL(n)
        for i in range(n):
            for j in range(n):ideal[order[i]][order[j]]=BLa[i][j]
        edits=sum(S[i][j]!=ideal[i][j] for i in range(n) for j in range(i+1,n))
        require(edits<=2*k,'constructive edit bound fails')
        require(lower>=2*C*k,'spectral-to-backedge bound fails')
        mode='nearly_regular'
    else:
        ideal=BL(n);order=list(range(n));k=swaps=None
        edits=sum(S[i][j]!=ideal[i][j] for i in range(n) for j in range(i+1,n))
        require(lower>=G,'score exclusion gap fails');mode='non_nearly_regular'
    require(lower>=C*edits,'global spectral recovery bound fails')
    require(all((F(1)+t*S[i][j])>=0 for i in range(n) for j in range(n)),'negative spectral matrix')
    ax=mv([[1+t*S[i][j] for j in range(n)] for i in range(n)],x)
    require(all(ax[i]==lam*x[i]+f-lam for i in range(n)),'comparison vector identity fails')
    return {'n':n,'u':str(u),'t':str(t),'lambda_BL':str(lam),'mode':mode,'backedges':k,'stable_swaps':swaps,'edits_to_returned_BL':edits,'returned_order':order,'certified_deficit_lower':str(lower),'edit_coefficient':str(C),'score_exclusion_gap':str(G)}

def weighted_matrix(m,gamma,t,S):
    n=len(m)
    return [[gamma[i] if i==j else (1+t*S[i][j])*m[j] for j in range(n)] for i in range(n)]

def poly_minimum(lam,m,gamma,t):
    p=F(1);q=F(1)
    for a,b in zip(m,gamma):
        p*=lam-b+(1-t)*a;q*=lam-b+(1+t)*a
    return ((1+t)*p-(1-t)*q)/(2*t)

def minimum_bracket(m,gamma,t,bits=90):
    require(len(m)==len(gamma)>=2 and all(x>0 for x in m) and all(x>=0 for x in gamma),'invalid masses/diagonal')
    require(0<t<1,'strict coupling required')
    lo=max(gamma);hi=lo+2*sum(m)
    require(poly_minimum(lo,m,gamma,t)<0 and poly_minimum(hi,m,gamma,t)>0,'root bracket fails')
    for _ in range(bits):
        mid=(lo+hi)/2
        if poly_minimum(mid,m,gamma,t)>0:hi=mid
        else:lo=mid
    return lo,hi

def perron_ratios(A,steps=220,scale=10**24):
    n=len(A);den=lcm(*(v.denominator for row in A for v in row));B=[[int(v*den) for v in row] for row in A]
    v=[scale]*n
    for _ in range(steps):
        x=[sum(a*b for a,b in zip(row,v)) for row in B];m=max(x)
        v=[max(1,a*scale//m) for a in x]
    z=[F(sum(a*b for a,b in zip(row,v)),den*v[i]) for i,row in enumerate(B)]
    return min(z),max(z)
