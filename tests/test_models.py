"""Tests for the declared structures, above all the axiom independence result."""

from __future__ import annotations

import pytest

from hyperethics import (
    AXIOM_NAMES,
    INDEPENDENCE_MODELS,
    MODELS,
    Status,
    check_axioms,
    failed_axioms,
    is_model,
    minimal_model,
    orbit_model,
    separating_model,
)


def test_every_axiom_has_an_independence_countermodel():
    """Section III claims four axioms with no redundancy. This is that claim."""
    assert set(INDEPENDENCE_MODELS) == set(AXIOM_NAMES)


@pytest.mark.parametrize("axiom", AXIOM_NAMES)
def test_each_countermodel_fails_exactly_its_own_axiom(axiom):
    """No L0 axiom follows from the other three: each fails while the rest hold.

    This is the conclusive half of the epistemic contract. One finite structure
    per axiom settles the independence of that axiom.
    """
    model = INDEPENDENCE_MODELS[axiom]()
    assert failed_axioms(model) == (axiom,)
    holding = [v.claim for v in check_axioms(model) if v.status is Status.HOLDS_IN_MODEL]
    assert len(holding) == 3
    assert axiom not in holding


@pytest.mark.parametrize("axiom", AXIOM_NAMES)
def test_an_independence_countermodel_is_not_a_model(axiom):
    assert not is_model(INDEPENDENCE_MODELS[axiom]())


@pytest.mark.parametrize("factory", MODELS, ids=lambda f: f.__name__)
def test_declared_models_are_models(factory):
    assert is_model(factory())


def test_minimal_model_is_the_smallest_declared_one():
    assert len(minimal_model().realms) == 2
    assert all(len(f().realms) >= 2 for f in MODELS)


def test_even_the_minimal_model_contains_a_bearer_that_is_not_self_contained():
    """Plurality of standing shows up at two realms; it is not an artifact of size."""
    from hyperethics import non_archetypal_bearers

    assert non_archetypal_bearers(minimal_model()) == ("world",)


def test_the_separating_model_distinguishes_the_archetype_from_another_creator():
    model = separating_model()
    assert "rival" in model.realms
    assert model.create("rival") == "world"
    assert ("rival", "world") not in model.inhabits
    assert (model.archetype, "world") in model.inhabits


def test_the_orbit_model_actually_cycles():
    model = orbit_model()
    assert model.create("first") == "second"
    assert model.create("second") == "first"
    assert model.create(model.create("first")) == "first"


@pytest.mark.parametrize("factory", MODELS, ids=lambda f: f.__name__)
def test_models_are_hashable_and_reconstructible(factory):
    """Frozen structures let a result be bound to the exact structure it came from."""
    first, second = factory(), factory()
    assert first == second
    assert hash(first) == hash(second)


def test_created_is_the_image_of_create_without_duplicates():
    model = separating_model()
    assert model.created == ("world",)
    assert minimal_model().created == ("world",)
    assert orbit_model().created == ("first", "second")
