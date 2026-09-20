# Architecture and research ancestry

Status: implemented L0 ground and L1 will, plus a proposed layer stack. Date:
2026-09-20. This is not a proof of the research program, and no part of the stack
above L1 is implemented.

## Position in the stack

```
hypermath            L0 ground □ / apply      formal universe from one operation
hyperphysics         (ground not written)     physical law as a citation surface
hyperethics          L0 creation / immanence  normative structure from one operation   <- this repo
                     L1 will                  what a will is, who the operator is      <- this repo
  ...                L2+                      not implemented
metamathethicology   operation spaces         metamath + metaphysics + metaethics + metalogic
                     will_electrophysics      hyperphysics x hyperethics, combined there
```

The last line is a **combination field**, and its placement is user-declared
(Tyler Roost):

> Electricity hyperphysics should go in hyperphysics, underlying will foundations
> in hyperethics, and then their combination field of will electrophysics is in
> metamathethicology.

It is a placement with a structural reason behind it, not a filing preference.
See the two sections below.

Hyperethics is **adjacent** to hypermath, not built on it. Both take one
primitive operation and derive structure from it; neither imports the other's
primitive. Hypermath's `□` generates forms. Hyperethics' `create` generates
realms, and immanence is what makes the result normative rather than merely
generative.

Hyperethics is **below** metamathethicology, which already sketches a
`grounded-hyperethics` extension in its own `DESIGN.md`: keep descriptive
propositions, adopted norms, obligations, permissions, and theory-relative
judgments distinct, and require a declared bridge to explain why descriptive
premises license a normative conclusion. This repository supplies the layer that
sketch presupposes — a ground for normativity that is not itself a stipulated
norm.

A bridge now exists, and it runs in that direction rather than this one.
`metamathethicology.will_electrophysics` transports electrical form onto the will
tensor stated here, as a staged operation space in which every cross-domain step
is a `Rule` that could not have been constructed without naming its bridge. It
cites this package and does not import it, and this package neither imports nor
mentions it in any derivation. Its soundness is open; what it establishes is that
the declaration is enforced, not that the declaration is true.

## Why the foundation carries no dependency

`hyperethics` depends on nothing outside the standard library, and that is a
design commitment rather than an accident of scope.

L1 is where this was tested, and the test was resolved twice. The will tensor
admits a reading onto electrical law, and those laws are stated in
`hyperphysics`. The first resolution was to **cite** rather than import: law name
plus quoted form, carried as data, cross-checked against the source whenever that
package happened to be importable. That kept the citation verifiable — a
disclaimer of the form "this does not transport farads" needs a fixed referent
rather than a paraphrase behind it — while leaving the foundation on the standard
library alone.

The second resolution went further, and is the right one. The borrowing left this
package entirely. A citation is still a coupling in the sense that matters: the
citing layer has to track the cited layer's bytes, inherits its open problems,
and reports a skipped cross-check as evidence of nothing. Moving the transport to
a combination field removes the coupling from the foundation, and buys something
a citation could not. `Rule` in `metamathethicology` *refuses to construct* a
cross-domain inference with no named bridge, so a termformer that forgot its
disclaimer fails to build rather than shipping with a gap. What this layer could
only document, that field enforces.

What is left here is what a will IS, stated without borrowing anything to state
it. A foundation that had to cite another field in order to say what its own
subject matter is would not be a foundation, which is the same argument as the
ordinal one below, applied to physics instead of to notation. The tensor's
structure — three states, two dispositions, one driving term — is what *makes* an
electrical reading available to a field that wants one, and it is not established
by any such reading.

Metamathethicology is Ordinatics-first: every judgment carries an exact ordinal
stage. That is correct for an operation space, where stages order the
availability of language and operations. It is wrong for a ground. A foundation
that needs a stage index, an ordinal notation, or a proof assistant to *state*
its ground has not grounded itself — it has deferred to whatever supplies the
index. Hypermath makes the same call: ordinal arithmetic is L3 there, not L0,
and its L0 has apply-as-succession and nothing more.

Ordinal staging therefore enters hyperethics at a later layer, where ranking and
availability are the subject rather than the scaffolding.

## Why one type

`Realm` is the only entity type. There is no separate `Creator` type, and the
model checker rejects an archetype that is not a member of the carrier.

