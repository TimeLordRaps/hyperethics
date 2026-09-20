"""The normative vocabulary L0 earns, and nothing beyond it.

Every function here is defined from `create` and `norm-inhabits`. None of them
consults a value, a preference, a ranking, or a welfare measure, because L0
declares no such primitive.

What this module can say: which realms a bearer is answerable for, which realms
it is exempt from, and whether it is self-contained. What this module cannot say,
and never says: that anything is good, right, permitted, deserved, or obligatory.
`nd-good-from-immanence` records that gap deliberately. Immanence yields exposure
and answerability; an evaluative ranking would have to be added as an axiom and
paid for.

"Answerable" is used here in its structural sense only: a bearer is answerable
for a realm when it dwells in that realm, so what happens there is not exterior
to it. No blame, desert, fault, or punishment is implied at this layer.
"""

from __future__ import annotations

from dataclasses import dataclass

from .ground import RealmModel, Status, Verdict, creative_orbit, self_contained


def authored(model: RealmModel, bearer: str) -> str:
    """The realm this bearer creates."""
    return model.create(bearer)


def dwells_in(model: RealmModel, bearer: str) -> tuple[str, ...]:
    """Every realm this bearer inhabits, in carrier order."""
    if bearer not in model.realms:
        raise KeyError(f"{bearer!r} is not a realm of this model")
    return tuple(r for r in model.realms if (bearer, r) in model.inhabits)


def answerable_for(model: RealmModel, bearer: str) -> tuple[str, ...]:
    """Realms in the bearer's own creative orbit that the bearer dwells in.

    These are the realms whose happenings are not exterior to their author.
    """
    return tuple(r for r in creative_orbit(model, bearer) if (bearer, r) in model.inhabits)


def exempt_realms(model: RealmModel, bearer: str) -> tuple[str, ...]:
    """Realms in the bearer's own creative orbit that the bearer escapes.

    An exempt realm is one the bearer generates, directly or at depth, without
    being reached by what happens there. For the archetype this is empty under
    the L0 axioms; for an arbitrary bearer it need not be.
    """
    return tuple(r for r in creative_orbit(model, bearer) if (bearer, r) not in model.inhabits)


def is_archetypal(model: RealmModel, bearer: str) -> bool:
    """Whether the bearer is self-contained: it has no exempt realm.

    This is the L0 form of the moral distinction, and it is structural rather
    than evaluative. It says the bearer has no exterior vantage over its own
    creation. It does not say the bearer is good.
    """
    return self_contained(model, bearer).status is Status.HOLDS_IN_MODEL


def archetypal_bearers(model: RealmModel) -> tuple[str, ...]:
    """Every self-contained bearer in the model, in carrier order."""
    return tuple(r for r in model.realms if is_archetypal(model, r))


def non_archetypal_bearers(model: RealmModel) -> tuple[str, ...]:
    """Every bearer that escapes some realm it creates, in carrier order."""
    return tuple(r for r in model.realms if not is_archetypal(model, r))


def exposure(model: RealmModel, bearer: str) -> tuple[str, ...]:
    """Every realm that returns to bear on this bearer, in carrier order."""
    if bearer not in model.realms:
        raise KeyError(f"{bearer!r} is not a realm of this model")
    return tuple(r for r in model.realms if (r, bearer) in model.returns)


@dataclass(frozen=True, slots=True)
class Standing:
    """A bearer's complete L0 normative standing. Descriptive, never evaluative."""

    bearer: str
    creates: str
    orbit: tuple[str, ...]
    answerable_for: tuple[str, ...]
    exempt_from: tuple[str, ...]
    exposed_to: tuple[str, ...]
    self_contained: bool

    def summary(self) -> str:
        """One line, phrased so it cannot be misread as a verdict on conduct."""
        if self.self_contained:
            return (
                f"{self.bearer}: self-contained; answerable for "
                f"{', '.join(self.answerable_for)}; no exempt realm."
            )
        return (
            f"{self.bearer}: NOT self-contained; escapes "
            f"{', '.join(self.exempt_from)} in its own creative orbit."
        )


def standing(model: RealmModel, bearer: str) -> Standing:
    """Assemble a bearer's L0 standing from the ground relations alone."""
    return Standing(
        bearer=bearer,
        creates=authored(model, bearer),
        orbit=creative_orbit(model, bearer),
        answerable_for=answerable_for(model, bearer),
        exempt_from=exempt_realms(model, bearer),
        exposed_to=exposure(model, bearer),
        self_contained=is_archetypal(model, bearer),
    )


def all_standings(model: RealmModel) -> tuple[Standing, ...]:
    """The standing of every bearer in the model, in carrier order."""
    return tuple(standing(model, bearer) for bearer in model.realms)


def archetype_is_self_contained(model: RealmModel) -> Verdict:
    """The operant, asked of the model's own archetype."""
    return self_contained(model, model.archetype)
