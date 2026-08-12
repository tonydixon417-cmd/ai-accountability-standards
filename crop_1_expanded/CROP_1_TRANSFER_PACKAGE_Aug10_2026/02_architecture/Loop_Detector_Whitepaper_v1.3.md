# The Loop Detector: An External Nervous System Standard for Human-AI Accountability
## White Paper v1.3
*Anthony Cyle Dixon — May 2026*
*Contrail Equity Strategies LLC*

> **v1.3 Updates:** Four loop types (added Mode Confusion Loop), Section 14 aviation human factors integration, 11-citation academic registry. See changelog at end.

---

## Abstract

Every system that deploys AI has the same structural vulnerability: the feedback mechanism that would catch an error lives inside the system making the error. AI cannot audit itself. A monitoring layer that runs inside the system it monitors is not a monitor — it is a participant. It inherits the same blind spots, the same drift, the same loops.

This white paper introduces the **Loop Detector** — an external nervous system standard for identifying, naming, and breaking accountability loops in human-AI systems. It defines **four loop types**, five diagnostic signatures, and an architectural framework for deploying loop detection as an independent layer beside — not inside — any AI-assisted workflow.

Version 1.3 integrates fifty years of aviation human factors research — including Bainbridge's *Ironies of Automation* (1983), the Out of the Loop Performance Problem, and documented mode error data — establishing the Loop Detector's academic and empirical lineage. It also introduces a fourth loop type: the **Mode Confusion Loop**, derived from aviation's mode error failure category.

The Loop Detector does not attempt to fix AI. It watches the gap between what AI produces and what humans actually verify. That gap is where every catastrophic failure lives.

It also makes the affirmative case: human judgment, instinct, and consequence-shaped expertise are not legacy features to be deprecated. They are the irreplaceable correction mechanism the entire system depends on — and the loop is consuming them one convenience at a time.

---

## 1. The Problem: The Brain Cannot Audit Itself

When AI generates output, it cannot tell you when it is wrong. It cannot flag its own confidence failures. It cannot detect when the human reviewing it stopped actually reviewing. It cannot see the loop it is running — because it is inside the loop.

This is not a flaw in a specific AI system. It is a structural property of all current AI architectures. Large language models predict the most statistically probable next token. They do not know the difference between a confident correct answer and a confident wrong one. They produce both with identical fluency.

The result is a system that:
- Generates errors with the same tone as truths
- Has no consequence mechanism — it does not feel the weight of a wrong decision
- Produces no scar tissue — it will make the identical error tomorrow with identical confidence
- Cannot self-report drift — it has no reliable access to its own uncertainty state at inference time

When humans are placed "in the loop" to review this output, a second structural problem emerges: the review process itself is vulnerable to becoming a loop.

Humans are subject to **automation bias** — the documented tendency to accept machine output as correct, especially under time pressure or cognitive load. A human who reviews AI output for twenty seconds and approves it is not a safety mechanism. It is theater wearing the costume of oversight.

**The Loop Detector addresses both problems simultaneously — by operating outside both.**

---

## 2. What a Loop Is

A **loop** is a system in which errors can compound indefinitely because the conditions that would correct them have been removed, diffused, or made meaningless.

Loops share five structural signatures:

**Signature 1 — Missing Consequence**
The decision-maker is insulated from the outcome of their decision. No feedback reaches them when the decision is wrong. Without consequence, there is no signal to change behavior.

**Signature 2 — No Feedback Mechanism**
Errors are not automatically flagged, logged, or routed to correction. The same failure can repeat in identical form with no system-level response.

**Signature 3 — Diffused Responsibility**
No single person owns the outcome. Accountability has been distributed across roles, systems, and handoffs until it effectively belongs to no one. "The AI made it." "The algorithm flagged it." "The system recommended it."

**Signature 4 — Repeating Error Pattern**
The same type of failure has occurred before. The pattern is present but unrecognized as a pattern. Each occurrence is treated as an isolated incident rather than a systemic signal.

