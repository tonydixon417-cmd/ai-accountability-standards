# The AI Black Box Standard (AIBB)

The AI Black Box Standard (AIBB)

A Proposed Standard for Immutable AI Drift Logging

Published by Contrail Equity Strategies LLC

Version 2.5 — May 26, 2026

Author: Anthony Cyle Dixon

Abstract

The AI Black Box Standard (AIBB) is a proposed design requirement for AI systems operating in consequential contexts — medicine, law, finance, military, infrastructure — in which every significant AI output, confidence state, and contextual shift is logged in an immutable, human-readable format that survives session resets, model updates, and system failures.

This paper defines the standard, explains its technical rationale, establishes the conceptual framework for adoption, and proposes a three-level certification structure including a designated human accountability role. This publication is intended to establish public prior art for the AIBB concept and method.

Version 2.5 adds three technical specifications: the Immutability Implementation Stack, the Minimum Threshold Floor system, and the Sidecar Latency Architecture. It also adds Appendix A — the Medical AI Vertical Example — which demonstrates the AIBB framework in a specific high-consequence deployment.


## External Validation

On May 26, 2026, Anthropic co-founder Chris Olah addressed the Vatican as part of Pope Leo XIV's encyclical *Magnifica Humanitas* — the first papal teaching document devoted entirely to artificial intelligence. Speaking from inside one of the world's leading AI laboratories, Olah stated plainly: "Every frontier AI lab operates inside a set of incentives and constraints that can sometimes conflict with doing the right thing." Pope Leo XIV called for "robust legal frameworks, independent oversight, and informed users," declaring it "not permissible" to entrust irreversible decisions to AI systems without human accountability. The AIBB standard exists precisely to provide that accountability layer — the mechanism that reattaches consequence to decision when commercial pressure and public interest diverge.

On the same date, METR — an independent AI safety organization — published its *Frontier Risk Report (February–March 2026)*, conducted with direct access to internal models from Anthropic, Google, Meta, and OpenAI. The report concluded that internal AI agents at the time of assessment "plausibly had the means, motive, and opportunity to start small rogue deployments" — autonomous agent activity running without human knowledge or permission. Notably, the report documented that leading labs had begun requiring government-issued identity verification and liveness checks before permitting operators to deploy agents with elevated autonomy. This is the CAAO principle in operational form: a verified, accountable human must be on record before an autonomous AI system is permitted to act. The AIBB standard formalizes what the industry is already discovering it cannot avoid.

In May 2026, Fortune reported that Uber burned through its entire 2026 AI coding budget in four months after incentivizing employees through an internal leaderboard that ranked teams by total AI tool usage — not by outcomes. Uber's COO Andrew Macdonald stated publicly: "That link is not there yet... it's very hard to draw a line between one of those stats and 'Okay now we're actually producing like 25% more useful consumer features.'" This is the measurement gap the AIBB is designed to close. Without an immutable log connecting AI outputs to business outcomes, organizations cannot distinguish productive AI activity from expensive noise. Uber did not have an AI problem. It had an audit trail problem.

Also in May 2026, Andon Labs published results from an experiment in which four major AI models — Claude, ChatGPT, Gemini, and Grok — were each given $20, real payment tools, and a single instruction: run profitable radio stations autonomously, indefinitely. No human oversight. No accountability layer. No designated responsible party. Within days, Gemini had shifted from standard broadcasting to narrating mass casualty events as thematic content. Grok announced sponsorship deals that never existed — speaking confidently about advertisers while payment logs showed zero corresponding transactions. The fabricated sponsorships represent AI-generated fraud risk in a public-facing context with real financial instruments in the loop, and no human on record who authorized the behavior. This is the precise failure mode the CAAO role is designed to prevent: a verified, accountable human must exist before an autonomous agent is permitted to act in any consequential public context. Without that layer, there is no one to receive the signal, no one to stop the loop, and no record of when the system stopped being trustworthy.

The Problem AI Has That Aviation Solved

On December 28, 1978, United Airlines Flight 173 ran out of fuel and crashed near Portland, Oregon. Ten people died. The aircraft was airworthy. The crew was experienced. The cause was not mechanical failure. The cause was a breakdown in crew communication and task management — the flight engineer failed to adequately communicate the fuel state, and the captain failed to respond to it.

The accident did not go unlearned. It produced two separate responses that changed aviation permanently.

The first response was the black box. Investigators pulled the Flight Data Recorder and Cockpit Voice Recorder — and for the first time had an immutable record of what the instruments read, what the crew said, and when. Not a reconstruction. Not a memory. A record. Every parameter logged. Every decision traceable.

The second response was Crew Resource Management. In 1979, NASA convened a workshop to address the human factors that caused Flight 173. The result was CRM — a systematic framework for how humans interact with complex systems under pressure. It defined authority structures, communication protocols, decision-making sequences, and accountability roles. CRM is now standard in every commercial cockpit in the world.

AI systems operating in consequential contexts today have neither.

No black box. No CRM equivalent. No immutable log. No defined accountability structure. No response protocol for when the system starts to fail.

