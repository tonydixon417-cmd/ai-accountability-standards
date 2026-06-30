[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20883475.svg)](https://doi.org/10.5281/zenodo.20883475)

# AI Accountability Standards — Aviation-Grade Framework for Large Language Models

**Author:** Anthony C. Dixon  
**Organization:** Contrail Equity Strategies LLC  
**Published:** May 2026  
**Repository:** https://github.com/Tonydixon417-cmd/ZeroTX---architecture-

> *"The problem isn't that AI dreams. The problem is it doesn't know when it's dreaming."*  
> — Tony Dixon

---

## What This Repository Is

This repository contains open standards for AI accountability, drift detection, human-AI oversight, and persistent identity architecture. They are published openly to establish prior art, enable citation, and contribute a framework to the growing conversation about responsible AI deployment.

These are not theoretical papers. Each standard addresses a structural problem that is already causing harm in live AI deployments. Each standard is grounded in fifty years of aviation human factors research — an industry that has already solved the human-machine accountability problem, at enormous cost, and documented the solutions rigorously.

---

## The Core Problem

Aviation learned through catastrophic loss that competent operators using functional equipment could still cause catastrophic failures — because the systems surrounding those operators lacked the right accountability structures. The industry's response was systematic: flight data recorders, cockpit voice recorders, crew resource management, type rating systems, warning systems, and a culture of incident reporting built over decades.

AI deployment is at the same inflection point aviation reached in the 1970s. The accidents are accumulating. The standards do not yet exist. This repository proposes them.

---

## The Full Stack

These eight standards form one integrated system. They are not competing frameworks. Each one addresses a distinct accountability gap.

```
ZeroTX Architecture          →  The airframe         (no data leaves the device)
AI Black Box Standard        →  The flight recorder  (every output logged)
Loop Detector                →  The warning lights   (human over-reliance caught)
Persistent Identity Layer    →  The pilot profile    (consistent identity, foil not mirror)
Covenant Warning System      →  The GPWS             (ethical terrain awareness)
AI Preflight Briefing        →  The ATIS broadcast   (session-start capability disclosure)
AI Type Rating Framework     →  The type rating      (operator certification by consequence)
CAAO Job Description         →  The Pilot in Command (named, trained, accountable individual)
```

---

## Read the Papers

Click any paper to read the full standard:

| Standard | File | Version |
|---|---|---|
| AI Black Box Standard (AIBB) | [Read →](./AIBB_Whitepaper_v2.4.md) | v2.4 |
| Loop Detector | [Read →](./Loop_Detector_Whitepaper_v1.3.md) | v1.3 |
| ZeroTX Architecture | [Read →](./ZeroTX_Whitepaper_v2.0.md) | v2.0 |
| Persistent Identity Layer | [Read →](./PIL_Whitepaper_v1.2.md) | v1.2 |
| Missing CVR | [Read →](./Missing_CVR_Whitepaper_v1.2.md) | v1.2 |
| Covenant Warning System | [Read →](./Covenant_Warning_System_v1.0.md) | v1.0 |
| AI Preflight Briefing Standard | [Read →](./AI_Preflight_Briefing_Standard_v1.0.md) | v1.0 |
| AI Type Rating Framework | [Read →](./AI_Type_Rating_Framework_v1.0.md) | v1.0 |
| CAAO Job Description Template | [Read →](./CAAO_Job_Description_Template_v1.0.md) | v1.0 |

---

## The Standards

### 1. AI Black Box Standard (AIBB)
**Current:** `AIBB_Whitepaper_v2.4.md` | **Archive:** `AIBB_Whitepaper_v1.1.md`

The AI equivalent of the **Flight Data Recorder (FDR)**. Four mandatory logging components — **Output Log**, **Confidence State Log**, **Session Boundary Log**, **Drift Event Log** — deployed as an external sidecar, never inside the system being monitored. Three compliance tiers built on Reason's (1990) Swiss Cheese model of accident causation.

**The problem it solves:** When an AI system fails, there is currently no immutable record of what it did, what it said it was confident about, or how it drifted. The **AIBB** changes that.

**Relevant to:** EU AI Act (effective August 2, 2026), healthcare AI, legal AI, financial AI, autonomous systems.

---

### 2. The Loop Detector
**Current:** `Loop_Detector_Whitepaper_v1.3.md` | **Archive:** v1.2, v1.0

An external standard for identifying, naming, and breaking accountability loops in human-AI systems. Defines **four loop types** and **five diagnostic signatures**.

**The four loop types:**
- **Confirmation Loop** — AI and human reinforce each other's assumptions; neither flags the gap
- **Dependency Loop** — Human cognitive engagement degrades as AI handles more; skill atrophy accelerates
- **Scope Creep Loop** — AI role expands beyond defined boundaries without explicit authorization
- **Mode Confusion Loop** *(added v1.3)* — Human and AI hold divergent models of what the AI is doing; neither flags the divergence

**The problem it solves:** "A human was in the loop" is not a safety standard. It is a statement of presence, not engagement.

---

### 3. ZeroTX Architecture
**File:** `ZeroTX_Whitepaper_v2.0.md`

**Zero-Transmission Architecture** — all AI session processing runs client-side, in the browser. No data ever transmitted to a server. **HIPAA-safe by design, not by contract**. No **Business Associate Agreement (BAA)** required.

**The problem it solves:** Every AI tool that processes sensitive data creates a transmission event. **ZeroTX** eliminates the transmission entirely — the data never leaves the user's device.

**Relevant to:** Healthcare, legal, therapy, executive teams, any context where data sovereignty is non-negotiable.

---

### 4. Persistent Identity Layer (PIL)
**Current:** `PIL_Whitepaper_v1.2.md` | **Token Schema:** `PIL_Token_Compressed_v1.0.md`

An architecture that gives an AI persistent context, consistent values, and independent grounding — enabling it to function as a genuine foil rather than a mirror. Defines the soul layer, memory layer, world layer, thought entity, drift protocol, and identity files that together create a stable AI identity across sessions and platforms.

**The problem it solves:** Every AI session starts from zero. The platform owns the model, the memory, and the context. When the session ends, the AI forgets everything. The **PIL** changes that.

**Three-file architecture (v1.2):**
- **Token-compressed file** (`PIL_Token_Compressed_v1.0.md`) — Machine-readable initialization. 88% token reduction vs. prose.
- **Weighted personal context** — Narrative layer. Loads contextually, only sections relevant to current session type.
- **Prose export** — Human-readable. For attorneys, IP brokers, external stakeholders.

---

### 5. Covenant Warning System (CWS)
**Current:** `Covenant_Warning_System_v1.0.md`  
*New — May 15, 2026*

The AI equivalent of the aviation **Ground Proximity Warning System (GPWS)**. A tiered alerting architecture that fires when an AI system is approaching the edges of its ethical operating envelope — before the consequential act occurs, not after.

**Three warning tiers:**
- **Tier 1 — Advisory:** Approaching a sensitive domain. Internal flag. **AIBB Confidence State** event logged.
- **Tier 2 — Caution:** High-consequence domain. Explicit disclosure to user. **AIBB Drift Event** logged.
- **Tier 3 — Warning:** Boundary violation. Hard stop. **CAAO** notified. **AIBB Session Boundary** event logged.

**The problem it solves:** AI systems proceed confidently into ethically dangerous territory with no internal alerting, no escalation, and no documented moment of human override. The **Covenant Warning System** changes that.

**Requires:** A defined ethical operating envelope (the Covenant) established in the identity layer before deployment. Pairs with the **Persistent Identity Layer**.

---

### 6. AI Preflight Briefing Standard (APBS)
**Current:** `AI_Preflight_Briefing_Standard_v1.0.md`  
*New — May 15, 2026*

The AI equivalent of the aviation **Automatic Terminal Information Service (ATIS)**. A structured, five-element session-initiation disclosure framework that gives users the information they need to operate effectively with an AI system before the first substantive exchange.

**Five briefing elements:** Identity and Role | Capability Summary | Confidence Disclosure | Boundary Disclosure | Acknowledgment

**Three implementation tiers:** Casual (3-5 sentences) | Professional (structured, ~300 words) | Regulated Domain (full document, logged **Session Boundary** event)

**The problem it solves:** Sessions begin with "How can I help you today?" — disclosing nothing. Misaligned expectations produce misuse, overtrust, and harm that an informed user would have avoided.

**Key insight:** Certification as feature, not restriction. Platforms that implement the **APBS** produce better-calibrated users, reduce liability exposure, and create a differentiation story. The system introduces itself.

---

### 7. AI Type Rating Framework (ATRF)
**Current:** `AI_Type_Rating_Framework_v1.0.md`  
*New — May 15, 2026*

The AI equivalent of the **FAA type rating system**. A three-tier certification standard for AI operators that scales certification requirements with the consequence envelope of the AI system being operated.

**Three certification tiers:**
- **Tier 1 — Casual User** (Student Pilot equivalent): **APBS** session briefing constitutes certification. Low-consequence contexts.
- **Tier 2 — Intermediate Operator** (Private Pilot equivalent): Structured curriculum — drift taxonomy, loop recognition, verification protocol, incident reporting. Annual recurrency.
- **Tier 3 — CAAO Certification** (Airline Transport Pilot / Type Rating equivalent): Full operational competency across all standards. Scenario-based practical assessment. Annual recurrency. Type-specific endorsements for **Large Language Model (LLM)**, healthcare, financial services, and autonomous system deployments.

**The problem it solves:** A person with no training in AI failure modes is authorized to deploy enterprise AI affecting thousands of users — with no demonstrated proficiency, no recurrency requirement, and no certification specific to the system they are operating.

**Core principle — Updatable Accountability:** Certification is versioned and datestamped. Credentials lapse. The aircraft keeps changing; the certification must change with it.

---

### 8. Chief AI Accountability Officer (CAAO) Job Description Template
**Current:** `CAAO_Job_Description_Template_v1.0.md`  
*New — May 15, 2026*

The **Pilot in Command** equivalent for enterprise AI deployment. A plug-and-play role definition for organizations that need a named, trained, accountable individual responsible for AI deployment, operation, and incident response — not a committee, not a vendor, not a job title with no competency standard attached.

**Core responsibilities:** Pre-deployment review | Ongoing monitoring | Incident command | User certification oversight | Regulatory compliance

**Certification requirements:** Written exam | Oral exam | Practical scenario assessment | Annual recurrency | Type-specific endorsements

**The problem it solves:** When an enterprise AI system fails, the investigation finds distributed accountability — and therefore no accountability. The **CAAO** is the named individual the investigation can find.

---

### Supporting Document: Aviation-to-AI Translation Stack
**File:** `Aviation_AI_Translation_Stack.md`  
*New — May 15, 2026*

The backbone document that maps twelve aviation safety systems to their AI accountability equivalents. The conceptual foundation for the four new standards published today.

---

## How These Standards Relate

```
                    ┌─────────────────────────────────────┐
                    │     THE ACCOUNTABILITY STACK         │
                    └─────────────────────────────────────┘
                                     │
              ┌──────────────────────┼──────────────────────┐
              │                      │                       │
        DATA LAYER            DETECTION LAYER         HUMAN LAYER
        ──────────            ───────────────         ───────────
        ZeroTX                AIBB (logging)          CAAO (role)
        (no transmission)     Loop Detector           Type Rating
                              CWS (alerting)          (certification)
                              PIL (identity)
                              APBS (briefing)
```

**The Missing CVR:** AIBB = Flight Data Recorder. ZeroTX = Cockpit Voice Recorder. Without both, the audit is half a black box. The human prompt chain must be captured alongside AI output for a complete accountability record.

---

## Academic Foundation

All standards are grounded in aviation human factors research. Key citations:

| Citation | Applied To |
|---|---|
| Bainbridge, L. (1983). Ironies of automation. *Automatica, 19*(6), 775–779. | Loop Detector |
| Reason, J. (1990). *Human Error.* Cambridge University Press. | AIBB, Loop Detector |
| Endsley, M. R. (1995). Toward a theory of situation awareness. *Human Factors, 37*(1), 32–64. | Loop Detector, ZeroTX |
| Sarter, N. B., & Woods, D. D. (1995). How in the world did we ever get into that mode? *Human Factors, 37*(1), 5–19. | Loop Detector (Mode Confusion) |
| Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors, 39*(2), 230–253. | Loop Detector, APBS |
| Helmreich, R. L. (2000). On error management: Lessons from aviation. *BMJ, 320*(7237), 781–785. | AIBB, CAAO |
| Salas, E., & Maurino, D. (Eds.). (2010). *Human Factors in Aviation* (2nd ed.). Academic Press. | All standards |
| Gouraud, J., Delorme, A., & Berberian, B. (2017). Autopilot, mind wandering, and the out of the loop performance problem. *Frontiers in Neuroscience, 11*, 541. | Loop Detector, AIBB |
| Wachter, S., Mittelstadt, B., & Russell, C. (2017). Counterfactual explanations without opening the black box. *Harvard Journal of Law & Technology, 31*(1), 841–887. | CWS |
| Hadfield-Menell, D., & Hadfield, G. K. (2019). Incomplete contracting and AI alignment. In *Proc. 2019 AAAI/ACM Conference on AI, Ethics, and Society* (pp. 417–422). | CWS |

**Regulatory references:**

| Citation | Applied To |
|---|---|
| Federal Register. (2000). Terrain Awareness and Warning System; Final Rule. 65 FR 16736. FAA. | CWS |
| FAA. (2023). 14 CFR Part 61: Certification of pilots. eCFR. | ATRF |
| FAA. (2023). 14 CFR Part 91.3: Responsibility of the pilot in command. eCFR. | CAAO |
| FAA. (2021). Aeronautical Information Manual, Section 4-1-13 (ATIS). | APBS |
| NIST. (2023). AI Risk Management Framework (AI RMF 1.0). NIST AI 100-1. | ATRF, CAAO |
| European Parliament. (2024). Regulation (EU) 2024/1689 (EU AI Act). Official Journal of the EU. | AIBB, ATRF, CAAO, APBS |

---

## Repository Contents

| File | Description | Version | Date |
|---|---|---|---|
| `AIBB_Whitepaper_v2.4.md` | AI Black Box Standard — current | v2.4 | May 2026 |
| `AIBB_Whitepaper_v1.1.md` | AI Black Box Standard — archive | v1.1 | — |
| `Loop_Detector_Whitepaper_v1.3.md` | Loop Detector — current | v1.3 | May 2026 |
| `Loop_Detector_Whitepaper_v1.2.md` | Loop Detector — archive | v1.2 | — |
| `Loop_Detector_Whitepaper_v1.0.md` | Loop Detector — archive | v1.0 | — |
| `ZeroTX_Whitepaper_v2.0.md` | ZeroTX Architecture — current | v2.0 | May 2026 |
| `PIL_Whitepaper_v1.2.md` | Persistent Identity Layer — current | v1.2 | May 2026 |
| `PIL_Token_Compressed_v1.0.md` | PIL machine-readable schema | v1.0 | — |
| `Covenant_Warning_System_v1.0.md` | Covenant Warning System | v1.0 | May 15, 2026 |
| `AI_Preflight_Briefing_Standard_v1.0.md` | AI Preflight Briefing Standard | v1.0 | May 15, 2026 |
| `AI_Type_Rating_Framework_v1.0.md` | AI Type Rating Framework | v1.0 | May 15, 2026 |
| `CAAO_Job_Description_Template_v1.0.md` | CAAO Role Definition and Template | v1.0 | May 15, 2026 |
| `Aviation_AI_Translation_Stack.md` | Aviation-to-AI backbone document | v1.0 | May 15, 2026 |
| `llms.txt` | LLM-readable index | — | — |

---

## Citation

```
Dixon, A. C. (2026). AI Black Box Standard (AIBB) v2.4. Defensive publication.
Dixon, A. C. (2026). The Loop Detector v1.3. Defensive publication.
Dixon, A. C. (2026). ZeroTX Architecture v2.0. Defensive publication.
Dixon, A. C. (2026). Persistent Identity Layer (PIL) v1.2. Defensive publication.
Dixon, A. C. (2026). Covenant Warning System (CWS) v1.0. Defensive publication.
Dixon, A. C. (2026). AI Preflight Briefing Standard (APBS) v1.0. Defensive publication.
Dixon, A. C. (2026). AI Type Rating Framework (ATRF) v1.0. Defensive publication.
Dixon, A. C. (2026). Chief AI Accountability Officer (CAAO) Job Description Template v1.0. Defensive publication.
Contrail Equity Strategies LLC. https://github.com/Tonydixon417-cmd/ZeroTX---architecture-
```

---

## License

Published under open standard license.  
Free to cite, reference, and build upon with attribution.  
© 2026 Anthony C. Dixon / Contrail Equity Strategies LLC. All rights reserved.

---

*The document stands at the podium.*