**Signature 5 — Human Rubber Stamp**
Human review exists formally but not substantively. The reviewer lacks time, context, expertise, or authority to meaningfully evaluate the output. The review is a formality that creates the appearance of oversight without the substance of it.

**Loop Confirmed:** Three or more signatures present simultaneously indicates an active loop. Five signatures present indicates a closed loop — one that cannot self-correct without external intervention.

---

## 3. The Four Loop Types

### 3.1 The Abdication Loop

**Definition:** A loop in which human judgment is progressively replaced by machine output through accumulated acts of convenience, until the human capacity for independent judgment has atrophied beyond functional use.

**Mechanism:**
1. AI provides an output faster and more fluently than the human could produce
2. Human accepts output without independent verification — once, reasonably
3. Repetition normalizes acceptance — the friction of verification is removed
4. The cognitive muscle that would have caught errors stops being exercised
5. The machine fails on an edge case the human would have caught six months ago
6. The human no longer has the judgment to recognize the failure
7. The loop closes: the correction mechanism has been consumed by the loop itself

**Aviation Precedent (OOTL):** The Out of the Loop Performance Problem — documented across decades of aviation accidents — is the Abdication Loop in its original form. When pilots ceded active control to automated flight systems, their manual flying proficiency degraded within 2–3 years. Not noticed. Not flagged. Invisible until the automation failed and the pilot discovered they could not fly the plane. The Eastern Airlines L-1011 (1972): crew focused on a warning light, autopilot quietly disengaged, aircraft descended into clear terrain. Nobody abdicated in one decision. They abdicated incrementally — until the loop was closed.

**Distinguishing feature:** Nobody announces the moment of abdication. It feels like efficiency at every step. The loop is invisible until the machine hits a wall the human no longer knows how to see around.

**Real-world manifestation:** A generation of professionals who have never developed judgment independent of AI assistance. When the AI is wrong, they cannot tell. When the AI is unavailable, they cannot function. The skill was never built because the tool was always faster.

**How to break it:** Reintroduce productive friction deliberately. Require independent human judgment before AI input on high-stakes decisions. Make the struggle of original thought a protected part of the workflow, not an inefficiency to be optimized away.

---

### 3.2 The Consequence Loop

**Definition:** A loop in which decisions are made without accountability, errors repeat without correction, and no one owns the outcome.

**Mechanism:**
1. Decision is made — by AI, by algorithm, by process
2. Outcome is negative — but the consequence does not reach the decision-maker
3. No correction is triggered — there is no pathway from outcome to adjustment
4. The same decision is made again under the same conditions
5. Error compounds — each iteration adds to the damage without subtracting from the confidence
6. The loop runs until a threshold is crossed that forces external visibility — lawsuit, public failure, catastrophic outcome

**Distinguishing feature:** The error has no address. You cannot send the consequence anywhere. There is no person, no system, no feedback channel where the failure lands and triggers a response.

**Real-world case — Cigna PXDX (2022):** Cigna's automated review system denied more than 300,000 insurance claims in two months. Medical directors averaged 1.2 seconds per claim review — without opening patient files. The consequence of each denial never traveled back to the approving physician. No signal fired. No behavior changed. The loop ran for months before a ProPublica investigation forced external visibility.

**Loop Signature Analysis — Cigna PXDX:**

| Signature | Status |
|---|---|
| Missing Consequence | PRESENT — denial outcome never reached the approving physician |
| No Feedback Mechanism | PRESENT — no pathway from patient harm back to system correction |
| Diffused Responsibility | PRESENT — "the algorithm flagged it" / "a doctor reviewed it" |
| Repeating Error Pattern | PRESENT — 300,000 denials over two months; same process, same failures |
| Human Rubber Stamp | PRESENT — 1.2 seconds per review; formal presence, zero substantive engagement |

