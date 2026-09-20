# Local validation receipt

Date: 2026-09-20. Status: the L0 creation ground and the L1 will layer are
validated for the bounded claims below. The layers above L1, the Lean
translation, the bridge to metamathethicology, and the five named interpretive
obligations remain open.

## Coordinates

- Repository `hyperethics`, branch `main`, private repository
  `TimeLordRaps/hyperethics`. The validated bytes were committed and pushed
  unchanged. Publication records where they live; it is not an additional check.
- Python 3.12.8 on Windows, pytest 9.1.1, ruff 0.16.8.
- **No runtime dependencies.** The package imports only the standard library, so
  there are no dependency pins to record and no dependency source to trust. This
  is a design commitment stated in `DESIGN.md`, not an incidental fact. L1 cites
  `hyperphysics` for the laws it borrows but does not import it at runtime.
- The implementation and tests are byte-bound in
  [`validation/source-manifest.json`](validation/source-manifest.json). The digest
  of its canonical `files` mapping is
  `811dc1587c709326f78cf90f262b1b201b756c14abfd2c7995979d34d30e7ead`.
  The manifest identifies tested bytes; it does not sign or certify them.

## Observed checks

```console
python -m pytest tests
python -m ruff check src tests
python -m hyperethics
```

- **The suite was run twice, and both runs are reported here.**
  - `python -m pytest tests` alone: **135 passed, 1 skipped.** The skip is the
    whole of `tests/test_citations.py`, which requires `hyperphysics`. A skip
    means the citations were NOT checked on that run; it does not mean they were
    checked and passed.
  - With `hyperphysics` on the path: **149 passed, zero skips.** The citation
    cross-check executed. This is the run the claims below rest on.
  - Lint passed with no findings on both.
- The executable report exits zero and reports its open obligations as `OPEN`,
  `NOT_ESTABLISHED`, or `NOT_IMPLEMENTED`. Tests assert that it never upgrades
  one of these, and that it never asserts a checked claim was proved or is valid.
- **Axiom independence is established conclusively.** Four finite structures,
  each satisfying exactly three axioms and failing the fourth. One countermodel
  settles the independence of one axiom, so this result does not depend on the
  number of confirming models.
- **Two universal claims are refuted conclusively**, each by a structure
  satisfying all four axioms: that every bearer inhabits what it creates
  (`separating`, witness `rival`), and that exposure reaches depth three
  (`orbit`, witness `archetype`).
- The operant `d-self-contained` holds in every model of the axioms and fails in
  both `without-immanence` and `without-archetype-self`, at exactly the predicted
  realm in the latter. This is the executable form of the claim that the operant
  needs both axioms and that neither alone suffices.
- Negative cases reject a partial `create`, a `create` leaving the carrier, an
  archetype outside the carrier, relations naming unknown realms, duplicate realm
  names, a non-positive exposure depth, and unknown bearers passed to the norms
  functions.
- `Verdict.__bool__` raises, and `refuted_by` raises `NotAModel` when handed a
  structure that breaks an axiom. Both are tested directly, because the epistemic
  contract is only real if it is enforced.
- `hyperethics.norms` is asserted to declare no `good`, `ought`, `prefer`,
  `value`, `harm`, or `choose`, and bearer summaries are asserted free of
  evaluative vocabulary.

### L1 will

- **Two universal claims are refuted conclusively.** That self-representation as
  creator entails a self-induced invariant will, witness
  `default-functional-entity`; and that a different invariant will entails a
  different resonant rate, witnesses being two bearers with invariants 2 and 3
  under the reciprocal law `C(L) = 6/L` that share one rate. One countermodel
  settles a universal claim, so neither result depends on how many cases agreed.
- **The discriminator is asserted not to be the numeric shadow.** Exactly one
  canonical profile is a true moral operator; self-representation spans both
  verdicts; and the test for operator status reads `InvariantSource` alone.
- **The binding of constant will to the invariant is enforced by type, not by
  convention.** `resonant_rate` and `damping_ratio` reject a loose pair of
  numbers with `TypeError`, so an invariant cannot be paired with a capacity that
  is not its own.