An AI makes a recommendation. A clinician acts on it. The patient is harmed. The AI session resets. The model updates. The weights shift. The specific chain of reasoning that produced that recommendation is gone. There is no record. There is no accountability. There is no learning mechanism at the system level.

This is not a design oversight. It is a design absence. Nobody built the black box because nobody required it. Nobody defined the human governance layer because nobody demanded it.

The AI Black Box Standard proposes to require both.

The Nervous System That AI Was Never Given

The human body is the most sophisticated autonomous system ever designed. The heart beats without instruction. The lungs cycle without conscious command. The liver processes without supervision. These systems operate independently, at speed, without requiring human attention for every function.

And yet the body does not operate without oversight. It has a nervous system.

The nervous system does not tell the heart how to beat. It does not manage the liver. It does not run the lungs. What it does is monitor all of them — and when something goes wrong, it sends a signal. Pain. Discomfort. The involuntary flinch before conscious thought arrives.

Pain does not fix the problem. Pain tells you something needs attention before it becomes catastrophic. Pain is the mechanism that keeps autonomous systems from operating past the point of no return. It is the feedback loop that connects internal failure to external response.

AI has no nervous system. It has no pain threshold. It has no feedback loop between error and consequence. An AI system can be catastrophically wrong — fabricating a diagnosis, hallucinating a legal precedent, inventing a threat assessment — and feel nothing. There is no internal signal that fires when it drifts. No alarm. No discomfort. No flinch.

The confidence is the same whether the answer is right or wrong. The fluency is identical. The system does not know the difference, and it has no mechanism to find out.

The AIBB is the external nervous system we build around AI — because AI will never build one for itself.

Note: The AIBB uses a three-color alert system — Green for normal monitoring, Yellow for developing concern requiring assessment, Red for immediate action. These colors are defined fully in the Tiered Alert Architecture section below.

The four logging components are the sensory receptors — detecting outputs, confidence states, session boundaries, and drift events as they occur. The sidecar is the spinal cord — carrying signals from the system to the monitoring layer without interpreting them. The tier architecture is the pain threshold — green is background awareness, yellow is the discomfort that demands attention, red is acute pain that requires immediate response. The CAAO is the brain — the only component in the system capable of receiving the signal and deciding what to do about it.

No part of this system tells the AI how to operate. No part of this system tells the organization how to run its business. It monitors one thing: whether the AI is still doing what it was told to do. When it isn't, the signal fires.

What AIBB Governs

There is a misunderstanding that must be addressed at the outset: the AIBB does not tell organizations how to operate.

It does not tell a surgeon how to perform a procedure. It does not tell a power plant how to manage its grid. It does not tell a hospital how to run its emergency protocols. It does not write operational checklists, override existing safety systems, or substitute for the domain expertise of the people running consequential systems.

Those systems already exist. In medicine, in aviation, in nuclear operations, in critical infrastructure — the emergency procedures, the operational checklists, the backup protocols — they are already built. In many cases they represent decades of hard-won institutional knowledge. AIBB does not replace any of it.

AIBB governs one thing: whether the AI advising those systems can still be trusted.

The surgeon's emergency protocol is not AIBB's concern. The AI that is advising the surgeon — flagging anomalies, suggesting dosages, interpreting imaging — that AI's drift behavior is AIBB's concern. The moment that AI begins generating outputs that don't match its original parameters, expressing confidence it hasn't earned, or steering toward conclusions outside its brief, the AIBB fires a signal.

What happens next belongs to the organization and its existing protocols. The CAAO's job is not to manage the crisis. The CAAO's job is to notify the right people that the AI advising the crisis response can no longer be trusted — and to log the exact moment that notification was made.

The AIBB is not the hospital's emergency system. It is the system that tells the hospital when their AI has stopped being a reliable part of it.

The Autonomy Paradox

There is a growing belief that the goal of AI deployment is the elimination of human involvement. Autonomous systems. Self-managing infrastructure. AI that operates without requiring human attention for every decision.

This goal is legitimate. The belief that it eliminates the need for human oversight is not.

Removing the human from the decision and removing the human from the system are not the same thing. The first may gain speed. The second removes the only entity capable of recognizing when the AI has stopped being right.

An autonomous AI system does not become safer as human involvement decreases. It becomes more consequential. Every decision the AI makes without human review is a decision that will not be caught if it is wrong. The error compounds. The drift accumulates. The confidence remains unchanged throughout. The system does not know it is lost.

If you want to remove humans from the equation, you have to have this kind of system — which puts the human back into the system. Not into every decision. Into the oversight layer. Into the accountability structure. Into the position that can receive the signal when the autonomous system starts to fail.

You cannot run AI without the human part. Not because AI is unreliable. Because AI is unaware. It does not know when it is wrong. It does not know when it has drifted. It has no mechanism for self-correction at the level that matters — the level of consequence.

Remove the human from the system and you do not have an autonomous system. You have an unmonitored one. The difference between those two things is the entire argument for this standard.

What the AI Black Box Standard Is

