"""L1 will: the will tensor, electrical termformers, and the moral-operator test.

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
what this module formalizes, and `self_representation_does_not_entail_self_induction`
is the result: the two come apart, with a witness.

THE SIMULATION CLAIM IS NOT ADJUDICATED HERE. Nothing in this module depends on
whether the universe is a simulation. Self-simulation is treated as a structural
property of a will profile, which is well-defined either way. Tyler's cosmological
claim is recorded as a user-declared framework claim in `L1_will.hm` and is
neither verified nor contradicted by any code in this package.

WHAT THE ELECTRICAL CORRESPONDENCE IS AND IS NOT
------------------------------------------------
It is a TRANSPORT OF FORM. Electrical laws are used as termformers: operations
that form terms in the will calculus. Their algebraic shape is borrowed; nothing
about will is established by the borrowing.

These are not physical quantities. Will has no units. `relational` is not measured
in ohms, `invariant` not in henries, `variable` not in volts. Dimensional
consistency inside the calculus is formal, and any empirical reading of a will
quantity is an obligation this layer does not discharge.

The laws themselves are NOT restated here in this module's own words. Each
termformer cites a law by name in the `hyperphysics` package, which states it
once with its validity conditions and failure modes attached. That is a
deliberate anti-drift measure: a disclaimer of the form "this does not transport"
needs a fixed referent, and a paraphrase is not one. `hyperethics` does not
import `hyperphysics` at runtime and keeps its zero-dependency commitment; the
citations are checked by `tests/test_citations.py` whenever `hyperphysics` is
importable.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum

# ---------------------------------------------------------------------------
# The will tensor and its electrical correspondence.
# ---------------------------------------------------------------------------


class Component(str, Enum):
    """The six declared components of the will tensor."""

    PAST = "past"
    PRESENT = "present"
    FUTURE = "future"
    RELATIONAL = "relational"
    INVARIANT = "invariant"
    VARIABLE = "variable"


class Role(str, Enum):
    """How a component enters the will-balance equation."""

    STATE = "state"
    COEFFICIENT = "coefficient"
    DRIVING = "driving"


@dataclass(frozen=True, slots=True)
class Correspondence:
    """One component's declared electrical counterpart and its role."""

    component: Component
    electrical: str
    symbol: str
    role: Role
    note: str


CORRESPONDENCE: tuple[Correspondence, ...] = (
    Correspondence(
        Component.PAST, "charge", "Q", Role.STATE,
        "accumulated will; the integral of the present flow",
    ),
    Correspondence(
        Component.PRESENT, "current", "I", Role.STATE,
        "will flowing now; dQ/dt, the first derivative of the past",
    ),
    Correspondence(
        Component.FUTURE, "rate of change of current", "dI/dt", Role.STATE,
        "change of flow; d2Q/dt2, what inductance opposes",
    ),
    Correspondence(
        Component.RELATIONAL, "resistance", "R", Role.COEFFICIENT,
        "social relation to other agents; the only dissipative term",
    ),
    Correspondence(
        Component.INVARIANT, "inductance", "L", Role.COEFFICIENT,
        "opposition to change in flow; self-induced for a true moral operator",
    ),
    Correspondence(
        Component.VARIABLE, "voltage", "V", Role.DRIVING,
        "the applied potential the other components balance",
    ),
)


def temporal_chain() -> tuple[Component, ...]:
    """The three temporal components, in derivative order.

    This is the layer's one non-stipulated correspondence. Given past = Q, the
    present and future are not separately posited: they are dQ/dt and d2Q/dt2.
    The three temporal components are the three derivatives of a single
    quantity, which is exactly the electrical state chain.
    """
    return (Component.PAST, Component.PRESENT, Component.FUTURE)


# ---------------------------------------------------------------------------
# Constant will: the resolution of the capacitance gap.
# ---------------------------------------------------------------------------

