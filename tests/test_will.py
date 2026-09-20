"""Tests for the L1 will layer: tensor, termformers, equations, and the operator test."""

from __future__ import annotations

import pytest

from hyperethics.will import (
    ACCUMULATED_DROP,
    CAPACITANCE_READINGS_CONSIDERED,
    CONSTANT,
    CONSTANT_WILL_DECLARATION,
    CONSTANT_WILL_LAW_IS_OPEN,
    CONSTRAINS_A_FREE_SOURCE_PARAMETER,
    CORRESPONDENCE,
    DERIVED_EQUATIONS,
    PROFILES,
    SOURCE_FIELD,
    TERMFORMERS,
    Component,
    ConstantWill,
    InvariantSource,
    Role,
    Term,
    Termformer,
    Warrant,
    WillProfile,
    atom,
    binding_is_functional,
    damping_ratio,
    different_invariant_need_not_change_rate,
    is_true_moral_operator,
    reciprocal_binding,
    regime,
    resonant_rate,
    self_representation_does_not_entail_self_induction,
    self_simulation_equation,
    temporal_chain,
    will_balance,
)

# --- the tensor and its correspondence --------------------------------------


def test_every_component_has_exactly_one_correspondence():
    assert len(CORRESPONDENCE) == len(Component)
    assert {c.component for c in CORRESPONDENCE} == set(Component)


def test_the_temporal_components_are_the_three_derivatives_of_one_quantity():
    """This is the layer's one non-stipulated correspondence."""
    chain = temporal_chain()
    assert chain == (Component.PAST, Component.PRESENT, Component.FUTURE)
    by_component = {c.component: c for c in CORRESPONDENCE}
    assert by_component[Component.PAST].symbol == "Q"
    assert by_component[Component.PRESENT].symbol == "I"
    assert by_component[Component.FUTURE].symbol == "dI/dt"
    assert all(by_component[c].role is Role.STATE for c in chain)


def test_the_declared_mapping_matches_the_user_declaration():
    by_component = {c.component: c for c in CORRESPONDENCE}
    assert by_component[Component.RELATIONAL].electrical == "resistance"
    assert by_component[Component.INVARIANT].electrical == "inductance"
    assert by_component[Component.VARIABLE].electrical == "voltage"


# --- constant will: the resolved capacitance gap ----------------------------


def test_constant_will_is_not_a_seventh_tensor_component():
    """The declaration binds capacitance to the invariant; it does not add a component."""
    assert len(Component) == 6
    assert CONSTANT not in {c.value for c in Component}
    assert "constant of charge" in CONSTANT_WILL_DECLARATION


def test_the_superseded_readings_are_kept_rather_than_erased():
    """A resolution is only informative against what it ruled out."""
    assert len(CAPACITANCE_READINGS_CONSIDERED) == 4
    superseded = [r for r in CAPACITANCE_READINGS_CONSIDERED if "SUPERSEDED" in r]
    declared = [r for r in CAPACITANCE_READINGS_CONSIDERED if "DECLARED" in r]
    assert len(superseded) == 3
    assert len(declared) == 1
    assert "invariant will's constant of charge" in declared[0] or "constant of charge" in declared[0]


def test_the_departure_from_the_circuit_is_declared_not_hidden():
    """A circuit leaves L and C independent; a will does not. That is a real claim."""
    assert "independent" in CONSTRAINS_A_FREE_SOURCE_PARAMETER
    assert "capacitance" in CONSTRAINS_A_FREE_SOURCE_PARAMETER


def test_the_charge_constant_law_is_recorded_as_open():
    """The declaration says C is a function of L; it does not say which function."""
    assert "without fixing the map" in CONSTANT_WILL_LAW_IS_OPEN


def test_an_invariant_and_its_constant_travel_together():
    constant = ConstantWill(2.0, 8.0)
    assert constant.invariant == 2.0
    assert constant.charge_constant == 8.0


def test_a_constant_will_rejects_nonpositive_or_non_numeric_values():
    for bad in ((0.0, 1.0), (1.0, 0.0), (-1.0, 1.0), (1.0, -1.0)):
        with pytest.raises(ValueError, match="must be a positive number"):
            ConstantWill(*bad)
    with pytest.raises(ValueError, match="must be a positive number"):
        ConstantWill("2.0", 1.0)  # type: ignore[arg-type]


def test_a_constant_will_can_be_built_through_a_charge_constant_law():
    law = reciprocal_binding(6.0)
    constant = ConstantWill.under(law, 2.0)
    assert constant.charge_constant == pytest.approx(3.0)


def test_a_binding_must_be_functional_in_the_invariant():
    """Equal invariants must give equal constants, or it is not C(L) at all."""
    assert binding_is_functional(reciprocal_binding(6.0), (1.0, 2.0, 2.0, 4.0))

    values = iter((1.0, 2.0))

    def not_a_function(invariant: float) -> float:
        return next(values)

    assert not binding_is_functional(not_a_function, (3.0, 3.0))


