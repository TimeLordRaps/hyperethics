"""Hyperethics: a self-grounded moral foundation derived from creation alone.

The grounding moral operation is immanence: an archetypal creator exists within
the universe that it creates. The number one operational operant is
self-consistency: that creator is self-contained, dwelling in its whole creative
orbit including itself.

This package implements `L0_creation.hm` and `L1_will.hm`, and nothing else. It
is dependency-free by design and by placement: L1 states what a will IS -- six
components, three roles, an ordering on the temporal three, and the source of the
invariant -- without borrowing anything to state it.

The electrical reading of that tensor is deliberately absent. Per Tyler's
declared placement, electrical law belongs in `hyperphysics` and the combination
of the two is a field of its own, `metamathethicology.will_electrophysics`, where
a cross-domain rule cannot be constructed without a named bridge. A foundation
that had to cite physics in order to say what its own subject matter is would
not be a foundation.

Nothing in this package tells anyone what to do. It derives exposure and
answerability from immanence; it does not derive good, right, or obligatory, and
`nd-good-from-immanence` records that limit as a deliberate one.
"""

from __future__ import annotations

from .ground import (
    AXIOM_NAMES,
    AXIOMS,
    DERIVES,
    NotAModel,
    RealmModel,
    Status,
    Verdict,
    ax_archetype_self,
    ax_immanence,
    ax_other,
    ax_return,
    check_axioms,
    check_derives,
    creative_orbit,
    d_authorship_exposure,
    d_no_exterior,
    d_self_contained,
    d_two_bearers,
    failed_axioms,
    is_model,
    operant_self_consistency,
    other_is_nonidentity,
    refuted_by,
    self_contained,
    transitive_exposure,
    universal_immanence,
)
from .models import (
    INDEPENDENCE_MODELS,
    MODELS,
    minimal_model,
    orbit_model,
    separating_model,
    without_archetype_self,
    without_immanence,
    without_other,
    without_return,
)
from .norms import (
    Standing,
    all_standings,
    answerable_for,
    archetypal_bearers,
    archetype_is_self_contained,
    authored,
    dwells_in,
    exempt_realms,
    exposure,
    is_archetypal,
    non_archetypal_bearers,
    standing,
)
from .will import (
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

__version__ = "0.1.0.dev0"

__all__ = [
    "AXIOMS", "AXIOM_NAMES", "DERIVES", "INDEPENDENCE_MODELS", "MODELS",
    "NotAModel", "RealmModel", "Standing", "Status", "Verdict",
    "all_standings", "answerable_for", "archetypal_bearers",
    "archetype_is_self_contained", "authored", "ax_archetype_self",
    "ax_immanence", "ax_other", "ax_return", "check_axioms", "check_derives",
    "creative_orbit", "d_authorship_exposure", "d_no_exterior",
    "d_self_contained", "d_two_bearers", "dwells_in", "exempt_realms",
    "exposure", "failed_axioms", "is_archetypal", "is_model", "minimal_model",
    "non_archetypal_bearers", "operant_self_consistency", "orbit_model",
    "other_is_nonidentity", "refuted_by", "self_contained", "separating_model",
    "standing", "transitive_exposure", "universal_immanence",
    "without_archetype_self", "without_immanence", "without_other",
    "without_return",
    # L1 will
    "ELECTROPHYSICS_LIVES_IN", "PROFILES", "ROLE_OF", "Component",
    "InvariantSource", "Role", "WillProfile", "components_with_role",
    "is_true_moral_operator", "role_of",
    "self_representation_does_not_entail_self_sourcing", "temporal_chain",
]