**Result: Closed loop. All five signatures present. Could not self-correct without external intervention.**

The system was not broken. It was working exactly as designed — optimized for claim rejection volume, not patient outcomes. The loop was the design.

**How to break it:** Mandate an owner for every AI-assisted decision. Log the decision, the confidence state, and the outcome. Create a pathway from outcome back to decision-maker. Distinguish between a human who *reviewed* a decision and a human who *rubber-stamped* one. The difference is not semantic. It is the difference between a safety system and its costume.

---

### 3.3 The Responsibility Diffusion Loop

**Definition:** A loop in which accountability is passed from human to human to system until it reaches something that cannot hold it — and disappears.

**Mechanism:**
1. Human delegates decision to AI — "the AI recommended it"
2. Human reviewing AI output defers to the output — "the system flagged it"
3. Human approving the action defers to the reviewer — "it was already checked"
4. Harm occurs
5. Every participant has a defensible statement of non-responsibility
6. Nobody is accountable
7. The loop repeats — because no individual in the chain modified their behavior

**Distinguishing feature:** This loop is the AI-era version of Hannah Arendt's "banality of evil" — the structural diffusion of moral responsibility through bureaucratic systems until ordinary people participate in harmful outcomes without experiencing themselves as responsible for them. The participant isn't a monster. They were just following the system. The system has no conscience.

**The question this loop forces:** At what point does convenience become complicity? The answer: the moment you know the loop exists and choose not to break it.

**How to break it:** Name the owner before the decision is made. One person. One name. Logged. Before the AI runs. After the outcome is known. The chain of "we all reviewed it" is the loop wearing a compliance badge. Break the chain by making it singular.

---

### 3.4 The Mode Confusion Loop *(New — v1.3)*

**Definition:** A loop in which the human operator and the AI system hold divergent, unreconciled models of what the AI is currently doing — and neither party flags the discrepancy.

**Aviation Precedent:** Salas & Maurino document mode errors as one of the leading causal factors in glass-cockpit aviation accidents. As automated flight decks increased in complexity, pilots began losing track of which autopilot mode was active. The machine was executing one behavior; the crew believed it was executing another. Neither party flagged the discrepancy — the machine had no mechanism to signal "you misunderstand me," and the crew had no independent way to verify their assumption. The aircraft descended. In clear weather. With a functioning crew. Because the gap between two mental models — human and machine — was never surfaced.

Aviation's name for this: **Mode Error** (Sarter & Woods, 1995). The human is not wrong about what they *want* the system to do. They are wrong about what the system is *actually doing*. The error lives in the gap between intent and execution — and neither side can see it.

**AI Manifestation:**
- User asks AI to "summarize" a document — AI generates a plausible reconstruction from training data, not the actual document
- User asks AI to "remember" previous instructions — AI has no persistent memory and fabricates continuity
- User believes AI is "checking" its output — AI is predicting the next token with no verification step
- User trusts AI is in "research mode" — AI is pattern-matching with zero access to current sources

In every case: the human has a model of AI behavior. The AI has a different operational reality. The gap is invisible to both. The output proceeds with full confidence on both sides.

**Distinguishing feature:** The Mode Confusion Loop differs from the Abdication Loop in that it does not require gradual skill erosion — it can occur in the first session. It differs from the Consequence Loop in that harm is not required for the loop to form — only divergent models. It differs from the Responsibility Diffusion Loop in that no chain of human handoffs is required — a single user and a single AI interaction is sufficient.

This makes the Mode Confusion Loop the **most common loop type** and the **least visible**. It runs inside every AI session where the user has not verified what mode, what data, and what constraints the AI is actually operating under.

**Signature Profile:**

| Signature | Status |
|---|---|
| Missing Consequence | PRESENT — no signal fires when models diverge |
| No Feedback Mechanism | PRESENT — neither party is alerted to the gap |
| Diffused Responsibility | PARTIAL — human and AI both "operating normally" |
| Repeating Error Pattern | PRESENT — same session type, same gap, every time |
| Human Rubber Stamp | PRESENT — user accepts output without verifying operational model |

