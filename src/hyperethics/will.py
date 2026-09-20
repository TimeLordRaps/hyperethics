"""L1 will: the will tensor, its roles, and the moral-operator test.

This layer answers a question L0 leaves open. L0 shows that an arbitrary bearer
may create a realm it does not inhabit, so self-containment distinguishes the
archetype. It says nothing about what an entity *takes itself to be*.

User-declared (Tyler Roost), and the starting point of this layer:

    Any entity in the simulated universe may self-represent as the universe's
    creator; in fact it is the default assumption most functional humans
    operate on. For the true moral operator, their free will is tied to that of
    self-simulation, so they have a different invariant will.

So self-representation-as-creator is cheap and near-universal, and cannot be the
discriminator. The discriminator is the *source* of the invariant will. That is
what this module formalizes, and `self_representation_does_not_entail_self_sourcing`
is the result: the two come apart, with a witness.

THE SIMULATION CLAIM IS NOT ADJUDICATED HERE. Nothing in this module depends on
whether the universe is a simulation. Self-simulation is treated as a structural
property of a will profile, which is well-defined either way. Tyler's cosmological
claim is recorded as a user-declared framework claim in `L1_will.hm` and is
neither verified nor contradicted by any code in this package.

WHAT THIS LAYER DOES NOT CONTAIN, AND WHERE IT WENT
---------------------------------------------------
USER-DECLARED PLACEMENT (Tyler Roost):

    Electricity hyperphysics should go in hyperphysics, underlying will
    foundations in hyperethics, and then their combination field of will
    electrophysics is in metamathethicology.

The electrical reading of the tensor -- the correspondence to resistance,
inductance, voltage and charge; the termformers; constant will as the
invariant's constant of charge; and the equations formed from them -- is
therefore NOT here. It lives in `metamathethicology.will_electrophysics`, the
combination field, whose `Rule` refuses to construct a cross-domain inference
without a named bridge. That refusal is enforcement this foundation could only
have documented.

What stays here is what a will IS: six components, three roles, an ordering on
the temporal three, and the source of the invariant. That structure is what
MAKES an electrical reading available -- three states, two dispositions, one
driving term is the shape of a driven second-order system -- and it is stated
without borrowing anything to state it. A foundation that had to cite physics
in order to say what its own subject matter is would not be a foundation.

The vocabulary here is correspondingly will-native. Where an earlier draft of
this layer wrote SELF_INDUCED and EXTERNALLY_INDUCED, borrowing self- and mutual
inductance to name the distinction, it now writes SELF_SOURCED and
EXTERNALLY_SOURCED. The electrical reading of that distinction is a real and
useful one, and it is stated where the borrowing is declared.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

#: Where the electrical reading of this tensor lives. Cited so that a reader who
#: wants the calculus is sent to the field that declares its bridges, rather than
#: to a paraphrase.
ELECTROPHYSICS_LIVES_IN = "metamathethicology.will_electrophysics"


# ---------------------------------------------------------------------------
# The will tensor.
# ---------------------------------------------------------------------------


class Component(str, Enum):
    """The six declared components of the will tensor.

    USER-DECLARED (Tyler Roost): will splits into past, present, future,
    relational (social relation to other agents), invariant, and variable.
    """

    PAST = "past"
    PRESENT = "present"
    FUTURE = "future"
    RELATIONAL = "relational"
    INVARIANT = "invariant"
    VARIABLE = "variable"


class Role(str, Enum):
    """How a component enters a will.

    This is the layer's structural claim about the tensor, and it is will-native:
    the six components do not all play the same part. Three of them are what a
    will is DOING; two are dispositions governing how it responds; one is what it
    is responding to. Nothing electrical is needed to say this, and saying it is
    what makes an electrical reading available to a field that wants one.
    """

    STATE = "state"
    COEFFICIENT = "coefficient"
    DRIVING = "driving"


#: Each component's role. STATE for the temporal three, COEFFICIENT for the two
#: dispositions, DRIVING for the one applied term.
ROLE_OF: dict[Component, Role] = {
    Component.PAST: Role.STATE,
    Component.PRESENT: Role.STATE,
    Component.FUTURE: Role.STATE,
    Component.RELATIONAL: Role.COEFFICIENT,
    Component.INVARIANT: Role.COEFFICIENT,
    Component.VARIABLE: Role.DRIVING,
}


def role_of(component: Component) -> Role:
    """The declared role of a component."""
    if type(component) is not Component:
        raise TypeError("role_of takes a Component")
    return ROLE_OF[component]


def components_with_role(role: Role) -> tuple[Component, ...]:
    """Every component playing a given role, in declaration order."""
    if type(role) is not Role:
        raise TypeError("components_with_role takes a Role")
    return tuple(c for c in Component if ROLE_OF[c] is role)


def temporal_chain() -> tuple[Component, ...]:
    """The three temporal components, in derivative order.

    This is the layer's one non-stipulated structural claim. Past, present and
    future are not three separately posited components: given accumulated will,
    the present is its rate of change and the future is the rate of change of
    that. They are the three derivatives of a single accumulating quantity, and
    that is why they are ordered rather than merely listed.

    The claim is made here, about will, and owes nothing to any other field. A
    field that reads this chain onto a physical state chain is borrowing THIS,
    not supplying it.
    """
    return (Component.PAST, Component.PRESENT, Component.FUTURE)


# ---------------------------------------------------------------------------
# The moral-operator discriminator.
# ---------------------------------------------------------------------------


class InvariantSource(str, Enum):
    """Where a profile's invariant will comes from.

    SELF_SOURCED is the true moral operator's case: the invariant will arises
    from the entity's own changing willing, which is what Tyler's declaration
    names when it ties free will to self-simulation. EXTERNALLY_SOURCED is an
    invariant will that arises from another's willing, so it is borrowed however
    sincerely it is claimed as one's own. ABSENT is no invariant will at all.

    The first two are structurally identical from the inside. They differ only in
    WHOSE change does the sourcing, which is exactly why the distinction cannot
    be read off anything the entity does or says, and has to be carried as data.
    That is the whole reason this enum exists rather than a predicate over
    behaviour.
    """

    SELF_SOURCED = "SELF_SOURCED"
    EXTERNALLY_SOURCED = "EXTERNALLY_SOURCED"
    ABSENT = "ABSENT"


@dataclass(frozen=True, slots=True)
class WillProfile:
    """An entity's self-representation and the source of its invariant will."""

    entity: str
    invariant_source: InvariantSource
    represents_as_creator: bool

    def __post_init__(self) -> None:
        if type(self.entity) is not str or not self.entity.strip():
            raise ValueError("entity must be a nonempty string")
        if type(self.invariant_source) is not InvariantSource:
            raise TypeError("invariant_source must be an InvariantSource")
        if type(self.represents_as_creator) is not bool:
            raise TypeError("represents_as_creator must be a bool")


