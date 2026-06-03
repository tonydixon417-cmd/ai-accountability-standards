# AI Testimony Standards: A Framework for the Admissibility and Attribution of AI-Generated Content in Formal Proceedings
**Whitepaper v1.0 — Defensive Publication**
**Author: Tony Dixon, Contrail Equity Strategies LLC**
**Date: May 2026**

---

## Abstract

Artificial intelligence output is being used in legal proceedings, medical determinations, hiring decisions, and regulatory findings at a rapidly accelerating rate — without any established standard for how that output should be evaluated, attributed, or challenged. Aviation accident investigation developed rigorous standards for the admissibility and interpretation of recorded data decades ago. Those standards — governing the Chain of Custody, Confidence Qualification, and Attribution Boundary of recorded evidence — apply directly to AI-generated content. This paper proposes a foundational AI Testimony Standard (ATS) drawn from aviation evidentiary practice and existing AI audit literature.

---

## The Problem

Courts, medical review boards, HR departments, and regulatory bodies are already receiving AI-generated content as evidence, recommendation, or finding — with no standard framework for evaluating it.

Current gaps:
- No standard for qualifying AI output as reliable vs. unreliable in a given context
- No standard for attribution: who is responsible when AI-generated content is wrong?
- No chain of custody requirement for AI output used in formal decisions
- No confidence qualification standard — AI systems routinely assert conclusions without communicating their uncertainty
- No standard for challenging AI output — how does a party in a legal or formal proceeding contest an AI-generated finding?

These gaps are not theoretical. They are already producing outcomes in courtrooms, hospitals, and HR departments. The law is catching up slowly. The standard does not yet exist.

---

## The Aviation Precedent

Aviation developed some of the most rigorous evidentiary standards in any industry, driven by the legal and investigative requirements of accident investigation.

**1. Flight Data Recorder (FDR) Chain of Custody**
NTSB regulations require documented chain of custody for all recorded data from the moment of recovery. Any break in the chain renders the data suspect. The FDR is not simply read — it is received, logged, transported under documented control, and read by certified personnel using certified equipment.

**2. Cockpit Voice Recorder (CVR) Admissibility Standards**
CVR transcripts are not simply played in court. Federal law (49 U.S.C. § 1154) restricts their use specifically to prevent unreliable or out-of-context interpretation. The NTSB produces an official transcript — not a raw recording — with documented methodology for what was audible, what was ambiguous, and what was inaudible.

**3. Confidence Qualification in Investigation Reports**
NTSB probable cause findings are carefully worded to distinguish between "the probable cause was" (high confidence), "a contributing factor was" (moderate confidence), and "could not be determined" (insufficient evidence). The report does not assert certainty it does not have.

**4. Attribution Boundary**
Aviation investigation distinguishes precisely between: the physical cause, the human factors cause, the systems cause, and the organizational cause. Each finding names specifically who or what is attributed with what portion of responsibility. Diffuse attribution is not acceptable.

---

## Proposed Standard: AI Testimony Standard (ATS)

**ATS-1: Chain of Custody for AI Output**
Any AI-generated content used in a formal proceeding must be accompanied by:
- The session ID and timestamp of generation
- The model and version that produced it
- The complete prompt or input that produced it
- The AIBB session log for that generation event (if applicable)
- Documentation of any post-generation editing

Without these, AI output cannot be treated as reliable evidence.

**ATS-2: Confidence Qualification Requirement**
AI output used in formal proceedings must include an explicit confidence qualification:
- High confidence: model had full context, well-established domain, no ambiguity flags
- Moderate confidence: partial context, domain extrapolation, or ambiguity present
- Low confidence: limited context, novel domain, or known hallucination risk present
- Unqualified: confidence state not logged — treat as unreliable

*This maps directly to the AIBB Confidence State logging component (Dixon, 2026).*

**ATS-3: Attribution Boundary Statement**
AI-generated content used in formal proceedings must include an explicit attribution boundary:
- What the AI determined independently
- What the AI was told to conclude
- What the human operator verified
- What the human operator did not verify

Diffuse attribution — "the AI said it" — is not acceptable in formal proceedings any more than "the instrument said it" is acceptable in aviation investigation.

**ATS-4: Challenge Protocol**
Any party in a formal proceeding has the right to challenge AI-generated content by requesting:
- The full session log (ATS-1 chain of custody)
- The confidence qualification (ATS-2)
- The attribution boundary (ATS-3)
- An independent re-run of the same prompt under documented conditions

**ATS-5: Drift Event Disclosure**
If the AI session that produced the contested output included any logged drift events (per AIBB Drift Event Log), those events must be disclosed to all parties. A session with multiple confidence inflation events is not equivalent to a clean session.

---

## Connection to Existing Standards

- **AIBB v2.4** (Dixon, 2026) — Provides the logging infrastructure for ATS-1, ATS-2, and ATS-5
- **Federal Rules of Evidence Rule 702** — Expert testimony reliability standard (Daubert) — AI output as expert evidence
- **NTSB CVR admissibility rules (49 U.S.C. § 1154)** — Model for restricting AI output to documented, qualified use
- **EU AI Act Articles 13-14** — Transparency and human oversight requirements for high-risk AI
- **Reardon v. Merck (2024)** and emerging case law on AI-generated medical recommendations

---

## Why This Matters Now

State and federal courts are already grappling with AI-generated evidence, legal briefs written by AI, and AI-assisted medical findings. The American Bar Association and several state bar associations have issued preliminary guidance — but no evidentiary standard exists.

The NTSB did not wait for aviation to produce perfect data recorders before establishing chain of custody standards. It established the standards first and required the industry to meet them.

The same logic applies here. Establish the standard. Let the industry meet it.

---

## Conclusion

AI output is already functioning as testimony in formal proceedings. It is being used without chain of custody, without confidence qualification, without attribution boundaries, and without any challenge protocol. Aviation built the standards for exactly this type of problem — recorded, machine-generated output used as evidence in high-stakes determinations.

The AI Testimony Standard proposed here borrows directly from that framework. No new technology is required. What is required is acknowledgment that AI output, when used in formal proceedings, must be subject to the same evidentiary discipline as any other recorded evidence.

*The CVR transcript is not simply played in court. The AI session log should not be either.*

---

**Prior Art Notice:** This framework is published openly for defensive publication purposes. The concepts, taxonomy, and proposed standards contained herein are claimed as original intellectual work of Tony Dixon / Contrail Equity Strategies LLC, May 2026. All rights reserved.

**GitHub:** github.com/Tonydixon417-cmd
