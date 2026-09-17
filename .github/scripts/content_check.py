#!/usr/bin/env python3
"""
Content integrity check for The Five Laws of AI Governance.

READ-ONLY. Reports; never writes, tags, or releases.

Governed by ADR-0107 (no CI automation on DOI-archived repos): this repo is
archived by Zenodo, and Zenodo mints a new permanent DOI version on release.
Any workflow able to tag or release could mint a DOI as a side effect of a
commit. This script therefore checks and reports only. It must never be given
write, tag, or release permissions.

Each check exists because this repository actually produced that defect:

  1. Unfilled placeholders  - '## [1.0.0] - 2026-XX-XX' shipped and stayed
                              live for 69 days on the canonical doctrine record.
  2. Claim-structure refs   - a near-miss on a DOI-bound artifact (2026-09-15)
                              where the sweep matched internal claim IDs but
                              not plain ranges like 'Claims 81-84'.
  3. Version/date agreement - CHANGELOG and CITATION.cff disagreed and nobody
                              noticed.
  4. Doctrine wording       - Law I and Law III drifted across six files; the
                              published repo understated the position for two
                              months.

Usage:  python3 .github/scripts/content_check.py [repo_root]
Exit:   0 = clean, 1 = findings
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# --- check 1: unfilled template placeholders -------------------------------
# Deliberately narrow. Matches leftover scaffolding, not prose.
PLACEHOLDERS = [
    (re.compile(r"\b\d{4}-XX-XX\b", re.I), "unfilled date placeholder"),
    (re.compile(r"\bXXXX\b"), "unfilled placeholder"),
    (re.compile(r"\bTK\b"), "'TK' to-come marker"),
    (re.compile(r"\b(TODO|FIXME|TBD)\b"), "unresolved marker"),
    (re.compile(r"<!--\s*(TODO|FIXME|DRAFT)", re.I), "draft comment"),
    (re.compile(r"\bLorem ipsum\b", re.I), "placeholder text"),
]

# --- check 2: patent claim-structure references ----------------------------
# A serial number or a claim TOTAL is a notice and is allowed. What must never
# appear is a map from a feature to a claim range or spec section.
CLAIM_REFS = [
    (re.compile(r"\bClaims?\s+\d+\s*[-‐-―]\s*\d+"), "claim range"),
    (re.compile(r"Patent anchor", re.I), "patent anchor line"),
    (re.compile(r"§\s*\d+\.\d+"), "spec section reference"),
    (re.compile(r"\bIC-\d"), "internal claim ID"),
    (re.compile(r"\bPC-0\d"), "internal claim ID"),
    (re.compile(r"\bX\+\d"), "internal claim ID"),
    (re.compile(r"(?<![A-Za-z0-9])D\d{2}(?![0-9])"), "internal claim ID"),
]

# Internal-only vocabulary that must not ship in a published file.
INTERNAL_MARKERS = [
    (re.compile(r"<!--.*?(POSITIONING GUARD|OPSEC|DO NOT|INTERNAL)", re.I | re.S),
     "internal guidance in an HTML comment"),
    (re.compile(r"\bpre-non-prov(isional)?\b", re.I), "internal disclosure-tier vocabulary"),
    (re.compile(r"\bTier\s*1\s*(blackout|BLACKOUT)\b"), "internal disclosure-tier vocabulary"),
]

SKIP_DIRS = {".git", ".github", "node_modules"}


def md_files(root: Path) -> list[Path]:
    return sorted(
        p for p in root.rglob("*.md")
        if not any(part in SKIP_DIRS for part in p.parts)
    )


def scan_patterns(root: Path, patterns, label: str) -> list[str]:
    findings = []
    for path in md_files(root):
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for rx, why in patterns:
                m = rx.search(line)
                if m:
                    findings.append(
                        f"{path.relative_to(root)}:{i} [{label}] {why}: "
                        f"{m.group(0).strip()!r}"
                    )
    return findings


def check_version_agreement(root: Path) -> list[str]:
    """CHANGELOG's newest release header must match CITATION.cff."""
    cff, chg = root / "CITATION.cff", root / "CHANGELOG.md"
    if not (cff.exists() and chg.exists()):
        return []

    text = cff.read_text(encoding="utf-8")
    cff_ver = re.search(r'^version:\s*"?([^"\n]+)"?', text, re.M)
    cff_date = re.search(r'^date-released:\s*"?([0-9]{4}-[0-9]{2}-[0-9]{2})"?', text, re.M)

    header = re.search(
        r"^##\s*\[([^\]]+)\]\s*[-‐-―]\s*(\S+)",
        chg.read_text(encoding="utf-8"), re.M,
    )
    if not (cff_ver and cff_date and header):
        return ["CITATION.cff or CHANGELOG.md is missing a version/date field"]

    out = []
    if header.group(1).strip() != cff_ver.group(1).strip():
        out.append(
            f"version mismatch: CHANGELOG '{header.group(1)}' != "
            f"CITATION.cff '{cff_ver.group(1)}'"
        )
    if header.group(2).strip() != cff_date.group(1):
        out.append(
            f"date mismatch: CHANGELOG '{header.group(2)}' != "
            f"CITATION.cff '{cff_date.group(1)}'"
        )
    return [f"CHANGELOG.md [version agreement] {o}" for o in out]