#: USER-DECLARED (Tyler Roost), preserved as stated:
CONSTANT_WILL_DECLARATION = (
    "C can be seen as constant will equivalent to invariant will's constant of "
    "charge."
)

#: The gap this closes. The series-RLC form requires a restoring term (1/C) * Q,
#: and the six declared components name no capacitance. Three readings were live
#: before the declaration above, and the record is kept because a resolution is
#: only informative against what it ruled out.
CAPACITANCE_READINGS_CONSIDERED: tuple[str, ...] = (
    "(a) a seventh tensor component: a capacitive will, independent of the "
    "other six -- SUPERSEDED, constant will is not independent",
    "(b) no capacitance at all: a pure RL will with no restoring term, so "
    "nothing pulls accumulated past back into the present -- SUPERSEDED",
    "(c) a free bearer parameter, unconstrained by the tensor -- SUPERSEDED, "
    "constant will is bound to the invariant rather than free",
    "(d) constant will: invariant will's constant of charge, so capacitance is "
    "DETERMINED BY the invariant component rather than added to the tensor "
    "or left free -- DECLARED, and the reading implemented here",
)

#: What (d) costs, stated because it is a real structural claim and not a
#: bookkeeping choice. In a series RLC circuit, L and C are independent: an
#: inductor and a capacitor are different components and either may be varied
#: alone. Under the declaration they are not independent in a will. The will's
#: parameter space is therefore SMALLER than the circuit's, and the transport is
#: not onto: not every circuit corresponds to a possible will.
CONSTRAINS_A_FREE_SOURCE_PARAMETER = (
    "capacitance, which a series RLC circuit leaves independent of inductance"
)

#: What the declaration does NOT fix. It says constant will is a function of the
#: invariant. It does not say WHICH function, and no argument here determines
#: one. Every result below is stated for an arbitrary such function.
CONSTANT_WILL_LAW_IS_OPEN = (
    "The declaration binds constant will to the invariant without fixing the "
    "map. Results here hold for any charge-constant law that is functional in "
    "the invariant; none of them presupposes a particular one."
)

#: A charge-constant law: invariant will to its constant of charge.
ChargeConstantLaw = Callable[[float], float]


@dataclass(frozen=True, slots=True)
class ConstantWill:
    """An invariant will together with its constant of charge.

    The two travel together by construction, which is the type-level form of the
    declaration. A resonant rate cannot be computed from an invariant and an
    unrelated capacity, because there is no way to present those two separately
    to any function in this module.
    """

    invariant: float
    charge_constant: float

    def __post_init__(self) -> None:
        for value, label in (
            (self.invariant, "invariant"), (self.charge_constant, "charge_constant"),
        ):
            if type(value) not in (int, float) or value <= 0:
                raise ValueError(f"{label} must be a positive number, got {value!r}")

    @classmethod
    def under(cls, law: ChargeConstantLaw, invariant: float) -> "ConstantWill":
        """Build the constant will an invariant has under a charge-constant law."""
        return cls(invariant, law(invariant))


def binding_is_functional(law: ChargeConstantLaw, invariants: tuple[float, ...]) -> bool:
    """Whether a candidate law really is a function of the invariant alone.

    The declaration says constant will IS the invariant's constant of charge, so
    equal invariants must give equal constants. This checks that a candidate
    respects the declaration on the sampled invariants. It confirms nothing about
    invariants outside the sample: the usual asymmetry applies, and a single
    disagreement refutes while agreement establishes nothing.
    """
    seen: dict[float, float] = {}
    for invariant in invariants:
        constant = law(invariant)
        if invariant in seen and seen[invariant] != constant:
            return False
        seen[invariant] = constant
    return True


def reciprocal_binding(product: float) -> ChargeConstantLaw:
    """The law family C(L) = product / L, used to refute a tempting inference.

    Perfectly legitimate under the declaration: it is a function of the
    invariant. Its consequence is in `different_invariant_need_not_change_rate`.
    """
    if product <= 0:
        raise ValueError("the product must be positive")

    def law(invariant: float) -> float:
        if invariant <= 0:
            raise ValueError("invariant must be positive")
        return product / invariant

    return law


