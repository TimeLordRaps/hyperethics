# Local validation receipt

Date: 2026-09-20. Status: the L0 creation ground and the L1 will layer are
validated for the bounded claims below. The layers above L1, the Lean
translation, the transport of L0 standing into an operation space, and the named
interpretive obligations remain open.

This receipt supersedes the one recorded earlier the same day. The electrical
reading of the will tensor left this package between the two runs, on a declared
placement recorded in `L1_will.hm`; what it covered is now covered by
`metamathethicology`'s own receipt. The counts below fell accordingly, and a
lower count here is the expected consequence of that move rather than a loss of
coverage.

## Coordinates

- Repository `hyperethics`, branch `main`, private repository
  `TimeLordRaps/hyperethics`. The validated bytes were committed and pushed
  unchanged. Publication records where they live; it is not an additional check.
- Python 3.12.8 on Windows, pytest 9.1.1, ruff 0.16.8.
- **No runtime dependencies.** The package imports only the standard library, so
  there are no dependency pins to record and no dependency source to trust. This
  is a design commitment stated in `DESIGN.md`, not an incidental fact. As of
  this receipt the package also carries no *citation* of another field: the
  borrowing that needed one moved to `metamathethicology.will_electrophysics`,
  and the cross-checks holding it to `hyperphysics`' exact bytes moved with it.
- The implementation and tests are byte-bound in
  [`validation/source-manifest.json`](validation/source-manifest.json). The digest
  of its canonical `files` mapping is
  `4bc06ea5963d400e30e58705610549e30437a87e22f52b44cd8bea9ae5b64e74`.
  The manifest identifies tested bytes; it does not sign or certify them.

## Observed checks

```console
python -m pytest tests
python -m ruff check src tests
python -m hyperethics
```

- **96 passed, zero skips, one run.** The package has no optional import and no
  conditional path, so there is no second configuration to report. The earlier
  receipt reported two runs because `tests/test_citations.py` required
  `hyperphysics`; that module now lives in `metamathethicology`, and the dual-run
  disclosure lives in that repository's receipt.
- Lint passed with no findings.
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

- **One universal claim is refuted conclusively.** That self-representation as
  creator entails a self-sourced invariant will, witness
  `default-functional-entity`, which represents as creator while its invariant
  will is sourced entirely from outside. One countermodel settles a universal
  claim, so the result does not depend on how many cases agreed.
- **A second refutation bearing on the same discriminator is proved elsewhere.**
  That a different invariant will entails a different resonant rate is refuted in
  `metamathethicology.will_electrophysics`, where the transported numbers live.
  It is recorded in `L1_will.hm` and published by this report as a fact this
  layer relies on and does not prove. **Nothing in this repository checks it.**
  That package's receipt is where the check is recorded.
- **The discriminator is asserted to read the source and nothing else.** Exactly
  one canonical profile is a true moral operator; self-representation spans both
  verdicts; and two profiles differing only in `InvariantSource` receive opposite
  verdicts.
- **The tensor's structure is checked.** The six components are asserted to be
  exactly the declared ones in the declared order; every component has exactly
  one role; every role is occupied; the division is three states, two
  coefficients and one driving term; and the temporal chain is asserted to be the
  state components, in derivative order.
- **The layer is asserted not to contain what left it.** Thirteen names belonging
  to the transport are asserted absent from `hyperethics.will`; no public name
  and no enum value in that module contains an electrical term; and the package
  is asserted not to import its own combination field. These are the checks that
  keep a documented split from quietly becoming a duplicated one, and the
  vocabulary check is the one that matters most, because a borrowing hides in
  names long after it has been removed from imports.
- **The report is asserted to publish the tensor, its roles, the refutation this
  layer owns, the refutation it no longer owns, and the name of the field that
  took the rest.** A report that quietly dropped one of these would fail.
- Negative cases reject a non-`Component` passed to `role_of`, a non-`Role`
  passed to `components_with_role`, and profiles carrying a non-enum source, an
  empty entity, or a non-boolean self-representation.

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
- **The six-component decomposition of will is declared, not derived.** No
  argument is offered that six is the right number, that these six are
  independent, or that an L0 bearer has a will at all. `will-of` is a new opaque
  predicate and a new seam between the layers, and L1 added it while closing none
  of the three that were already open at L0.
- **The 3/2/1 role division is declared, not derived.** It is the claim an
  electrical reading of the tensor depends on, and it is not established by one.
  A reading that succeeds does not license the structure it presupposed.
- **The obligations belonging to the transport are not discharged by having
  moved.** The warrant for the transport, the charge-constant law, and the
  absence of units are now carried by `metamathethicology.will_electrophysics`
  and appear in its receipt, not this one. Moving material relocates the
  obligation; it does not retire it. `hyperphysics` records the general form of
  the warrant problem as its own `GC-4`, and no field in this family fills it.
- **Nothing here checks the transport's citations.** The earlier receipt for this
  repository reported a run in which every borrowed law was checked against
  `hyperphysics` character for character. No run of this suite does that any
  more, because the module that did it is no longer here. Do not read the earlier
  receipt as covering these bytes.
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
