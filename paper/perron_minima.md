---
title: "Exact Perron optimisation with factorised pair interactions"
subtitle: "Robust design, structural limits and constructive tournament stability"
author: [Anonymous]
date: "Evidence Press · Version 1.0.1-candidate · 28 September 2026"
abstract: |
  We minimise the Perron eigenvalue over matrices with arbitrary prescribed nonnegative diagonal and factorised symmetric off-diagonal entries, allowing each pairwise interaction to be redistributed between its two directions. Every local minimum is a saturated transitive orientation, and all transitive orientations, with the labelled vertex data fixed, have one explicit characteristic polynomial. This common optimiser yields an exact minimax rule under parameter uncertainty and a rational strict-stability test. We characterise factorisation by order-independent transitive spectra for all diagonal choices: the obstruction is a four-cycle determinant difference proportional to a classical tetrad. An arbitrarily small nonfactorised perturbation can produce strict nonglobal local minima; an exact four-vertex example certifies this phenomenon. Multiplicative approximation to factorisation nevertheless gives a uniform approximation guarantee. Separately, an ordered resolvent identity and a parity argument provide constructive edit-distance stability for Brualdi–Li tournaments along the full Levinger path. We distinguish its conservative uniform coefficient from stronger input-dependent certificates. All analytic arguments are included; accompanying rational and symbolic programs check identities and examples, not universal validity by finite testing.
---

# 1. Introduction

Fix positive numbers $m_1,\ldots,m_n$, nonnegative numbers $\gamma_1,\ldots,\gamma_n$, and $0<t<1$. We consider
$$
 A_{ii}(S)=\gamma_i,\qquad
 A_{ij}(S)=\sqrt{m_im_j}(1+tS_{ij})\quad(i\ne j),
 \qquad S^\top=-S,\quad |S_{ij}|\le1.                         \tag{1.1}
$$
The diagonal and the pair sums $A_{ij}+A_{ji}=2\sqrt{m_im_j}$ remain fixed. The optimisation changes the directional allocation of each pair. Every off-diagonal entry is positive; the diagonal may be zero. Write $\rho(A)$ for the spectral radius, which is a simple Perron eigenvalue in this family.

A saturated orientation has $S_{ij}\in\{-1,1\}$ for distinct indices. It is *transitive* if some ordering of the vertices makes $S_{ij}=1$ above the diagonal. Our principal theorem classifies **every local minimum** of $\rho(A(S))$: it is transitive, and every transitive orientation is a global minimum. This is a statement about the whole continuous optimisation landscape, not just its tournament vertices. All transitive orientations have the same characteristic polynomial even though the labelled pairs $(m_i,\gamma_i)$ are held fixed.

Three further conclusions identify the reach and limits of this principle. First, one fixed transitive order minimises every member of a parameter-uncertain family, so its worst-case design problem reduces to the scalar optimum. Second, factorisation of the pair weights is equivalent to transitive-order cospectrality for every diagonal. Third, nonglobal local minima can appear under arbitrarily small violations of factorisation. Thus the exact landscape is structurally restricted, while its optimum has a quantitative approximation guarantee under bounded multiplicative error.

The last part of the paper concerns a different extremum. For an even-order tournament, the Brualdi–Li matrix maximises the full Levinger path. An input-dependent resolvent ordering supplies an exact nonnegative remainder. Together with the inherited parity mechanism and a stable interleaving argument, it yields a labelled extremal tournament and an explicit spectral-deficit/edit-distance bound.

## 1.1. Relation to prior work

The classical tools used here are Perron differentiation, positive test-vector bounds, resolvent identities, the rank-one determinant formula, and symmetric-part Rayleigh bounds. None is claimed as new. General concavity of the spectral radius along Levinger paths is false [AC20]; no such concavity assumption enters our arguments.

Psarrakos and Tsatsomeros [PT03, PT06] study a **rank-one symmetric part**, including Perron-vector geometry and derivative and variance-dependent bounds. Their tournament transformation is exactly
$$
 I+2\big[(1-\alpha)T+\alpha T^\top\big]
   =J+(1-2\alpha)(T-T^\top).                                  \tag{1.2}
$$
In (1.1), the symmetric part is generally *diagonal plus rank one*. It is rank one when $\gamma_i=m_i$, but that restriction is not imposed here. The earlier variance criterion cannot distinguish almost regular tournaments, which all have score variance $1/4$.

Kirkland [K95] gives conditions for comparing tournament Perron roots under a single arc reversal using row structure and left and right Perron vectors. That is a close predecessor to the derivative mechanism. Its publisher abstract was inspected, but the full published proof was not obtained; we make no claim that every proof-level overlap has been excluded. Engel and Sergeev [ES23, Theorems 3.3–3.4] characterise spectral extrema under **independent permutations within rows**. Our admissible variables instead couple the two opposite entries of each pair. Their rearrangement condition does not directly apply to this domain.

| Result in this article | Closest antecedent and scope | Additional conclusion here |
|:--|:--|:--|
| Theorem 2.1: heterogeneous minimum | [PT03, PT06]: rank-one symmetric part and bounds along one path; [K95]: individual arc reversals | Every local minimum on a pair-coupled continuous box, arbitrary diagonal, common attained polynomial |
| Theorems 3.2–3.3: robust design | Standard common-optimiser minimax argument and entrywise Perron monotonicity | Explicit worst corner and scalar test from the common minimum |
| Theorem 4.1: structural characterisation | Classical rank-one tetrads [DSS07] | Equivalence with transitive-order spectra, through an explicit four-cycle difference |
| Proposition 4.2: fragility | Smooth dependence of a simple Perron root | Strict nonglobal minima arbitrarily close to factorisation, with an exact example |
| Theorem 6.2: constructive recovery | [EP26]: qualitative full-path maximum and odd-lattice argument; [D12]: classical endpoint | Input-dependent remainder, alternating repair, and explicit edit-distance control |