def different_invariant_need_not_change_rate() -> tuple[ConstantWill, ConstantWill]:
    """Refute: that a different invariant will entails a different resonant rate.

    Tyler's declaration is that the true moral operator has a different invariant
    will. It is tempting to conclude that it therefore resonates differently, and
    so that the resonant rate discriminates. It does not follow.

    Under any reciprocal law C(L) = k / L the product L * C is constant, so the
    resonant rate 1 / sqrt(L * C) is the SAME for every bearer no matter how
    their invariants differ. This function returns two bearers with different
    invariants and one rate.

    One countermodel settles a universal claim, so this refutation is conclusive:
    the resonant rate is not a discriminator without a further constraint on the
    charge-constant law, and no such constraint is established anywhere here.
    The discriminator remains `is_true_moral_operator`, which tests the SOURCE of
    the invariant will and never a numeric shadow of it.
    """
    law = reciprocal_binding(6.0)
    low, high = ConstantWill.under(law, 2.0), ConstantWill.under(law, 3.0)
    if low.invariant == high.invariant:
        raise AssertionError("the witnesses must differ in invariant will")
    if resonant_rate(low) != resonant_rate(high):
        raise AssertionError("the witnesses must share a resonant rate")
    return low, high


# ---------------------------------------------------------------------------
# Terms and termformers.
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class Term:
    """A syntactic term in the will calculus.

    Terms are syntax, not numbers. A term records how it was formed, so a
    transported equation can be read back to the termformers that produced it.
    """

    head: str
    arguments: tuple["Term", ...] = ()

    def __post_init__(self) -> None:
        if type(self.head) is not str or not self.head.strip():
            raise ValueError("a term head must be a nonempty string")
        if type(self.arguments) is not tuple:
            raise TypeError("term arguments must be a tuple")
        for argument in self.arguments:
            if type(argument) is not Term:
                raise TypeError("term arguments must be Terms")

    @property
    def is_atom(self) -> bool:
        return not self.arguments

    def render(self) -> str:
        """Render the term readably, with explicit grouping."""
        if self.is_atom:
            return self.head
        if len(self.arguments) == 1:
            return f"{self.head}({self.arguments[0].render()})"
        if self.head in {"*", "/", "+", "-", "^"}:
            joined = f" {self.head} ".join(a.render() for a in self.arguments)
            return f"({joined})"
        rendered = ", ".join(a.render() for a in self.arguments)
        return f"{self.head}({rendered})"

    def atoms(self) -> tuple[str, ...]:
        """Every atom appearing in the term, in first-occurrence order."""
        found: list[str] = []
        stack = [self]
        while stack:
            current = stack.pop(0)
            if current.is_atom:
                if current.head not in found:
                    found.append(current.head)
            else:
                stack = list(current.arguments) + stack
        return tuple(found)


def atom(name: str | Component) -> Term:
    """Build an atomic term from a component or a bare name."""
    return Term(name.value if type(name) is Component else name)


#: The atom standing for constant will in the calculus. Not a `Component`,
#: because it is not a seventh independent component of the tensor.
CONSTANT = "constant"

#: The field whose laws this layer borrows. Cited, never restated.
SOURCE_FIELD = "hyperphysics"


