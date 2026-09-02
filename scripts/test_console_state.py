#!/usr/bin/env python3
"""Regression tests for the console state extractor.

These lock in behavior that the console's honesty claims depend on. Each test
exists because the opposite behavior would let the console present a system as
better verified than its evidence supports.

Stdlib only, no test framework, consistent with the other scripts here.

    python3 scripts/test_console_state.py
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("build_console_state", ROOT / "scripts" / "build_console_state.py")
bcs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bcs)

FAILURES: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    if condition:
        print(f"  pass  {name}")
    else:
        print(f"  FAIL  {name}{': ' + detail if detail else ''}")
        FAILURES.append(name)


def with_evidence(patched_block: str, original_block: str):
    """Temporarily swap a block into acceptance-evidence.yaml."""
    src = ROOT / "evaluations" / "acceptance-evidence.yaml"
    backup = src.read_text(encoding="utf-8")
    if original_block not in backup:
        raise AssertionError("fixture block not found; update the test to match the file")
    src.write_text(backup.replace(original_block, patched_block, 1), encoding="utf-8")
    return src, backup


# ---------------------------------------------------------------------------

def test_yaml_same_indent_sequence() -> None:
    """A block sequence may sit at the same indent as its key.

    The committed files all use inline `evidence: []`, so this path is only
    reached once real evidence is recorded. Getting it wrong would crash the
    console exactly when the repository starts proving things.
    """
    print("YAML: block sequence at parent indent")
    text = "results:\n  a:\n    status: pass\n    evidence:\n    - run-1\n    - run-2\n  b:\n    status: not_run\n"
    tmp = ROOT / "scripts" / ".test_tmp.yaml"
    try:
        tmp.write_text(text, encoding="utf-8")
        parsed = bcs.read_yaml(tmp)
        check("parses same-indent list", parsed["results"]["a"]["evidence"] == ["run-1", "run-2"],
              repr(parsed.get("results", {}).get("a")))
        check("sibling key after list", parsed["results"]["b"]["status"] == "not_run")
    finally:
        tmp.unlink(missing_ok=True)


def test_invalidation_dominates() -> None:
    """Rule 16: a material change invalidates the evidence it affects.

    A recorded pass that also carries invalidated_evidence is stale, not proven.
    Without this, a stale critical pass counts toward critical_proven and the
    console can present a release as current on dead evidence.
    """
    print("Acceptance: invalidation dominates recorded status")
    original = "  handoff-authority:\n    status: not_run\n    evidence: []"
    patched = (
        "  handoff-authority:\n    status: pass\n    evidence:\n    - run-2026-08-01\n"
        "    invalidated_evidence:\n      reason: superseded by later hardening"
    )
    src, backup = with_evidence(patched, original)
    try:
        a = bcs.collect_acceptance()
        row = next(t for t in a["tests"] if t["id"] == "handoff-authority")
        check("invalidated pass resolves to stale", row["state"] == "stale", f"got {row['state']}")
        check("stale pass excluded from critical_proven", a["critical_proven"] == 0,
              f"got {a['critical_proven']}")
    finally:
        src.write_text(backup, encoding="utf-8")


def test_skill_identity_from_frontmatter() -> None:
    """Skill identity is the SKILL.md `name`, not the directory basename.

    skills/founder-command-center-operator/ declares `name: cofound-operator`,
    which is what the fitness registry uses. Keying on the basename splits one
    skill into a phantom registry-only row and a phantom contract-only row, and
    inflates the total.
    """
    print("Skills: identity read from frontmatter")
    s = bcs.collect_skills()
    names = [k["name"] for k in s["items"]]
    check("no duplicate identities", len(names) == len(set(names)))
    check("directory basename not used as identity",
          "founder-command-center-operator" not in names)
    row = next((k for k in s["items"] if k["name"] == "cofound-operator"), None)
    check("declared name present", row is not None)
    if row:
        check("unified: has both contract and registry entry",
              row["has_contract"] and row["registered"],
              f"contract={row['has_contract']} registered={row['registered']}")


def test_no_self_referential_commit() -> None:
    """The payload records no commit identity of its own.

    This artifact is committed, so any SHA it records is the one before the
    commit containing it, and the tree is dirty at generation time so a dirty
    flag would be baked in permanently. Both would be wrong by construction.
    """
    print("Payload: no self-referential repository metadata")
    state = bcs.build_state()
    check("no 'repo' key", "repo" not in state)
    flat = repr(state)
    check("no dirty flag", "'dirty'" not in flat)


def test_verdict_never_better_than_worst_input() -> None:
    """The headline verdict is governed by the worst material input."""
    print("Verdict: governed by worst material input")
    state = bcs.build_state()
    v = state["verdict"]
    if v["blocking"]:
        check("blocking conditions prevent a proven verdict", v["state"] != "proven",
              f"got {v['state']} with {len(v['blocking'])} blocking")
    else:
        check("no blocking conditions recorded", True)
    a = state["acceptance"]
    check("critical_proven never exceeds critical_total",
          a["critical_proven"] <= a["critical_total"])
    check("executed never exceeds total", a["executed"] <= a["total"])


def main() -> int:
    for test in (
        test_yaml_same_indent_sequence,
        test_invalidation_dominates,
        test_skill_identity_from_frontmatter,
        test_no_self_referential_commit,
        test_verdict_never_better_than_worst_input,
    ):
        test()

    print()
    if FAILURES:
        print(f"console state tests FAILED: {len(FAILURES)} failure(s)")
        for name in FAILURES:
            print(f"  - {name}")
        return 1
    print("console state tests PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