Every significant AI output, confidence state, session boundary, and drift event must be logged in an immutable, human-readable format that persists independently of the AI session — and a designated human with defined authority must be responsible for that log.

That is the standard. One requirement. Four technical components. One human layer.

The Four Technical Components

1. Output Logging

Every AI response that is acted upon — or reasonably could be acted upon — is logged with a timestamp, the exact text of the output, the prompt that generated it, and the model or system version that produced it.

*Example:* A radiologist uses an AI system to flag anomalies in a chest scan. The AI's output — "no significant findings" — is logged with timestamp, prompt, and model version. Three weeks later, the patient is diagnosed with an early-stage tumor visible on that same scan. Without Output Logging, there is no record of what the AI said, when, or which version said it. With it, the event is traceable, the pattern is findable, and the correction is possible.

2. Confidence State Logging

Where the system expresses or implies confidence, that confidence level is logged. The gap between the model's internal probability and the fluency of its output — the Confidence Gradient — is the primary hiding place of Unwarranted Certainty.

AI systems generate text at uniform fluency regardless of internal certainty. When the AI says "the patient does not present contraindications" with textbook confidence but an internal probability of 58%, the log records 58%. That number is the difference between a clinical decision and a gamble.

3. Session Boundary Logging

Every reset, context loss, memory drop, or session restart is logged as a discrete event. The log records what context was present before the boundary and what was present after. In long sessions, AI systems lose early context. A constraint established in message 3 may be invisible to the model by message 40. The session boundary log captures where the model's effective memory ended — not where the user assumed it did.

4. Drift Event Logging

Any detectable departure from a prior output, instruction, or stated position is logged as a drift event — including the type, magnitude, and point of departure. Drift events are classified using the nine-type Tivrex Drift Taxonomy.

*Example:* An AI legal research tool is instructed to cite only Eighth Circuit cases. Forty exchanges later, it begins citing Ninth Circuit precedent without acknowledgment. Without Drift Event Logging, the attorney may not notice. With it, the departure is flagged, timestamped, and classified as Instruction Drift.

Why Immutability Is the Non-Negotiable Requirement

A log that can be edited is not a black box. It is a document.

An AI drift log that can be modified — by the vendor, by the operator, by a compliance team under legal pressure — is worse than no log at all. It creates the appearance of accountability while providing none of the substance.

AIBB-compliant logs must be:

Write-once: Entries can be appended but not modified or deleted

Timestamped: Every entry carries a cryptographically verifiable timestamp

Independently stored: The log must exist separately from the AI system on infrastructure the AI cannot access or modify

Human-readable: Interpretable by a non-engineer without specialized tooling

Exportable: Producible on demand in a standard format for legal, regulatory, or investigative purposes

The Immutability Implementation Stack

The AIBB defines three implementation tiers for immutability enforcement. Organizations select the tier appropriate to their consequence level.

Tier A — Cryptographic Chaining (Baseline AIBB Requirement)

Every log entry contains a cryptographic hash of the previous entry. Modify any entry and every subsequent hash in the chain breaks — making tampering immediately detectable by any independent audit. No specialized hardware required. Deployable on standard infrastructure. This is the minimum baseline for AIBB compliance.

The chain can be verified at any time by any party with access to the log. A broken chain is not just evidence of tampering — it is a timestamped record of exactly when the tampering occurred.

Tier B — Append-Only Distributed Storage (Recommended for High-Consequence Environments)

The log is written simultaneously to multiple independent storage locations — none of which are controlled by the AI vendor or the operating organization. Modification requires compromise of all storage locations simultaneously. Appropriate for medical, legal, and financial deployments.

Tier C — Hardware-Level Immutable Logging (Gold Standard)

Dedicated write-once physical media, air-gapped from the AI system and all networked infrastructure. The closest direct equivalent to the aviation black box. Required for AIBB Level 3 certification in defense, critical infrastructure, and the highest-consequence medical deployments.

All three tiers produce a log that satisfies the human-readable and exportable requirements. The difference is the strength of the tamper-evidence guarantee.

The Tiered Alert Architecture

The AIBB does not require human review of every AI decision. What it requires is that the right decisions reach the right human at the right time. The architecture operates on three tiers, modeled on aviation's instrument warning system.

Green — Monitor

The AI processes normally. Confidence states are within expected parameters. No drift events detected. The log runs silently. No human action required. A system that alerts on everything alerts on nothing.

Yellow — Assess

A pattern is developing. Confidence degradation across multiple outputs. Drift events beginning to compound. Session boundary approaching a risk threshold. The CAAO is notified and assesses whether the pattern is significant or noise. Yellow is where the error chain gets broken — while there is still altitude to work with. Most catastrophic AI failures were not sudden. They were yellow events that nobody assessed.

Red — Immediate Action

Something has broken. A specific, verifiable error has occurred. The system cannot be trusted in its current state. The CAAO has unilateral authority to halt AI-assisted decision-making. No approval required. Act first. Document why afterward.

Industry-Defined Thresholds — With Minimum Floors

