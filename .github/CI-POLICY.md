# CI policy for this repository

**This repository has one workflow, and it is read-only by design.**

## Why there is no build, deploy, tag, or release automation

This repo is **archived by Zenodo**, which mints a new permanent DOI version
on each GitHub *release*.

- Version DOI: `10.5281/zenodo.21271750`
- Concept DOI: `10.5281/zenodo.21271749`

A workflow holding tag or release permissions could therefore **mint a
permanent, un-retractable DOI version as a side effect of an ordinary commit**
— an irreversible outward-facing act with no human at the dispatch point.

That is precisely what this project's own doctrine forbids:

> **Second Law — Binding at Dispatch.** A system may not be governed only in
> retrospect. Authority must constrain the action before the action occurs.

> **Fifth Law — Revocable Authority.** The power to halt or revoke must remain
> live, external, and superior to the system at all times.

**Tagging and releasing stay deliberate human acts.**

## What the one workflow does

`content-check.yml` runs `scripts/content_check.py`. It reads files, prints a
report, and exits 0 or 1. It has `permissions: contents: read` and nothing else.

Five checks, each earned by a defect this repository actually produced:

| Check | The defect it exists for |
|---|---|
| Unfilled placeholders | `## [1.0.0] — 2026-XX-XX` shipped and stayed live 69 days |
| Claim-structure references | A 2026-09-15 near-miss where the sweep matched internal claim IDs but not plain ranges like `Claims 81–84` |
| Internal-only content | An internal positioning-guard HTML comment nearly shipped in `CROSSWALKS.md` |
| Version / date agreement | `CHANGELOG.md` and `CITATION.cff` disagreed and nobody noticed |
| Doctrine wording | Law I and Law III drifted across six files; the published repo understated the position for two months |

The doctrine check **derives canon from `FIVE-LAWS.md`** rather than hardcoding
it, so the check cannot itself drift away from the archived text.

## Running it locally

```bash
python3 .github/scripts/content_check.py .
```

No dependencies. Exit 0 = clean, 1 = findings.

## If you are adding a workflow

Read `ADR-0107` first. The short version: **do not grant this repository's
automation any permission beyond `contents: read`.** If a task genuinely needs
more, it belongs in a separate, human-triggered workflow, reviewed against that
ADR — not bolted onto this one.