This table is a bounded comparison, not an exhaustive priority claim. The fixed-trace diagonal optimisation in [JLOvD96] varies the diagonal and concerns a different feasible family. No result about arbitrary fixed pair sums is attributed to that paper. The one-factor tetrads in [DSS07] are classical algebraic constraints; our contribution is their spectral interpretation, not their discovery.

The predecessor [EP26] is identified by its full title, version and content-addressed archive in the bibliography and evidence bundle. The qualitative Brualdi–Li maximum and parity mechanism belong to that predecessor, not independently to the present quantitative supplement. Drury's endpoint theorem retains its classical attribution even though the required comparison is reproved below.

## 1.2. Notation

Let $\mathbf1$ be the all-ones column vector, $J=\mathbf1\mathbf1^\top$, and
$$\mathcal K_n=\{S\in\mathbb R^{n\times n}:S^\top=-S,\ |S_{ij}|\le1\}.$$
Let $Q_n$ denote the transitive skew matrix with $+1$ above its diagonal. For even $n$, put
$$r_*=(-1,1,\ldots,-1,1)^\top,\qquad B_n=\operatorname{diag}(r_*)Q_n\operatorname{diag}(r_*).$$
This is a Brualdi–Li skew tournament in an interleaved order. Edge distance $d_E$ counts differing **unordered** vertex pairs. A simultaneous row-column permutation changes labels; positive diagonal similarity does not change eigenvalues. All comparisons in Sections 5–6 explicitly distinguish the continuous box from its tournament vertices.

# 2. The exact heterogeneous minimum

**Theorem 2.1 (local minima, global value and cospectrality).** For (1.1), with $n\ge2$, every local minimum on $\mathcal K_n$ is a saturated transitive orientation. Every saturated transitive orientation is a global minimum. All $n!$ such orientations have characteristic polynomial
$$
 \Phi(\lambda)=
 \frac{(1+t)\prod_i[\lambda-\gamma_i+(1-t)m_i]
       -(1-t)\prod_i[\lambda-\gamma_i+(1+t)m_i]}{2t}.           \tag{2.1}
$$
The minimum $\lambda_-$ is the unique root above $\max_i\gamma_i$ of
$$
 \prod_i\frac{\lambda-\gamma_i+(1-t)m_i}
                  {\lambda-\gamma_i+(1+t)m_i}
       =\frac{1-t}{1+t}.                                    \tag{2.2}
$$
The labelled vertex data do not move when the orientation changes. Thus cospectrality is not a consequence of merely relabelling a weighted matrix.

## 2.1. The local landscape

Write $w_i=\sqrt{m_i}$, $W=\operatorname{diag}(w)$, $D=\operatorname{diag}(\gamma_i-m_i)$ and $K=tWSW$. Then
$$A=D+ww^\top+K.$$
For its Perron root $\lambda$, each positive Perron-vector row equation gives $\lambda>\gamma_i$. Consequently
$$Z=\lambda I-D\succ0,\qquad R=(Z-K)^{-1}$$
are well-defined. Indeed the symmetric part of $Z-K$ is positive definite. Set
$$x=Rw,\qquad y=R^\top w.$$
The right and left Perron equations imply $x,y>0$ and
$$w^\top Rw=1,\qquad \frac{R+R^\top}{2}=R^\top ZR\succ0.       \tag{2.3}$$
The latter identity follows by adding $R^{-1}$ and $R^{-\top}$ between $R^\top$ and $R$.

Let $f(\lambda,S)=w^\top Rw$. Holding $\lambda$ fixed gives
$$f_\lambda=-y^\top x<0.$$
For the coordinate $s=S_{ij}$ let
$$E=t\sqrt{m_im_j}(e_ie_j^\top-e_je_i^\top).$$
Then
$$f_s=y^\top Ex,\qquad f_{ss}=2y^\top ERE x.                 \tag{2.4}$$
At a stationary point of the Perron root along this coordinate, $f_s=0$, so $y_i/x_i=y_j/x_j=\zeta>0$. Hence $Ey=\zeta Ex$ and
$$f_{ss}=-2\zeta(Ex)^\top R(Ex)<0.$$
Implicit differentiation of $f(\lambda(s),S(s))=1$ gives
$$\lambda''=-f_{ss}/f_\lambda<0.                             \tag{2.5}$$
A stationary coordinate cannot occur at a local minimum. This also applies at a box endpoint: since the first derivative vanishes and the second is negative, a sufficiently small permitted inward displacement decreases the objective.

Thus all independent entries of a local minimum lie at $\pm1$, and the ratios $y_i/x_i$ are distinct. Order these ratios increasingly. Since
$$
 \lambda_s=
 \frac{t\sqrt{m_im_j}(y_ix_j-y_jx_i)}{y^\top x},              \tag{2.6}
$$
its sign forces $S_{ij}=1$ for $i<j$ in that order. Every local minimum is transitive. The argument does not assert convexity or concavity of $S\mapsto\rho(A(S))$.

## 2.2. Evaluation of the minimum

Put $a_i=\lambda-\gamma_i+m_i$. Every even-order principal minor of $Q_n$ has determinant one and every odd-order principal minor is zero. The even assertion follows by Pfaffian expansion: the alternating sum of an odd number of unit terms is one. Expanding by the diagonal therefore gives
$$
 \det(\lambda I-D-tWQ_nW)
 =\frac12\left\{\prod_i(a_i+tm_i)+\prod_i(a_i-tm_i)\right\}. \tag{2.7}
$$
For $\lambda>\max\gamma_i$, all $a_i>m_i>tm_i$. To evaluate the rank-one correction, solve
$$(\operatorname{diag}(a_i/m_i)-tQ_n)v=\mathbf1.$$
Let $f=\sum_i v_i$, $C_i=\sum_{j\le i}v_j$ and $z_i=1+tf-2tC_i$. Subtracting consecutive partial-sum equations yields
$$
 (a_i/m_i+t)v_i=1+tf-2tC_{i-1},\qquad
 z_i=z_{i-1}\frac{a_i-tm_i}{a_i+tm_i}.