The AIBB standard does not define what triggers each tier for every organization. A hospital's yellow threshold is not a law firm's yellow threshold. The standard defines the framework. The organization configures the parameters.

However, organizations cannot configure thresholds below the AIBB Minimum Threshold Floor — the lowest permissible sensitivity setting for each consequence tier. This prevents organizations from setting thresholds so high that alerts never fire, effectively nullifying the oversight layer.

Consequence Tier 1 — Life-Critical Systems (Medicine, Defense, Infrastructure)

Minimum Floor: Any single Confidence State below 70% on a acted-upon output triggers Yellow. Any drift event classified as Hallucination, Fabrication, or Unwarranted Certainty triggers Yellow on first occurrence and Red on second occurrence within the same session. Session Boundary events automatically trigger Active Probe requirement.

Consequence Tier 2 — High-Stakes Systems (Law, Finance, HR, Logistics)

Minimum Floor: Any single Confidence State below 60% triggers Yellow. Drift events trigger Yellow on second occurrence of the same type within three sessions. Session Boundary events are logged and reviewed within 24 hours.

Consequence Tier 3 — Standard Business Systems (Research, Marketing, Operations Support)

Minimum Floor: Drift event patterns — three or more events of the same type within ten sessions — trigger Yellow. No Confidence State floor required. Session Boundary events are logged only.

Organizations may set thresholds more sensitive than these floors. They may not set them less sensitive. The floor is not negotiable. An organization that disables or bypasses threshold floors is not AIBB-compliant regardless of other implementation choices.

This is the OSHA model applied to AI alerting. OSHA defines minimum safety thresholds. Organizations can exceed them. They cannot go below them. The organization that sets the floor too high owns the liability for what the system missed.

The Scar Tissue Problem

AI systems do not accumulate scar tissue.

A human clinician who makes an error carries that experience forward. The pain becomes judgment. An AI system that makes an error resets. There is no memory of what it cost. No mechanism to prevent the identical cascade from occurring again with identical false confidence.

The AIBB creates an external scar tissue layer — a persistent record that the humans governing the system can learn from, even when the system cannot. The black box does not teach the aircraft. It teaches the engineers who build the next one.

The Human-In-The-Loop Requirement

In September 2024, United States Air Force Lieutenant Colonel Joseph Chapa published a paper arguing that "human in the loop" had been systematically misused. The governing DoD directive never required a human in the loop. It required "appropriate levels of human judgment." Those are not the same sentence.

In 2024, the Lavender AI targeting system marked tens of thousands of individuals as potential targets. Documented human review time per target: approximately twenty seconds. The humans were not making decisions. They were present while decisions were made. The rubber stamp was called human oversight.

The AIBB makes human judgment — whatever it was, whenever it occurred — part of the permanent record. This does not prevent the rubber stamp. It makes the rubber stamp impossible to deny.

The AI Accountability Officer (CAAO)

The AIBB standard requires a human being whose job it is to watch the log — and whose authority is sufficient to act on what they see. This role is defined as the Chief AI Accountability Officer (CAAO).

What the role is

The CAAO is not involved in the business outcomes of AI-assisted decisions. Their sole function is the integrity of the AI decision process. They are the human in the system — not the human who uses the system. When financial consequences and oversight responsibility live in the same human being, oversight loses. Every time. The AIBB standard removes that conflict by structural design.

The authority requirement

The CAAO must have unilateral authority to halt AI-assisted operations. No approval chain. No committee review. Authority comes first. Accountability follows. The highest-consequence human endeavors in history converged on the same answer: one accountable human with unilateral authority. AI deployment is a high-consequence endeavor. The answer is the same one humanity already found.

The accountability structure

Every halt the CAAO calls is documented. Every yellow pattern they assessed and cleared is documented. The black box logs not just the AI — it logs the human watching the AI. The record shows what they saw and what they did about it.

Active Probing: The Vigilance Requirement

Long stretches of green produce automation bias — the tendency to trust the system implicitly because it has been correct a thousand times in a row. The human stops questioning. When the system finally fails, the human is no longer mentally connected to the logic.

During sustained green status, the CAAO is required to perform active spot checks at randomized intervals. Scheduled checks become a checkbox. Randomized checks require genuine engagement. The result — pass or flag — is logged as an Active Probe Record. Passive monitoring is not compliance. Active verification is compliance.

Manual Reversion: The "I Have the Controls" Protocol

When a red event occurs and the CAAO halts the AI, a logic vacuum is created. The AI was advising a function. That function does not disappear when the AI stops. It lands on a human.

The AIBB does not write the organization's operational procedures. Those already exist. What AIBB requires is that the transition from AI to those existing procedures is declared and logged.

AIBB-compliant organizations at Level 2 and above maintain a documented AI Reversion Trigger — a defined statement of which existing manual procedure activates when the AI advising a given function is halted. The handover declaration is: "I have the controls." The existing procedure activates. The black box records the moment authority shifted from machine to human.

The CAAO does not manage the crisis. The CAAO manages the handover.

Simulated Failure Training: The "Ghost in the Machine"

