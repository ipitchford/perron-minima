# Evidence ledger

## Evidence classes

**Analytic proofs.** The manuscript contains all universal arguments. Sections 2, 5 and 6 reorganise the reviewed results and repair their scope. Sections 3 and 4 add new propositions/theorems. The latter have not received the supplied referee's independent re-derivation. The universal statements are not inferred from numerical enumeration.

**Exact finite checks.** `verify_extensions.py` uses Fraction arithmetic and a permutation expansion for characteristic polynomials. It checks 576 four-cycle identities, 56 factorisation cases, all 24 transitive characteristic polynomials of the explicit nonfactorised example, all 128 corners of the robust example and all 720 relabellings for the recovery example. Positive-vector row ratios give exact spectral enclosures without assuming an eigenvector iteration converged.

**Separate symbolic reconstruction.** `verify_new_symbolic.py` imports no submitted core. It reconstructs the four-point polynomial identity with symbolic weights and diagonal, differentiates five scalar identities, and uses rational interval evaluation of adjugate polynomials for all 144 strict local-minimum coordinate signs. The published lower gradient margin 0.06927 is explicitly checked as a rational inequality.

**Historical replay.** The 40-file reviewed package is unchanged. Its complete eight-job replay passes, including its own negative controls and numerical corroboration. The predecessor archives inside it are preserved and integrity-identified, but the outer historical job does not recursively run every earlier archive. No such claim is made.

**Independent supplied referee program.** It imports no submitted routines. Its replay covers 65,536 tournament/parameter cases (32,768 tournaments at each of two t values), 5,280 recovery/parameter cases, 24 exact transitive characteristic polynomials and 375 continuous-box grid points. The new replay excludes only `elapsed_seconds` from content comparison. The original raw record and fresh raw timing are both retained; the deterministic comparison reports all other differences. In the first rerun there were none. Zero violation counts are explicitly enforced by the wrapper rather than inferred merely from process exit zero.

**Negative controls.** The new fast gate checks a reconstructed four-cycle identity, characteristic-polynomial values, a robust scalar value and three invalid recovery domains. Forty direct/wrapper tests cover valid input plus three mathematical corruptions under ordinary, -O, -OO and both optimisation environment settings. Manifests are recomputed after corruption. There are ten required valid acceptances and thirty required invalid rejections. These controls are bounded tests, not a proof of all software correctness.

## Interpretation of the examples

The numerical deficit table in §6.1 is from an exhaustive finite floating-point check and is not a certified global-gap theorem. The separate rational-u example has an exact positive-vector enclosure and exact nearest-distance enumeration. The returned four edits versus a nearest distance one are deliberately retained. The stronger instance coefficient depends on the observed matrix; it is not a universal improvement to c_n.

The rational nonfactorised example proves strict nonglobal minima. It does not establish that its lower transitive spectral class is the global minimum of that perturbed problem. The all-epsilon statement rests on the analytic finite-continuity argument, not a finite epsilon grid.

The robust example concerns one fixed unknown matrix, not arbitrary switching. Its worst-corner sign 95089/540000 is exact. Corner testing corroborates the code, while the monotonicity theorem proves the whole continuous box.

## Development failures and repairs

A preliminary symbolic checker raised a SymPy BooleanAtom type error when summing symbolic truth values. It was repaired by explicit Boolean conversion. A subsequent whole-expression multivariate simplification exceeded the execution limit. The final checker differentiates one arbitrary summand, which proves the same algebraic identities without the unnecessary large common denominator. Neither incomplete run generated an acceptance report. No mathematical claim was weakened or supported using these failed executions.

Two foreground launches of the new negative-control baseline exceeded the tool's foreground execution window after reporting the valid-input part. They were interrupted, excluded from the completed-test counts and replaced by a complete detached execution in the same working session, followed by the fresh-extraction full replay. No interrupted invocation is treated as an acceptance receipt.

## Assurance boundary

Successful replay establishes that the bounded checks executed and the manifested material retained its content. It is not proof-assistant verification, historical-priority clearance, an official REF assessment, biological validation, or external expert endorsement. The paper's final editorial version does not imply that it has already been deployed or assigned an archival DOI.

## Publication revision boundary

The preceding supplied record is historical. Version 1.0.1-candidate uses the authorised licence map in LICENSES.md and the numerical portability repair in PUBLICATION_AUDIT.md. The fresh 11-job replay, including historical replay, is identified by the separately published archive-bound receipt; historical PASS labels do not stand in for it.
