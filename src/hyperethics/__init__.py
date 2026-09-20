"""Hyperethics: a self-grounded moral foundation derived from creation alone.

The grounding moral operation is immanence: an archetypal creator exists within
the universe that it creates. The number one operational operant is
self-consistency: that creator is self-contained, dwelling in its whole creative
orbit including itself.

This package implements `L0_creation.hm` and `L1_will.hm`. It is dependency-free
by design: the L1 will layer borrows the algebraic shape of electrical law, and
it CITES those laws in the `hyperphysics` package by name rather than importing
it, so the foundation still stands on the standard library alone. Ordinal
staging, proof transport, and the bridge to metamathethicology belong to later
layers and are not present here.

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
    ChargeConstantLaw,
    Component,
    ConstantWill,
    Correspondence,
    Equation,
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
    temporal_chain,
    will_balance,
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
    "CAPACITANCE_READINGS_CONSIDERED", "CONSTANT", "CONSTANT_WILL_DECLARATION",
    "CONSTANT_WILL_LAW_IS_OPEN", "CONSTRAINS_A_FREE_SOURCE_PARAMETER",
    "CORRESPONDENCE", "DERIVED_EQUATIONS", "PROFILES", "SOURCE_FIELD",
    "TERMFORMERS", "ChargeConstantLaw", "Component", "ConstantWill",
    "Correspondence", "Equation", "InvariantSource", "Role", "Term",
    "Termformer", "Warrant", "WillProfile", "atom", "binding_is_functional",
    "damping_ratio", "different_invariant_need_not_change_rate",
    "is_true_moral_operator", "reciprocal_binding", "regime", "resonant_rate",
    "self_representation_does_not_entail_self_induction", "temporal_chain",
    "will_balance",
]