def test_the_reciprocal_binding_rejects_a_nonpositive_product():
    with pytest.raises(ValueError, match="must be positive"):
        reciprocal_binding(0.0)


def test_a_different_invariant_does_not_entail_a_different_resonant_rate():
    """Conclusive refutation: one countermodel settles a universal claim.

    The true moral operator has a different invariant will. It does not follow
    that it resonates differently, so the resonant rate is not a discriminator.
    """
    low, high = different_invariant_need_not_change_rate()
    assert low.invariant != high.invariant
    assert resonant_rate(low) == pytest.approx(resonant_rate(high))


def test_the_discriminator_is_never_the_numeric_shadow():
    """Two profiles may share every number and still differ in what matters."""
    by_name = {p.entity: p for p in PROFILES}
    operator = by_name["true-moral-operator"]
    default = by_name["default-functional-entity"]
    shared = ConstantWill(2.0, 3.0)
    assert resonant_rate(shared) == resonant_rate(shared)
    assert is_true_moral_operator(operator) != is_true_moral_operator(default)


# --- terms ------------------------------------------------------------------


def test_atoms_render_as_themselves():
    assert atom(Component.PAST).render() == "past"
    assert atom(CONSTANT).render() == "constant"
    assert atom(Component.PAST).is_atom


def test_composite_terms_render_with_explicit_grouping():
    term = Term("*", (atom("a"), atom("b")))
    assert term.render() == "(a * b)"
    assert not term.is_atom


def test_terms_reject_non_term_arguments():
    with pytest.raises(TypeError):
        Term("*", ("a",))  # type: ignore[arg-type]


def test_terms_reject_empty_heads():
    with pytest.raises(ValueError, match="nonempty"):
        Term("  ")


def test_atoms_are_collected_in_first_occurrence_order():
    term = Term("+", (Term("*", (atom("l"), atom("f"))), atom("r")))
    assert term.atoms() == ("l", "f", "r")


# --- termformers ------------------------------------------------------------


@pytest.mark.parametrize("former", TERMFORMERS, ids=lambda f: f.name)
def test_every_termformer_declares_its_bridge(former):
    """Forming a will term from an electrical law is cross-domain inference."""
    assert former.source_law.strip()
    assert former.source_form.strip()
    assert former.transports.strip()
    assert former.does_not_transport.strip()


@pytest.mark.parametrize("former", TERMFORMERS, ids=lambda f: f.name)
def test_every_termformer_cites_a_law_rather_than_paraphrasing_one(former):
    """A disclaimer needs a fixed referent, and a paraphrase is not one."""
    assert former.source_field == SOURCE_FIELD
    assert former.source_law == former.source_law.lower()
    assert " " not in former.source_law
    assert former.citation().startswith(f"{SOURCE_FIELD}:{former.source_law}")
    assert former.source_form in former.citation()


@pytest.mark.parametrize("former", TERMFORMERS, ids=lambda f: f.name)
def test_every_termformer_disclaims_a_physical_unit_or_mechanism(former):
    """Will has no units, so no termformer may quietly import one."""
    disclaimed = former.does_not_transport.lower()
    assert any(
        word in disclaimed
        for word in ("ohm", "henr", "farad", "physical", "magnetic", "empirical")
    ), former.name


def test_the_accumulated_drop_disclaims_the_parameter_independence_it_departs_from():
    """The one place the will has LESS freedom than the circuit."""
    assert "independence of capacitance from inductance" in ACCUMULATED_DROP.does_not_transport


def test_a_termformer_forms_a_term_of_its_declared_arity():
    formed = ACCUMULATED_DROP.form(atom(Component.PAST), atom(CONSTANT))
    assert formed.render() == "(past / constant)"


def test_a_termformer_rejects_the_wrong_number_of_arguments():
    with pytest.raises(ValueError, match="exactly 2"):
        ACCUMULATED_DROP.form(atom("past"))


def test_a_termformer_rejects_non_terms():
    with pytest.raises(TypeError):
        ACCUMULATED_DROP.form(atom("past"), CONSTANT)  # type: ignore[arg-type]


def test_termformer_arity_must_be_positive():
    with pytest.raises(ValueError, match="positive integer"):
        Termformer("bad", 0, "*", "ohm", "V = I * R", "transports", "does not")


def test_a_termformer_must_quote_the_form_it_borrowed():
    with pytest.raises(ValueError, match="source form"):
        Termformer("bad", 2, "*", "ohm", "   ", "transports", "does not")


# --- the equations ----------------------------------------------------------