$$
With $P=\prod_i(a_i-tm_i)/(a_i+tm_i)$, the endpoints $z_0=1+tf$ and $z_n=1-tf$ give
$$w^\top(\lambda I-D-tWQ_nW)^{-1}w=\frac{1-P}{t(1+P)}.$$
The rank-one determinant formula and (2.7) now give (2.1). The identity first holds on an open half-line, hence holds as a polynomial identity. Its leading coefficient is one, and it is symmetric in the labelled pairs $(m_i,\gamma_i)$.

Every factor on the left of (2.2) is positive and strictly increasing on $\lambda>\max\gamma_i$. At the left endpoint, at least one factor equals $(1-t)/(1+t)$ and every other factor is below one. At infinity their product tends to one. This proves existence and uniqueness of the root. A global minimum exists by compactness and continuity, and Section 2.1 makes it transitive. The common polynomial gives the converse for every transitive order. This proves Theorem 2.1.

**Endpoints.** The strict assumption $t<1$ is substantive. At $t=1$, the minimum is $\max\gamma_i$, attained by transitive matrices, but other reducible orientations can also minimise. At $t=0$, there is only one matrix. When $\gamma_i=0$, our matrices have positive off-diagonal entries, rather than being entrywise strictly positive. Irreducibility and Perron simplicity still apply.

## 2.3. The rest of the continuous range

Let $H=D+ww^\top$ and let $v_H>0$ be its Perron vector. The standard symmetric-part Rayleigh argument gives
$$\max_{S\in\mathcal K_n}\rho(A(S))=\rho(H)=:\lambda_+,      \tag{2.8}$$
with equality exactly when $WSWv_H=0$. Indeed a right Perron vector $v$ satisfies
$$\rho(A)=v^\top Hv/\|v\|^2\le\rho(H).$$
Equality forces $v$ into the simple top eigenspace of $H$, and then the eigenvector equation gives the null condition. Conversely that condition supplies a positive Perron vector. The choice $S=0$ always attains the upper endpoint. Continuity on the connected compact box makes the full range $[\lambda_-,\lambda_+]$.

This upper-end argument is classical; the main result is the attained lower endpoint and its landscape. For $\gamma=m$, $\lambda_+=\sum_i m_i$ and upper equality means $Sm=0$. In this case
$$\sum_i\operatorname{artanh}(tm_i/\lambda_-)=\operatorname{artanh}t.$$
With all $m_i=\gamma_i=1$, the minimum becomes
$$\lambda_-=t\coth\!\left(\frac{\operatorname{artanh}t}{n}\right). \tag{2.9}$$

# 3. Robust design and approximate factorisation

## 3.1. Sensitivity of the exact value

**Proposition 3.1.** The minimum is smooth in the interior of its parameter domain and is strictly increasing in each $m_i$ and each $\gamma_i$, and strictly decreasing in $t$. Put
$$z_i=\lambda_--\gamma_i+m_i,\quad D_i=z_i^2-t^2m_i^2,\quad C=\sum_jm_j/D_j.$$
Then
$$
 \frac{\partial\lambda_-}{\partial\gamma_i}=
 \frac{m_i/D_i}{C},\qquad
 \frac{\partial\lambda_-}{\partial m_i}=
 \frac{(\lambda_--\gamma_i)/D_i}{C}.                          \tag{3.1}
$$
In particular, the diagonal derivatives sum to one.

**Proof.** Equation (2.2) is equivalent to
$$F(\lambda)=\sum_i\operatorname{artanh}(tm_i/z_i)-\operatorname{artanh}t=0.$$
Its derivative is $F_\lambda=-tC<0$. Differentiating a single summand gives (3.1). For the coupling sign write $u_i=\operatorname{artanh}(tm_i/z_i)>0$; at the root $\sum u_i=\operatorname{artanh}t$. Holding $\lambda$ fixed,
$$F_t=\frac{\sum_i\sinh(2u_i)-\sinh(2\sum_i u_i)}{2t}<0.$$
Strict superadditivity of $\sinh$ on positive arguments follows from its addition formula. Since $\partial_t\lambda_-=-F_t/F_\lambda$, the sign is negative. The implicit-function theorem proves smoothness.

## 3.2. A common optimiser under uncertainty

**Theorem 3.2 (simultaneous and minimax optimality).** Let $\Theta$ be a nonempty compact set of admissible triples $(m,\gamma,t)$ of fixed order. For any fixed transitive $Q$,
$$
 \rho(A_\theta(Q))=\min_{S\in\mathcal K_n}\rho(A_\theta(S))
 \quad\text{for every }\theta\in\Theta.
$$
Consequently
$$
 \min_S\max_{\theta\in\Theta}\rho(A_\theta(S))
 =\max_{\theta\in\Theta}\lambda_-(\theta)
 =\max_{\theta\in\Theta}\min_S\rho(A_\theta(S)).              \tag{3.2}
$$
The same order minimises any expectation of the Perron value under a probability law on $\Theta$.

**Proof.** Theorem 2.1 supplies a pointwise common minimiser. Every $S$ is at least as costly at every parameter, while $Q$ attains the pointwise bound. Taking maxima or expectations proves the statements. This is a consequence of common optimality, not a general minimax theorem for unrelated uncertainty sets.

**Theorem 3.3 (rectangular uncertainty and stability).** Suppose
$$
 0<m_i^-\le m_i\le m_i^+,\quad
 0\le\gamma_i^-\le\gamma_i\le\gamma_i^+,\quad
 0<t^-\le t\le t^+<1.
$$
Then the optimal worst-case value in (3.2) is
$$\lambda_-(m^+,\gamma^+,t^-).                              \tag{3.3}$$
There exists a fixed admissible orientation that makes every matrix in this box strictly Schur stable if and only if
$$\max_i\gamma_i^+<1\quad\text{and}\quad
 \Phi_{m^+,\gamma^+,t^-}(1)>0.                              \tag{3.4}$$
Every transitive orientation attains the optimum.

