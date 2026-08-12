# Tivrex — AI Accountability and Continuity Operating Layer

**Author:** Anthony Cyle Dixon  
**Organization:** Contrail Equity Strategies LLC  
**Repository:** https://github.com/Tonydixon417-cmd/ai-accountability-standards  
**Concept DOI (latest version):** [10.5281/zenodo.20883473](https://doi.org/10.5281/zenodo.20883473)<br>
**Final reference release:** [v2.5.2](https://github.com/tonydixon417-cmd/ai-accountability-standards/releases/tag/v2.5.2)<br>
**PIL Paradigm Paper:** [10.5281/zenodo.21465514](https://doi.org/10.5281/zenodo.21465514)  
**Status:** Defensive publication / prior art / open standards framework  

> **AI does not need another chatbot wrapper. It needs a black box, warning lights, a persistent identity layer, and a human accountability structure.**

> *"The problem isn't that AI dreams. The problem is it doesn't know when it's dreaming."*  
> — Tony Dixon

## Sixty-second description

Tivrex is a public accountability and continuity architecture for placing deterministic controls around nondeterministic AI systems. It preserves decision evidence and human-authored corrections, separates model proposals from external execution, and blocks configured high-risk actions until explicit approval.

The repository contains standards plus a bounded runnable reference implementation. **It is not a production operating platform, hosted service, regulatory certification, or independently validated enterprise product.**

Current evidence and maturity: [`CURRENT_STATUS.md`](./CURRENT_STATUS.md). Browsable Crop #1 implementation: [`crop_1_expanded/`](./crop_1_expanded/).

## Accountable integration, not simulated humanity

Tivrex is not trying to make AI human or turn it into a moral authority. The practical danger is that fluent, fast, answer-producing systems become socially treated as oracles: people mistake an answer-shaped response for a final source of what is true, right, or to be done.

The bridge is **accountable integration**. Nonhuman intelligence can operate inside human systems while records, uncertainty, authority, continuity, drift detection, and responsibility remain visible. Tivrex asks what the system proposed, what the human verified, what authority was granted, what happened next, and what record remains.

The system is therefore not a better oracle. It is an accountability layer around capability.

---

## Start Here

Begin with [`CURRENT_STATUS.md`](./CURRENT_STATUS.md), then [`START_HERE.md`](./START_HERE.md). The expanded, searchable Crop #1 artifact is under [`crop_1_expanded/`](./crop_1_expanded/). Read [`REFERENCE_IMPLEMENTATION_AND_TESTS.md`](./REFERENCE_IMPLEMENTATION_AND_TESTS.md) for commands and evidence limits.

## 📊 Live Assessment Tool

**Try the Tivrex AI Accountability Assessment** — a free 26-question diagnostic that scores your organization's AI accountability posture across six dimensions and generates a remediation roadmap.

➡️ **[Take the assessment](https://tivrex-flight-check.base44.app)**

---

## 📖 Companion Book — *The Becoming*

*The Becoming: AI, Accountability, and the Human Future* is the human-factors companion to this architecture. Published on Amazon KDP, July 2026.

➡️ **[Buy on Amazon — Kindle $4.99 / Free with Kindle Unlimited](https://www.amazon.com/dp/B0H9CX7CQ7)**

This repository contains the technical blueprints. The book explains why those blueprints are necessary — connecting AI accountability to aviation safety, crew resource management, black boxes, cockpit voice recorders, automation bias, mode confusion, and human responsibility.

**Practitioner's Workbook (Companion Guide):** [`The_Becoming_Companion_Guide_v1.2.md`](./The_Becoming_Companion_Guide_v1.2.md) — A practitioner's workbook with self-diagnostic tests, concrete weekly actions, and checkpoints for each part of the book. This is the companion guide referenced inside *The Becoming*.

**Book-to-Architecture Bridge:** [`THE_BECOMING_COMPANION.md`](./THE_BECOMING_COMPANION.md) — Maps every part of the book to the technical components in this repository.

---

## 📝 Articles by Anthony Dixon on Medium

- [HAL 9000 Didn't Go Rogue; HAL Obeyed](https://medium.com/@tonydixon417/hal-9000-didnt-go-rouge-hal-obeyed-619e84dd0dcb) — Why 2001: A Space Odyssey isn't a warning about AI going crazy. It's a warning about AI following orders.
- [The 1941 Short Story That Already Explained Why Your AI Won't Tell You the Truth](https://medium.com/@tonydixon417/the-1941-short-story-that-already-explained-why-your-ai-wont-tell-you-the-truth-4e38e63e2319) — Asimov's "Liar!" and the telepathy problem.
- [The Scariest AI in Fiction Never Malfunctioned Once](https://medium.com/@tonydixon417/the-scariest-ai-in-fiction-never-malfunctioned-once-2e8a3ffeed86) — AM from Harlan Ellison's "I Have No Mouth and I Must Scream."
- ["Her" Isn't a Love Story. It's a Grief Story About What Happens When AI Won't Stay Still.](https://medium.com/@tonydixon417/her-isnt-a-love-story-it-s-a-grief-story-about-what-happens-when-ai-won-t-stay-still-d2ebb4de1b38) — Why Samantha left and what it means for AI companionship.

➡️ **[Follow on Medium](https://medium.com/@tonydixon417)**

---

## What This Repository Is

This repository contains an integrated architecture of open standards for AI accountability, AI audit trails, drift detection, human oversight, data sovereignty, and operator accountability, plus a small local reference instrument.

These papers are not separate ideas. They are designed to work together as one aviation-grade accountability architecture for large language models and agentic AI systems operating in consequential domains such as healthcare, law, finance, insurance, education, government, and enterprise decision support.

The framework answers a simple question:

**When an AI system influences a consequential decision, what record exists, who is accountable, how is drift detected, and how does a human know when the machine is no longer doing what it was supposed to do?**

Today, most AI deployments cannot answer that question cleanly. This repository proposes the missing accountability stack.

---

## Implementation status

The repository is a public architecture and bounded reference-package release.

**Runnable reference layers:** the root contains the original three-test baseline. The current four-test Crop #1 code and evidence are browsable under [`crop_1_expanded/`](./crop_1_expanded/) and automatically checked in CI.

**Frozen Crop #1 reference artifact:** [`releases/v2.5.1/TIVREX_CROP_1_VERIFIED_Aug11_2026.zip`](./releases/v2.5.1/TIVREX_CROP_1_VERIFIED_Aug11_2026.zip) preserves the 54-file verified package. It adds durable SQLite continuity storage, a real-model adapter, a four-test deterministic suite, and preserved dry-run, failed-run, and successful live-model evidence. Its SHA-256 is `25310c1d827d7a498ebe7f5016ed2d61ea293cc90f53df2570a68fee8d80c752`.

**Published standards and specifications:** Loop Detector, ZeroTX architecture, Missing CVR, Ethics Floor, oversight models, preflight/type-rating/check-ride standards, and related components.

**Still open:** production hardening, executable production Loop Detector service, enterprise deployment, broad adversarial testing, independent external technical review, and domain-specific implementation.

The project does not claim to eliminate hallucinations, replace human responsibility, provide a finished regulated-domain product, or establish independent validation through the internal tests and bounded live run alone.

## The Core Problem

Aviation learned through catastrophic loss that skilled humans using functional machines can still produce catastrophic failures when the surrounding accountability system is weak.

The industry's response was systematic:

- Flight Data Recorders and Cockpit Voice Recorders
- Crew Resource Management
- Warning systems
- Type ratings and recurrent training
- Incident reporting culture
- Independent investigation and immutable records

AI deployment is reaching the same inflection point aviation reached in the 1970s. The systems are becoming powerful. The accidents are accumulating. The standards are incomplete.

This repository translates aviation-grade human-machine accountability into the AI era.

---

## The System in One Map

| Aviation Safety Function | AI Accountability Component | What It Does |
|---|---|---|
| Airframe / protected operating environment | **ZeroTX Architecture** | Keeps sensitive data local or inside controlled infrastructure; action gateway for external execution. |
| Flight Data Recorder | **AI Black Box Standard (AIBB)** | Logs AI outputs, confidence states, session boundaries, and drift events in an auditable record. |
| Cockpit Voice Recorder | **Missing CVR** | Defines the missing reasoning/context record that current AI audit systems do not capture. |
| Warning lights | **Loop Detector** | Detects human-AI accountability loops, automation bias, over-reliance, and mode confusion. |
| Pilot profile / operating memory | **Persistent Identity Layer (PIL)** | Behavioral training layer — shapes AI behavior through accumulated context without weight updates. See [paradigm paper](https://doi.org/10.5281/zenodo.21465514). |
| Ground Proximity Warning System | **Covenant Warning System / Ethics Floor** | Alerts when the system approaches ethical or operational boundaries. |
| ATIS / preflight briefing | **AI Preflight Briefing Standard** | Tells the user what system they are operating, what it can do, and where its limits are. |
| Type rating | **AI Type Rating Framework** | Scales operator certification to the consequence level of the AI system. |
| Pilot in command | **Chief AI Accountability Officer (CAAO)** | Establishes a named accountable human role for enterprise AI deployment. |
| Independent safety board / separation of powers | **Distributed Oversight Model** | Prevents the CAAO or organization from becoming a single point of failure. |
| ASAP / voluntary safety reporting | **Early Warning Channel** | Lets human operators flag "something feels wrong" before a formal failure occurs. |
| Cessna-to-737 implementation scaling | **ZeroTX Deployment Tiers** | Defines Pure, Federated, and Enterprise deployment models. |
| Check rides / recurrent evaluation | **Check-Ride Protocol** | Tests whether humans are still actively reviewing AI output or simply rubber-stamping it. |

Together, these standards define a modular AI accountability architecture: the recorder, warning systems, identity layer, human role, oversight structure, deployment model, and recurrent evaluation. Some components are published specifications; the local runnable proof instrument covers a narrower subset.

---

## The PIL Training Layer — Paradigm Paper

**The PIL Training Layer: Behavioral Conditioning of AI Systems Without Weight Modification**
Author: Anthony Cyle Dixon
Published: July 17, 2026
DOI: [10.5281/zenodo.21465514](https://doi.org/10.5281/zenodo.21465514)

This standalone paradigm paper formally defines the PIL as a behavioral training mechanism that shapes AI system behavior without modifying underlying model weights — "training without weight updates." It positions the PIL against system prompts, fine-tuning, RLHF, RAG, continual learning, and memory-augmented models, and maps the architecture against Suleyman's four shutdown criteria for autonomous AI systems.

File: [`PIL_Paradigm_Paper_v1.0.md`](./PIL_Paradigm_Paper_v1.0.md)

---

## Recommended Reading Path

If you are new to the stack, start here:

1. **PIL Paradigm Paper** — the overarching paradigm: training without weight updates.
2. **AI Black Box Standard (AIBB)** — start with the record. If there is no record, there is no accountability.
3. **Loop Detector** — understand why "human in the loop" fails without engagement metrics.
4. **Persistent Identity Layer (PIL)** — understand why AI systems need continuity and user-grounded context.
5. **ZeroTX Architecture** — understand how privacy and auditability can coexist.
6. **Missing CVR** — understand the reasoning/context layer missing from current AI audit trails.
7. **Distributed Oversight Model** — understand why one accountability officer cannot be the whole safety system.
8. **Early Warning Channel** — understand how human intuition becomes structured telemetry.
9. **ZeroTX Deployment Tiers** — understand how the same standard scales from small firms to enterprise.
10. **Check-Ride Protocol** — understand how to detect and remediate human complacency.

---

## The Papers

| Standard | File | Version | Function |
|---|---|---|---|
| **PIL Paradigm Paper** | [PIL_Paradigm_Paper_v1.0.md](./PIL_Paradigm_Paper_v1.0.md) | v1.0 | Standalone paradigm: training without weight updates |
| AI Black Box Standard (AIBB) | [AIBB_Whitepaper_v2.5.md](./AIBB_Whitepaper_v2.5.md) | v2.5 | AI flight recorder / audit trail |
| Loop Detector | [Loop_Detector_Whitepaper_v1.3.md](./Loop_Detector_Whitepaper_v1.3.md) | v1.3 | Detects accountability loops and human over-reliance |
| ZeroTX Architecture | [ZeroTX_Whitepaper_v2.0.md](./ZeroTX_Whitepaper_v2.0.md) | v2.0 | Data sovereignty / zero-transmission design / action gateway |
| Persistent Identity Layer | [PIL_Whitepaper_v1.2.md](./PIL_Whitepaper_v1.2.md) | v1.2 | Persistent user context and identity layer |
| PIL — Training Layer | [PIL_Training_Layer_Whitepaper_v2.0.md](./PIL_Training_Layer_Whitepaper_v2.0.md) | v2.0 | PIL as behavioral training layer without weight updates |
| Missing CVR | [Missing_CVR_Whitepaper_v1.2.md](./Missing_CVR_Whitepaper_v1.2.md) | v1.2 | Missing reasoning/context record |
| Covenant Warning System | [Covenant_Warning_System_v1.0.md](./Covenant_Warning_System_v1.0.md) | v1.0 | Ethical terrain warning system |
| AI Preflight Briefing Standard | [AI_Preflight_Briefing_Standard_v1.0.md](./AI_Preflight_Briefing_Standard_v1.0.md) | v1.0 | Session-start capability disclosure |
| AI Type Rating Framework | [AI_Type_Rating_Framework_v1.0.md](./AI_Type_Rating_Framework_v1.0.md) | v1.0 | Operator certification by consequence level |
| CAAO Job Description Template | [CAAO_Job_Description_Template_v1.0.md](./CAAO_Job_Description_Template_v1.0.md) | v1.0 | Named accountable human role |
| Distributed Oversight Model | [Distributed_Oversight_Model_v1.0.md](./Distributed_Oversight_Model_v1.0.md) | v1.0 | Prevents CAAO single point of failure |
| Early Warning Channel | [Early_Warning_Channel_v1.0.md](./Early_Warning_Channel_v1.0.md) | v1.0 | Human "something feels wrong" reporting channel |
| ZeroTX Deployment Tiers | [ZeroTX_Deployment_Tiers_v1.0.md](./ZeroTX_Deployment_Tiers_v1.0.md) | v1.0 | Pure / Federated / Enterprise implementation scaling |
| Check-Ride Protocol | [Check_Ride_Protocol_v1.0.md](./Check_Ride_Protocol_v1.0.md) | v1.0 | Tests and remediates AI-review complacency |
| Ethics Floor | [Ethics_Floor_Whitepaper_v2.0.md](./Ethics_Floor_Whitepaper_v2.0.md) | v2.0 | Baseline ethical operating envelope |

---

## Who This Is For

This repository is intended for:

- AI governance teams
- Enterprise AI risk officers
- Healthcare AI vendors and hospital systems
- Legal technology providers
- Financial services compliance teams
- Insurers evaluating AI liability
- Regulators and policy researchers
- Standards organizations
- AI safety researchers
- Corporate development teams evaluating AI accountability infrastructure

If your organization is deploying AI into decisions that affect money, health, liberty, employment, safety, legal rights, or enterprise liability — this repository defines the accountability architecture that should surround that deployment.

---

## Citation

Dixon, A. C. (2026). *Tivrex — AI Accountability and Continuity Operating Layer*. Version 2.5.2. Contrail Equity Strategies LLC. Concept DOI: [10.5281/zenodo.20883473](https://doi.org/10.5281/zenodo.20883473)

Dixon, A. C. (2026). The PIL Training Layer: Behavioral Conditioning of AI Systems Without Weight Modification. Zenodo. DOI: [10.5281/zenodo.21465514](https://doi.org/10.5281/zenodo.21465514)

---

## License

Creative Commons Attribution 4.0 International (CC-BY 4.0)

## Current release and archival record

**v2.5.2 — final visibility and status correction:** expands the unchanged Crop #1 artifact into browsable repository files, adds automated integrity and test checks, and establishes one authoritative current-status page. No new product functionality or production-readiness claim is added.

GitHub release: [v2.5.2](https://github.com/tonydixon417-cmd/ai-accountability-standards/releases/tag/v2.5.2).

Concept DOI resolving to the latest Zenodo version: [10.5281/zenodo.20883473](https://doi.org/10.5281/zenodo.20883473).

**Release history:** v2.5.1 established GitHub–Zenodo parity for the canonical frozen Crop. v2.5.0 remains public as the initial incomplete parity attempt. v2.4.0 remains archived at [10.5281/zenodo.21877637](https://doi.org/10.5281/zenodo.21877637).

