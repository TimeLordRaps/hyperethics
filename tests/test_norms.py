"""Tests for the normative vocabulary, including what it deliberately cannot say."""

from __future__ import annotations

import inspect

import pytest

from hyperethics import (
    Status,
    all_standings,
    answerable_for,
    archetypal_bearers,
    archetype_is_self_contained,
    authored,
    dwells_in,
    exempt_realms,
    exposure,
    is_archetypal,
    minimal_model,
    non_archetypal_bearers,
    norms,
    orbit_model,
    separating_model,
    standing,
    without_archetype_self,
)

MODEL_FACTORIES = (minimal_model, separating_model, orbit_model)


@pytest.mark.parametrize("factory", MODEL_FACTORIES, ids=lambda f: f.__name__)
def test_the_archetype_is_archetypal_wherever_the_axioms_hold(factory):
    model = factory()
    assert is_archetypal(model, model.archetype)
    assert exempt_realms(model, model.archetype) == ()
    assert archetype_is_self_contained(model).status is Status.HOLDS_IN_MODEL


def test_an_arbitrary_creator_need_not_be_archetypal():
    """This is the L0 moral distinction, and it is structural rather than evaluative."""
    model = separating_model()
    assert not is_archetypal(model, "rival")
    assert "world" in exempt_realms(model, "rival")
    assert archetypal_bearers(model) == ("archetype",)
    assert non_archetypal_bearers(model) == ("rival", "world")


def test_a_bearer_escapes_itself_when_it_does_not_dwell_in_itself():
    model = separating_model()
    assert "rival" in exempt_realms(model, "rival")


def test_answerable_and_exempt_partition_the_creative_orbit():
    model = separating_model()
    for bearer in model.realms:
        entry = standing(model, bearer)
        assert set(entry.answerable_for) | set(entry.exempt_from) == set(entry.orbit)
        assert set(entry.answerable_for) & set(entry.exempt_from) == set()


def test_dropping_the_self_axiom_makes_the_archetype_non_archetypal():
    model = without_archetype_self()
    assert not is_archetypal(model, model.archetype)
    assert exempt_realms(model, model.archetype) == (model.archetype,)


def test_authored_and_dwells_in_read_the_ground_relations():
    model = minimal_model()
    assert authored(model, model.archetype) == "world"
    assert dwells_in(model, model.archetype) == ("archetype", "world")
    assert dwells_in(model, "world") == ()


def test_exposure_reports_what_returns_to_a_bearer():
    model = minimal_model()
    assert exposure(model, model.archetype) == ("world",)


def test_standing_summary_never_states_a_verdict_on_conduct():
    """L0 derives exposure and answerability. It must not imply an evaluation."""
    forbidden = ("good", "bad", "right", "wrong", "ought", "should",
                 "evil", "virtuous", "deserve", "blame", "guilty")
    for factory in MODEL_FACTORIES:
        for entry in all_standings(factory()):
            text = entry.summary().lower()
            assert not any(word in text for word in forbidden), entry.summary()


def test_the_norms_module_declares_no_evaluative_primitive():
    """nd-good-from-immanence is a commitment, so hold the code to it."""
    source = inspect.getsource(norms)
    names = [n for n in dir(norms) if not n.startswith("_")]
    for banned in ("good", "ought", "prefer", "value", "harm", "choose"):
        assert not any(n.lower() == banned for n in names), banned
    assert "def good" not in source
    assert "def ought" not in source


def test_unknown_bearers_are_rejected_rather_than_silently_empty():
    model = minimal_model()
    for function in (dwells_in, exposure, exempt_realms, answerable_for):
        with pytest.raises(KeyError):
            function(model, "nowhere")


def test_standing_covers_every_bearer_in_carrier_order():
    model = separating_model()
    entries = all_standings(model)
    assert tuple(e.bearer for e in entries) == model.realms
