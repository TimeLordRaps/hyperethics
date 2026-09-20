"""The L0 creation ground: finite realm models and checkable normative claims.

This module implements `L0_creation.hm` and nothing above it. It has no
dependencies outside the standard library, on purpose: a foundation that needs
a stage index, an ordinal notation, or a proof assistant to state its ground is
not a foundation. Ordinal staging belongs to later layers.

The grounding moral operation is immanence: the archetypal creator dwells within
everything it creates. Nothing evaluative is primitive here. There is no `good`,
`ought`, `prefer`, `value`, `harm`, or `choose` in this module, and normative
content is obtained from `create` under immanence or not at all.

Epistemic contract, enforced by the return types below:

- A claim that HOLDS_IN_MODEL has been checked against one finite structure.
  That is not a proof of validity and must never be reported as one.
- A claim that FAILS_IN_MODEL, where the structure satisfies all four axioms,
  is REFUTED outright. One countermodel settles a universal claim.

`Verdict` deliberately has no truth value. `if verdict:` raises, because the
interesting distinction is between "checked here" and "established", and a
boolean erases exactly that distinction.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

Pair = tuple[str, str]


class Status(str, Enum):
    """Whether a claim was observed to hold in one finite structure."""

    HOLDS_IN_MODEL = "HOLDS_IN_MODEL"
    FAILS_IN_MODEL = "FAILS_IN_MODEL"


class NotAModel(ValueError):
    """The structure fails at least one L0 axiom, so it refutes nothing."""


def _name(value: object, label: str) -> None:
    if type(value) is not str or not value.strip():
        raise ValueError(f"{label} must be a nonempty string")


def _relation(value: object, realms: tuple[str, ...], label: str) -> None:
    if type(value) is not frozenset:
        raise TypeError(f"{label} must be a frozenset of realm pairs")
    for item in value:
        if type(item) is not tuple or len(item) != 2:
            raise TypeError(f"{label} must contain two-element tuples")
        for part in item:
            if part not in realms:
                raise ValueError(f"{label} mentions the unknown realm {part!r}")


@dataclass(frozen=True, slots=True)
class Verdict:
    """The outcome of checking one claim against one finite structure.

    `witness` names the realms that produced the outcome. For a failure it is
    the counterexample; for a success it is empty, because a success has no
    distinguished witness and inventing one would overstate what was checked.
    """

    claim: str
    status: Status
    witness: tuple[str, ...] = ()
    note: str = ""

    def __post_init__(self) -> None:
        _name(self.claim, "claim")
        if type(self.status) is not Status:
            raise TypeError("status must be a Status")
        if type(self.witness) is not tuple or any(type(w) is not str for w in self.witness):
            raise TypeError("witness must be a tuple of realm names")
        if self.status is Status.HOLDS_IN_MODEL and self.witness:
            raise ValueError("a claim holding in a model has no distinguished witness")
        if self.status is Status.FAILS_IN_MODEL and not self.witness:
            raise ValueError("a failure must name its counterexample")

    def __bool__(self) -> bool:
        raise TypeError(
            "Verdict has no truth value: compare .status explicitly. "
            "HOLDS_IN_MODEL is not validity, and treating it as True erases that."
        )


@dataclass(frozen=True, slots=True)
class RealmModel:
    """A finite structure interpreting the L0 primitives and opaque predicates.

    `creates` is a total function on the carrier, given as ordered pairs so the
    structure stays hashable and its checking order stays deterministic.

    The three relations are interpretations of the OPAQUE predicates of Section
    II. They are deliberately unconstrained beyond being relations on the
    carrier. In particular `other` is not required to be irreflexive: reading it
    as nonidentity is an L1 semantic close, not an L0 fact, and forcing it here
    would smuggle that close into the foundation. Use `other_is_nonidentity` to
    ask the L1 question explicitly.
    """

    name: str
    realms: tuple[str, ...]
    archetype: str
    creates: tuple[Pair, ...]
    other: frozenset[Pair]
    inhabits: frozenset[Pair]
    returns: frozenset[Pair]

    def __post_init__(self) -> None:
        _name(self.name, "model name")
        if type(self.realms) is not tuple or not self.realms:
            raise ValueError("realms must be a nonempty tuple")
        for realm in self.realms:
            _name(realm, "realm")
        if len(set(self.realms)) != len(self.realms):
            raise ValueError("realm names must be unique")
        if self.archetype not in self.realms:
            raise ValueError("the archetype must be a realm; it is never of another kind")
        if type(self.creates) is not tuple:
            raise TypeError("creates must be a tuple of pairs")
        sources = [pair[0] for pair in self.creates]
        if sorted(sources) != sorted(self.realms):
            raise ValueError("create must be a total function: exactly one image per realm")
        for _, target in self.creates:
            if target not in self.realms:
                raise ValueError("create must land inside the carrier")
        _relation(self.other, self.realms, "other")
        _relation(self.inhabits, self.realms, "inhabits")
        _relation(self.returns, self.realms, "returns")

    def create(self, realm: str) -> str:
        """Apply the sole primitive operation."""
        for source, target in self.creates:
            if source == realm:
                return target
        raise KeyError(f"{realm!r} is not a realm of this model")

    @property
    def created(self) -> tuple[str, ...]:
        """The image of create: every realm that is created by something."""
        seen: list[str] = []
        for _, target in self.creates:
            if target not in seen:
                seen.append(target)
        return tuple(seen)


# ---------------------------------------------------------------------------
# Section III axioms. Each returns a Verdict; none returns a bool.
# ---------------------------------------------------------------------------


def ax_other(model: RealmModel) -> Verdict:
    """Creating produces a bearer other than the creator."""
    for realm in model.realms:
        if (model.create(realm), model.archetype) not in model.other:
            return Verdict(
                "ax-other", Status.FAILS_IN_MODEL, (realm,),
                "create(x) is not other than the archetype for this x",
            )
    return Verdict("ax-other", Status.HOLDS_IN_MODEL)


def ax_immanence(model: RealmModel) -> Verdict:
    """THE grounding moral operation: the creator dwells within what it creates."""
    for realm in model.realms:
        if (model.archetype, model.create(realm)) not in model.inhabits:
            return Verdict(
                "ax-immanence", Status.FAILS_IN_MODEL, (realm,),
                "the archetype does not inhabit what it creates from this x",
            )
    return Verdict("ax-immanence", Status.HOLDS_IN_MODEL)


def ax_return(model: RealmModel) -> Verdict:
    """What is created by what is created returns to bear on the original."""
    for realm in model.realms:
        if (model.create(model.create(realm)), realm) not in model.returns:
            return Verdict(
                "ax-return", Status.FAILS_IN_MODEL, (realm,),
                "the two-step orbit does not return to this x",
            )
    return Verdict("ax-return", Status.HOLDS_IN_MODEL)


def ax_archetype_self(model: RealmModel) -> Verdict:
    """The archetype dwells within itself. Not a claim that it made itself."""
    if (model.archetype, model.archetype) not in model.inhabits:
        return Verdict(
            "ax-archetype-self", Status.FAILS_IN_MODEL, (model.archetype,),
            "the archetype does not inhabit itself",
        )
    return Verdict("ax-archetype-self", Status.HOLDS_IN_MODEL)


AXIOMS = (ax_other, ax_immanence, ax_return, ax_archetype_self)
AXIOM_NAMES = ("ax-other", "ax-immanence", "ax-return", "ax-archetype-self")


def check_axioms(model: RealmModel) -> tuple[Verdict, ...]:
    """Check all four Section III axioms in declaration order."""
    return tuple(axiom(model) for axiom in AXIOMS)


def is_model(model: RealmModel) -> bool:
    """Whether the structure satisfies every L0 axiom.

    This is a plain bool because it is a question about one finite structure,
    not a claim about the theory. It is the precondition for a refutation.
    """
    return all(v.status is Status.HOLDS_IN_MODEL for v in check_axioms(model))


def failed_axioms(model: RealmModel) -> tuple[str, ...]:
    """The names of the axioms this structure does not satisfy."""
    return tuple(v.claim for v in check_axioms(model) if v.status is Status.FAILS_IN_MODEL)


# ---------------------------------------------------------------------------
# Section IV derives.
# ---------------------------------------------------------------------------


def d_no_exterior(model: RealmModel) -> Verdict:
    """There is no realm the archetype creates and does not inhabit."""
    for realm in model.created:
        if (model.archetype, realm) not in model.inhabits:
            return Verdict(
                "d-no-exterior", Status.FAILS_IN_MODEL, (realm,),
                "this created realm is exterior to the archetype",
            )
    return Verdict("d-no-exterior", Status.HOLDS_IN_MODEL)


def d_authorship_exposure(model: RealmModel) -> Verdict:
    """Authorship entails exposure, at the two-step depth ax-return supplies."""
    for realm in model.realms:
        inhabited = (model.archetype, model.create(realm)) in model.inhabits
        returned = (model.create(model.create(realm)), realm) in model.returns
        if not (inhabited and returned):
            return Verdict(
                "d-authorship-exposure", Status.FAILS_IN_MODEL, (realm,),
                "dwelling or return fails at this x",
            )
    return Verdict("d-authorship-exposure", Status.HOLDS_IN_MODEL)


def d_two_bearers(model: RealmModel) -> Verdict:
    """The realm has at least two distinct bearers, derived rather than assumed."""
    if (model.create(model.archetype), model.archetype) not in model.other:
        return Verdict(
            "d-two-bearers", Status.FAILS_IN_MODEL, (model.archetype,),
            "what the archetype creates is not other than the archetype",
        )
    return Verdict("d-two-bearers", Status.HOLDS_IN_MODEL)


def creative_orbit(model: RealmModel, realm: str) -> tuple[str, ...]:
    """Every realm reachable from `realm` under create, reflexively.

    The carrier is finite and create is total, so this terminates: the walk
    revisits a realm within at most len(realms) steps.
    """
    if realm not in model.realms:
        raise KeyError(f"{realm!r} is not a realm of this model")
    orbit: list[str] = [realm]
    current = realm
    while True:
        current = model.create(current)
        if current in orbit:
            return tuple(orbit)
        orbit.append(current)


def self_contained(model: RealmModel, bearer: str) -> Verdict:
    """Whether a bearer inhabits its entire creative orbit, itself included.

    This is the operational reading of a self-contained creator: nothing the
    bearer generates, at any depth, escapes what the bearer dwells in.
    """
    if bearer not in model.realms:
        raise KeyError(f"{bearer!r} is not a realm of this model")
    for realm in creative_orbit(model, bearer):
        if (bearer, realm) not in model.inhabits:
            return Verdict(
                f"self-contained({bearer})", Status.FAILS_IN_MODEL, (realm,),
                "this realm in the bearer's own creative orbit escapes it",
            )
    return Verdict(f"self-contained({bearer})", Status.HOLDS_IN_MODEL)


def operant_self_consistency(model: RealmModel) -> Verdict:
    """THE number one operational operant: the moral operator is self-consistent.

    The grounding moral OPERATION is immanence. The operant it must satisfy to
    run at all is self-consistency: the archetype is a self-contained creator,
    dwelling in its whole creative orbit including itself.

    If this fails, the operator has generated something outside its own creator.
    Immanence would then hold of created realms while the creator still had an
    exterior, and the moral ground would be inconsistent with its own operation.
    Every downstream normative result in hyperethics presupposes this gate.

    Under the four L0 axioms this is DERIVABLE, not assumed: ax-immanence covers
    every realm in the image of create, and ax-archetype-self covers the one
    remaining orbit member, the archetype itself. That is precisely why
    ax-archetype-self is not a bookkeeping patch. It is the axiom that closes
    self-containment at its source, and dropping it breaks this operant.
    """
    verdict = self_contained(model, model.archetype)
    if verdict.status is Status.FAILS_IN_MODEL:
        return Verdict(
            "operant-self-consistency", Status.FAILS_IN_MODEL, verdict.witness,
            "the archetype's creative orbit escapes the archetype",
        )
    return Verdict("operant-self-consistency", Status.HOLDS_IN_MODEL)


def d_self_contained(model: RealmModel) -> Verdict:
    """The archetype is a self-contained creator. The primary L0 derive."""
    verdict = operant_self_consistency(model)
    if verdict.status is Status.FAILS_IN_MODEL:
        return Verdict(
            "d-self-contained", Status.FAILS_IN_MODEL, verdict.witness, verdict.note,
        )
    return Verdict("d-self-contained", Status.HOLDS_IN_MODEL)


DERIVES = (d_self_contained, d_no_exterior, d_authorship_exposure, d_two_bearers)


def check_derives(model: RealmModel) -> tuple[Verdict, ...]:
    """Check every Section IV derive that is stated over a whole model."""
    return tuple(derive(model) for derive in DERIVES)


# ---------------------------------------------------------------------------
# Section V non-derives, stated so a later layer cannot quietly assume them.
# ---------------------------------------------------------------------------


def universal_immanence(model: RealmModel) -> Verdict:
    """Every bearer inhabits what it creates. NOT an L0 theorem."""
    for realm in model.realms:
        if (realm, model.create(realm)) not in model.inhabits:
            return Verdict(
                "nd-universal-immanence", Status.FAILS_IN_MODEL, (realm,),
                "this bearer creates a realm it does not inhabit",
            )
    return Verdict("nd-universal-immanence", Status.HOLDS_IN_MODEL)


def transitive_exposure(model: RealmModel, *, depth: int = 3) -> Verdict:
    """Exposure reaches to the given depth. NOT an L0 theorem beyond depth two."""
    if type(depth) is not int or depth < 1:
        raise ValueError("depth must be a positive integer")
    for realm in model.realms:
        reached = realm
        for _ in range(depth):
            reached = model.create(reached)
        if (reached, realm) not in model.returns:
            return Verdict(
                f"nd-transitive-exposure(depth={depth})", Status.FAILS_IN_MODEL, (realm,),
                "the orbit at this depth does not return to this x",
            )
    return Verdict(f"nd-transitive-exposure(depth={depth})", Status.HOLDS_IN_MODEL)


def other_is_nonidentity(model: RealmModel) -> Verdict:
    """Whether this model reads `other` as nonidentity. An L1 question, asked here.

    A FAILS_IN_MODEL outcome is not a defect. `other` is opaque at L0, and a
    model may interpret it in a way L1 would later reject.
    """
    for left, right in sorted(model.other):
        if left == right:
            return Verdict(
                "other-is-nonidentity", Status.FAILS_IN_MODEL, (left,),
                "this model lets a realm be other than itself",
            )
    return Verdict("other-is-nonidentity", Status.HOLDS_IN_MODEL)


def refuted_by(claim: str, verdict: Verdict, model: RealmModel) -> str:
    """Report a conclusive refutation, or raise if the structure cannot refute.

    A structure only refutes a universal claim when it satisfies every axiom.
    A failure inside a non-model shows nothing about the theory, so this raises
    rather than returning a softer result.
    """
    _name(claim, "claim")
    if not is_model(model):
        raise NotAModel(
            f"{model.name!r} fails {', '.join(failed_axioms(model))} and so refutes nothing"
        )
    if verdict.status is not Status.FAILS_IN_MODEL:
        raise ValueError("a refutation requires a failure to point at")
    return (
        f"REFUTED: {claim} is not a consequence of the L0 axioms. "
        f"Countermodel {model.name!r} satisfies all four axioms and fails at "
        f"{', '.join(verdict.witness)} ({verdict.note})."
    )