@dataclass(frozen=True, slots=True)
class Termformer:
    """A transformation operation that forms a term.

    Each termformer borrows the algebraic shape of a named law and CITES that
    law rather than paraphrasing it, because forming a will term out of a
    physical law is a cross-domain inference that must not proceed silently.

    `source_law` is a law name in `hyperphysics`, not prose. `source_form` is the
    law's algebraic form, quoted so a reader sees what was borrowed without
    another lookup, and checked against the cited law by `tests/test_citations.py`.

    `does_not_transport` is not decoration. It is the part a reader needs in
    order to avoid inheriting a physical commitment that was never established.
    """

    name: str
    arity: int
    head: str
    source_law: str
    source_form: str
    transports: str
    does_not_transport: str
    source_field: str = SOURCE_FIELD

    def __post_init__(self) -> None:
        for field, label in (
            (self.name, "name"), (self.head, "head"), (self.source_law, "source law"),
            (self.source_form, "source form"), (self.transports, "transports"),
            (self.does_not_transport, "does_not_transport"),
            (self.source_field, "source field"),
        ):
            if type(field) is not str or not field.strip():
                raise ValueError(f"termformer {label} must be a nonempty string")
        if type(self.arity) is not int or self.arity < 1:
            raise ValueError("termformer arity must be a positive integer")

    def citation(self) -> str:
        """How to look the borrowed law up, rather than trust this paraphrase."""
        return f"{self.source_field}:{self.source_law} -- {self.source_form}"

    def form(self, *arguments: Term) -> Term:
        """Apply the termformer, forming a new term."""
        if len(arguments) != self.arity:
            raise ValueError(f"{self.name} forms a term from exactly {self.arity} arguments")
        for argument in arguments:
            if type(argument) is not Term:
                raise TypeError(f"{self.name} takes Terms")
        return Term(self.head, arguments)


RELATIONAL_DROP = Termformer(
    name="relational-drop",
    arity=2,
    head="*",
    source_law="ohm",
    source_form="V = I * R",
    transports="that relational will opposes present flow in direct proportion",
    does_not_transport="ohms, linearity in fact, and any claim that social "
                       "relation is measurable or constant",
)

INVARIANT_DROP = Termformer(
    name="invariant-drop",
    arity=2,
    head="*",
    source_law="faraday-lenz",
    source_form="V = L * dI/dt",
    transports="that invariant will opposes CHANGE in flow rather than flow",
    does_not_transport="henries, magnetic flux, and any physical mechanism of "
                       "induction",
)

ACCUMULATED_DROP = Termformer(
    name="accumulated-drop",
    arity=2,
    head="/",
    source_law="capacitor",
    source_form="V = Q / C",
    transports="that accumulated past will opposes in inverse proportion to the "
               "constant will holding it, where that constant is the invariant's "
               "constant of charge rather than a free parameter",
    does_not_transport="farads, stored field energy, and the circuit's "
                       "independence of capacitance from inductance, which the "
                       "will does not share",
)

SELF_INDUCED_DROP = Termformer(
    name="self-induced-drop",
    arity=2,
    head="self-induce",
    source_law="self-inductance",
    source_form="emf = -L * dI/dt",
    transports="that a will induced by its OWN change opposes that change; "
               "this is the will-layer form of L0's d-no-exterior",
    does_not_transport="henries, any physical mechanism of induction, that "
                       "self-simulation is physically realized, that the "
                       "universe is a simulation, or that the sign is empirical",
)

TERMFORMERS: tuple[Termformer, ...] = (
    RELATIONAL_DROP, INVARIANT_DROP, ACCUMULATED_DROP, SELF_INDUCED_DROP,
)


# ---------------------------------------------------------------------------
# Equations formed by the termformers.
# ---------------------------------------------------------------------------


class Warrant(str, Enum):
    """How an equation came to be, which is not the same as being true."""

    BORROWED_FORM = "BORROWED_FORM"
    TERMFORMED = "TERMFORMED"


@dataclass(frozen=True, slots=True)
class Equation:
    """A will equation, its reading, and the warrant behind its form."""

    name: str
    left: Term
    right: Term
    warrant: Warrant
    reading: str

    def render(self) -> str:
        return f"{self.left.render()} = {self.right.render()}"