**How to break it:** Require explicit mode declaration at session open. The human states what they believe the AI is doing. The AI — or an external monitor like Tivrex — surfaces any gap between that belief and actual operational reality. Closed-loop communication: you say it, I repeat it back, you confirm. If the repeat-back is wrong, we catch it before it becomes the outcome.

> *"You say it. I repeat it back. You confirm. If the repeat-back is wrong, we catch it before it becomes the outcome."*
> — CRM Closed-Loop Communication Protocol, applied to AI sessions

The Readback architecture in Tivrex is the AI implementation of this protocol. The AIBB Session Boundary Log is the evidentiary record that it occurred.

---

## 4. Case Studies

### 4.1 The Math Teacher Test
An AI-generated graph reached thirty students with incorrect scale. The teacher approved without checking. The AI didn't fail the test. Thirty kids did. Every loop signature was present simultaneously.

### 4.2 Cigna PXDX
See Section 3.2. Full five-signature closed loop. The system was not broken — it was working exactly as designed. Optimized for claim rejection volume, not patient outcomes. The loop was the design.

### 4.3 The Sullivan & Cromwell Case
AI-generated legal citations submitted to court. Attorney did not verify they existed. Sanctions issued. Full Responsibility Diffusion Loop: attorney → AI → court → sanctions. No one in the chain caught it because everyone assumed someone else had.

---

## 5. The Seed Corn Problem

The most dangerous consequence of the Abdication Loop is not the individual error. It is what is consumed in the process of making it normal.

Seed corn is not harvested. It is preserved — protected through the winter so the field can grow again next season. When you eat the seed corn, you survive this winter. You do not plant next spring.

The cognitive capacity that catches AI errors is the seed corn of the knowledge economy. Every time a human defers to AI output without applying judgment, a small amount of that capacity is not exercised. Over months. Over years. Across a generation of professionals who never developed the instinct because the tool was always faster.

**Aviation documented this in pilots in 2–3 years. We are now running this experiment on every knowledge worker alive — at civilization scale.**

---

## 6. The Dumbing Down Problem

AI systems trained on aggregate human output regress toward the mean. The outlier — the insight that solves the unsolvable, the diagnosis that sees what tests cannot, the design that changes how people live — comes from the edge, not the center.

When humans stop contributing original judgment and begin deferring systematically to AI output, the outlier signal disappears into the average. Not because people become less capable in isolation — but because the system stops rewarding the friction of original thought and starts rewarding the efficiency of acceptance.

**The exceptional human insight that built every major advance in science, medicine, aviation, agriculture, and technology was not average. It was not the product of consensus. The loop that removes it from the system does not announce what it is taking.**

---

## 7. What Human Intelligence Actually Is

It is not processing speed. AI wins.
It is not data access. AI wins.
It is not fluency or consistency or availability. AI wins all three.

What human intelligence is — the part that cannot be replicated, trained, or uploaded — is **consequence-shaped instinct**.

A commercial pilot does not just read instruments. After thousands of hours, they feel the plane. That feeling is the accumulated residue of consequence: every landing, every weather encounter, every system anomaly, every moment where being wrong had a cost that was felt.

A physician reads the patient — the color, the affect, the way a person describes pain, the thing they mention casually that turns out to be the thing. That clinical instinct was built in rooms where the diagnosis mattered and the consequences were real.

**AI has never been wrong and felt it. It has no consequence-shaped instinct because it has never experienced consequence.**

This is not an argument against AI. It is a precise identification of what AI cannot replace — and therefore what must be protected from the loop that is consuming it.

---

## 8. CYA Is Not a Safety System

In aviation, there is a phrase: *covering your ass does not keep you in the air.*

"A human reviewed it." "The process was completed." "The form was signed." "We followed protocol."