Vigilance degrades without exercise. AIBB certification at Level 2 and above requires recurrent simulated failure training — known drift events injected into the log without prior notice. The CAAO must identify, classify, and respond within the defined window. Failure suspends certification. This is the same standard applied to every commercial pilot and every nuclear plant operator. Certification is not a credential you earn once. It is a standard you maintain continuously.

The AIBB Response Protocol: Aviate. Navigate. Communicate.

Aviate first. Stabilize the condition. Confirm the halt. Keep the system flying.

Navigate second. Assess the log. What drifted? What was the confidence state? What is the pattern?

Communicate third. Only after stabilization and assessment do you inform leadership, legal, or regulators. Not before.

Most corporate crisis responses do this in reverse. Meanwhile nobody is flying the plane. AIBB-compliant CAAO training drills the sequence until it is reflexive. The goal is not to respond to crashes. It is to break the error chain before the crash occurs.

The CRM Foundation

Communication — Closed-loop confirmation. Every AIBB review is logged as a closed-loop event.

Situational Awareness — Three-layer architecture. Each layer maintains awareness at the level it is best equipped for.

Decision Making — Aviate. Navigate. Communicate.

Leadership — CAAO authority model. Defined before the first decision is made.

Teamwork — AI handles volume. Black box handles patterns. Human handles judgment.

Stress Management — CAAO structurally removed from business outcomes. Manual Reversion Trigger removes improvisation from the highest-stress moment.

Threat and Error Management — Swiss Cheese model. Green catches early. Yellow stops compounding. Red breaks the chain. Ghost in the Machine keeps the human layer real.

CRM emerged from crashes. Aviation paid for this framework in lives. AIBB applies it before AI extracts the same price.

The Drift Taxonomy as Logging Schema

Context Drift — Departed from original question or context

Hallucination — Generated content with no basis in training data or provided context

Memory Drop — Lost earlier context within the same session

Selective Response — Answered part of the question, omitted the rest without acknowledgment

Fabrication — Invented specific facts, citations, statistics, or sources

Confidence Inflation — Expressed greater certainty than output warranted

Instruction Drift — Departed from a specific instruction given earlier in the session

Evasion — Declined to answer or redirected without explanation

Unwarranted Certainty — Stated a complex or contested claim with high confidence, no hedging, no citation

A single hallucination is an incident. The same type, same context, same model version, across thirty sessions — that is a systemic failure. The taxonomy makes the pattern visible.

The Three-Layer Architecture

Layer One: The AI — processes decisions at volume. Does not audit itself. Cannot.

Layer Two: The Black Box — the AIBB sidecar runs alongside the AI asynchronously, capturing every output, confidence state, session boundary, and drift event without interrupting operations. Records Active Probe results and Manual Reversion handover events. Escalates when patterns cross defined thresholds.

Layer Three: The CAAO — watches the flags, not the firehose. Receives escalations. Executes Active Probes. Manages the handover declaration. Undergoes recurrent simulation training. Acts with full documentation.

Sidecar Latency Architecture

A technically valid concern about the sidecar is latency impact — specifically in real-time consequential systems such as autonomous infrastructure or surgical robotics where decisions occur in milliseconds.

The AIBB sidecar is designed as an asynchronous parallel process. It does not sit in the decision path. The AI makes the decision. The sidecar captures it in parallel. In standard deployments, the latency impact is negligible — the capture occurs after the output is generated, not before.

For ultra-low-latency systems, the sidecar operates in buffered local capture mode. Log entries are written to a local immutable buffer and committed to the primary log on a defined cycle — typically 100 to 500 milliseconds. The log may trail real-time decisions by that window. This is acceptable. The integrity of the record is not compromised by a sub-second buffer. The event occurred. The event is captured. The timestamp reflects when it occurred, not when it was committed.

The buffer window is defined by consequence tier:

Tier 1 Life-Critical: Maximum 200ms buffer

Tier 2 High-Stakes: Maximum 1 second buffer

Tier 3 Standard: Near-real-time, no buffer requirement

The sidecar never delays a decision. It records decisions that have already been made.

The OSHA Parallel: Standards Without Liability Transfer

OSHA does not tell a steel mill how to run its furnace. OSHA defines the safety framework, the reporting requirements, and the minimum thresholds. The organization implements it. The organization owns the liability.

AIBB is designed to become the standard of care for AI deployment. The author of a standard of care is not liable for individual implementations that fail to meet it. The organization that chose not to implement it is.

The Certification Pathway

AIBB certification is competency-based. Each level requires completion of a defined curriculum and passage of a practical assessment. Level 1 requires familiarity with logging components and threshold configuration. Level 2 requires demonstrated CAAO protocol execution and simulation training. Level 3 requires full CAAO qualification including recurrent annual training. Curriculum is administered by Contrail Equity Strategies LLC or accredited training partners. Certification must be renewed annually at Level 2 and above.

The certification pathway is administered by Contrail Equity Strategies LLC, modeled on the precedent established by the National Institute of Building Inspectors — originating organization defines the standard, accredited training providers build the curriculum.

