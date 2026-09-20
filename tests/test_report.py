"""Tests that the executable report reports honestly.

These are not cosmetic. The report is the artifact most readers will run, and a
report that quietly upgraded an open obligation or called a checked claim proved
would misrepresent the whole layer.
"""

from __future__ import annotations

from hyperethics.report import OPEN_OBLIGATIONS, build_report, main


def test_the_report_runs_clean():
    assert main() == 0


def test_the_report_never_claims_universal_validity_for_a_checked_claim():
    """Catch affirmative overclaims only.

    A bare keyword scan is wrong here: the report legitimately contains the word
    "theorem" inside "no proof-assistant theorem", which is a disclaimer. What
    must never appear is an assertion that something was proved or is valid.
    """
    text = "\n".join(build_report()).lower()
    overclaims = (
        "is proved", "is proven", "we prove", "proves that", "is a theorem",
        "is valid", "hereby established", "has been established",
        "establishes that", "demonstrates that this is true",
    )
    for overclaim in overclaims:
        assert overclaim not in text, overclaim
    assert "no proof-assistant theorem" in text


def test_the_report_states_the_confirm_refute_asymmetry():
    text = "\n".join(build_report()).lower()
    assert "confirms nothing universally" in text
    assert "single countermodel settles" in text


def test_every_open_obligation_appears_unresolved():
    lines = build_report()
    text = "\n".join(lines)
    for title, status, _ in OPEN_OBLIGATIONS:
        assert title in text
        assert status in ("OPEN", "NOT_ESTABLISHED", "NOT_IMPLEMENTED")
    assert "OPEN OBLIGATIONS" in text


def test_the_paradox_is_named_exactly_and_left_open():
    text = "\n".join(build_report())
    assert "Universal Consistency Self-Maintenance Paradox" in text
    assert "OPEN" in text


def test_the_report_names_both_the_operation_and_the_operant():
    text = "\n".join(build_report())
    assert "GROUNDING MORAL OPERATION" in text
    assert "NUMBER ONE OPERANT" in text
    assert "self-contained" in text


def test_the_report_carries_every_conclusive_refutation():
    """Two from L0's realm models, one from L1's will layer."""
    text = "\n".join(build_report())
    assert text.count("REFUTED:") == 3
    assert "every bearer inhabits what it creates" in text
    assert "exposure reaches to depth three" in text
    assert "self-representation as creator entails a self-sourced" in text


def test_the_report_shows_the_independence_result():
    text = "\n".join(build_report())
    assert "No L0 axiom is a consequence of the others." in text
    assert "UNEXPECTED" not in text


def test_the_report_publishes_the_tensor_and_its_roles():
    """A reader who runs only this must see what a will is taken to be."""
    text = "\n".join(build_report())
    assert "L1 WILL" in text
    assert "temporal chain: past -> present -> future" in text
    for role in ("state", "coefficient", "driving"):
        assert role in text


def test_the_report_says_where_the_electrical_reading_went():
    """The split must be legible to a reader who runs only the report."""
    text = "\n".join(build_report())
    assert "WHAT THIS LAYER DOES NOT CONTAIN" in text
    assert "metamathethicology.will_electrophysics" in text
    assert "named bridge" in text


def test_the_report_records_the_numeric_refutation_it_no_longer_owns():
    """The result bears on this layer's discriminator, so the report keeps it."""
    text = "\n".join(build_report())
    assert "does NOT entail a different resonant rate" in text
    assert "is_true_moral_operator is what" in text


def test_the_report_no_longer_carries_the_borrowed_material():
    """A leftover copy here would drift from the field that declares the bridges."""
    text = "\n".join(build_report())
    for gone in ("TERMFORMERS", "BORROWED_FORM", "SUPERSEDED", "hyperphysics:ohm",
                 "DEPARTURE FROM THE SOURCE DOMAIN"):
        assert gone not in text