def check_doctrine_wording(root: Path) -> list[str]:
    """
    FIVE-LAWS.md is the canonical, Zenodo-archived text. Canon is DERIVED from
    it rather than hardcoded here, so this check cannot itself drift.

    Any other file stating a law must use the canonical opening clause.
    """
    canon_path = root / "FIVE-LAWS.md"
    if not canon_path.exists():
        return ["FIVE-LAWS.md not found - cannot verify doctrine wording"]

    canon_text = canon_path.read_text(encoding="utf-8")

    # First sentence of each law, as published.
    law_rx = re.compile(r"^(A system may not [^.]+\.|No party may certify itself\.)", re.M)
    canon = {m.group(1) for m in law_rx.finditer(canon_text)}
    if len(canon) < 5:
        return [f"FIVE-LAWS.md: expected 5 law statements, found {len(canon)}"]

    # Known drift variants, retired 2026-06-16 (commit be431d6).
    drift = [
        (re.compile(r"may not be the measure of its own conduct", re.I),
         "Law I drift - canon is 'may not PRODUCE the measure'"),
        (re.compile(r"sole witness", re.I),
         "Law III drift - canon is 'may not be the CUSTODIAN of the record'"),
        (re.compile(r"weak fits for Laws?\s*II", re.I),
         "positioning drift - the gap is NIST's, not the Laws'"),
        (re.compile(r"Weak in NIST", re.I),
         "positioning drift - state the condition, not a judgment"),
    ]

    findings = []
    for path in md_files(root):
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for rx, why in drift:
                if rx.search(line):
                    findings.append(
                        f"{path.relative_to(root)}:{i} [doctrine wording] {why}"
                    )
    return findings


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()

    groups = [
        ("Unfilled placeholders", scan_patterns(root, PLACEHOLDERS, "placeholder")),
        ("Patent claim-structure references", scan_patterns(root, CLAIM_REFS, "claim ref")),
        ("Internal-only content", scan_patterns(root, INTERNAL_MARKERS, "internal")),
        ("Version / date agreement", check_version_agreement(root)),
        ("Doctrine wording", check_doctrine_wording(root)),
    ]

    total = sum(len(f) for _, f in groups)
    print(f"Content check - {root.name}\n")

    for name, findings in groups:
        if findings:
            print(f"  FAIL  {name}")
            for f in findings:
                print(f"          {f}")
        else:
            print(f"  ok    {name}")

    if total:
        print(f"\n{total} finding(s). This check reports only - nothing was modified.")
        return 1

    print("\nClean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