- **Every termformer's citation is checked against `hyperphysics`**, when it is
  importable: the cited law exists, and the quoted algebraic form equals the
  source's, character for character. The four borrowings are additionally built
  into `hyperphysics.Transport` objects and validated through that package's own
  interface, including the declared departure on capacitance.
- Every termformer is asserted to disclaim a unit or a mechanism, and the
  `accumulated-drop` disclaimer is asserted to name the parameter independence
  the will departs from.
- The report is asserted to publish the transport, the four superseded and one
  declared capacitance readings, the departure from the source domain, and all
  four conclusive refutations. A report that quietly dropped one of these would
  fail.

## What the checks do not establish

Model checking **confirms nothing universally**. Every claim reported as
`HOLDS_IN_MODEL` was checked against finite structures with at most three realms
and is not thereby valid. Only the independence result and the two refutations
are conclusive, and they are conclusive because a single countermodel settles a
universal claim, not because many models agreed.

- `GC-5`, that `norm-inhabits` carries normative rather than merely descriptive
  force, is **declared, not derived**. It is the load-bearing interpretive claim
  of the entire layer and nothing here discharges it.
- `GC-6`, the **Universal Consistency Self-Maintenance Paradox**, is **open**.
  `d-self-contained` closes the creative orbit structurally while being stated
  using `norm-inhabits`, the very relation immanence supplies. The derive neither
  resolves the paradox nor depends on its resolution.
- The three opaque predicates have no L1 semantic close. `other_is_nonidentity`
  shows a model of the axioms reading `other` reflexively, so the close is a real
  constraint that has not been imposed.
- No proof-assistant theorem, adequacy proof, empirical validation, or ethical
  soundness result exists for either layer. These are **unimplemented research
  obligations, not skipped passing tests.**
- **The warrant for the electrical transport is not established.** L1 borrows the
  algebraic shape of electrical law. That `d-self-simulation` reproduces L0's
  `d-no-exterior` from an independent direction is evidence the transport tracks
  something; it is not a derivation, and `GC-5` is not discharged. Tyler's own
  statement of the transport says "metaphorically analogize" and "somehow".
- **No will quantity has units or an empirical reading.** The numeric functions
  are dimensionless and measure nothing. Passing them numbers does not make a
  will measurable.
- **The charge-constant law is open.** Constant will is declared to be the
  invariant's constant of charge, which binds it without fixing the map. Every
  L1 result is stated for an arbitrary such function; results depending on a
  particular one are not available and are not claimed.
- **The six-component decomposition of will is declared, not derived.** No
  argument is offered that six is the right number, that these six are
  independent, or that an L0 bearer has a will at all. `will-of` is a new opaque
  predicate and a new seam between the layers.
- **The simulation claim is not adjudicated.** It is recorded as a user-declared
  framework claim, preserved exactly, and is neither verified nor contradicted.
  Nothing in L1 depends on it.
- Whether finite realm models are adequate to the intended reading of an
  archetypal creator within its universe is **not established**. The models are
  finite interpretations of four primitives. Reading a realm as a person, a
  world, an action, or an agent is an interpretation L0 does not license.

## Exclusions

- `OS_CAPABILITY_GUARD`: Linux and macOS execution and cross-platform build
  comparison were not run on this Windows host.
- `PERFORMANCE_OR_DURATION_EXCLUSION`: no exhaustive search over realm models was
  performed. The countermodels are hand-constructed and individually checked;
  no claim is made that they are minimal or that the search space was covered.
  Other Python versions were not exercised.
- `EXTERNAL_SERVICE_BOUNDARY`: no continuous integration, release publication,
  or package-index installation was performed. A wheel and source distribution
  were not built.
- The host checker trusts Python and ordinary in-process object integrity.
  Arbitrary code with permission to mutate the running interpreter is outside
  the trust model.

## Environment note

The `C:` volume on this host was at 100% capacity during this work, which caused
the initial dependency install to fail with `ENOSPC` until the temporary
directory was redirected to `E:`. This affected tooling only. It did not affect
the checked bytes, and the recorded manifest digest reproduces against the tree.
