"""Tests for the L0 ground: structure validation, axioms, derives, and the operant."""

from __future__ import annotations

import pytest

from hyperethics import (
    NotAModel,
    RealmModel,
    Status,
    Verdict,
    check_axioms,
    check_derives,
    creative_orbit,
    d_self_contained,
    failed_axioms,
    is_model,
    minimal_model,
    operant_self_consistency,
    orbit_model,
    other_is_nonidentity,
    refuted_by,
    self_contained,
    separating_model,
    transitive_exposure,
    universal_immanence,
    without_archetype_self,
    without_immanence,
)

MODEL_FACTORIES = (minimal_model, separating_model, orbit_model)


# --- the epistemic contract -------------------------------------------------


def test_verdict_has_no_truth_value():
    """HOLDS_IN_MODEL is not validity, so a Verdict must not be usable as a bool."""
    verdict = Verdict("some-claim", Status.HOLDS_IN_MODEL)
    with pytest.raises(TypeError, match="no truth value"):
        bool(verdict)
    with pytest.raises(TypeError, match="no truth value"):
        if verdict:  # pragma: no branch - the guard is the point
            pass


def test_a_holding_verdict_may_not_carry_a_witness():
    with pytest.raises(ValueError, match="no distinguished witness"):
        Verdict("c", Status.HOLDS_IN_MODEL, ("x",))


def test_a_failing_verdict_must_name_its_counterexample():
    with pytest.raises(ValueError, match="must name its counterexample"):
        Verdict("c", Status.FAILS_IN_MODEL)


def test_a_non_model_refutes_nothing():
    """A failure inside a structure that breaks an axiom says nothing about the theory."""
    broken = without_immanence()
    verdict = universal_immanence(broken)
    assert verdict.status is Status.FAILS_IN_MODEL
    with pytest.raises(NotAModel, match="refutes nothing"):
        refuted_by("every bearer inhabits what it creates", verdict, broken)


def test_a_refutation_requires_an_actual_failure():
    model = minimal_model()
    holding = Verdict("c", Status.HOLDS_IN_MODEL)
    with pytest.raises(ValueError, match="requires a failure"):
        refuted_by("c", holding, model)


# --- structure validation ---------------------------------------------------


def test_create_must_be_a_total_function():
    with pytest.raises(ValueError, match="total function"):
        RealmModel(
            name="partial", realms=("a", "b"), archetype="a",
            creates=(("a", "b"),),
            other=frozenset(), inhabits=frozenset(), returns=frozenset(),
        )


def test_create_may_not_leave_the_carrier():
    with pytest.raises(ValueError, match="land inside the carrier"):
        RealmModel(
            name="escaping", realms=("a",), archetype="a",
            creates=(("a", "elsewhere"),),
            other=frozenset(), inhabits=frozenset(), returns=frozenset(),
        )


def test_the_archetype_is_never_of_another_kind():
    """Co-typing is the structural precondition of immanence, so this must fail."""
    with pytest.raises(ValueError, match="must be a realm"):
        RealmModel(
            name="two-typed", realms=("w",), archetype="outside",
            creates=(("w", "w"),),
            other=frozenset(), inhabits=frozenset(), returns=frozenset(),
        )


def test_relations_may_not_mention_unknown_realms():
    with pytest.raises(ValueError, match="unknown realm"):
        RealmModel(
            name="dangling", realms=("a",), archetype="a",
            creates=(("a", "a"),),
            other=frozenset({("a", "ghost")}), inhabits=frozenset(), returns=frozenset(),
        )


def test_realm_names_must_be_unique():
    with pytest.raises(ValueError, match="unique"):
        RealmModel(
            name="dup", realms=("a", "a"), archetype="a",
            creates=(("a", "a"),),
            other=frozenset(), inhabits=frozenset(), returns=frozenset(),
        )


# --- axioms and derives -----------------------------------------------------


@pytest.mark.parametrize("factory", MODEL_FACTORIES, ids=lambda f: f.__name__)
def test_declared_models_satisfy_every_axiom(factory):
    model = factory()
    assert is_model(model), failed_axioms(model)
    assert all(v.status is Status.HOLDS_IN_MODEL for v in check_axioms(model))