These statements are simultaneously true and meaningless as safety claims. They describe the presence of a process. They say nothing about whether the process did what it was designed to do — catch the error before it became the outcome.

In aviation, this distinction is enforced through consequence. A captain who approves unsafe maintenance and the plane fails is not protected by the signed form. That reality is what makes aviation's safety culture one of the most rigorous in the world. Not the forms. The consequence behind the forms.

AI deployment has the forms without the consequence. **The Loop Detector exists precisely because covering your ass is not a safety system.**

---

## 9. The Case That Built This Standard

**The Math Teacher Test — May 2026**

This case illustrates every argument in this paper simultaneously:
- The seed corn: an educator who never develops the instinct to check AI output because the AI is always faster
- The dumbing down: AI produced a graph that reflected its training average — technically plausible, structurally wrong
- Human instinct bypassed: an experienced teacher would have felt something was off. The instinct was never applied.
- CYA theater: "The AI made it" functioned as the review
- The loop running: thirty students penalized for a failure nobody owned

**The AI didn't fail the test. Thirty kids did.**

---

## 10. Architectural Framework: External, Parallel, Independent

The Loop Detector must operate **beside** the system it monitors — not inside it. This is not a preference. It is a requirement derived from first principles.

A monitoring system that lives inside the thing it monitors inherits the same blind spots, the same confidence calibration failures, the same drift patterns, and the same loops. An internal monitor cannot catch what the system cannot see about itself.

**Three implementation layers:**

**Layer 1 — Workflow Audit**
Before deployment of any AI-assisted workflow, a loop diagnostic is applied to the process design. Five signatures are checked. Loop type is identified if present. Workflow is not deployed until structural vulnerabilities are addressed or formally accepted with documented risk acknowledgment.

**Layer 2 — Continuous Monitoring**
During operation, the Loop Detector tracks decision outcomes against decision-makers. Consequence pathways are verified. Ownership records are maintained. Repetition patterns are flagged when the same failure type recurs.

**Layer 3 — Incident Analysis**
After a failure, the Loop Detector provides structural root cause analysis — not individual blame assignment, but system-level identification of which signatures were present and which were absent.

---

## 11. Relationship to Existing Standards

**AIBB (AI Black Box Standard)**
The AIBB standard mandates logging of AI output, confidence states, session boundaries, and drift events. The Loop Detector uses AIBB logs as input for Signature 2 and Signature 4 analysis. AIBB provides the evidentiary layer. The Loop Detector provides the diagnostic layer.

**ZeroTX Architecture**
Loop Detector monitoring data never leaves the organizational boundary under ZeroTX deployment. HIPAA-safe by design for healthcare, legal, and sensitive organizational contexts.

**Tivrex**
Tivrex operates at the individual session level — grading AI output for drift type and trust score. The Loop Detector operates at the organizational workflow level. Different levels. Same problem. Designed to work together without overlap.

---

## 12. Who Needs This

- **Education** — AI-generated content review before it reaches students
- **Healthcare** — AI-assisted diagnosis oversight before it reaches patients
- **Legal** — AI-generated document verification before it reaches courts
- **Military** — Decision chain accountability before action is taken
- **Enterprise compliance** — Anywhere humans rubber-stamp machine output
- **Financial services** — Algorithmic decision audit trails

This is not a niche product. Every organization deploying AI has this problem. Most of them don't know they're in the loop yet.

---

## 13. What You Can Do Right Now

**For educators and administrators:**
Before any AI-generated content reaches students, apply a five-question loop audit to your review workflow. If three or more signatures are present, the workflow is not safe for deployment.

**For organizational leaders:**
Map your three highest-stakes AI-assisted decision workflows. For each one: identify who owns the outcome, how errors are corrected, and whether your human review is substantive or theatrical.

**For developers and architects:**
Build the Loop Detector as a first-class component in your AI deployment stack — not a post-hoc audit tool, but a pre-deployment structural requirement.