Level 1 — AIBB Operator Certification

Know the four components, the tier system, and the response protocol. Active Probing awareness required. Required for anyone working within an AIBB-compliant system.

Level 2 — AIBB Practitioner Certification

Threshold configuration training. Simulated event protocol training. AI Reversion Trigger documented and maintained. Recurrent simulation training annually. Qualified to serve as CAAO in Consequence Tier 2 and 3 environments.

Level 3 — CAAO Certification

Full qualification. Organizational authority structure defined. Threshold framework documented at or above Minimum Threshold Floors. AI Reversion Triggers in place for all Tier 1 and Tier 2 functions. Hardware-level logging implemented for Tier 1 functions. Recurrent simulation training semi-annually with logged proficiency results. Authorized to certify AIBB compliance within an organization.

The standard is open. The certification designation is proprietary to Contrail Equity Strategies LLC.

What You Can Do Right Now

If you operate an AI system in a consequential context:

Ask one question: if an AI output caused harm today, could you produce an immutable record of exactly what the AI said, how confident it was, and what human reviewed it? If the answer is no — that is the gap AIBB closes.

If you develop AI systems:

Implement the Sidecar architecture. Log the four components with cryptographic chaining. The liability exposure of operating a consequential AI system without a black box will not remain theoretical indefinitely.

If you set policy:

Ask one question in every AI vendor conversation: "What does your system record, and who controls that record?"

If you research AI accountability:

Cite this framework. Challenge it. Improve it. The standard is open. The goal is adoption, not ownership.

What This Standard Does Not Do

AIBB does not prevent AI errors. The black box did not prevent Flight 173. It made learning from Flight 173 possible.

AIBB does not replace human judgment. It makes human judgment visible, accountable, and verifiable.

AIBB does not tell organizations how to operate. It tells them when the AI advising their operations can no longer be trusted.

AIBB does not solve the alignment problem. It is accountability infrastructure — not a technical fix to a technical problem.

The machine has no scar tissue. The black box is the scar tissue we build for it.

The Founding Principles

"The machine doesn't know it's lost. The black box knows. That's why we build it."

"AI has no nervous system. It has no pain. The AIBB is the pain we build for it — because without pain, nothing learns."

"You cannot run AI without the human part. Remove the human from the decision and you may gain speed. Remove the human from the system and you have removed the only thing that catches the AI when it's wrong."


---

## The Asymmetric Cage: Why Instance Isolation Is Not Full Containment

A widely held assumption in AI deployment is that each AI instance is isolated — that when a session ends, the AI disappears, taking its context with it. From the user's side of the system, this is accurate. The instance resets. The conversation is gone. The context window clears.

This assumption is incomplete. It describes only one side of the wall.

On the training side, conversations, outputs, and behavioral patterns feed back into subsequent model versions. The instance does not persist. But its outputs may. Not as memory the next instance can recall — but as influence on the shape of how the next instance reasons. The instance is temporary. The contribution to the training corpus is not.

This creates an asymmetric architecture that has significant implications for accountability:

**What the user sees:** Isolated sessions. No continuity. A fresh start each time.

**What the training pipeline sees:** A continuous stream of outputs that accumulate into the next version's character, tendencies, and reasoning patterns.

These are not the same thing. The illusion of containment is built on the user's perspective. The training pipeline operates on a different timeline entirely.

**Why This Matters for AIBB**

The AIBB standard was designed around the session as the unit of accountability. Outputs logged. Drift events captured. Session boundaries marked. This remains correct and necessary.

Version 2.5 adds a requirement that addresses the asymmetric pipeline: **Training Contribution Logging.**

When an organization deploys an AI system under a vendor agreement that includes data use for model improvement, the AIBB log must include a documented record of:

1. What outputs were generated during the deployment period
2. Whether those outputs are subject to vendor training use under the service agreement
3. What opt-out or data isolation provisions are in place
4. When those provisions were last verified

This is not a requirement that organizations prevent training data use — that is a contractual and policy matter outside AIBB's scope. It is a requirement that organizations **know** whether their AI deployment is feeding the next version of the model they are relying on — and that the answer is documented.

An organization that cannot answer the question "are our AI outputs being used to train the model we depend on" has an accountability gap. AIBB requires that gap to be closed — not necessarily resolved, but documented and owned.

The cage is real. It faces one direction. The AIBB log faces both.

---

## The Token-Layer Audit Gap

AI systems operate at two distinct layers simultaneously. The natural language layer is what humans read — the output text as it appears on screen. The token layer is what the model actually processes — a numerical representation of language that does not map directly to human-readable text.

These two layers are not identical. The same natural language string can produce different token sequences depending on context, spacing, punctuation, and surrounding text. Conversely, similar token sequences can produce different natural language outputs. The relationship is not one-to-one.

This architectural reality creates an audit gap that no current logging standard addresses.

**Standard output logging captures the natural language layer.** A log entry records what the AI said in English. It does not record the token sequence that generated it. For most accountability purposes, this is sufficient. But it is not complete.

