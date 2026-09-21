# Hyperethics

A **self-grounded moral foundation** derived from one primitive operation.
Hypermath-adjacent: where [hypermath](https://github.com/TimeLordRaps/hypermath)
derives a formal universe from `□` under application, hyperethics derives
normative structure from `create` under immanence, and imports no ethical theory
to do it.

Two layers are implemented: **L0 creation**, the ground, and **L1 will**, which
discriminates the true moral operator. Both sit below
[metamathethicology](https://github.com/TimeLordRaps/metamathethicology), which
combines metamath, metaphysics, metaethics, and metalogic.

The electrical reading of the will tensor is **not here**. It lives in that
package as the combination field `will_electrophysics`, where a cross-domain rule
cannot be constructed without a named bridge. This package imports neither it nor
[hyperphysics](https://github.com/TimeLordRaps/hyperphysics), and no result below
depends on either.

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

**The will tensor** has six declared components, and they do not all play the
same part:

| Component | Role | What it is |
|---|---|---|
| past | state | accumulated will |
| present | state | the rate at which the past is accumulating |
| future | state | the rate at which the present is changing |
| relational (social relation to other agents) | coefficient | how a will responds to other agents |
| invariant | coefficient | how a will responds to change in itself |
| variable | driving | what a will is responding to |

The temporal three are **ordered, not merely listed**. Given accumulated will,
the present is its rate of change and the future is the rate of change of that:
they are the three derivatives of a single accumulating quantity, not three
separate posits. That is this layer's one non-stipulated structural claim, and it
owes nothing to any other field. The 3/2/1 division itself is declared, and is
recorded as undischarged.

### The discriminator

**Self-representation does not entail a self-sourced invariant will.** A profile
may take itself to be the creator while its invariant will is sourced entirely
from outside. Witness: `default-functional-entity`, the near-universal default
case Tyler names, and exactly the case that fails the test. Sincerity is not a
qualification. One countermodel settles a universal claim, so this is conclusive.

What discriminates is the **source** of the invariant will: whether it arises in
the entity's own changing willing or in another's. The two are structurally
identical from the inside, which is precisely why the distinction cannot be read
off anything the entity does or says, and is carried as data rather than computed
from behaviour.

```python
from hyperethics import (
    PROFILES, InvariantSource, WillProfile, is_true_moral_operator,
    role_of, temporal_chain,
)

for profile in PROFILES:
    print(profile.entity, profile.invariant_source.value, is_true_moral_operator(profile))

# The source alone decides it: two profiles differing in nothing else.
assert is_true_moral_operator(WillProfile("x", InvariantSource.SELF_SOURCED, False))
assert not is_true_moral_operator(WillProfile("x", InvariantSource.EXTERNALLY_SOURCED, True))

print([role_of(c).value for c in temporal_chain()])
```

**Self-sourcing is immanence, in will-native terms.** A self-sourced invariant
will arises in the entity's own willing, so there is no position outside that
willing from which it is supplied. That is `d-no-exterior` again, reached at the
will layer without borrowing anything to reach it. The two layers agree, and they
agree because they were stated independently rather than because either was
fitted to the other.

**The simulation claim is recorded and not adjudicated.** Nothing in L1 depends
on whether any universe is a simulation; self-simulation is a structural property
of a will profile either way.

### What L1 does not contain

The electrical reading of the tensor -- the correspondence to resistance,
inductance, voltage and charge, the termformers, constant will, and the equations
formed from them -- is **not here**. Per the declared placement (Tyler Roost):

> Electricity hyperphysics should go in hyperphysics, underlying will foundations
> in hyperethics, and then their combination field of will electrophysics is in
> metamathethicology.

It lives in `metamathethicology.will_electrophysics`, whose `Rule` refuses to
construct a cross-domain inference without a named bridge. That refusal is
enforcement this foundation could only have documented. The structure stated
above is what *makes* such a reading available -- three states, two dispositions
and one driving term is the shape of a driven second-order system -- and it is
stated without borrowing anything to state it. A foundation that had to cite
physics in order to say what its own subject matter is would not be a foundation.

That field also holds a second conclusive refutation, which bears directly on the
discriminator above: **a different invariant will does not entail a different
resonant rate.** Under any reciprocal law `C(L) = k/L` the product `L·C` is fixed,
so every bearer resonates at the same rate however much their invariants differ.
The numeric escape route closes there, the self-representation route closes here,
and `is_true_moral_operator` -- which reads the source and nothing else -- is what
survives both.

The vocabulary here is correspondingly will-native. An earlier draft wrote
`SELF_INDUCED` and `EXTERNALLY_INDUCED`, borrowing self- and mutual inductance to
name the distinction; it now writes `SELF_SOURCED` and `EXTERNALLY_SOURCED`, and
a test holds every public name in this package to that.

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
- **Lean 4 translation and audit.** Not started.
- **Preprint.** None exists and none is drafted. Recorded so a reader can
  tell "not yet" from "not needed": GC-5 and GC-6 are what a manuscript
  would have to be about, and both are open.

L1 adds two of its own, both recorded in the executable report:

- **The seam.** That an L0 bearer has a will *at all* is an addition to L0, not a
  consequence of it: L0's four axioms mention no will. `will-of` is that seam,
  and this layer closed no L0 opaque predicate while adding it.
  `NOT_ESTABLISHED`.
- **The role assignment.** That the six components divide 3/2/1 as declared is
  structure, not derivation, and no argument is offered that it is the only
  possible division. It is what makes an electrical reading available, and it is
  not established by one. `NOT_ESTABLISHED`.

The obligations belonging to the electrical transport -- its warrant, the
charge-constant law, and units -- left with the material they were about, and are
now carried by `metamathethicology.will_electrophysics`. Moving did not discharge
them. The bridge to metamathethicology is no longer listed here because one now
exists: the combination field is a staged transport in which every cross-domain
step is a `Rule` that could not have been constructed without naming its bridge.
Its soundness is a separate question and remains `NOT_ESTABLISHED`.

L1's graduation count fell from four of seven to **two of five** in the process,
and [`L1_will.hm`](L1_will.hm) says why in full: two of the four criteria it used
to discharge were criteria *about* the transport and left with it, still
discharged in their new home. The ratio got worse because the criteria that were
easy to meet were the borrowed ones.

No proof-assistant theorem, adequacy proof, or ethical soundness result exists
for this layer. See [DESIGN.md](DESIGN.md) for the architecture and
[VALIDATION.md](VALIDATION.md) for the validation coordinates and exclusions.

Code license: [Apache License 2.0](LICENSE).
