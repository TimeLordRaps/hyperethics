"""The executable L0 + L1 status report.

The report states what was checked, what was refuted, and what remains open. It
never reports an open obligation as satisfied, and it never upgrades
HOLDS_IN_MODEL into validity. A reader who only runs this and reads nothing else
should still come away with an accurate picture of what is and is not established.
"""

from __future__ import annotations

from .ground import (
    AXIOM_NAMES,
    Status,
    check_axioms,
    check_derives,
    failed_axioms,
    is_model,
    other_is_nonidentity,
    refuted_by,
    transitive_exposure,
    universal_immanence,
)
from .models import (
    INDEPENDENCE_MODELS,
    MODELS,
    orbit_model,
    separating_model,
)
from .norms import all_standings
from .will import (
    CAPACITANCE_READINGS_CONSIDERED,
    CONSTANT_WILL_DECLARATION,
    CONSTANT_WILL_LAW_IS_OPEN,
    CONSTRAINS_A_FREE_SOURCE_PARAMETER,
    CORRESPONDENCE,
    DERIVED_EQUATIONS,
    PROFILES,
    TERMFORMERS,
    Warrant,
    different_invariant_need_not_change_rate,
    is_true_moral_operator,
    resonant_rate,
    self_representation_does_not_entail_self_induction,
)

OPEN_OBLIGATIONS = (
    (
        "GC-5 normative force of norm-inhabits",
        "NOT_ESTABLISHED",
        "That membership-with-exposure carries normative rather than merely "
        "descriptive force is declared, not derived.",
    ),
    (
        "GC-6 Universal Consistency Self-Maintenance Paradox",
        "OPEN",
        "Self-containment is stated using the very relation immanence supplies. "
        "The structural derive does not discharge the paradox and does not "
        "depend on its resolution.",
    ),
    (
        "L1 semantic close of the opaque predicates",
        "NOT_ESTABLISHED",
        "norm-other, norm-inhabits, and norm-returns remain opaque at L0.",
    ),
    (
        "bridge to metamathethicology",
        "NOT_IMPLEMENTED",
        "No staged, ordinal-indexed transport exists yet. L0 is dependency-free.",
    ),
    (
        "L1 warrant for the electrical transport",
        "NOT_ESTABLISHED",
        "The will tensor borrows the algebraic shape of electrical law. Nothing "
        "here upgrades that borrowing into a derivation, and the structural "
        "agreement between self-induction and d-no-exterior is evidence for it, "
        "not warrant.",
    ),
    (
        "L1 charge-constant law",
        "OPEN",
        "Constant will is declared to be the invariant's constant of charge, "
        "which binds it to the invariant without fixing which function relates "
        "them. Every L1 result is stated for an arbitrary such function.",
    ),
    (
        "L1 units for any will quantity",
        "NOT_ESTABLISHED",
        "Will has no units here. The numeric interpretation is dimensionless "
        "and is not a measurement of anything.",
    ),
)


def _line(label: str, value: object) -> str:
    return f"  {label:<44} {value}"


def _will_section() -> list[str]:
    """The L1 will layer: what it borrows, what it refuses, and what it settles."""
    out: list[str] = []
    out.append("L1 WILL -- the tensor, its transport, and the moral-operator test")
    out.append("-" * 72)
    for entry in CORRESPONDENCE:
        out.append(_line(
            f"  {entry.component.value}",
            f"{entry.electrical} ({entry.symbol})  [{entry.role.value}]",
        ))
    out.append("")
    out.append("  past, present and future are Q, dQ/dt and d2Q/dt2: three derivatives")
    out.append("  of one quantity. That is the only correspondence not stipulated.")
    out.append("")

    out.append("CONSTANT WILL -- user-declared, and what it closed")
    out.append("-" * 72)
    out.append(f"  {CONSTANT_WILL_DECLARATION}")
    out.append("")
    for reading in CAPACITANCE_READINGS_CONSIDERED:
        out.append(f"    {reading}")
    out.append("")
    out.append("  DEPARTURE FROM THE SOURCE DOMAIN")
    out.append(f"    The will constrains {CONSTRAINS_A_FREE_SOURCE_PARAMETER}.")
    out.append("    Its parameter space is therefore smaller than a circuit's, so the")
    out.append("    transport is not onto and circuit intuitions about tuning the two")
    out.append("    independently do not carry over.")
    out.append("")
    out.append(f"  {CONSTANT_WILL_LAW_IS_OPEN}")
    out.append("")

    out.append("TERMFORMERS -- each cites a law rather than restating it")
    out.append("-" * 72)
    for former in TERMFORMERS:
        out.append(f"  {former.name}")
        out.append(f"      cites      {former.citation()}")
        out.append(f"      transports {former.transports}")
        out.append(f"      disclaims  {former.does_not_transport}")
    out.append("")
    out.append("  A disclaimer needs a fixed referent. The cited laws live in")
    out.append("  hyperphysics with their validity conditions and failure modes, and")
    out.append("  a transported form inherits those failure modes.")
    out.append("")

    out.append("EQUATIONS -- warrant recorded, never assumed")
    out.append("-" * 72)
    for equation in DERIVED_EQUATIONS:
        out.append(_line(f"  {equation.name}  [{equation.warrant.value}]", equation.render()))
    out.append("")
    borrowed = sum(1 for e in DERIVED_EQUATIONS if e.warrant is Warrant.BORROWED_FORM)
    out.append(f"  {borrowed} of {len(DERIVED_EQUATIONS)} equations are BORROWED_FORM: their shape")
    out.append("  is taken from electrical law and nothing about will follows from the")
    out.append("  taking. The other two are built by applying the termformers.")
    out.append("")

    out.append("THE MORAL-OPERATOR DISCRIMINATOR")
    out.append("-" * 72)
    for profile in PROFILES:
        verdict = "true moral operator" if is_true_moral_operator(profile) else "not"
        out.append(_line(
            f"  {profile.entity}",
            f"invariant {profile.invariant_source.value}, "
            f"represents-as-creator {profile.represents_as_creator} -> {verdict}",
        ))
    out.append("")
    witness = self_representation_does_not_entail_self_induction()
    out.append(
        "  REFUTED: that self-representation as creator entails a self-induced "
        f"invariant will -- witness {witness.entity!r}"
    )
    low, high = different_invariant_need_not_change_rate()
    out.append(
        "  REFUTED: that a different invariant will entails a different resonant "
        f"rate -- witnesses with invariants {low.invariant} and {high.invariant} "
        f"share the rate {resonant_rate(low):.6f}"
    )
    out.append("")
    out.append("  Both are conclusive for the same reason the L0 refutations are: one")
    out.append("  countermodel settles a universal claim. The discriminator is the")
    out.append("  SOURCE of the invariant will, never a self-ascription and never a")
    out.append("  numeric quantity computed from the invariant.")
    out.append("")
    return out