**Proof.** Apply Proposition 3.1 to each interval. The strictly increasing ratio in (2.2) proves (3.4). These statements concern one matrix with fixed but unknown parameters. They do **not** assert stability of arbitrary time-varying products of matrices from the family.

The criterion is exactly rational for rational input. For
$$
\begin{gathered}
 m^-=(1/4,1/2,3/4),\quad m^+=(1/3,2/3,1),\\
 \gamma^-=0,\quad\gamma^+=(1/20,1/25,1/30),\quad
 [t^-,t^+]=[3/4,9/10].
\end{gathered}
$$
the optimal worst-case Perron root is enclosed near $0.910844108421038$, and
$$\Phi_{m^+,\gamma^+,t^-}(1)=\frac{95089}{540000}>0.          \tag{3.5}$$
Thus one fixed transitive orientation is a robust stable design throughout this box. No search over orientations or uncertainty samples is needed for that conclusion.

The nonnegative-diagonal restriction can also be removed when the objective is the spectral abscissa of a Metzler matrix. Add a sufficiently large common scalar to the diagonal, apply Theorem 2.1 and subtract the scalar. This standard shift gives the same formula for arbitrary real diagonal entries, with strict Hurwitz feasibility tested by $\max\gamma_i<0$ and $\Phi(0)>0$. It is a corollary, not an independent spectral theorem.

## 3.3. Approximate factorisation remains useful

**Proposition 3.4.** Let $b_{ij}=b_{ji}>0$ and suppose known $w_i>0$ and $\kappa\ge1$ satisfy
$$\kappa^{-1}w_iw_j\le b_{ij}\le\kappa w_iw_j\quad(i\ne j).$$
Keep a nonnegative diagonal and $0<t<1$. Write $A_b(S)_{ij}=b_{ij}(1+tS_{ij})$ off the diagonal. If $\lambda_0$ is the factorised minimum for $m_i=w_i^2$, then
$$
 \kappa^{-1}\lambda_0\le\min_S\rho(A_b(S))\le\kappa\lambda_0,
 \qquad
 \rho(A_b(Q))\le\kappa^2\min_S\rho(A_b(S))                 \tag{3.6}
$$
for every transitive $Q$.

**Proof.** Including the unchanged nonnegative diagonal,
$\kappa^{-1}A_0(S)\le A_b(S)\le\kappa A_0(S)$ entrywise. Perron monotonicity proves the first comparison after minimisation. For $Q$, the upper comparison is $\rho(A_b(Q))\le\kappa\lambda_0$, while the minimum is at least $\kappa^{-1}\lambda_0$. No sharpness is asserted for the factor $\kappa^2$.

This quantitative guarantee is compatible with the loss of exact local/global equivalence proved next.

# 4. The structural boundary of the minimum principle

The factorisation in (1.1) is sufficient for order-independent transitive spectra. In a precise universal-diagonal sense, it is also necessary. The algebraic condition is the classical vanishing of off-diagonal rank-one tetrads [DSS07]; here it is detected by characteristic polynomials.

## 4.1. A converse from four vertices

**Theorem 4.1 (spectral characterisation of factorisation).** Fix $n\ge4$, $0<t<1$ and positive symmetric off-diagonal weights $b_{ij}$. The following are equivalent.

1. There are $w_i>0$ such that $b_{ij}=w_iw_j$ for all distinct $i,j$.
2. For every nonnegative diagonal $\gamma$, all transitive orientations of the matrices $A_{ii}=\gamma_i$, $A_{ij}=b_{ij}(1+tS_{ij})$ have the same characteristic polynomial.
3. On every four-vertex principal set, all transitive orientations with zero diagonal have the same determinant.
4. For all four distinct indices,
$$b_{ij}b_{kl}=b_{ik}b_{jl}=b_{il}b_{jk}.                    \tag{4.1}$$

The universal quantifier on the diagonal in statement 2 is part of the theorem. No equivalence with absence of nonglobal local minima for *every* nonfactorised family is asserted.

**Proof.** Theorem 2.1 gives $1\Rightarrow2$. For $2\Rightarrow3$, characteristic polynomials are polynomials in the independent diagonal variables. Equality on the nonnegative orthant is polynomial identity. The coefficient of the product of the diagonal variables outside a chosen four-set isolates, up to a common sign, that set's characteristic polynomial. Set its diagonal and spectral variable to zero.

For $3\Rightarrow4$, consider four labels $1,2,3,4$. Denote the characteristic polynomials for the total orders $1234$ and $1324$ by $\chi_{1234}$ and $\chi_{1324}$. Expansion by permutation cycles gives the identity
$$
 \chi_{1234}(\lambda)-\chi_{1324}(\lambda)
 =-4t^2(1-t^2)b_{14}b_{23}
          (b_{12}b_{34}-b_{13}b_{24}).                       \tag{4.2}
$$
It holds for every diagonal. Two-cycles, transitive three-cycles and their diagonal complements are order-independent. Of the three undirected Hamilton cycles, precisely one has directional product sum $2(1-t^4)$; the other two have $2(1-t^2)^2$. Their difference is $4t^2(1-t^2)$, and the determinant sign of a four-cycle is negative. This proves (4.2). Relabel the four vertices to obtain all tetrads. Positivity of the other factors gives (4.1).

Finally assume 4. Set
$$w_1=\sqrt{b_{12}b_{13}/b_{23}},\qquad w_i=b_{1i}/w_1\quad(i>1).$$
For each $i>3$, the tetrads on $\{1,2,3,i\}$ give $b_{2i}=w_2w_i$ and $b_{3i}=w_3w_i$. The tetrads on $\{1,2,i,j\}$ then give $b_{ij}=w_iw_j$ for all remaining pairs. The edges among $1,2,3$ agree by construction. Thus $4\Rightarrow1$.

For three vertices every positive edge-weight triple factors; there is no four-point obstruction. The positivity assumption avoids the additional zero-pattern cases that arise in general algebraic rank-one completion.

## 4.2. Nonglobal local minima appear arbitrarily close

