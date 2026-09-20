"""Cross-check every borrowed law against the package that states it.

`hyperethics` does not depend on `hyperphysics` at runtime and does not want to:
the zero-dependency commitment in `DESIGN.md` is load-bearing for a foundation.
But a citation nobody checks is a paraphrase with extra steps, and paraphrases
drift. So the check lives here, and it runs whenever `hyperphysics` happens to be
importable.

When it is absent this module skips. A skip means the citations were NOT checked
on that run; it does not mean they were checked and passed. `VALIDATION.md`
records which of the two happened.
"""

from __future__ import annotations

import pytest

from hyperethics.will import (
    ACCUMULATED_DROP,
    CONSTRAINS_A_FREE_SOURCE_PARAMETER,
    TERMFORMERS,
)

hyperphysics = pytest.importorskip(
    "hyperphysics",
    reason="hyperphysics is not installed, so the cited laws cannot be checked",
)


@pytest.mark.parametrize("former", TERMFORMERS, ids=lambda f: f.name)
def test_every_cited_law_exists_in_hyperphysics(former):
    """A citation with no referent is the failure this interface exists to catch."""
    assert former.source_law in hyperphysics.LAWS_BY_NAME, (
        f"{former.name} cites '{former.source_law}', which hyperphysics does not state"
    )


@pytest.mark.parametrize("former", TERMFORMERS, ids=lambda f: f.name)
def test_every_quoted_form_matches_the_law_it_quotes(former):
    """The quoted form is a convenience, so it must not drift from the source."""
    law = hyperphysics.LAWS_BY_NAME[former.source_law]
    assert former.source_form == law.form


def test_the_will_balance_borrows_the_series_form_in_full():
    """Each of the three drops comes from one constituent of the series RLC form."""
    constituents = {law.name for law in hyperphysics.SERIES_RLC_CONSTITUENTS}
    borrowed = {f.source_law for f in TERMFORMERS}
    assert {"ohm", "faraday-lenz", "capacitor"} <= borrowed
    assert {"ohm", "faraday-lenz", "capacitor"} <= constituents


def test_self_and_mutual_induction_are_the_distinction_the_discriminator_uses():
    """hyperphysics records that the two differ only in source, not in form."""
    self_law = hyperphysics.LAWS_BY_NAME["self-inductance"]
    mutual = hyperphysics.LAWS_BY_NAME["mutual-inductance"]
    renamed = self_law.form.replace("L", "M").replace("dI/dt", "dI_1/dt")
    assert renamed == mutual.form.replace("emf_2", "emf")


def test_the_declared_departure_is_a_parameter_the_source_really_leaves_free():
    """Constraining capacitance is a departure only because a circuit leaves it free."""
    assert hyperphysics.Quantity.CAPACITANCE in hyperphysics.PARAMETERS_ARE_INDEPENDENT
    assert "capacitance" in CONSTRAINS_A_FREE_SOURCE_PARAMETER


def test_the_borrowing_satisfies_the_transport_interface():
    """Build hyperphysics Transports from the termformers and validate them."""
    transports = tuple(
        hyperphysics.Transport(
            law=former.source_law,
            target_field="hyperethics.will",
            target_form=former.head,
            transports=former.transports,
            does_not_transport=former.does_not_transport,
            warrant=hyperphysics.Warrant.BORROWED_FORM,
            constrains_parameters=(
                (hyperphysics.Quantity.CAPACITANCE,)
                if former is ACCUMULATED_DROP
                else ()
            ),
            constraint_reason=(
                CONSTRAINS_A_FREE_SOURCE_PARAMETER if former is ACCUMULATED_DROP else ""
            ),
        )
        for former in TERMFORMERS
    )
    for transport in transports:
        assert hyperphysics.validate(transport) is transport
    assert hyperphysics.audit(transports)


def test_transporting_the_capacitor_relation_inherits_its_failure_modes():
    """What the will layer takes on by borrowing, listed by the source."""
    transport = hyperphysics.Transport(
        law=ACCUMULATED_DROP.source_law,
        target_field="hyperethics.will",
        target_form="past / constant",
        transports=ACCUMULATED_DROP.transports,
        does_not_transport=ACCUMULATED_DROP.does_not_transport,
        warrant=hyperphysics.Warrant.BORROWED_FORM,
    )
    modes = hyperphysics.inherited_failure_modes(transport)
    assert any("dielectric" in mode for mode in modes)


def test_units_do_not_transport_is_the_standing_rule_on_both_sides():
    assert "do not attach to the algebraic form" in hyperphysics.UNITS_DO_NOT_TRANSPORT