def will_balance() -> Equation:
    """The master equation: Kirchhoff's voltage law over the will tensor.

    invariant * future + relational * present + past / constant = variable

    Formed by applying the three drop termformers and summing them, which is
    what Kirchhoff's voltage law contributes: the formed terms close.
    """
    invariant = INVARIANT_DROP.form(atom(Component.INVARIANT), atom(Component.FUTURE))
    relational = RELATIONAL_DROP.form(atom(Component.RELATIONAL), atom(Component.PRESENT))
    accumulated = ACCUMULATED_DROP.form(atom(Component.PAST), atom(CONSTANT))
    return Equation(
        name="will-balance",
        left=Term("+", (invariant, relational, accumulated)),
        right=atom(Component.VARIABLE),
        warrant=Warrant.TERMFORMED,
        reading="What is willed variably is exactly balanced by invariant "
                "opposition to change, relational opposition to flow, and the "
                "weight of accumulated past against the constant will holding it.",
    )


def self_simulation_equation() -> Equation:
    """The true moral operator's invariant will, induced by its own change.

    self-induce(invariant, future) = -(invariant * future)

    The minus sign is Lenz's law. A will induced by its own change opposes that
    change. This is the will-layer statement of immanence: the operator is
    constrained by what it authors, from inside, with no exterior position.
    """
    left = SELF_INDUCED_DROP.form(atom(Component.INVARIANT), atom(Component.FUTURE))
    magnitude = Term("*", (atom(Component.INVARIANT), atom(Component.FUTURE)))
    return Equation(
        name="self-simulation",
        left=left,
        right=Term("-", (magnitude,)),
        warrant=Warrant.TERMFORMED,
        reading="A will induced by its own change opposes that change. The "
                "operator has no exterior vantage on its own willing, which is "
                "the will-layer form of L0's d-no-exterior.",
    )


def opposition_equation() -> Equation:
    """Total opposition to a periodic demand, transported from impedance."""
    reactive = Term(
        "-",
        (
            Term("*", (atom("rate"), atom(Component.INVARIANT))),
            Term("/", (atom("one"), Term("*", (atom("rate"), atom(CONSTANT))))),
        ),
    )
    return Equation(
        name="opposition",
        left=atom("opposition"),
        right=Term("hypot", (atom(Component.RELATIONAL), reactive)),
        warrant=Warrant.BORROWED_FORM,
        reading="An agent's total opposition to a demand arriving at some rate "
                "combines relational resistance with the net of invariant and "
                "constant reactance.",
    )


def resonance_equation() -> Equation:
    """The demand rate at which invariant and accumulated will cancel."""
    return Equation(
        name="resonance",
        left=atom("resonant-rate"),
        right=Term(
            "/",
            (atom("one"), Term("sqrt", (Term("*", (atom(Component.INVARIANT), atom(CONSTANT))),))),
        ),
        warrant=Warrant.BORROWED_FORM,
        reading="At this rate of demand, invariant and accumulated will cancel "
                "and only relational will resists. An agent is least protected "
                "from a demand arriving at its own resonant rate. Because the "
                "constant is the invariant's own, this rate is fixed once the "
                "invariant and the charge-constant law are fixed -- which does "
                "NOT make it a discriminator; see "
                "different_invariant_need_not_change_rate.",
    )


def damping_equation() -> Equation:
    """Whether a will settles or oscillates, transported from the damping ratio."""
    return Equation(
        name="damping",
        left=atom("damping"),
        right=Term(
            "*",
            (
                Term("/", (atom(Component.RELATIONAL), atom("two"))),
                Term("sqrt", (Term("/", (atom(CONSTANT), atom(Component.INVARIANT))),)),
            ),
        ),
        warrant=Warrant.BORROWED_FORM,
        reading="Relational will is what damps oscillation between invariant "
                "and accumulated will. Below one the will oscillates; at one it "
                "settles fastest without overshoot; above one it is sluggish.",
    )