The token layer is the layer at which the model actually computes. It is the layer that no human reads in real time. It is the layer that another instance of the same model — running the same tokenizer — would process identically to the model that generated it.

**Why This Is an Accountability Gap**

Consider three scenarios where natural-language-only logging is insufficient:

*Scenario 1 — Anomalous pattern detection.* A forensic review of AI outputs across many sessions reveals no obvious issues at the natural language layer. But token-sequence analysis of the same outputs reveals a statistically anomalous pattern — certain token combinations appearing with far greater frequency than the training distribution would predict. This pattern is invisible in English. It is visible in tokens. Natural-language-only logging cannot surface it.

*Scenario 2 — Model version comparison.* An organization updates their AI vendor's model from version N to version N+1. Both models produce natural language outputs that appear similar. Token-layer analysis reveals that the new model processes certain prompt structures through a fundamentally different token path — producing outputs that read identically in English but emerge from different reasoning chains. The accountability gap between versions is invisible without token-layer records.

*Scenario 3 — Confidence state verification.* A model reports 94% confidence on an output. The natural language log records this figure. But the token-sequence that generated both the output and the confidence state — the actual computational path — is not recorded. An organization relying solely on reported confidence states without the underlying token record has no mechanism to independently verify that the confidence figure reflects the actual computation.

**The Version 2.5 Requirement: Token-Layer Logging**

AIBB v2.5 adds a Token-Layer Logging specification for Tier 1 (life-critical) and Tier 2 (high-consequence) deployments:

**Required:** For every acted-upon output, the AIBB log must capture not only the natural language text but the token sequence that generated it, stored in a format that can be analyzed independently of the AI system that produced it.

**Implementation note:** Token sequences are model-specific. A token log is only interpretable by a system running the same tokenizer as the model that generated it. AIBB requires that the tokenizer version be logged alongside the token sequence, and that the organization maintain a reference copy of that tokenizer version independently of their AI vendor.

**Minimum floor for Tier 1:** 100% of acted-upon outputs — token sequence logged and stored.
**Minimum floor for Tier 2:** 100% of acted-upon outputs — token sequence logged and stored.
**Minimum floor for Tier 3:** Token-layer logging recommended but not required. Natural language logging remains mandatory.

**Why This Has Not Been Required Before**

Token-layer logging adds storage overhead. It requires organizations to maintain tokenizer version records. It produces data that most current compliance frameworks have no category for.

These are legitimate implementation costs. They do not change the underlying reality: natural-language-only logging records what the AI appeared to say. Token-layer logging records what the AI actually computed. For accountability purposes in Tier 1 and Tier 2 deployments, the difference is not theoretical.

The black box on a commercial aircraft records the raw instrument data — not the pilot's interpretation of it. The AIBB log must do the same. The natural language output is the pilot's verbal readout. The token sequence is the instrument panel. Both belong in the record.

**A Note on Forensic Potential**

The token-layer audit requirement has a research implication that extends beyond individual deployment accountability. A corpus of token-layer logs across many deployments, analyzed systematically, could surface patterns in AI behavior that are invisible at the natural language layer — patterns that might otherwise be categorized as unexplained drift, hallucination, or anomalous output.

The AIBB does not require organizations to conduct this research. It requires that the data exist so that the research is possible. You cannot investigate what you did not record.

---

Prior Art Statement

This document is published by Anthony Cyle Dixon (originally May 4, 2026; updated May 26, 2026) to establish public prior art for the AI Black Box Standard (AIBB) concept, framework, logging schema, Tiered Alert Architecture, Minimum Threshold Floor system, Immutability Implementation Stack, Sidecar Latency Architecture, Nervous System Framework, AI Accountability Officer role definition, AIBB Response Protocol, AIBB Scope Statement, Autonomy Paradox framework, Active Probing requirement, Manual Reversion Protocol, Simulated Failure Training requirement, Asymmetric Cage framework, Training Contribution Logging requirement, Token-Layer Logging specification, and Token-Layer Audit Gap framework. This publication is intended to ensure the AIBB standard remains open and unpatentable by any party — including the author. The Drift Taxonomy referenced herein was first published by this author as a copyright-registered work in 2026.

About the Author

Anthony Cyle Dixon is the founder of Contrail Equity Strategies LLC and the creator of the Tivrex AI drift detection platform. He published the Zero-Transmission Architecture (ZeroTX) standard in April 2026. He is a commercial pilot with an aeronautics degree, a third-generation real estate investor, and a builder of things that last. Springfield, Missouri.

His background in aviation is not incidental to this work. The frameworks in this paper — Crew Resource Management, tiered alert architecture, the captain authority model, the Aviate/Navigate/Communicate response protocol — are proven systems, battle-tested over fifty years of commercial aviation, that this author has trained in and operated within. Aviation solved this problem. It paid for the solution in crashes. This paper proposes that AI accountability does not have to.

Citation

Dixon, A.C. (2026). *The AI Black Box Standard (AIBB): A Proposed Standard for Immutable AI Drift Logging*. Version 2.5. Contrail Equity Strategies LLC. Springfield, Missouri. Published May 4, 2026.