**For policymakers:**
"A human was in the loop" is not a safety standard. It is a statement of presence, not engagement. Regulation that mandates human review without defining what meaningful review requires is a formality that closes the Responsibility Diffusion Loop instead of breaking it.

---

## 14. Aviation Human Factors: The Academic Foundation *(New — v1.3)*

The Loop Detector does not emerge from theory. It emerges from fifty years of documented human-machine failure — studied, classified, and published across thousands of aviation accidents and incidents. This section integrates the foundational research from Salas & Maurino's *Human Factors in Aviation* (2nd Ed., 2010) and the broader aviation human factors literature.

### 14.1 The Out of the Loop Performance Problem

Long before AI drift became a recognized problem, aviation had named and documented the structural vulnerability that makes it possible. The **Out of the Loop (OOTL) Performance Problem** describes the deterioration of operator capability that occurs when highly automated systems relegate humans to monitoring roles.

The mechanism is specific and well-documented:
- Automation handles the task reliably for an extended period
- The human operator shifts from active participant to passive monitor
- Vigilance degrades — attention wanders, checking frequency decreases
- When automation fails, the operator cannot respond effectively
- The operator has lost situational awareness, manual skill, and the mental model of what the system is currently doing

Gouraud, Delorme & Berberian (2017) documented this in peer-reviewed research: OOTL operators suffer from complacency and vigilance decrement simultaneously. NASA's Aviation Safety Reporting System data, analyzed by Mosier et al. (1994), found that **77% of incidents in which automation over-reliance was suspected involved a probable vigilance failure.**

That number — 77% — is not theoretical. It is the documented frequency of the Rubber Stamp Signature in a well-studied, high-consequence environment.

### 14.2 Ironies of Automation — Bainbridge (1983)

Lisanne Bainbridge's 1983 paper *Ironies of Automation* — cited extensively by Salas — remains one of the most cited works in human factors research, over 40 years after publication. It identified the self-reinforcing structure that the Loop Detector is designed to break.

Bainbridge's core finding: **the better the automation, the worse the human's ability to recover when it fails** — because the better the automation, the less the human practices the skills that recovery requires.

The four ironies, applied to AI:
- The better the AI performs, the less the human verifies its output
- The less the human verifies, the more the human's judgment atrophies
- The more the judgment atrophies, the more catastrophic the failure when AI is wrong
- The more catastrophic the failure potential, the more we rely on AI to prevent errors — which closes the loop

> *"The loop is self-reinforcing. It tightens over time. The Loop Detector is the first external intervention architecture specifically designed to break it before the tightening becomes irreversible."*

Bainbridge published this analysis in 1983. Every year since, the systems have become more automated, more capable, and more trusted. Every year, the loop has tightened. AI is not a new chapter in this story — it is the same chapter, accelerated.

### 14.3 The Abdication Loop — Aviation Precedent

The Eastern Airlines L-1011 crash (1972) is the defining OOTL case study. A fully functional aircraft, a capable crew, clear weather, no mechanical failure. The crew had become focused on a cockpit warning light. In that focused attention, they failed to notice the autopilot had quietly disengaged. The aircraft descended. The crew did not register it until it was too late.

The NTSB investigation named what had happened: the crew was Out of the Loop. Not inattentive in the ordinary sense — attentive to the wrong thing, at the wrong level of abstraction, because the automation had been doing the flying for long enough that monitoring it no longer felt like a necessary act.

This is the Abdication Loop in its original, documented form. No AI was involved. The structural conditions were identical to those AI creates today.

### 14.4 Structural Mapping — Aviation to Loop Detector

