# Framework Crosswalks — The Five Laws of AI Governance

**Author:** Pharns Genece · **Version:** 1.0 · **Published:** 2026

> This document presents the **summary** alignment between the Five Laws and established AI governance frameworks. It shows *where* the Laws sit relative to NIST AI RMF and ISO/IEC 42001. It does **not** specify control implementations or scoring mechanisms.

---

## The credibility chain

> 5 Laws (doctrine) → 9 governance domains → 24 controls → 49 NIST AI RMF subcategories (federally cataloged via NIST OLIR).

The Laws are the **memorable top** of a stack that is **already cataloged at the bottom.** The doctrine inherits the credibility of the underlying framework alignment, which is published as a NIST OLIR concept crosswalk.

---

## Law-by-law summary alignment

| Law | NIST AI RMF | ISO/IEC 42001:2023 | Fit |
|---|---|---|---|
| **I — Independent Measure** | MEASURE-1.1 (metric selection); MEASURE-2.13 (TEVV) | A.5.2 (impact assessment process) | Strong |
| **II — Binding at Dispatch** | *No native subcategory* — maps to process subcategories (GOVERN-1.1, MANAGE-1.x) | A.6.2.6 (operation & monitoring) — closest | **Weak in NIST — the white space** |
| **III — External Witness** | MEASURE-2.13 (TEVV) + audit subcategories | **A.6.2.8 (recording of event logs)** | Partial in NIST; strong on ISO A.6.2.8 |
| **IV — Separated Authority** | GOVERN-6.1 (third-party); GOVERN-1.1 (org policy) | A.3.2 (AI roles & responsibilities) | Strong |
| **V — Revocable Authority** | MANAGE-2.4 (*supersede, disengage, or deactivate*); GOVERN-1.7 (safe decommission) | A.9.2 (responsible use) | Strong |

---

## The strategic finding

The alignment maps cleanly to Laws **I, IV, and V**. But the controls for Law **II** (binding at dispatch) and Law **III** (external witness) had to be mapped to NIST **process** subcategories — because **NIST AI RMF has no native runtime-enforcement or external-attestation subcategory.**

That is not a weakness in the Laws. It is the **white space** the standard occupies. Existing frameworks describe *what should be true*; they leave *runtime enforcement* and *external attestation* to prose. The weak fits for Laws II and III are the evidence that a runtime-conformance standard needs to exist.

---

## Relationship to the declarative Properties

The Laws are the **prohibitive inversion** of a set of declarative governance properties — the same architecture in two voices, one property per law, no gap:

| Property (declarative) | Law (prohibitive) |
|---|---|
| Measurement layer that survives the system | I. A system shall not measure itself |
| Dispatch-time enforcement | II. A system shall not be governed after the fact |
| Tamper-evident attestation | III. A system shall not witness itself |
| Federated authority | IV. A system shall not certify itself |
| Fail-closed off-switch (revocable from outside) | V. A system shall not outlive its off-switch |

---

*The Five Laws of AI Governance · Pharns Genece · 2026 · Version 1.0*
