# Local validation receipt

Date: 2026-09-20. Status: the L0 creation ground is validated for the bounded
claims below. The layers above L0, the Lean translation, the bridge to
metamathethicology, and the two named interpretive obligations remain open.

## Coordinates

- Repository `hyperethics`, branch `main`, private repository
  `TimeLordRaps/hyperethics`. The validated bytes were committed and pushed
  unchanged. Publication records where they live; it is not an additional check.
- Python 3.12.8 on Windows, pytest 9.1.1, ruff 0.16.8.
- **No runtime dependencies.** The package imports only the standard library, so
  there are no dependency pins to record and no dependency source to trust. This
  is a design commitment stated in `DESIGN.md`, not an incidental fact.
- The implementation and tests are byte-bound in
  [`validation/source-manifest.json`](validation/source-manifest.json). The digest
  of its canonical `files` mapping is
  `12254a9ec82aa40e0876ff36d94817454b6c25ee5d891049f29039c929f1c910`.
  The manifest identifies tested bytes; it does not sign or certify them.

## Observed checks

```console
python -m pytest tests
python -m ruff check src tests
python -m hyperethics
```

- **71 tests passed with zero skips.** Lint passed with no findings.
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
  soundness result exists for this layer. These are **unimplemented research
  obligations, not skipped passing tests.**
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
