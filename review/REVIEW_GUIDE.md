# Review guide — final editorial candidate v1.0

Read `paper/perron_minima.pdf` first. The stronger weighted theorem leads the article. The key additional obligations not covered by the supplied referee review are:

1. Theorem 4.1: the four-cycle difference (4.2), the all-diagonals coefficient extraction, and positive reconstruction from tetrads. The theorem's universal diagonal quantifier is intentional.
2. Proposition 4.2: strict coordinate signs imply a strict local minimum at a box vertex; finite continuity preserves them under small pair-weight perturbations. The nonzero constant polynomial difference forbids a common Perron root.
3. Proposition 3.1: derivatives of the scalar equation and the strict coupling sign. The robust minimax result then follows from a pointwise common optimiser, not a minimax exchange theorem.
4. Section 6.1: distinguish the uniform coefficient, the exact remainder and the input-dependent coefficient. Neither the coefficient nor the returned copy is claimed optimal.

The full proof of the reviewed weighted landscape theorem is in Section 2. Sections 5–6 include the inherited parity mechanism with explicit attribution. Check the even-order tournament restriction before using (5.7).

Run `python replay.py --full --out /path/outside/the/bundle`. It includes the original eight-job replay and the independently supplied referee program. New negative controls are split across four jobs. `python replay.py --smoke` checks the current reference identities and domain guards. The exact new program imports the retained rational core; the separate SymPy implementation does not import it. The referee program imports no submitted routines.

`reference_extensions.json` is a set of frozen expectations, not an axiom: the checks reconstruct determinants, roots and signs independently. Altering its cycle coefficient, a polynomial constant or its robust polynomial value must be rejected even if its manifest is updated. Acceptance uses explicit exceptions, never Python assertions.

Suggested close-prior-art follow-up: the complete Kirkland 1995 arc-reversal paper and the remaining fixed-pair-sum literature. The primary full-text comparisons undertaken here are listed in `SOURCE_LEDGER.md`. A bounded nonmatch is not proof of priority.