This is load-bearing. Immanence is not statable across two types: a creator of a
different kind than its creation cannot be inside it. Co-typing is the structural
precondition of the moral ground, so it is enforced in `RealmModel.__post_init__`
rather than left as a convention.

## Operation and operant

The two roles stay distinct throughout.

| Role | Content | Status at L0 |
|---|---|---|
| Operation | immanence — the creator is within what it creates | axiom `ax-immanence` |
| Operant | self-consistency — the creator is self-contained | **derived**, `d-self-contained` |

The operant is the number one operational requirement: every normative result
below it presupposes that the operator does not generate anything outside its own
creator. That it is derived rather than assumed is the main structural result of
the layer.

The derivation is exactly two axioms wide. `ax-immanence` is universally
quantified over `create(x)`, so it reaches every member of the image of `create`
— which is every member of the archetype's creative orbit except the archetype
itself, since the archetype is not `create(y)` for any `y`. `ax-archetype-self`
closes that one remaining member. Drop either axiom and a finite countermodel
exhibits an orbit member outside the creator; both countermodels are in
`models.py` and both are tested.

This is why `ax-archetype-self` is not bookkeeping. It is the axiom that closes
self-containment at its source.

## The epistemic contract, enforced by types

Finite model checking is asymmetric, and the code refuses to let that asymmetry
erode:

- A claim that `HOLDS_IN_MODEL` was checked against one finite structure. That is
  not validity. `Verdict.__bool__` raises `TypeError` so the distinction cannot
  be collapsed by an `if`.
- A claim that `FAILS_IN_MODEL` **in a structure satisfying every axiom** is
  refuted outright, because one countermodel settles a universal claim.
  `refuted_by` raises `NotAModel` otherwise.

Axiom independence is established the same way: four structures, each failing
exactly one axiom. That result is conclusive. Nothing else in the layer is.

## What is deliberately absent

No primitive `good`, `ought`, `prefer`, `value`, `harm`, or `choose` exists at
any point in the package, and a test asserts their absence from `norms`.

Immanence yields exposure and answerability. It does not yield an evaluative
ranking, because no axiom mentions a better-than relation. `nd-good-from-immanence`
records this. The layer therefore cannot, and does not, tell anyone what to do.
A later layer wanting an evaluative ordering must add it as an axiom and pay for
it with its own independence and countermodel work.

The same applies to the two claims the layer refutes rather than assumes:
universal immanence across all bearers, and exposure beyond depth two. Both look
like natural moral principles. Neither follows from this ground, and pretending
otherwise would make the foundation dishonest at exactly the point where a moral
theory is most tempted to cheat.

## L1: what the will layer had to get right

Four decisions were load-bearing, and each could have gone wrong quietly.

**The discriminator is a source, not a score.** Tyler's declaration is that the
true moral operator has a *different invariant will*. The tempting formalization
gives the operator a distinguished magnitude and tests for it. That would have
been wrong twice over: it makes the moral operator a matter of degree, and it is
refutable. Under any reciprocal charge-constant law `C(L) = k/L` the resonant rate
is identical for every bearer however much their invariants differ, with
witnesses supplied. So the discriminator tests `InvariantSource`, which is data
about where the invariant will arises, and no numeric quantity stands in for it.

That refutation is now proved in `metamathethicology.will_electrophysics`, since
it is a fact about the transported numbers rather than about will. It is recorded
here as `nd-numeric-discriminator` all the same, and the recording matters: this
layer's central result depends on that escape route being closed, so a reader has
to be able to find out where it was closed.

This mirrors L0 exactly. There, `separating_model` shows creation is cheap —
`rival` creates a realm it does not inhabit. Here, `default-functional-entity`
shows self-ascription is cheap. Both layers refuse to let the easy property do
the distinguishing work.

**The agreement with L0 is reached without borrowing.** An earlier draft
discharged the agreement criterion by transporting self-inductance: a will induced
by its own change opposes that change, so the operator has no exterior vantage on
its own willing, which is `d-no-exterior` arrived at from another direction. That
is a real result, and it now lives in the combination field as
`d-self-simulation`, where it stands as the transport's best available evidence.