@pytest.mark.parametrize("factory", MODEL_FACTORIES, ids=lambda f: f.__name__)
def test_every_derive_holds_in_every_model_of_the_axioms(factory):
    model = factory()
    for verdict in check_derives(model):
        assert verdict.status is Status.HOLDS_IN_MODEL, verdict


# --- the number one operational operant -------------------------------------


@pytest.mark.parametrize("factory", MODEL_FACTORIES, ids=lambda f: f.__name__)
def test_the_operant_holds_wherever_the_axioms_hold(factory):
    """Self-consistency is derived from ax-immanence plus ax-archetype-self."""
    model = factory()
    assert operant_self_consistency(model).status is Status.HOLDS_IN_MODEL
    assert d_self_contained(model).status is Status.HOLDS_IN_MODEL


def test_dropping_the_self_axiom_breaks_the_operant_at_exactly_one_realm():
    """The archetype is the one orbit member immanence alone cannot reach."""
    model = without_archetype_self()
    verdict = operant_self_consistency(model)
    assert verdict.status is Status.FAILS_IN_MODEL
    assert verdict.witness == (model.archetype,)


def test_dropping_immanence_breaks_the_operant_too():
    model = without_immanence()
    assert operant_self_consistency(model).status is Status.FAILS_IN_MODEL


def test_the_operant_needs_both_axioms_and_neither_alone_suffices():
    """Exactly the two axioms d-self-contained cites are the ones that break it."""
    assert operant_self_consistency(without_immanence()).status is Status.FAILS_IN_MODEL
    assert operant_self_consistency(without_archetype_self()).status is Status.FAILS_IN_MODEL


# --- orbits -----------------------------------------------------------------


def test_creative_orbit_terminates_on_a_cycle():
    model = orbit_model()
    assert creative_orbit(model, model.archetype) == ("archetype", "first", "second")
    assert creative_orbit(model, "first") == ("first", "second")


def test_creative_orbit_is_reflexive():
    model = minimal_model()
    assert creative_orbit(model, "world")[0] == "world"


def test_creative_orbit_rejects_an_unknown_realm():
    with pytest.raises(KeyError):
        creative_orbit(minimal_model(), "nowhere")


def test_self_contained_rejects_an_unknown_bearer():
    with pytest.raises(KeyError):
        self_contained(minimal_model(), "nowhere")


# --- conclusive refutations -------------------------------------------------


def test_universal_immanence_is_refuted_conclusively():
    model = separating_model()
    verdict = universal_immanence(model)
    assert verdict.status is Status.FAILS_IN_MODEL
    assert verdict.witness == ("rival",)
    assert "REFUTED" in refuted_by("universal immanence", verdict, model)


def test_exposure_does_not_reach_depth_three():
    model = orbit_model()
    assert transitive_exposure(model, depth=2).status is Status.HOLDS_IN_MODEL
    verdict = transitive_exposure(model, depth=3)
    assert verdict.status is Status.FAILS_IN_MODEL
    assert "REFUTED" in refuted_by("depth-three exposure", verdict, model)


def test_depth_must_be_a_positive_integer():
    with pytest.raises(ValueError, match="positive integer"):
        transitive_exposure(minimal_model(), depth=0)


# --- the L1 question, asked but not answered at L0 --------------------------


def test_other_is_opaque_at_l0_so_a_reflexive_reading_is_allowed():
    """`other` being nonidentity is an L1 close, not an L0 constraint."""
    reflexive = RealmModel(
        name="reflexive-other", realms=("a", "w"), archetype="a",
        creates=(("a", "w"), ("w", "w")),
        other=frozenset({("w", "a"), ("a", "a")}),
        inhabits=frozenset({("a", "a"), ("a", "w")}),
        returns=frozenset({("w", "a"), ("w", "w")}),
    )
    assert is_model(reflexive)
    assert other_is_nonidentity(reflexive).status is Status.FAILS_IN_MODEL
    assert other_is_nonidentity(minimal_model()).status is Status.HOLDS_IN_MODEL