**Proposition 4.2 (structural fragility).** Fix $0<t<1$. At order four with zero diagonal and initially all pair weights equal to one, change only $b_{12}=b_{21}$ to $1+\varepsilon$. For every sufficiently small $\varepsilon>0$, the continuous skew-box problem has a strict local minimum that is not global.

**Proof.** At $\varepsilon=0$, every transitive vertex is a minimum by Theorem 2.1. The proof of that theorem also shows that every signed coordinate derivative there is strictly negative:
$$S_{ij}\,\partial_{S_{ij}}\rho(A)<0.$$
A feasible displacement from a saturated vertex has the opposite sign in each nonzero coordinate. Hence the positive first variation gives strict local minimality. Perron simplicity makes these derivatives continuous in the pair weights. There are finitely many transitive vertices and coordinates, so all transitive vertices remain strict local minima for sufficiently small positive $\varepsilon$.

But (4.2) becomes the nonzero constant
$$\chi_{1234}-\chi_{1324}=-4\varepsilon t^2(1-t^2).           \tag{4.3}$$
The two characteristic polynomials have no common root, so their Perron values differ. The larger one is a strict nonglobal local minimum. This proves the claim without inferring it from an optimiser.

**Exact example.** For $t=1/2$ and $\varepsilon=1/100$, the 24 transitive orientations fall into two spectral classes:
$$
\begin{aligned}
 P_H(\lambda)&=\lambda^4-\frac{180603}{40000}\lambda^2
                      -\frac{603}{100}\lambda-\frac{392991}{160000},\\
 P_L(\lambda)&=\lambda^4-\frac{180603}{40000}\lambda^2
                      -\frac{603}{100}\lambda-\frac{391791}{160000}.
\end{aligned}                                               \tag{4.4}
$$
There are 16 transitive orientations of the first class and 8 of the second. Their Perron values are respectively near $2.668314817950297$ and $2.668151280483751$. Both are enclosed by disjoint rational intervals. Each polynomial has one positive root by Descartes' rule, and positive left and right eigenvectors are supplied by the adjugate at that root. Outward rational interval evaluation verifies all 144 signed derivative inequalities at the 24 vertices. Every inward coordinate derivative is greater than $0.06927$. In particular the higher-valued vertices are certified strict nonglobal local minima. We do not infer that the lower class is globally optimal over this nonfactorised box.

For the same perturbed weights, Proposition 3.4 with $w_i=1$ gives $\kappa=101/100$. Any transitive order is still within the factor $10201/10000$ of the global optimum. Exact landscape fragility therefore need not mean a large value penalty.

# 5. Constructive resolvent ordering and parity

The remaining results concern the quantitative Brualdi–Li problem. Their qualitative full-path comparison and odd-lattice mechanism are inherited from [EP26]. We include the needed arguments so that the present paper is self-contained.

For $n\ge2$ and $0<u<1/(n-1)$ write
$$
 R_S=(I-uS)^{-1},\quad f_u(S)=\mathbf1^\top R_S\mathbf1,
 \quad q=\frac{1-u}{1+u},\quad
 F_n(u)=\frac{1-q^n}{u(1+q^n)}.
$$
Define
$$
 \eta=1-(n-1)u,\qquad B=\frac{1+nu}{1+u},\qquad
 a_n(u)=\frac{4u^2\eta q^{n-2}}{(1+u)^3(1+q^n)}.             \tag{5.1}
$$

**Lemma 5.1.** For $S\in\mathcal K_n$, $x=R_S\mathbf1$ and $R_S^\top\mathbf1$ are positive, and
$$\frac{\eta}{1+u}\le\min_i x_i\le\max_i x_i\le B.$$

**Proof.** At the first hypothetical zero along $(I-vS)^{-1}\mathbf1$, $x\ge0$ and $\|x\|_2^2=\mathbf1^\top x=f$. At most $n-1$ entries are nonzero, so $f\le n-1$. The zero-coordinate equation gives $1\le vf\le u(n-1)<1$, a contradiction. Apply the same argument to $-S$. In general $f\le n$ by Cauchy–Schwarz, giving $(1+u)x_i\le1+uf\le1+un$. Also
$$0\le\sum_{j\ne i}(x_j-1)^2=n-1-f+2x_i-x_i^2$$
implies $f\le n-1+2x_i$. Combining this with $x_i\ge1-u(f-x_i)$ gives the lower bound. Positivity of these two vectors does not mean that the entire inverse is entrywise positive.

Sort the coordinates so $x_1\ge\cdots\ge x_n$, breaking ties arbitrarily, and put
$$y=(I+uQ_n)^{-1}\mathbf1,\qquad y_i=Cq^{n-i},\quad
 C=\frac2{(1+u)(1+q^n)}.$$

**Theorem 5.2 (ordered remainder).** In this selected order,
$$
 f_u(S)-F_n(u)=
 u\sum_{i<j}(1-S_{ij})(y_jx_i-y_ix_j)
 \ge a_n(u)E(S),                                           \tag{5.2}
$$
where $E(S)=\sum_{i<j}(1-S_{ij})$ is an entrywise discrepancy. At tournament vertices $E(S)=2k$, with $k$ the number of backward edges. Equality $f_u(S)=F_n(u)$ holds precisely at transitive tournament vertices.

**Proof.** The resolvent identity $R_S-R_Q=uR_Q(S-Q)R_S$, multiplied by the all-ones vectors, gives the displayed paired-entry sum. Adjacent equations for $y$ give its geometric expression and $\sum y_i=F_n(u)$. For $i<j$,
$$
 y_jx_i-y_ix_j=(y_j-y_i)x_i+y_i(x_i-x_j)
 \ge Cq^{n-2}(1-q)\frac\eta{1+u}>0.
$$
This proves the inequality and equality case. One linear solve and a sort construct the certificate; no convexity claim is used.

## 5.1. The odd-lattice bound and a strict penalty