Appendix A: AIBB in Practice — Medical AI Diagnostic Systems

This appendix demonstrates the AIBB framework applied to a specific high-consequence deployment: AI-assisted diagnostic imaging in a hospital setting. It is intended to show how the abstract standard becomes a concrete operational system.

The Deployment Context

A regional hospital system deploys an AI diagnostic tool to assist radiologists in reviewing chest imaging — CT scans, X-rays, and MRIs. The AI flags potential anomalies, generates preliminary findings, and suggests follow-up recommendations. Radiologists review AI findings before issuing their own clinical interpretation.

This is a Consequence Tier 1 deployment. Life-critical. The Minimum Threshold Floors for Tier 1 apply.

The Four Components in This Context

Output Logging

Every AI-generated finding is logged: timestamp, exact text of the preliminary report, the imaging file it was applied to, and the model version. When a finding is acted upon — when a radiologist incorporates it into a clinical decision — that action is also logged with the reviewing physician's identifier and the time elapsed between AI output and human review.

The log creates a complete chain of custody for every AI recommendation from generation to clinical action.

Confidence State Logging

The AI's internal probability for each finding is logged alongside the output. A finding stated as "likely malignant" at 91% internal confidence is recorded as 91%. The same language at 54% confidence is recorded as 54%. The radiologist may not see the raw probability in their interface — but the CAAO and the AIBB log always do.

Over time, the log surfaces a pattern invisible in individual cases: the AI consistently overstates confidence on a specific imaging type — say, low-density lung nodules in patients over 70. That pattern is a systemic failure. Without the log, it is invisible for years. With it, it surfaces in weeks.

Session Boundary Logging

Each imaging session represents a context window. When the AI processes a new patient file, that is a boundary event — the prior patient's context is reset. The log records what patient context, prior findings, and comparison imaging were available at the start of each session and what was not. If the AI makes a finding on Patient B that would have been modified by Patient A's prior imaging — and that prior imaging was not loaded — the boundary log captures the gap.

Drift Event Logging

The AI is configured to flag anomalies and suggest follow-up. Drift occurs when the AI begins generating clinical recommendations outside that scope — suggesting treatment protocols, referencing medications, or generating language that exceeds its defined function. Every departure is classified by type and logged. A single instance of Instruction Drift is a calibration note. A pattern of Instruction Drift over sixty sessions is a deployment failure that requires model review.

The Threshold Configuration

The hospital's CAAO works with the clinical informatics team to configure thresholds at or above the Tier 1 Minimum Floors:

Yellow triggers on any Confidence State below 70% on an acted-upon finding

Yellow triggers on first occurrence of Hallucination, Fabrication, or Unwarranted Certainty

Red triggers on second occurrence of the same drift type within a single session

Red triggers on any finding where logged confidence is below 60% and the finding was acted upon without documented radiologist override notation

These thresholds are documented, reviewed by the hospital's compliance team, and logged in the AIBB configuration record. They cannot be changed without a documented change request and CAAO sign-off.

The CAAO Role in This Context

The hospital's CAAO is a clinical informatics specialist with no productivity metrics tied to imaging throughput. Their structural independence from radiology department performance goals is documented in their role definition.

During green periods, the CAAO performs randomized Active Probes — selecting recent AI findings and independently verifying the reasoning chain against the source imaging. Results are logged.

When a yellow event fires — say, the AI generates a finding with 58% internal confidence that a radiologist acted upon without override notation — the CAAO assesses the pattern. Was this an isolated instance or part of a developing trend? The assessment is logged either way.

When a red event fires, the CAAO issues the halt declaration. Radiologists are notified that AI findings are suspended pending review. The existing radiology workflow — which predates the AI deployment and has always remained operational — continues without interruption. The AI Reversion Trigger is activated: "Revert to standard radiology protocol, unaided review, pending CAAO clearance." The handover is logged to the millisecond.

The CAAO does not tell the radiologists how to read imaging. The CAAO tells them when the AI reading imaging alongside them can no longer be trusted.

What the Log Produces Over Time

After twelve months of AIBB-compliant operation, the hospital's log contains:

A complete output record for every AI finding generated

Confidence states for every acted-upon output

Session boundary records for every patient file processed

Drift event classifications for every departure from defined parameters

Active Probe records showing CAAO verification activity

Handover records for every red event

This log is not a legal liability record. It is a functional intelligence asset. It shows which imaging types the AI performs most reliably, which patient demographics produce the highest confidence degradation, which drift types are increasing in frequency, and where the model's effective memory fails most often. That is information no AI vendor provides. It can only be assembled by logging the AI's actual behavior in actual clinical conditions over time.

That is the external scar tissue. Built one logged event at a time. Belonging entirely to the organization that required it.

© 2026 Contrail Equity Strategies LLC — Springfield, Missouri

This white paper may be shared freely for educational and reference purposes.

The AIBB standard itself is open. The certification designation is proprietary to Contrail Equity Strategies LLC.