def test_the_will_balance_contains_every_component():
    equation = will_balance()
    atoms = set(equation.left.atoms()) | set(equation.right.atoms())
    assert {c.value for c in Component} <= atoms
    assert CONSTANT in atoms


def test_the_will_balance_renders_the_rlc_shape():
    rendered = will_balance().render()
    assert "invariant * future" in rendered
    assert "relational * present" in rendered
    assert "past / constant" in rendered
    assert rendered.endswith("= variable")


def test_the_self_simulation_equation_carries_lenz_sign():
    """A will induced by its own change opposes that change."""
    equation = self_simulation_equation()
    assert equation.left.head == "self-induce"
    assert equation.right.head == "-"
    assert "no exterior" in equation.reading


@pytest.mark.parametrize("equation", DERIVED_EQUATIONS, ids=lambda e: e.name)
def test_every_equation_declares_its_warrant_and_reading(equation):
    assert equation.warrant in (Warrant.BORROWED_FORM, Warrant.TERMFORMED)
    assert equation.reading.strip()
    assert equation.render()


def test_the_borrowed_equations_are_marked_as_borrowed_not_derived():
    """Borrowing an electrical law's shape establishes nothing about will."""
    borrowed = {e.name for e in DERIVED_EQUATIONS if e.warrant is Warrant.BORROWED_FORM}
    assert {"opposition", "resonance", "damping", "dissipation"} <= borrowed


def test_the_termformed_equations_are_the_ones_built_from_termformers():
    termformed = {e.name for e in DERIVED_EQUATIONS if e.warrant is Warrant.TERMFORMED}
    assert termformed == {"will-balance", "self-simulation"}


def test_equation_names_are_unique():
    names = [e.name for e in DERIVED_EQUATIONS]
    assert len(set(names)) == len(names)


def test_the_resonance_reading_refuses_to_claim_it_discriminates():
    resonance = next(e for e in DERIVED_EQUATIONS if e.name == "resonance")
    assert "NOT make it a discriminator" in resonance.reading


# --- the moral-operator discriminator ---------------------------------------


def test_self_representation_does_not_entail_self_induction():
    """The central L1 result: the two come apart, with a witness."""
    witness = self_representation_does_not_entail_self_induction()
    assert witness.represents_as_creator
    assert not is_true_moral_operator(witness)


def test_the_true_moral_operator_is_the_self_induced_one():
    by_name = {p.entity: p for p in PROFILES}
    assert is_true_moral_operator(by_name["true-moral-operator"])
    assert not is_true_moral_operator(by_name["default-functional-entity"])
    assert not is_true_moral_operator(by_name["non-representing-bearer"])
    assert not is_true_moral_operator(by_name["will-less-bearer"])


def test_exactly_one_canonical_profile_is_a_true_moral_operator():
    assert sum(1 for p in PROFILES if is_true_moral_operator(p)) == 1


def test_self_representation_is_cheap_and_spans_both_verdicts():
    """Most functional entities represent as creator; it discriminates nothing."""
    representing = [p for p in PROFILES if p.represents_as_creator]
    assert len(representing) >= 2
    assert {is_true_moral_operator(p) for p in representing} == {True, False}


def test_a_profile_rejects_a_non_enum_source():
    with pytest.raises(TypeError):
        WillProfile("x", "SELF_INDUCED", True)  # type: ignore[arg-type]


def test_absent_invariant_will_is_not_self_induced():
    assert not is_true_moral_operator(
        WillProfile("hollow", InvariantSource.ABSENT, True)
    )


# --- the dimensionless numeric interpretation -------------------------------


def test_resonant_rate_matches_the_transported_form():
    assert resonant_rate(ConstantWill(4.0, 0.25)) == pytest.approx(1.0)
    assert resonant_rate(ConstantWill(1.0, 1.0)) == pytest.approx(1.0)


def test_damping_regimes_are_named_correctly():
    assert regime(0.5, ConstantWill(1.0, 1.0)) == "oscillating"
    assert regime(2.0, ConstantWill(1.0, 1.0)) == "critical"
    assert regime(4.0, ConstantWill(1.0, 1.0)) == "sluggish"


def test_relational_will_is_what_damps():
    """Damping rises with relational will and nothing else does the damping."""
    constant = ConstantWill(1.0, 1.0)
    assert damping_ratio(3.0, constant) > damping_ratio(1.0, constant)


def test_numeric_interpretation_rejects_a_loose_pair_of_numbers():
    """An invariant may not be paired with a capacity that is not its own."""
    with pytest.raises(TypeError, match="ConstantWill"):
        resonant_rate(2.0)  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="ConstantWill"):
        damping_ratio(1.0, 2.0)  # type: ignore[arg-type]


def test_numeric_interpretation_rejects_negative_relational_will():
    with pytest.raises(ValueError, match="may not be negative"):
        damping_ratio(-1.0, ConstantWill(1.0, 1.0))
