# AI index — Exact Perron minima

Anonymous · 1.0.1-candidate · https://doi.org/10.5281/zenodo.23014818

Unrefereed candidate. Written universal arguments are not formally verified. Producer-side replay and a separately written supplied checker do not establish unaffiliated reproduction or authenticated external specialist review. Bounded prior-art checking does not establish priority.

## Read first
[Claims](CLAIMS.json), [paper PDF](paper/perron_minima.pdf), [TeX](paper/perron_minima.tex), [Markdown](paper/perron_minima.md), [assurance](ASSURANCE.md), [status](STATUS.md).

## Claim and dependency map
- **MIN**, Theorem 2.1: For n>=2, positive m, nonnegative gamma and 0<t<1, every local Perron minimum on the skew box is saturated transitive; all n! transitive orders are globally optimal and share polynomial (2.1).
- **ROBUST**, Theorems 3.2–3.3: Every fixed transitive order simultaneously minimises all admissible parameter instances. Over a rectangular uncertainty box the worst optimum is at (m+, gamma+, t-), and a robustly Schur-stable orientation exists exactly under (3.4).
- **APPROX**, Proposition 3.4: If positive pair weights are within multiplicative kappa of a factorisation, every transitive orientation is within kappa squared of the optimum, for fixed nonnegative diagonal and 0<t<1.
- **TETRAD**, Theorem 4.1: For n>=4 and fixed 0<t<1, positive pair factorisation is equivalent to transitive-order cospectrality for every nonnegative diagonal, and to the four-point determinant/tetrad conditions.
- **FRAGILE**, Proposition 4.2: For fixed 0<t<1, increasing one unit pair weight in order four by every sufficiently small epsilon>0 produces a strict nonglobal local minimum.
- **RECOVERY**, Theorem 6.2: For even-order tournaments n>=4 and 0<t<=1, the specified construction returns a Brualdi–Li copy with spectral deficit at least c_n(u) times its unordered-edge distance; recovery need not be nearest.

The weighted minimum and structural consequences do not depend on the separate tournament maximum. Sections 5–6 reuse the content-identified EP26 qualitative comparison and odd-lattice mechanism, with proofs included. Classical tetrads are not new. [Claim/check map](CLAIM_CHECK_MAP.md) identifies finite versus analytic support.

## Evidence and replay
[Replay entrypoint](replay.py), [requirements](requirements.txt), [environment](ENVIRONMENT.json), [source ledger](SOURCES.md), [citation audit](CITATION_AUDIT.md), [review response](review/RESPONSE_TO_REVIEW.md), [publication audit](PUBLICATION_AUDIT.md), [receipt](REPLAY_RECEIPT.md), [manifest](MANIFEST.sha256).
Run `python -B replay.py --full --out ../perron-replay`; run again with `-OO` for optimisation safety. Eleven current jobs include exact/symbolic checks, forty existing semantic controls, six numerical-comparator corruptions, historical exact/numerical replay and the supplied referee code. Outputs belong outside the archive. Exact reports must match; numerical reports are retained with explicit tolerances/differences, not byte identity.

## Safe reuse
Do not infer arbitrary-switching stability, nearest tournament recovery, sharp uniform constants, or global optimality of the lower perturbed four-point class. Sections 3–4 are not covered by the supplied favourable review. Numerical plots/experiments are not proof. The full path maximum is inherited; Drury retains classical endpoint priority. A claim hash fingerprints text, not mathematical equivalence.

## Rights and provenance
[Provenance](PROVENANCE.md), [component terms](LICENSES.md), [CC0](LICENSE), [MIT code](LICENSE-CODE). Original CC0/MIT; retained supplied material is excluded from blanket relicensing.