The symmetric part of $R_S$ is
$$H_S=(I-u^2S^2)^{-1},\qquad0\prec H_S\preceq I.$$
For every odd integer vector $z\in\mathbf1+2\mathbb Z^n$,
$$z^\top R_Sz\ge F_n(u).                                    \tag{5.3}$$
To prove this, minimise $z^\top H_Sz$ on that lattice coset. Coercivity gives a minimiser. Comparing with $z\pm2e_i$ gives $|(H_Sz)_i|\le(H_S)_{ii}\le1$. But
$$\|H_S^{-1}\|_\infty\le d_u:=1+u^2(n-1)^2<2,$$
so every coordinate of the minimiser is $\pm1$. Switching $S$ by these signs reduces the conclusion to Theorem 5.2. Equality also requires the switched matrix to be transitive.

If $\|z\|_\infty\ge3$, the argument strengthens to
$$z^\top R_Sz\ge F_n(u)+4\left(\frac{\|z\|_\infty}{d_u}-1\right). \tag{5.4}$$
Indeed, some coordinate of $H_Sz$ has magnitude at least $\|z\|_\infty/d_u$. Moving that coordinate of $z$ by two towards reducing the quadratic form decreases it by at least the second term of (5.4). Apply (5.3) to the new odd vector.

## 5.2. Spectral transfer: tournament domain, even $n\ge4$

Here and throughout Section 6 let $S$ be a **skew tournament matrix of even order $n\ge4$**. Its score vector $r=S\mathbf1$ is odd, and
$$f_u(S)=n-u^2r^\top R_Sr\le n-u^2F_n(u).                   \tag{5.5}$$
This follows by expanding $R_S=I+uS+u^2S^2R_S$ and using skew-symmetry. Equality forces $r_i=\pm1$ and $\operatorname{diag}(r)S\operatorname{diag}(r)$ transitive. Reorder the latter to $Q_n$; the score equation is $Q_nr=\mathbf1$. Adjacent rows force alternating signs, and the last row fixes $r=r_*$. Thus equality is precisely Brualdi–Li.

For $0<t\le1$, set $\lambda_0=\rho(J+tB_n)$ and $u=t/\lambda_0$. Its row sums are $n\pm t$. For $t<1$, $\lambda_0\ge n-t>n-1$. At $t=1$, the interleaved Brualdi–Li order has the directed Hamilton cycle $1,3,\ldots,n-1,2,4,\ldots,n,1$ (here $n\ge4$). Its row sums are unequal, so the strict Perron bound gives $\lambda_0>n-1$. Consequently $u<1/(n-1)$, and
$$\lambda_0=n-u^2F_n(u),\qquad t=u\lambda_0.                 \tag{5.6}$$
For any skew tournament $S$ of this order, $x=R_S\mathbf1>0$ satisfies
$$ (J+tS)x=\lambda_0x+(f_u(S)-\lambda_0)\mathbf1.$$
Positive test-vector row ratios give
$$
 \delta_S:=\lambda_0-\rho(J+tS)
 \ge\frac{\lambda_0-f_u(S)}{\max_i x_i}
 \ge\frac{\lambda_0-f_u(S)}B.                               \tag{5.7}
$$
The numerator is nonnegative by (5.5). This step is not asserted on the full skew box: $S=0$ would have $f_u(S)=n>\lambda_0$. The excluded case $n=2,t=1$ has $\lambda_0=n-1$ and is not covered by the strict resolvent condition.

If $S$ is not nearly regular, then $\|r\|_\infty\ge3$ and
$$\delta_S\ge G_n(u):=\frac{4u^2}B
 \left(\frac3{1+u^2(n-1)^2}-1\right)>0.                    \tag{5.8}$$
A deficit below $G_n(u)$ therefore certifies near regularity. At $t=1$, the qualitative maximum is Drury's classical theorem [D12]; this self-contained argument reuses the proof mechanism of [EP26], rather than supplying a separate priority claim for that endpoint.

# 6. Constructive tournament stability and its numerical meaning

Suppose first that $r_i=\pm1$. Switch to $W=\operatorname{diag}(r)S\operatorname{diag}(r)$ and order by descending entries of $(I-uW)^{-1}\mathbf1$. Let $k$ be its backward-edge count. Then
$$\lambda_0-f_u(S)=u^2[f_u(W)-F_n(u)]\ge2a_n(u)u^2k.        \tag{6.1}$$

**Lemma 6.1 (stable alternating repair).** A labelled Brualdi–Li matrix $S^\sharp$ can be constructed with $d_E(S,S^\sharp)\le k+V\le2k$, where $V$ is the stable adjacent-interchange cost of alternating the score signs in the selected order.

**Proof.** In that order $Wr=\mathbf1$ and $\sum r_i=0$. Put $b=(Q_n-W)r=Q_nr-\mathbf1$. Each backward edge contributes at most two at each endpoint, so $\|b\|_1\le4k$. If negative signs occupy $p_1<\cdots<p_{n/2}$ and positive signs occupy $q_1<\cdots<q_{n/2}$, using one-based positions, then
$$b_{p_j}=-2[p_j-(2j-1)],\qquad b_{q_j}=2(q_j-2j).$$
Stable matching of the negative positions to $1,3,\ldots,n-1$ needs
$$V=\sum_j|p_j-(2j-1)|=\sum_j|q_j-2j|$$
adjacent interchanges. Hence $4V=\|b\|_1\le4k$. Changing the transitive order costs exactly $V$ edges, and switching back preserves pairwise disagreements. The alternating signs give $S^\sharp$ of Brualdi–Li form.

Put
$$
 c_n(u)=\frac{a_n(u)u^2}{B}
 =\frac{4u^4[1-(n-1)u]q^{n-2}}
 {(1+u)^2(1+q^n)(1+nu)}.                                  \tag{6.2}
$$

**Theorem 6.2 (constructive uniform stability).** For even $n\ge4$, any skew tournament $S$ and $0<t\le1$, the construction returns a Brualdi–Li copy satisfying
$$\delta_S\ge c_n(u)d_E(S,S^\sharp),\qquad u=t/\lambda_0.    \tag{6.3}$$
The same bound holds for the minimum distance to a Brualdi–Li copy.