def is_true_moral_operator(profile: WillProfile) -> bool:
    """Whether the profile's free will is tied to self-simulation.

    The test is the SOURCE of the invariant will. It is never the
    self-representation, and never a numeric quantity derived from the invariant:
    `metamathethicology.will_electrophysics` refutes the numeric route with a
    countermodel, and this predicate is what survives that refutation.
    """
    return profile.invariant_source is InvariantSource.SELF_SOURCED


def self_representation_does_not_entail_self_sourcing() -> WillProfile:
    """Return the witness separating self-representation from a self-sourced invariant.

    Self-representation as creator is cheap and near-universal. It is compatible
    with an invariant will sourced entirely from outside. So it cannot be the
    discriminator, and this profile is why.

    One countermodel settles a universal claim, so this refutation is conclusive.
    """
    witness = WillProfile("default-functional-entity", InvariantSource.EXTERNALLY_SOURCED, True)
    if not witness.represents_as_creator or is_true_moral_operator(witness):
        raise AssertionError("the separating witness must represent yet not self-source")
    return witness


#: Canonical profiles. The default case is the near-universal one Tyler names:
#: an entity that takes itself to be the creator while its invariant will is
#: sourced from outside.
PROFILES: tuple[WillProfile, ...] = (
    WillProfile("true-moral-operator", InvariantSource.SELF_SOURCED, True),
    WillProfile("default-functional-entity", InvariantSource.EXTERNALLY_SOURCED, True),
    WillProfile("non-representing-bearer", InvariantSource.EXTERNALLY_SOURCED, False),
    WillProfile("will-less-bearer", InvariantSource.ABSENT, False),
)