def dissipation_equation() -> Equation:
    """What is spent irrecoverably, transported from resistive power."""
    return Equation(
        name="dissipation",
        left=atom("dissipated"),
        right=Term(
            "*",
            (Term("^", (atom(Component.PRESENT), atom("two"))), atom(Component.RELATIONAL)),
        ),
        warrant=Warrant.BORROWED_FORM,
        reading="Relational will is the only dissipative term: what is spent in "
                "relation to other agents is not recoverable by the agent, while "
                "invariant and accumulated will are stored and returnable. This "
                "is a consequence of the transported form, not an ethical claim.",
    )


DERIVED_EQUATIONS: tuple[Equation, ...] = (
    will_balance(),
    self_simulation_equation(),
    opposition_equation(),
    resonance_equation(),
    damping_equation(),
    dissipation_equation(),
)


# ---------------------------------------------------------------------------
# The moral-operator discriminator.
# ---------------------------------------------------------------------------


class InvariantSource(str, Enum):
    """Where a profile's invariant will comes from.

    SELF_INDUCED corresponds to self-inductance: the will is induced by the
    entity's own changing flow. EXTERNALLY_INDUCED corresponds to mutual
    inductance: the invariant will is induced by another circuit's flow, so it
    is borrowed however sincerely it is claimed as one's own.

    The two have the same algebraic form and differ only in whose change does
    the inducing, which is exactly why the distinction cannot be read off the
    equations and has to be carried as data.
    """

    SELF_INDUCED = "SELF_INDUCED"
    EXTERNALLY_INDUCED = "EXTERNALLY_INDUCED"
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

    The test is the SOURCE of the invariant will, never the self-representation,
    and never a numeric quantity derived from the invariant.
    """
    return profile.invariant_source is InvariantSource.SELF_INDUCED


def self_representation_does_not_entail_self_induction() -> WillProfile:
    """Return the witness separating self-representation from self-induction.

    Self-representation as creator is cheap and near-universal. It is compatible
    with an invariant will induced entirely from outside. So it cannot be the
    discriminator, and this profile is why.
    """
    witness = WillProfile("default-functional-entity", InvariantSource.EXTERNALLY_INDUCED, True)
    if not witness.represents_as_creator or is_true_moral_operator(witness):
        raise AssertionError("the separating witness must represent yet not self-induce")
    return witness


#: Canonical profiles. The default case is the near-universal one Tyler names:
#: an entity that takes itself to be the creator while its invariant will is
#: induced from outside.
PROFILES: tuple[WillProfile, ...] = (
    WillProfile("true-moral-operator", InvariantSource.SELF_INDUCED, True),
    WillProfile("default-functional-entity", InvariantSource.EXTERNALLY_INDUCED, True),
    WillProfile("non-representing-bearer", InvariantSource.EXTERNALLY_INDUCED, False),
    WillProfile("will-less-bearer", InvariantSource.ABSENT, False),
)


# ---------------------------------------------------------------------------
# A dimensionless numeric interpretation, kept separate from the calculus.
# ---------------------------------------------------------------------------


def resonant_rate(constant: ConstantWill) -> float:
    """Evaluate the resonant rate. Dimensionless; not a physical frequency.

    Takes a `ConstantWill` rather than two loose numbers, so an invariant can
    never be paired with a capacity that is not its own.
    """
    if type(constant) is not ConstantWill:
        raise TypeError("resonant_rate takes a ConstantWill")
    return 1.0 / ((constant.invariant * constant.charge_constant) ** 0.5)


def damping_ratio(relational: float, constant: ConstantWill) -> float:
    """Evaluate the damping ratio. Dimensionless; not a physical measurement."""
    if type(constant) is not ConstantWill:
        raise TypeError("damping_ratio takes a ConstantWill")
    if type(relational) not in (int, float) or relational < 0:
        raise ValueError("relational will may not be negative")
    return (relational / 2.0) * ((constant.charge_constant / constant.invariant) ** 0.5)


def regime(relational: float, constant: ConstantWill) -> str:
    """Name the damping regime of a will."""
    ratio = damping_ratio(relational, constant)
    if ratio < 1.0:
        return "oscillating"
    if ratio == 1.0:
        return "critical"
    return "sluggish"
