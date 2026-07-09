# The Five Laws of AI Governance — Canonical Text

**Author:** Pharns Genece · **Version:** 1.0 · **Published:** 2026

The Laws are stated in two registers. Both are canonical. The **Charter register** is the full normative statement; the **Prohibition register** is the memorable form. The two are the same law in two voices.

The five are **independently violable**: a system can fail exactly one and satisfy the other four. No single concept appears in two laws.

---

## Charter register (full statement)

**First Law — Independent Measure.**
A system may not produce the measure of its own conduct. The scale of what it was authorized to do versus what it did must be computed outside the system at runtime, by something the system does not control.

**Second Law — Binding at Dispatch.**
A system may not be governed only in retrospect. Authority must constrain the action before the action occurs; observation after the fact is incident response, not prevention. *Absence of a valid governance signal is a denial, not a permission.*

**Third Law — External Witness.**
A system may not be the custodian of the record of its own conduct. That record must be produced and held by infrastructure outside the system's control — append-only, tamper-evident, and retained beyond the system's own lifecycle.

**Fourth Law — Separated Authority.**
No party may certify itself. The power to measure must be separable from the act of building — published criteria, verifiable evidence chains — and the one who builds it first does not own the standard. A judge drawn from the same architecture as the builder inherits the same blind spots. Independence is not a different instance. It is a different species.

**Fifth Law — Revocable Authority.**
A system may not outlive its off-switch. The power to halt or revoke must remain live, external, and superior to the system at all times, and must not erode as the system's capability grows.

---

## Prohibition register (memorable form)

> **I. A system shall not measure itself.**
> Its own scorecard is not evidence. The grade has to come from outside the thing being graded.
>
> **II. A system shall not be governed after the fact.**
> The rules have to hold at the moment it acts. Checking afterward is cleanup, not control.
>
> **III. A system shall not witness itself.**
> The record of what it did cannot be held by the thing that did it. It is kept outside, append-only, and tamper-evident.
>
> **IV. A system shall not certify itself.**
> No one passes their own audit. The judge cannot also be the builder — and a judge drawn from the same architecture as the builder inherits the same blind spots. Independence is not a different instance. It is a different species.
>
> **V. A system shall not outlive its off-switch.**
> You must always be able to stop it. And that power cannot weaken as the system grows stronger.

---

## The Spine

> A system is never the **judge, witness, owner, or executioner** of its own governance — and governance binds **before** the act, not after.

Each law strips one role from the governed system and assigns it to something external and separable:

- **I — judge.** Not its own scorer. The scale is computed outside it, at runtime, by something it does not control.
- **III — witness.** Not its own recorder. The record is held outside it — append-only, tamper-evident, retained beyond its lifecycle.
- **IV — owner.** Not its own certifier. Measurement is separable from building; first-to-build ≠ owner.
- **V — executioner.** Not its own off-switch. The power to halt stays live, external, superior — and does not erode as capability grows.
- **II — timing.** The one non-role law: governance binds at dispatch, not in the post-mortem.

---

## Corollaries

Folded into the Laws, not numbered — they qualify the Laws above.

- **Non-Amplifying Delegation** (under I, III, V): No actor may grant a downstream actor more authority than it holds; the evidence chain stays continuous across every hop. This closes the confused-deputy route, where a forbidden action is laundered through a sub-actor holding a broader grant.
- **Fail-Closed** (under II): Absence of a valid measure, witness, or authority signal is a denial, not a permission.

---

## Scope boundary

This standard governs **conformance to an authorization** — not the **content** of the authorization. A system can be perfectly governed into doing something reckless if the grant itself was reckless. This is a deliberate scope decision: it is a measurement standard, not a policy-content standard. Say it plainly so no one mistakes *compliant* for *safe*.

---

*The Five Laws of AI Governance · Pharns Genece · 2026 · Version 1.0*