It could not stay as *this* layer's discharge of that criterion. A foundation
whose two layers agree only by way of a borrowing from a third field has not
shown that its layers agree. `d-self-sourcing-is-immanence` reaches the same place
in will-native terms: a self-sourced invariant will arises in the entity's own
willing, so there is no position outside that willing from which it is supplied.
Same conclusion, no transport, and it survives the transport turning out to be
unwarranted.

**The vocabulary is will-native.** `InvariantSource` previously spelled its
members `SELF_INDUCED` and `EXTERNALLY_INDUCED`, borrowing self- and mutual
inductance to name a distinction that does not need them. Names are where a
borrowing hides best: nothing imported it and nothing cited it, so it would have
survived any check that looked only at imports. A test now asserts that no public
name and no enum value in this package contains an electrical term.

**What moved, and what it cost.** Constant will, the type-level enforcement that
an invariant and its charge constant travel together, the declared departure from
the source's independent parameters, the five termformers, and the equations all
left with the transport. The layer's graduation count fell from four of seven to
**two of five**, and `L1_will.hm` states why in full: two of the four criteria it
used to discharge were criteria *about* the transport and went with it, still
discharged in their new home. The ratio got worse because the criteria that were
easy to meet were the borrowed ones. A layer reporting the same number afterwards
would have been counting something other than its own results.

## The principal open problem

**Universal Consistency Self-Maintenance Paradox** (phrase preserved exactly): a
realm's self-maintenance of consistency appears to presuppose the very
consistency relation being maintained.

Immanence sharpens this rather than resolving it. The archetype maintaining its
realm's consistency is itself inside that realm, and so is subject to the
consistency it maintains. There is no exterior position from which maintenance
could be performed — `d-no-exterior` says so — which is precisely why the paradox
is not avoidable by construction here.

Structurally, `d-self-contained` closes the orbit. Interpretively it does not
discharge the paradox, because self-containment is stated *using* `norm-inhabits`,
the very relation immanence supplies. The structural derive neither resolves the
paradox nor depends on its resolution, and both facts are recorded rather than
elided.

## Next obligations, in order

1. **Semantic close of the opaque predicates.** Interpret `norm-other`,
   `norm-inhabits`, and `norm-returns` as grounding acts, as hypermath's L1
   closes its three opaque structural predicates. `other_is_nonidentity` already
   asks one of these questions and shows a model of the axioms answering it
   negatively, so the close is a real constraint rather than a formality.
   L1 did not do this: the will layer adds `will-of`, which is a new opaque
   predicate and a new seam, rather than closing the three that were already
   there.
2. **The normative-force obligation, GC-5.** Either derive that
   membership-with-exposure carries normative force, or state precisely what
   further structure a derivation would need. It is currently declared.
3. **Lean 4 translation and an audit that publishes its own open obligations,**
   following hypermath's pattern, with admissions and assumptions counted rather
   than hidden.
4. **Staged bridge for L0 standing.** `metamathethicology.will_electrophysics`
   already transports the L1 tensor into domain-tagged, ordinal-staged judgments
   under declared bridges, so the pattern exists and satisfies that package's
   requirement rather than bypassing it. L0 standing has not been transported.
   A bridge justification stating why a structural fact about inhabitation
   licenses a `METAETHICS` judgment still has to be written, and it will not be
   supplied by the will transport, which begins above that seam rather than
   crossing it.
5. **Arbitrary-depth exposure, if wanted.** Currently refuted at depth three. Any
   axiom restoring it must be shown independent of the existing four and must not
   break the operant.
6. **The role assignment, L1 `GC-4`.** That the six components divide 3/2/1 is
   declared structure. Either derive the division from the tensor, or state what
   a derivation would need. It is the claim an electrical reading depends on, and
   it is not established by one.
7. **Obligations that left with the transport, listed so the move is not
   mistaken for a discharge.** The warrant for the transport, the charge-constant
   law, and units are now carried by `metamathethicology.will_electrophysics` as
   its `GC-3`, `GC-4` and `GC-5`. `hyperphysics` records the general form of the
   warrant problem as its own `GC-4`: no soundness criterion for a transport
   exists, so there is currently nothing to derive such a licence from. Neither
   field fills that hole and neither claims to.

These are additive research obligations. None of them is permission to assume an
unproved principle or to weaken an existing countermodel.