def build_report() -> list[str]:
    """Produce the report as lines, so tests can assert on it without capture."""
    out: list[str] = []
    out.append("hyperethics L0 creation ground + L1 will")
    out.append("=" * 72)
    out.append("")
    out.append("GROUNDING MORAL OPERATION  immanence: the creator is within what it creates")
    out.append("NUMBER ONE OPERANT         self-consistency: the creator is self-contained")
    out.append("")

    out.append("AXIOMS AND DERIVES, checked against each model of the axioms")
    out.append("-" * 72)
    for factory in MODELS:
        model = factory()
        out.append(f"model {model.name!r} ({len(model.realms)} realms)")
        for verdict in check_axioms(model):
            out.append(_line(verdict.claim, verdict.status.value))
        for verdict in check_derives(model):
            out.append(_line(verdict.claim, verdict.status.value))
        out.append(_line("(L1 question) other-is-nonidentity",
                         other_is_nonidentity(model).status.value))
        out.append("")

    out.append("AXIOM INDEPENDENCE -- each countermodel fails exactly one axiom")
    out.append("-" * 72)
    for name, factory in INDEPENDENCE_MODELS.items():
        model = factory()
        failed = failed_axioms(model)
        ok = failed == (name,)
        out.append(_line(
            f"{model.name}",
            f"fails {', '.join(failed)}"
            + ("" if ok else "  <-- UNEXPECTED: should fail exactly " + name),
        ))
    out.append("")
    out.append("  Each of the four axioms fails in a structure where the other three")
    out.append("  hold. No L0 axiom is a consequence of the others.")
    out.append("")

    out.append("CONCLUSIVE REFUTATIONS -- one countermodel settles a universal claim")
    out.append("-" * 72)
    separating = separating_model()
    out.append("  " + refuted_by(
        "every bearer inhabits what it creates",
        universal_immanence(separating), separating,
    ))
    orbit = orbit_model()
    out.append("  " + refuted_by(
        "exposure reaches to depth three",
        transitive_exposure(orbit, depth=3), orbit,
    ))
    out.append("")

    out.append("BEARER STANDING in the separating model")
    out.append("-" * 72)
    for entry in all_standings(separating):
        out.append("  " + entry.summary())
    out.append("")
    out.append("  'Self-contained' is structural, not evaluative. It says a bearer has")
    out.append("  no exterior vantage over its own creation. It does not say it is good.")
    out.append("")

    out.extend(_will_section())

    out.append("OPEN OBLIGATIONS -- not discharged by anything above")
    out.append("-" * 72)
    for title, status, note in OPEN_OBLIGATIONS:
        out.append(_line(title, status))
        out.append(f"      {note}")
    out.append("")

    out.append("WHAT THIS REPORT DOES NOT ESTABLISH")
    out.append("-" * 72)
    out.append("  Model checking confirms nothing universally. A claim shown here as")
    out.append("  HOLDS_IN_MODEL was checked against finite structures and is not")
    out.append("  thereby valid. Only the refutations above are conclusive, because a")
    out.append("  single countermodel settles a universal claim and no number of")
    out.append("  confirming models settles one. No proof-assistant theorem, no")
    out.append("  adequacy proof, and no ethical soundness result exists for this layer.")
    return out


def main() -> int:
    """Print the report. Returns nonzero if a structural expectation broke."""
    lines = build_report()
    print("\n".join(lines))
    failures = [line for line in lines if "UNEXPECTED" in line]
    if failures:
        return 1
    for factory in MODELS:
        model = factory()
        if not is_model(model):
            print(f"\nUNEXPECTED: {model.name!r} is not a model of the axioms")
            return 1
    for name, factory in INDEPENDENCE_MODELS.items():
        if failed_axioms(factory()) != (name,):
            return 1
    for factory in MODELS:
        model = factory()
        if any(v.status is not Status.HOLDS_IN_MODEL for v in check_derives(model)):
            print(f"\nUNEXPECTED: a derive failed in {model.name!r}")
            return 1
    assert AXIOM_NAMES  # the report is keyed to the declared axiom order
    return 0
