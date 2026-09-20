"""Finite realm models, including the countermodels the L0 spec commits to.

Three kinds of structure live here.

Models of the axioms
    `minimal_model`, `separating_model`, and `orbit_model` satisfy all four L0
    axioms. They are used to exhibit the derives and, where they fail a stronger
    claim, to refute that claim conclusively.

Independence countermodels
    `without_other`, `without_immanence`, `without_return`, and
    `without_archetype_self` each satisfy exactly three axioms and fail the
    fourth. Together they establish that no L0 axiom follows from the other
    three, which is what Section III's "no redundancy" line asserts. This is a
    genuine result with finite witnesses, not a stylistic claim.

None of these structures is a model of any actual moral situation. They are
finite interpretations of four primitives. Reading a realm here as a person, a
world, an action, or an agent is an interpretation the L0 layer does not license.
"""

from __future__ import annotations

from .ground import RealmModel

ARCHETYPE = "archetype"


def minimal_model() -> RealmModel:
    """The smallest structure satisfying all four axioms.

    Two realms. The archetype creates `world`; `world` creates itself. Note that
    `world` creates a realm it does not inhabit, so even the smallest model of
    the axioms already contains a bearer that is not self-contained.
    """
    return RealmModel(
        name="minimal",
        realms=(ARCHETYPE, "world"),
        archetype=ARCHETYPE,
        creates=((ARCHETYPE, "world"), ("world", "world")),
        other=frozenset({("world", ARCHETYPE)}),
        inhabits=frozenset({(ARCHETYPE, ARCHETYPE), (ARCHETYPE, "world")}),
        returns=frozenset({("world", ARCHETYPE), ("world", "world")}),
    )


def separating_model() -> RealmModel:
    """Satisfies every axiom and contains a second creator that is not immanent.

    `rival` creates `world` and does not dwell in it. This separates the
    archetype from an arbitrary bearer and refutes `nd-universal-immanence`:
    the axioms constrain the archetype, not every creator.
    """
    return RealmModel(
        name="separating",
        realms=(ARCHETYPE, "rival", "world"),
        archetype=ARCHETYPE,
        creates=((ARCHETYPE, "world"), ("rival", "world"), ("world", "world")),
        other=frozenset({("world", ARCHETYPE)}),
        inhabits=frozenset({(ARCHETYPE, ARCHETYPE), (ARCHETYPE, "world")}),
        returns=frozenset(
            {("world", ARCHETYPE), ("world", "rival"), ("world", "world")}
        ),
    )


def orbit_model() -> RealmModel:
    """Satisfies every axiom while the three-step orbit fails to return.

    Creation cycles between `first` and `second`, so the two-step return that
    `ax-return` supplies holds while the three-step return does not. This
    refutes `nd-transitive-exposure`: exposure is a two-step result at L0 and
    any deeper reach must be paid for with an axiom.

    The archetype is still self-contained here, so the operant holds: a bounded
    exposure depth is not a failure of self-consistency.
    """
    return RealmModel(
        name="orbit",
        realms=(ARCHETYPE, "first", "second"),
        archetype=ARCHETYPE,
        creates=((ARCHETYPE, "first"), ("first", "second"), ("second", "first")),
        other=frozenset({("first", ARCHETYPE), ("second", ARCHETYPE)}),
        inhabits=frozenset(
            {(ARCHETYPE, ARCHETYPE), (ARCHETYPE, "first"), (ARCHETYPE, "second")}
        ),
        returns=frozenset(
            {("second", ARCHETYPE), ("first", "first"), ("second", "second")}
        ),
    )


MODELS = (minimal_model, separating_model, orbit_model)


# ---------------------------------------------------------------------------
# Independence countermodels: each fails exactly one axiom.
# ---------------------------------------------------------------------------


def without_other() -> RealmModel:
    """Fails only `ax-other`: nothing created is recorded as other than the creator."""
    base = minimal_model()
    return RealmModel(
        name="without-other",
        realms=base.realms,
        archetype=base.archetype,
        creates=base.creates,
        other=frozenset(),
        inhabits=base.inhabits,
        returns=base.returns,
    )


def without_immanence() -> RealmModel:
    """Fails only `ax-immanence`: the creator stands outside what it creates.

    This is the structure that shows the grounding moral operation is doing real
    work. Everything generative still holds here. What is gone is the normative
    force, and with it the operant: the archetype's orbit escapes it.
    """
    base = minimal_model()
    return RealmModel(
        name="without-immanence",
        realms=base.realms,
        archetype=base.archetype,
        creates=base.creates,
        other=base.other,
        inhabits=frozenset({(ARCHETYPE, ARCHETYPE)}),
        returns=base.returns,
    )


def without_return() -> RealmModel:
    """Fails only `ax-return`: authored consequence never lands."""
    base = minimal_model()
    return RealmModel(
        name="without-return",
        realms=base.realms,
        archetype=base.archetype,
        creates=base.creates,
        other=base.other,
        inhabits=base.inhabits,
        returns=frozenset(),
    )


def without_archetype_self() -> RealmModel:
    """Fails only `ax-archetype-self`: the creator is not self-contained.

    Immanence still reaches every created realm. The single point it cannot
    reach is the archetype itself, because the archetype is not `create(x)` for
    any `x`. The number one operational operant fails here at exactly one realm,
    which is why the self axiom is not bookkeeping.
    """
    base = minimal_model()
    return RealmModel(
        name="without-archetype-self",
        realms=base.realms,
        archetype=base.archetype,
        creates=base.creates,
        other=base.other,
        inhabits=frozenset({(ARCHETYPE, "world")}),
        returns=base.returns,
    )


INDEPENDENCE_MODELS = {
    "ax-other": without_other,
    "ax-immanence": without_immanence,
    "ax-return": without_return,
    "ax-archetype-self": without_archetype_self,
}
