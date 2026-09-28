---
title: "Response to the review"
subtitle: "Exact Perron optimisation with factorised pair interactions"
date: "Version 1.0 · 28 September 2026"
author: []
---

## Scope of the revision

The review of *Constructive resolvent ordering and weighted Perron minima*, research draft 0.1, recommended major revision with a favourable mathematical assessment and a provisional 3-star judgement. The supplied review and checking archive are preserved unchanged. No external specialist identity is inferred from them.

Version 1.0 is a complete standalone article centred on the heterogeneous minimum. It repairs the endpoint and domain statements, gives explicit predecessor comparisons, and presents the stability coefficient with its actual limitations. It also supplies new structural and robust-design results. **Those additions have written proofs and exact checks, but are not covered by the supplied referee's favourable proof assessment.** No revised star rating is claimed.

## Required revisions

| Review request | Action and location |
|:--|:--|
| 4.1: theorem-level novelty comparison | Section 1.1 distinguishes rank-one Levinger theory, single arc reversals, independent row permutations, diagonal optimisation, classical tetrads, and the content-identified predecessor. Full-text limitations are explicit. |
| 4.1: stable predecessor identity | The bibliography gives the predecessor's complete title, version, date and full archive SHA-256. The exact archive is nested in the retained reviewed input; its content identity is independently checked. No DOI has been invented. |
| 4.2: coefficient/slack diagnostics | Section 6.1 reproduces the referee's two six-point diagnostics, explicitly noting that the uniform bound does not beat the trivial 15-edge bound there. The independent referee program is replayed. |
| 4.2: worked recovery example | An entirely rational parameter choice yields a four-edit return although a one-edit copy exists. All 720 relabellings are checked. The uniform, exact remainder and instance-dependent coefficient are separated. |
| 4.3: endpoint | Section 5.2 restricts spectral transfer to even $n\ge4$. It explicitly excludes the $n=2,t=1$ endpoint, while continuous resolvent lemmas retain their valid $n\ge2$ scope. |
| 4.3: matrix domain | Section 5.2 says 'skew tournament' where the numerator sign needs parity. It gives $S=0$ as a counterexample to extending that step to the full box. |
| 4.4: strongest conclusion first | Conventional abstract and introduction lead with local-minimum classification, global attainment, fixed-data cospectrality and the scalar minimum. The complete proof is Section 2. |

The proof-critical recovery code already enforced the correct tournament domain and $n\ge4$; the review exposed an overbroad manuscript statement, not an accepted invalid runtime input. Both guards have explicit negative regression tests in the publication package.

## Mathematical strengthening

**Proposition 3.1 and Theorems 3.2–3.3.** Differentiating the explicit scalar equation gives positive mass/diagonal sensitivities and strict decrease with the directional parameter. One fixed transitive orientation is optimal at every parameter instance. This gives minimax equality for a compact uncertainty family and identifies the exact corner for rectangular uncertainty. The robust stability test is a rational polynomial sign. The restriction to a fixed unknown matrix, rather than arbitrary switching, is explicit. These are consequences of the common optimiser, not claims of a new abstract minimax theorem.

**Proposition 3.4.** A multiplicatively accurate factorisation supplies a $\kappa^2$ approximation guarantee for any transitive order. The factor is not claimed sharp.

**Theorem 4.1.** Factorisation is necessary and sufficient for transitive-order cospectrality for every diagonal choice. An exact four-cycle determinant difference exposes the classical tetrad obstruction. The classical rank-one equations are attributed to their factor-analysis context. The theorem does not characterise every possible no-spurious-minimum family.

**Proposition 4.2.** Arbitrarily small departures from factorisation can create strict nonglobal local minima. The proof uses continuity of strict inward derivatives at transitive vertices and an exact nonzero constant difference between two characteristic polynomials. At the rational example $b_{12}=101/100$, $t=1/2$, all 24 transitive vertices are certified strict local minima and have two different Perron values. The larger ones are therefore nonglobal. There is no claim that the smaller class is the global minimum over that nonfactorised box.

These additions address the review's significance concern by explaining both why the weighted principle yields a universal design rule and where its exact landscape fails. They do not establish historical priority or a four-star assessment.

## Smaller corrections

The entrywise discrepancy is now explicitly $E=2k$, not confused with edge distance. Matrices with zero diagonal are described as having positive off-diagonal entries. The one-sided second-derivative argument is expanded. Arithmetic complexity is separated from bit complexity and from general interval treatment of an input $t$. Assurance material is in Appendix A and the evidence ledgers. The core text no longer requires the reader to reconstruct conversational provenance.

The title, publication date and local editorial release identifier are fixed in `RELEASE.json`. The manuscript remains anonymous. Public DOI/URL, accountable steward and an effective public reuse licence remain publisher-controlled fields. A proposed licensing choice is recorded in `publisher/LICENCE_HANDOFF.md`; it is not silently activated. Thus the review's licensing suggestion is handed off explicitly, rather than represented as author-approved.

## Source comparison and remaining access limits

Both supplied Psarrakos–Tsatsomeros papers remain the full-text basis for their comparison. Relevant statements of Engel–Sergeev's row-permutation characterisation and Drton–Sturmfels–Sullivant's tetrad result were inspected in primary preprints during this revision. The publisher record for the latter confirms the 2007 issue date and DOI.

Kirkland's 1995 published body and Drury's complete published proof were not obtained. Their publisher/author records support the scoped statements used, not a proof-level novelty clearance. The fixed-trace diagonal-perturbation paper is likewise abstract-level context. Search queries, consulted sections and failures are recorded in `SOURCE_LEDGER.md`. No claim is justified merely by a missing search hit.

## Evidence and acceptance criteria

The reviewed eight-job full replay passed with its 40-file manifest. The new Fraction checker reconstructs four-point determinants by permutation expansion. The independent symbolic checker reconstructs characteristic polynomials and uses rational interval arithmetic on Perron adjugates to certify all 144 inward-coordinate signs in the fragility example. The robust example, factorisation reconstruction and non-nearest recovery example have exact receipts.

The final replay checks file integrity before and after execution. It reruns the reviewed package and the independently supplied referee program in temporary copies; historical originals remain unchanged. Timing is excluded only from the referee result comparison, never from a mathematical check. Every failed, changed or tolerance-tested quantity is identified in the resulting receipt. Negative controls recompute disposable manifests before testing mathematical corruption under ordinary and optimised Python. The bundle is not proof-assistant verification, external specialist endorsement, a deployed website release or an official research-assessment decision.
