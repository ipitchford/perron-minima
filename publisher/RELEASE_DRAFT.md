# When every locally best ordering is globally best

## For general readers

Some optimisation problems have traps: a solution can look best under every small change and still lose to a distant alternative. This paper identifies a structured family of positive interaction matrices in which those traps do not occur. The pairwise interaction totals factor into contributions from their two vertices, while the vertices may have different weights and different self-interactions.

Every locally optimal directional allocation is a fully ordered one, and every such order gives the same best spectral value. A single equation computes that value. The same order remains optimal when the parameters are unknown within a specified set, producing an exact worst-case stability test.

The special structure matters. Changing just one pair weight by an arbitrarily small amount can create genuine nonglobal local minima. A four-vertex rational example demonstrates the failure without numerical guesswork. Nevertheless a sufficiently accurate factorisation still gives a quantitative near-optimality guarantee.

A second result constructs a Brualdi–Li tournament from a nearly extremal tournament and certifies the relation between its spectral deficit and the number of changed edges. The uniform bound is conservative; the release includes an example where the input-specific certificate is much stronger and the returned configuration is not the nearest one.

## For specialists

The family is $A_{ii}=\gamma_i\ge0$, $A_{ij}=\sqrt{m_im_j}(1+tS_{ij})$, $m_i>0$, $0<t<1$, with $S$ in the continuous skew box. The proof excludes tied left/right Perron-coordinate ratios at a local minimum by a negative second derivative and then forces transitivity. A symmetric product formula supplies fixed-vertex-data cospectrality and the common minimum. The final revision adds a robust parameter theorem and a universal-diagonal converse via four-cycle/tetrad identities, with a certified perturbative obstruction outside factorisation.

The qualitative full-Levinger-path maximum and odd-lattice mechanism are inherited and attributed. The quantitative contribution is the ordered resolvent remainder and constructive alternating repair. The work does not establish a general weighted tournament maximum, sharp edit coefficient, arbitrary-switching stability, or historical priority.

## Assurance and publication fields

Unrefereed analytic candidate. The original main results received a favourable supplied mathematical review; the added structural and robust-design results have not yet received a separate specialist review. Exact and symbolic checks, executable rational diagnostics, corrupted-input tests and replay records accompany the paper. None constitutes proof-assistant verification.

Editorial identifier: EP-PERRON-MINIMA-2026-09-28-v1.0. Public DOI, canonical release URL, reuse licence and accountable stewardship are to be assigned by the publisher. This draft does not imply deployment.