**Proof.** In the nearly regular case combine (5.7), (6.1) and Lemma 6.1. Otherwise return a fixed Brualdi–Li copy, whose distance is at most $N=n(n-1)/2$. We have $G_n(u)\ge2u^2/B$ and $c_n(u)\le4u^4\eta/B$. With $v=u(n-1)$,
$$2Nu^2\eta=\frac n{n-1}v^2(1-v)\le\frac{16}{81}<1.$$
Thus $Nc_n(u)\le G_n(u)$, and (5.8) proves the claim.

The algorithm uses a score calculation, a linear solve, sorting and stable interleaving. Its cost is $O(n^3)$ arithmetic operations, excluding scalar root computation; no polynomial bit-complexity bound under arbitrary conditioning is asserted. It does not necessarily return a nearest copy.

## 6.1. Uniform versus instance-dependent certificates

The uniform coefficient is positive but conservative. For fixed $n$ and $t\downarrow0$, $c_n(u)\sim2t^4/n^4$, while $G_n(u)$ is of order $t^2$. This separates the nearly regular fourth-order regime from score imbalance. Dimension and proximity to the resolvent limit further weaken $c_n$.

The exact remainder retains information discarded by the uniform estimate. For a nearly regular input define
$$
 L(S,u)=\frac{u^2[f_u(W)-F_n(u)]}{\max_i[(I-uS)^{-1}\mathbf1]_i}.
                                                                  \tag{6.4}
$$
Then $\delta_S\ge L(S,u)$. If $k>0$, the sharper input-dependent edit coefficient
$$c_{\rm inst}(S,u)=\frac{L(S,u)}{k+V}                    \tag{6.5}$$
satisfies $\delta_S\ge c_{\rm inst}d_E(S,S^\sharp)$. This is a posteriori and input-dependent; it is not a replacement uniform sharp constant.

The independent supplied referee program enumerates all $32\,768$ labelled six-point tournaments at each of two parameters. Rounded floating-point diagnostics are:

| $t$ | Uniform $c_6(u)$ | Smallest nonextremal deficit | Deficit divided by $c_6(u)$ |
|:--:|--:|--:|--:|
| $1/2$ | $2.4346507\,10^{-5}$ | $0.0013920828$ | $57.18$ |
| $1$ | $4.0343898\,10^{-5}$ | $0.0165951755$ | $411.34$ |

There are only 15 unordered edges. Thus the uniform distance upper bound is vacuous for every nonextremal input in those two enumerations. This does not invalidate Theorem 6.2, but it limits its numerical interpretation. The table is an exhaustive finite floating-point diagnostic, not a certified sharp-gap calculation.

**An exact non-nearest example.** Use $n=6$ and the tournament encoded by integer $9564$: bit positions enumerate pairs $(0,1),(0,2),\ldots,(4,5)$ lexicographically, with bit one meaning $S_{ij}=1$. Take $u=1/12$, giving
$$t=\frac{1638984}{3299185},\qquad\lambda_0=\frac{19667808}{3299185}.$$
The construction returns the order $(4,2,5,1,3,0)$, with $k=4$, $V=2$ and four edits. An exhaustive check of all 720 labelled copies proves the nearest distance is one. The independent positive-vector spectral enclosure yields
$$\delta_S\simeq0.001358390753775.$$
The uniform bound for the actual four edits is only $0.000095877588324$, whereas
$$L(S,u)=\frac{1218003072}{999154878065}
       \simeq0.001219033303785.$$
Here $c_{\rm inst}=L/6\simeq0.000203172217297$. Combining the certified spectral upper bound with (6.5) certifies at most six edits, improving the trivial 15; the constructed distance is actually four. None of these numbers is presented as nearest recovery or a sharp uniform coefficient.

For exact input handling, the diagnostic accepts rational $u$, constructs rational $\lambda_0=n-u^2F_n(u)$ and $t=u\lambda_0$, and checks $t\le1$. No floating-point eigenvalue authorises acceptance. The mathematical theorem permits arbitrary real $t$; a general certified interface supplied with $t$ rather than $u$ would need interval treatment of the scalar root and is not claimed here.

# 7. Scope, evidence and further questions

The weighted minimum and its structural results are independent of the predecessor tournament maximum. The recovery theorem is self-contained as written, but its qualitative comparison and odd-lattice idea are inherited from [EP26]. We do not count the classical Perron principles, the rank-one determinant formula, symmetric-part upper bound, tetrad identities, or common-optimiser minimax reasoning as separate inventions.

The new structural results delimit the factorised hypothesis rather than extending the exact landscape to arbitrary pair weights. Theorem 4.1 characterises universal-diagonal **cospectrality**, not every class without nonglobal minima. Proposition 4.2 proves fragility near one factorised family; it is not a classification of all nonfactorised landscapes. The approximation factor in Proposition 3.4 and the recovery coefficient in Theorem 6.2 are not claimed sharp.

The robust results concern a single unknown but fixed system. They do not imply stability under arbitrary switching, nonlinear dynamics, or unmodelled network interactions. The general weighted maximum over tournament vertices is still unresolved. For example, cyclic blocks of sizes $3,1,1$, with the three-vertex block cyclic and masses $(1,1,1,3,3)$, give a tournament with $Sm=0$ and rank-one-case upper endpoint nine. It is not switching-equivalent to a transitive tournament: an odd transitive skew matrix has kernel spanned by an alternating sign vector, whereas this kernel contains a positive vector of unequal magnitudes. A universal weighted Brualdi–Li analogue therefore cannot be presumed.

The accompanying programs distinguish exact identity checking, rational acceptance certificates, symbolic reconstruction and numerical diagnostics. The universal results rest on the displayed proofs. Appendix A and the evidence ledger give the revision-specific scope. An independent specialist review of the newly added Section 3–4 results has not yet been supplied. The final version is an unrefereed research candidate prepared for Evidence Press, not a proof-assistant-verified or institutionally rated output.

