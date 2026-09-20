"""L1 will: the tensor, its roles, and the moral-operator test.

These tests check the will foundation only. The electrical reading of the tensor
lives in `metamathethicology.will_electrophysics` and is tested there; the tests
at the end of this module check that it has genuinely left, because a foundation
that quietly kept a copy would be the drift this split exists to prevent.
"""

from __future__ import annotations

import pytest

from hyperethics.will import (
    ELECTROPHYSICS_LIVES_IN,
    PROFILES,
    ROLE_OF,
    Component,
    InvariantSource,
    Role,
    WillProfile,
    components_with_role,
    is_true_moral_operator,
    role_of,
    self_representation_does_not_entail_self_sourcing,
    temporal_chain,
)

# --- the tensor -------------------------------------------------------------


def test_the_tensor_has_exactly_the_six_declared_components():
    assert [c.value for c in Component] == [
        "past", "present", "future", "relational", "invariant", "variable",
    ]


def test_every_component_has_exactly_one_role():
    assert set(ROLE_OF) == set(Component)
    assert all(type(role) is Role for role in ROLE_OF.values())


def test_the_roles_divide_the_tensor_three_two_one():
    """Three states, two dispositions, one driving term."""
    assert components_with_role(Role.STATE) == (
        Component.PAST, Component.PRESENT, Component.FUTURE,
    )
    assert components_with_role(Role.COEFFICIENT) == (
        Component.RELATIONAL, Component.INVARIANT,
    )
    assert components_with_role(Role.DRIVING) == (Component.VARIABLE,)


def test_every_role_is_occupied():
    for role in Role:
        assert components_with_role(role)


def test_role_lookup_rejects_a_non_component():
    with pytest.raises(TypeError, match="Component"):
        role_of("past")


def test_components_with_role_rejects_a_non_role():
    with pytest.raises(TypeError, match="Role"):
        components_with_role("state")


def test_the_temporal_components_are_ordered_not_merely_listed():
    """The layer's one non-stipulated structural claim."""
    assert temporal_chain() == (Component.PAST, Component.PRESENT, Component.FUTURE)
    assert all(role_of(c) is Role.STATE for c in temporal_chain())


def test_the_temporal_chain_is_exactly_the_states():
    assert temporal_chain() == components_with_role(Role.STATE)


# --- the moral-operator discriminator ---------------------------------------


def test_self_representation_does_not_entail_a_self_sourced_invariant():
    """The conclusive refutation: one countermodel settles a universal claim."""
    witness = self_representation_does_not_entail_self_sourcing()
    assert witness.represents_as_creator is True
    assert is_true_moral_operator(witness) is False


def test_the_true_moral_operator_is_the_self_sourced_one():
    operator = next(p for p in PROFILES if p.entity == "true-moral-operator")
    assert operator.invariant_source is InvariantSource.SELF_SOURCED
    assert is_true_moral_operator(operator) is True


def test_exactly_one_canonical_profile_is_a_true_moral_operator():
    assert sum(1 for p in PROFILES if is_true_moral_operator(p)) == 1


def test_self_representation_is_cheap_and_spans_both_verdicts():
    """Representing as creator is near-universal, so it cannot discriminate."""
    representing = [p for p in PROFILES if p.represents_as_creator]
    assert len(representing) >= 2
    assert {is_true_moral_operator(p) for p in representing} == {True, False}


def test_the_source_alone_decides_the_verdict():
    """Two profiles differing only in source get opposite verdicts."""
    self_sourced = WillProfile("x", InvariantSource.SELF_SOURCED, False)
    externally = WillProfile("x", InvariantSource.EXTERNALLY_SOURCED, False)
    assert is_true_moral_operator(self_sourced) is True
    assert is_true_moral_operator(externally) is False


def test_absent_invariant_will_is_not_self_sourced():
    assert is_true_moral_operator(WillProfile("none", InvariantSource.ABSENT, True)) is False


def test_a_profile_rejects_a_non_enum_source():
    with pytest.raises(TypeError, match="InvariantSource"):
        WillProfile("x", "SELF_SOURCED", True)


def test_a_profile_rejects_an_empty_entity():
    with pytest.raises(ValueError, match="nonempty"):
        WillProfile("   ", InvariantSource.SELF_SOURCED, True)


def test_a_profile_rejects_a_non_boolean_self_representation():
    with pytest.raises(TypeError, match="bool"):
        WillProfile("x", InvariantSource.SELF_SOURCED, 1)


# --- what this layer deliberately does not contain --------------------------


def test_the_electrical_reading_is_not_in_this_layer():
    """Per the declared placement, the combination field holds all of it.

    Checked rather than documented: a foundation that kept a private copy of the
    correspondence would drift from the field that declares the bridges, which is
    exactly the failure the citation discipline exists to prevent.
    """
    import hyperethics.will as module

    for absent in (
        "CORRESPONDENCE", "Correspondence", "Termformer", "TERMFORMERS", "Term",
        "atom", "Equation", "DERIVED_EQUATIONS", "ConstantWill", "resonant_rate",
        "damping_ratio", "regime", "reciprocal_binding",
    ):
        assert not hasattr(module, absent), f"{absent} belongs to {ELECTROPHYSICS_LIVES_IN}"


def test_the_layer_names_where_the_electrical_reading_went():
    assert ELECTROPHYSICS_LIVES_IN == "metamathethicology.will_electrophysics"


def test_the_vocabulary_of_this_layer_is_will_native():
    """No enum member or public name here borrows an electrical term."""
    import hyperethics.will as module

    borrowed = ("induct", "ohm", "henry", "farad", "volt", "capacit", "resist")
    names = [n for n in dir(module) if not n.startswith("_")]
    for name in names:
        assert not any(word in name.lower() for word in borrowed), name
    for source in InvariantSource:
        assert not any(word in source.value.lower() for word in borrowed)


def test_this_package_does_not_import_its_combination_field():
    """The dependency runs one way; importing it back would cycle the stack."""
    import hyperethics

    assert not hasattr(hyperethics, "electrophysics_space")
    assert "metamathethicology" not in getattr(hyperethics, "__dict__", {})
