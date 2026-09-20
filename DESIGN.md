# Architecture and research ancestry

Status: implemented L0 ground plus a proposed layer stack. Date: 2026-09-20.
This is not a proof of the research program, and no part of the stack above L0
is implemented.

## Position in the stack

```
hypermath            L0 ground □ / apply      formal universe from one operation
hyperethics          L0 creation / immanence  normative structure from one operation   <- this repo
  ...                L1+                      not implemented
metamathethicology   operation spaces         metamath + metaphysics + metaethics + metalogic
```

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
norm. The bridge between them is not implemented; see the obligations below.

## Why the foundation carries no dependency

`hyperethics` depends on nothing outside the standard library, and that is a
design commitment rather than an accident of scope.

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

1. **L1 semantic close.** Interpret `norm-other`, `norm-inhabits`, and
   `norm-returns` as grounding acts, as hypermath's L1 closes its three opaque
   structural predicates. `other_is_nonidentity` already asks one of these
   questions and shows a model of the axioms answering it negatively, so the
   close is a real constraint rather than a formality.
2. **The normative-force obligation, GC-5.** Either derive that
   membership-with-exposure carries normative force, or state precisely what
   further structure a derivation would need. It is currently declared.
3. **Lean 4 translation and an audit that publishes its own open obligations,**
   following hypermath's pattern, with admissions and assumptions counted rather
   than hidden.
4. **Staged bridge to metamathethicology.** Transport L0 standing into
   domain-tagged, ordinal-staged judgments in an `OperationSpace`, with the
   bridge justification stating why a structural fact about inhabitation licenses
   a `METAETHICS` judgment. Metamathethicology already requires a declared bridge
   for cross-domain inference; this must satisfy that requirement rather than
   bypass it.
5. **Arbitrary-depth exposure, if wanted.** Currently refuted at depth three. Any
   axiom restoring it must be shown independent of the existing four and must not
   break the operant.

These are additive research obligations. None of them is permission to assume an
unproved principle or to weaken an existing countermodel.