# Appendix A. Reproducibility and revision record

The reviewed v0.1 archive and the supplied referee-check archive are retained unchanged, with full SHA-256 identifiers. The present manuscript corrects the Section 3 endpoint and domain overstatement of that draft: spectral transfer requires an even-order tournament with $n\ge4$. The original runtime recovery interface already imposed that domain; no false acceptance caused by the manuscript wording was found.

The reviewed analytic results are reproduced with their proof obligations explicit. The additions are the parameter sensitivities, common robust optimiser and worst-corner formula, approximate-factorisation bound, spectral characterisation of factorisation, and the arbitrarily small nonglobal-minimum obstruction. The point-by-point response separates those additions from revisions already covered by the supplied review.

The new exact verifier checks the four-cycle determinant identity by a direct permutation expansion, reconstructs positive factor weights, encloses the two fragility roots, checks the robust corner example, and independently certifies the worked recovery spectrum and nearest distance. A separate SymPy implementation imports none of those algebra routines: it constructs the general characteristic polynomials, differentiates the scalar equation, and certifies all signed Perron derivatives of the rational fragility example by outward interval evaluation of adjugate polynomials. The supplied referee implementation is preserved and replayed separately, without being described as an authenticated external specialist endorsement.

Every acceptance check raises an explicit exception on failure. Mutation tests alter a four-cycle coefficient, a characteristic-polynomial coefficient and a robust scalar value in disposable copies, then recompute their manifests. Valid inputs must pass and corrupt inputs must fail directly and through the replay wrapper under ordinary execution, `-O`, `-OO`, `PYTHONOPTIMIZE=1` and `PYTHONOPTIMIZE=2`. A matching checksum alone is not treated as a mathematical check.

See `README.md` for the exact commands and `CLAIM_CHECK_MAP.md` for their scope. Version 1.0 has editorial package identifier `EP-PERRON-MINIMA-2026-09-28-v1.0`. This is a content-version label, not a DOI or a claim that the website has deployed the paper. Public archival identifiers, accountable release stewardship and the reuse licence are recorded as publisher-controlled fields rather than inferred from the research workflow.

\begingroup
\small

# References

## Spectral optimisation and tournament matrices

[AC20] Altenberg, L., & Cohen, J. E. (2020). Nonconcavity of the spectral radius in Levinger’s theorem. *Linear Algebra and its Applications, 606*, 201–218. <https://doi.org/10.1016/j.laa.2020.07.028>

[D12] Drury, S. W. (2012). Solution of the conjecture of Brualdi and Li. *Linear Algebra and its Applications, 436*(9), 3392–3399. <https://doi.org/10.1016/j.laa.2011.11.031>. Author exposition: <https://www.math.mcgill.ca/drury/research/brualdili/>. The author exposition, not the complete published proof, was inspected.

[ES23] Engel, G. M., & Sergeev, S. (2023). Bounding the row sum arithmetic mean by Perron roots of row-permuted matrices. *Linear Algebra and its Applications, 673*, 220–232. <https://doi.org/10.1016/j.laa.2023.05.014>. Inspected preprint: <https://arxiv.org/abs/2209.01991>.

[JLOvD96] Johnson, C. R., Loewy, R., Olesky, D. D., & van den Driessche, P. (1996). Maximizing the spectral radius of fixed trace diagonal perturbations of nonnegative matrices. *Linear Algebra and its Applications, 241–243*, 635–654. <https://doi.org/10.1016/0024-3795(95)00258-8>. Publisher abstract inspected; full-text comparison remains bounded.

[K95] Kirkland, S. (1995). Spectral radii of tournament matrices whose graphs are related by an arc reversal. *Linear Algebra and its Applications, 217*, 179–202. <https://doi.org/10.1016/0024-3795(94)00160-F>. Publisher abstract and author listing inspected; full published text not obtained.

[PT03] Psarrakos, P. J., & Tsatsomeros, M. J. (2003). The Perron eigenspace of nonnegative almost skew-symmetric matrices and Levinger’s transformation. *Linear Algebra and its Applications, 360*, 43–57. <https://doi.org/10.1016/S0024-3795(02)00439-1>. Supplied full text inspected.

[PT06] Psarrakos, P. J., & Tsatsomeros, M. J. (2006). Bounds for Levinger’s function of nonnegative almost skew-symmetric matrices. *Linear Algebra and its Applications, 416*(2–3), 759–772. <https://doi.org/10.1016/j.laa.2005.12.018>. Supplied full text inspected.

## Algebraic factorisation

[DSS07] Drton, M., Sturmfels, B., & Sullivant, S. (2007). Algebraic factor analysis: Tetrads, pentads and beyond. *Probability Theory and Related Fields, 138*, 463–493. <https://doi.org/10.1007/s00440-006-0033-2>. One-factor representation and Theorem 16 inspected in <https://arxiv.org/abs/math/0509390>.

## Content-identified predecessor

[EP26] *Brualdi–Li extremality along the full Levinger path: Resolvent minimisation, odd lattice vectors and sharp reciprocal-matrix envelopes*. (2026). Research version 0.1, 27 September [Unrefereed manuscript]. Archive `tournament_envelope_v0_1.zip`, SHA-256

`25a90b62e165d2a8e779f1760859283da67387bc06a7fdc334cb88c9a6071ac4`.

Preserved inside the reviewed archive in `provenance/resolvent_extensions_v0_1.zip`. No public DOI or independently authenticated authorship is assigned by this citation.

\endgroup

## Publication note, version 1.0.1-candidate

Version DOI: https://doi.org/10.5281/zenodo.23014818. Original prose/data CC0-1.0; original code MIT, with retained-material exceptions. Theorem 3.3 wording now explicitly states existence of a fixed stabilising orientation. Historical numerical byte identity did not reproduce at intake; the current wrapper separates exact replay from tolerance-tested numerical corroboration and retains all differences. See PUBLICATION_AUDIT.md. No mathematical claim is strengthened by this packaging revision.
