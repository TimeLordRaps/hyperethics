# Architecture and research ancestry

Status: implemented L0 ground and L1 will, plus a proposed layer stack. Date:
2026-09-20. This is not a proof of the research program, and no part of the stack
above L1 is implemented.

## Position in the stack

```
hypermath            L0 ground □ / apply      formal universe from one operation
hyperphysics         (ground not written)     physical law as a citation surface
hyperethics          L0 creation / immanence  normative structure from one operation   <- this repo
                     L1 will                  who the moral operator is                <- this repo
  ...                L2+                      not implemented
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

L1 is where this was tested, because L1 borrows the algebraic shape of electrical
law and those laws are stated in `hyperphysics`. The obvious move is to import
that package. The resolution is that L1 **cites** it — law name plus quoted form,
carried as data — and `tests/test_citations.py` cross-checks every citation
whenever `hyperphysics` is importable, skipping cleanly when it is not.

That keeps two things that would otherwise conflict. The citation is verifiable,
so a disclaimer of the form "this does not transport farads" has a fixed referent
rather than a paraphrase behind it. And the foundation still stands on the
standard library alone, so nothing that depends on hyperethics inherits a physics
package. A skip means the citations were not checked on that run; it does not
mean they were checked and passed, and `VALIDATION.md` records which happened.

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

Three decisions were load-bearing, and each could have gone wrong quietly.

**The discriminator is a source, not a score.** Tyler's declaration is that the
true moral operator has a *different invariant will*. The tempting formalization
gives the operator a distinguished magnitude and tests for it. That would have
been wrong twice over: it makes the moral operator a matter of degree, and it is
refutable. Under any reciprocal charge-constant law `C(L) = k/L`, the resonant
rate is identical for every bearer regardless of invariant, and
`different_invariant_need_not_change_rate` supplies the witnesses. So the
discriminator tests `InvariantSource`, which is data about where the will is
induced from, and no numeric quantity can stand in for it.

This mirrors L0 exactly. There, `separating_model` shows creation is cheap —
`rival` creates a realm it does not inhabit. Here, `default-functional-entity`
shows self-ascription is cheap. Both layers refuse to let the easy property do
the distinguishing work.

**Constant will is bound, and the binding is enforced by type.** The declaration
is that capacitance is the invariant's constant of charge. `ConstantWill` carries
the invariant together with its charge constant, and `resonant_rate` accepts
nothing else, so there is no way to compute a rate from an invariant and a
capacity that is not its own. The alternative — two loose floats and a comment —
would have left the central structural claim of the section unenforced.

The same discipline as `Verdict.__bool__` raising: if a constraint matters, the
types carry it.

**What the declaration cost is stated.** A series RLC circuit leaves `L` and `C`
independent; a will does not. The will's parameter space is a proper subset of
the circuit's, so the transport is not onto. Left undeclared, a reader imports
the circuit's freedom along with its algebra and reasons about degrees of freedom
the target does not have. It is declared in `L1_will.hm`, disclaimed in the
`accumulated-drop` termformer, published by the report, and registered through
`hyperphysics`' own `Transport.constrains_parameters`.

**What was not upgraded.** The structural agreement between `d-self-simulation`
and L0's `d-no-exterior` is the strongest evidence that the transport tracks
something: two layers stated independently arrive at "no exterior vantage" from
different directions. It is still evidence and not warrant, and `GC-5` stays
open. Tyler's own statement of the transport says "metaphorically analogize" and
"somehow"; nothing here is more confident than its source.

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
4. **Staged bridge to metamathethicology.** Transport L0 standing into
   domain-tagged, ordinal-staged judgments in an `OperationSpace`, with the
   bridge justification stating why a structural fact about inhabitation licenses
   a `METAETHICS` judgment. Metamathethicology already requires a declared bridge
   for cross-domain inference; this must satisfy that requirement rather than
   bypass it.
5. **Arbitrary-depth exposure, if wanted.** Currently refuted at depth three. Any
   axiom restoring it must be shown independent of the existing four and must not
   break the operant.
6. **The charge-constant law** (L1). Constant will is bound to the invariant
   without the map being fixed. Fixing it is not free: a reciprocal law makes the
   resonant rate identical across bearers, other families do not, and choosing
   one decides whether any of the borrowed numeric structure distinguishes
   anything at all.
7. **Warrant for the electrical transport** (L1 `GC-5`). Either argue that the
   target independently reproduces a relation the source predicts — the
   self-induction/`d-no-exterior` agreement is the one candidate in hand — or
   state precisely what more such an argument would need. `hyperphysics` records
   the general form of this problem as its own `GC-4`.

These are additive research obligations. None of them is permission to assume an
unproved principle or to weaken an existing countermodel.
