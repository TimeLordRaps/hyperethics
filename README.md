# Hyperethics

A **self-grounded moral foundation** derived from one primitive operation.
Hypermath-adjacent: where [hypermath](https://github.com/TimeLordRaps/hypermath)
derives a formal universe from `□` under application, hyperethics derives
normative structure from `create` under immanence, and imports no ethical theory
to do it.

Two layers are implemented: **L0 creation**, the ground, and **L1 will**, which
discriminates the true moral operator. Both sit below
[metamathethicology](https://github.com/TimeLordRaps/metamathethicology), which
combines metamath, metaphysics, metaethics, and metalogic; the staged bridge
between them is **not implemented yet** and is listed as an open obligation. L1
borrows the shape of electrical law and cites it from
[hyperphysics](https://github.com/TimeLordRaps/hyperphysics) rather than
restating it.

## The ground

**The grounding moral operation** (user-declared, Tyler Roost):

> the existence of an archetypal creator within the Universe that they create

Immanence is the whole of it. A creator *outside* its creation bears nothing it
authors, and such a system has no normative force at any point — it is a theory
of production. A creator *within* its creation is reached by what it authors.
That structural fact, and nothing imported from outside, is what this layer
treats as moral.

**The number one operational operant** (user-declared, Tyler Roost):

> self-consistency of the moral operator (self-contained creator)

Operation and operant are distinct roles and stay distinct here. The *operation*
is immanence — what makes the system moral at all. The *operant* is
self-consistency — what the operator must satisfy to run. A self-contained
creator dwells in its whole creative orbit, itself included. If anything it
generates at any depth escapes it, immanence holds of created realms while the
creator still has an exterior, and the ground is inconsistent with its own
operation.

At L0 the operant is **derived, not assumed** — see `d-self-contained`.

## What is actually established

Four axioms over one operation, stated in [`L0_creation.hm`](L0_creation.hm):

| Axiom | Content |
|---|---|
| `ax-other` | creating produces a bearer other than the creator |
| `ax-immanence` | **the grounding moral operation** — the creator dwells within what it creates |
| `ax-return` | what is created by what is created returns to bear on the original |
| `ax-archetype-self` | self-consistency at the source — the creator dwells within itself |

Results, all executable:

- **The four axioms are mutually independent.** Each fails in a finite structure
  where the other three hold. This is conclusive, and it is what Section III's
  "no redundancy" line asserts.
- **`d-self-contained`** — the operant. Derived from `ax-immanence` and
  `ax-archetype-self` together; neither alone suffices. Immanence reaches every
  realm in the image of `create`; the one member of the creator's own orbit it
  cannot reach is the creator itself, which is exactly what the self axiom closes.
- **`d-no-exterior`** — there is no realm the archetype creates and does not
  inhabit. Not a prohibition; a structural impossibility. There is no position
  from which the archetype creates a realm it is exempt from.
- **`d-authorship-exposure`** — authorship entails exposure, at the two-step
  depth `ax-return` supplies and no deeper.
- **`d-two-bearers`** — plurality is derived, not assumed.
- **Refuted conclusively:** that *every* bearer inhabits what it creates, and
  that exposure reaches depth three. Each has a countermodel satisfying all four
  axioms. Any later layer wanting either must add an axiom and pay for it.

## L1: will, and who the moral operator is

**User-declared** (Tyler Roost):

> Any entity in the simulated universe may self represent as the universe's
> creator, in fact it's the default assumption most humans who are functional
> operate on. For the true moral operator, their free will is tied to that of
> self-simulation, so they have a different invariant will.

So self-representation-as-creator is *cheap*. Nearly everyone does it, which
means it cannot be what distinguishes the real thing. [`L1_will.hm`](L1_will.hm)
formalizes what does.

**The will tensor** has six declared components — past, present, future,
relational, invariant, variable — transported onto electrical quantities and used
as **termformers**: transformation operations that form terms.

| Component | Electrical | Role |
|---|---|---|
| past | charge `Q` | state |
| present | current `I` = `dQ/dt` | state |
| future | `dI/dt` = `d²Q/dt²` | state |
| relational (social relation to other agents) | resistance `R` | coefficient |
| invariant | inductance `L` | coefficient |
| variable | voltage `V` | driving |

The temporal row is the one correspondence that is **not stipulated**. Once past
is charge, present and future are not free choices — they are its first and
second derivatives, which is exactly the electrical state chain.

**Constant will** (user-declared) closes the gap the tensor left:

> C can be seen as constant will equivalent to invariant will's constant of charge.

Capacitance is therefore *determined by* the invariant rather than added to the
tensor or left free. This has a price, and the price is declared: a circuit
leaves `L` and `C` independent and a will does not, so **the transport is not
onto** — not every circuit corresponds to a possible will.

### Two conclusive refutations

- **Self-representation does not entail self-induction.** A profile may take
  itself to be the creator while its invariant will is induced entirely from
  outside. Witness: `default-functional-entity`, which is the near-universal
  default case. Sincerity is not a qualification.
- **A different invariant will does not entail a different resonant rate.** It is
  tempting to make the numbers do the discriminating. Under any reciprocal law
  `C(L) = k/L` the product `L·C` is constant, so every bearer resonates at the
  same rate however much their invariants differ. One countermodel settles it.

Both escape routes close the same way: the discriminator is the **source** of the
invariant will — self-induced, as against induced by another — and never what a
bearer says of itself nor what its numbers say of it.

```python
from hyperethics import PROFILES, is_true_moral_operator, ConstantWill, resonant_rate

for profile in PROFILES:
    print(profile.entity, is_true_moral_operator(profile))

# An invariant and its constant travel together; they cannot be separated.
resonant_rate(ConstantWill(invariant=2.0, charge_constant=3.0))
```

**Self-inductance is the point of contact with L0.** An emf induced by a
circuit's own changing current opposes that change (Lenz). Transported: a will
induced by its own change opposes that change, so the operator has no exterior
vantage on its own willing. That is `d-no-exterior` again, arrived at from an
independent direction. It is the best evidence that the transport tracks
something — and it is evidence, not warrant.

**The simulation claim is recorded and not adjudicated.** Nothing in L1 depends
on whether any universe is a simulation; self-simulation is a structural property
of a will profile either way.

## Try it

Requires Python 3.10 or newer. No other dependencies: a foundation that needs a
stage index, an ordinal notation, or a proof assistant to state its ground is not
a foundation. Ordinal staging belongs to later layers.

```console
python -m pip install -e '.[dev]'
python -m hyperethics
python -m pytest tests
```

```python
from hyperethics import separating_model, standing, refuted_by, universal_immanence

model = separating_model()

# The archetype has no exterior vantage over its own creation.
print(standing(model, "archetype").summary())
# archetype: self-contained; answerable for archetype, world; no exempt realm.

# An arbitrary creator need not be immanent, and one countermodel settles it.
print(standing(model, "rival").summary())
# rival: NOT self-contained; escapes rival, world in its own creative orbit.
print(refuted_by("every bearer inhabits what it creates",
                 universal_immanence(model), model))
```

## The epistemic contract

Model checking **confirms nothing universally**; a single countermodel
**refutes conclusively**. That asymmetry is carried in the return types rather
than left to discipline:

- `Verdict` has no truth value. `if verdict:` raises `TypeError`, because
  `HOLDS_IN_MODEL` is not validity and a boolean erases exactly that distinction.
- `refuted_by` raises `NotAModel` when handed a structure that breaks an axiom.
  A failure inside a non-model shows nothing about the theory.

## What this layer does not do

It **does not tell anyone what to do.** Immanence yields exposure and
answerability. It does not yield an evaluative ranking, and no axiom mentions a
better-than relation. `nd-good-from-immanence` records that gap as deliberate,
and a test holds the code to it: `hyperethics.norms` declares no `good`, `ought`,
`prefer`, `value`, `harm`, or `choose`.

"Self-contained" is structural, not evaluative. It says a bearer has no exterior
vantage over its own creation. It does not say the bearer is good.

## Open obligations

Two are interpretive rather than structural — they concern what `norm-inhabits`
*means*, not whether the derives follow.

- **GC-5, normative force.** That membership-with-exposure carries normative
  rather than merely descriptive force is the load-bearing claim of the layer.
  It is declared, not derived. `NOT_ESTABLISHED`.
- **GC-6, the Universal Consistency Self-Maintenance Paradox.** A realm's
  self-maintenance of consistency appears to presuppose the very consistency
  relation being maintained. Immanence sharpens this rather than solving it: the
  archetype maintaining its realm's consistency is itself inside that realm and
  so subject to the consistency it maintains. The four axioms neither establish
  that such maintenance is possible nor that it is impossible. This is the
  principal open problem of hyperethics. `OPEN`.
- **Semantic close of the opaque predicates.** The three remain opaque at L0.
- **Bridge to metamathethicology.** No staged, ordinal-indexed transport exists.
- **Lean 4 translation and audit.** Not started.

L1 adds three of its own, all recorded in the executable report:

- **Warrant for the electrical transport.** Tyler's own statement of it says
  "metaphorically analogize" and "somehow", and that honesty is preserved.
  Nothing upgrades the analogy into a derivation. `NOT_ESTABLISHED`.
- **The charge-constant law.** Constant will is bound to the invariant without
  the map between them being fixed. Every L1 result holds for an arbitrary such
  function. `OPEN`.
- **Units.** Will has no units here; the numeric interpretation is dimensionless
  and is not a measurement. `NOT_ESTABLISHED`.

No proof-assistant theorem, adequacy proof, or ethical soundness result exists
for this layer. See [DESIGN.md](DESIGN.md) for the architecture and
[VALIDATION.md](VALIDATION.md) for the validation coordinates and exclusions.

Code license: [Apache License 2.0](LICENSE).