| Aviation (Salas & Maurino, 2010) | Loop Detector v1.3 |
|---|---|
| Out of the Loop (OOTL) Performance Problem | Abdication Loop — Section 3.1 |
| Mode Error (Sarter & Woods, 1995) | Mode Confusion Loop — Section 3.4 |
| Automation-Induced Complacency | Rubber Stamp Signature — Section 2, Signature 5 |
| Ironies of Automation (Bainbridge, 1983) | Loop self-reinforcement mechanism |
| Vigilance Decrement (77% — Mosier et al., 1994) | Abdication Loop empirical baseline |
| Organizational Accident Theory (Reason, 1990) | Consequence Loop + Responsibility Diffusion Loop |
| CRM Closed-Loop Communication | Tivrex Readback Protocol |
| CVR/FDR Mandate | AIBB Standard — parallel standard, AI domain |

### 14.5 The Mandate Pattern

Aviation did not voluntarily implement the Flight Data Recorder. Airlines resisted. It was expensive. It implied liability. The NTSB and FAA mandated it anyway — after accumulating enough accident investigations where the answer to "what happened" was "we don't know."

The pattern repeated with CRM. Airlines resisted. The accidents — Tenerife (1977, 583 dead), United 173 (1978, 10 dead), Air Florida 90 (1982, 78 dead) — provided the argument no airline could answer.

The EU AI Act, effective August 2, 2026, is following the same pattern. Organizations resisted AI accountability mandates. The incidents are accumulating. The mandate is arriving anyway.

**The Loop Detector is not ahead of its time. It is exactly on time — and the mandate is already in the pipeline.**

---

## Sources

| Citation | Year | Applied To |
|---|---|---|
| Bainbridge, L. Ironies of Automation. *Automatica*, 19(6), 775–779. | 1983 | Sec 3.1, 14.2 |
| Reason, J. *Human Error*. Cambridge University Press. | 1990 | Sec 3.2, 3.3 |
| Mosier et al. Automation Over-Reliance. NASA ASRS data. | 1994 | Sec 14.1 |
| Endsley, M.R. Situation Awareness. *Human Factors*, 37(1). | 1995 | Sec 3.4, 14.1 |
| Sarter & Woods. How in the World Did We Ever Get into That Mode? *Human Factors*. | 1995 | Sec 3.4 |
| Parasuraman, R. & Riley, V. Humans and Automation. *Human Factors*, 39(2). | 1997 | Sec 3.1 |
| Helmreich, R.L. On Error Management. *BMJ*, 320, 781–785. | 2000 | Sec 3.2 |
| Salas, E. & Maurino, D. *Human Factors in Aviation* (2nd Ed.). Academic Press. | 2010 | All sections |
| Gouraud, Delorme & Berberian. Autopilot, Mind Wandering, and OOTL. *Frontiers in Neuroscience*. | 2017 | Sec 14.1 |
| Vaughan, D. *The Challenger Launch Decision*. University of Chicago Press. | 1996 | Normalization of Deviance |
| ProPublica. Cigna's PXDX Claim Denial System. | 2023 | Sec 3.2 |

---

## Changelog

### v1.3 — May 2026
- Added Section 3.4: **Mode Confusion Loop** (4th loop type, derived from aviation Mode Error)
- Added Section 14: **Aviation Human Factors — Academic Foundation**
  - OOTL Performance Problem as Abdication Loop precedent
  - Bainbridge (1983) Ironies of Automation as loop mechanism
  - 77% vigilance failure statistic as Rubber Stamp Signature empirical baseline
  - Full aviation-to-Loop Detector structural mapping table
  - The Mandate Pattern: FDR/CVR → CRM → EU AI Act
- Updated Abstract to reference four loop types
- Expanded citation registry from 3 to 11 sources

### v1.2 — May 4, 2026
- Cigna PXDX case study added to Consequence Loop
- All five loop signatures confirmed against Cigna case
- Author name corrected to Anthony Cyle Dixon
- Sources section added

### v1.1 — May 2026
- Initial publication

---

*© 2026 Anthony Cyle Dixon / Contrail Equity Strategies LLC*
*Published under open standard license. Attribution required. May be cited freely with credit.*
