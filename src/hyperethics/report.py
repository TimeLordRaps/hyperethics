"""The executable L0 status report.

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
)


def _line(label: str, value: object) -> str:
    return f"  {label:<44} {value}"


def build_report() -> list[str]:
    """Produce the report as lines, so tests can assert on it without capture."""
    out: list[str] = []
    out.append("hyperethics L0 -- creation ground")
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
