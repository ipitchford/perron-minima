# Exact Perron optimisation with factorised pair interactions

Anonymous · 1.0.1-candidate · **Unrefereed candidate** · [Version DOI](https://doi.org/10.5281/zenodo.23014818)

[Paper](paper/perron_minima.pdf) · [AI index](AI_INDEX.md) · [Claims](CLAIMS.json) · [Publication audit](PUBLICATION_AUDIT.md)

Unrefereed candidate. Written universal arguments are not formally verified. Producer-side replay and a separately written supplied checker do not establish unaffiliated reproduction or authenticated external specialist review. Bounded prior-art checking does not establish priority.

## Run the checks
```sh
python -m pip install -r requirements.txt
python -B replay.py --full --out ../perron-replay
python -OO -B replay.py --full --out ../perron-optimized
```
Eleven jobs. Exact certificate/identity checks are separate from tolerance-tested numerical corroboration. The latter does not promise byte-identical output. Output must be outside the package. [Publication audit](PUBLICATION_AUDIT.md) documents the discovered historical portability limitation and repair.

## Interfaces
Use integer or rational-string JSON inputs with code/public_diagnostic.py: robust, factorisation and approximation commands; code/diagnostic.py accepts rational u for tournament recovery. Examples are in examples/.

## Evidence and reuse
## Claims in one paragraph

The paper classifies all local/global Perron minima in the specified factorised pair-interaction box and evaluates their common spectrum. It derives robust common-optimal design, characterises universal-diagonal order-independent spectra by tetrads, and certifies arbitrarily small nonglobal-minimum obstructions outside factorisation. It also provides an ordered resolvent certificate and constructive Brualdi–Li stability, with conservative uniform constants and stronger input-dependent diagnostics. It does not claim four-star status, exhaustive novelty clearance, arbitrary-switching stability or an optimal edit-recovery algorithm.


[Source ledger](SOURCES.md), [evidence ledger](EVIDENCE_LEDGER.md), [review response](review/RESPONSE_TO_REVIEW.pdf), [assurance](ASSURANCE.md). Historical generation records and nested archives remain unchanged; only declared scopes are replayed.

Original prose/data CC0-1.0, original code MIT; retained-material exceptions in LICENSES.md. Anonymous is the scholarly creator.
