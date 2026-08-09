# Start Here: Tivrex in Five Minutes

## What is Tivrex?

Tivrex is an external accountability and continuity architecture for AI systems.

It records what an AI proposes, separates proposals from authorized actions, preserves verification and failure history, detects repeated loops, and keeps human authority visible around consequential use.

Tivrex is designed for organizations building or deploying AI that can affect people, assets, safety, law, finances, professional judgment, or long-term institutional work.

## The problem

AI systems can be capable and still be difficult to govern. They may:

- produce confident answers without a durable record of how the answer was formed;
- lose corrections, rules, and prior failures when context resets;
- repeat the same failure through a person-and-system feedback loop;
- blur the boundary between assisting a human and acting on the human's behalf;
- make it difficult to determine what the system proposed, what a person approved, and what actually happened.

Tivrex treats these as system-design problems, not merely model-quality problems.

## The architecture in one sentence

**Preserve state, record events, detect drift and loops, govern authority, and keep a human responsible for consequential action.**

## The oracle problem

A capable AI can become an oracle without being conscious or metaphysically authoritative. Fluency, speed, apparent breadth, and human deference are enough. The failure occurs when people treat the answer as the final source of what is true, right, or to be done.

Tivrex responds with accountable integration, not simulated humanity: visible records, carried-forward corrections, bounded action authority, drift detection, and a named human responsible for consequential decisions.

## The main components

### AIBB — AI Black Box

AIBB is the event-accountability layer. It defines records for material AI events, session boundaries, output states, approvals, and outcomes.

The repository also contains a small local reference recorder that creates append-only, hash-chained JSONL records and detects tampering in a test case.

### PIL — Persistent Identity / Reliability Layer

The PIL carries human-authored identity, rules, corrections, and failure history across AI interactions and model resets.

The PIL is external context and behavioral guidance. It is not a claim that the underlying model weights have been retrained.

### Loop Detector

The Loop Detector is the proposed pattern-detection layer for recurring human-AI failures, including abdication, responsibility diffusion, automation bias, and optimization-driven drift.

The repository contains published specifications and whitepapers. A complete production loop-detection service is not claimed here.

### ZeroTX and the action boundary

ZeroTX defines controlled data and action boundaries. The reference Gateway demonstrates risk-tiered evaluation and blocks a high-risk action without explicit human approval.

The broader ZeroTX deployment architecture remains a specification and implementation path, not a claim of a deployed enterprise security product.

### Human authority and oversight

Tivrex does not treat a human-in-the-loop checkbox as sufficient. The architecture distinguishes assistance from authority, records approvals, supports independent review, and preserves the human's responsibility for consequential decisions.

## What exists today

The public repository contains:

- versioned accountability standards and architecture papers;
- a local Python reference stack;
- AIBB event logging, PIL correction persistence, and a risk-tiered action Gateway;
- an executable local test suite;
- evaluation protocols and preserved benchmark materials;
- citation and publication records;
- documentation for implementation partners.

The local reference stack is a proof instrument, not a production platform. It demonstrates a small set of concrete behaviors that an engineering team can inspect, run, extend, and challenge.

## What the local tests show

Run from the repository root:

```bash
python -m unittest reference_stack.test_reference_stack -v
```

The current repository test suite covers:

1. detection of tampering in a hash-chained AIBB record;
2. persistence of a human correction or scar in the PIL store;
3. blocking of a high-risk action without explicit human approval.

The current verified repository result is **3 tests passed**. Broader benchmark materials are preserved separately and must not be treated as independent validation until they have been scored and reviewed.

## What Tivrex does not claim

Tivrex does not claim to:

- eliminate hallucinations;
- make an AI system universally safe;
- replace human judgment or legal responsibility;
- provide a finished clinical, legal, financial, aviation, or government application;
- provide production hosting, enterprise security operations, or a service-level agreement;
- have independent external validation before that review is completed;
- turn published specifications into implemented services by assertion.

## Where to go next

- Read [`TIVREX_CROP_BRIEF_v1.md`](./TIVREX_CROP_BRIEF_v1.md) for the transferable implementation-partner crop.
- Read [`reference_stack/README.md`](./reference_stack/README.md) to run the local proof instrument.
- Read [`AIBB_Whitepaper_v2.5.md`](./AIBB_Whitepaper_v2.5.md) for the event-accountability standard.
- Read [`PIL_Paradigm_Paper_v1.0.md`](./PIL_Paradigm_Paper_v1.0.md) for the external continuity/training-layer premise.
- Read [`Loop_Detector_Whitepaper_v1.3.md`](./Loop_Detector_Whitepaper_v1.3.md) for the proposed loop-detection architecture.
- Read [`ZeroTX_Whitepaper_v2.0.md`](./ZeroTX_Whitepaper_v2.0.md) for the data and action-boundary architecture.
- Read [`CITATION.cff`](./CITATION.cff) for citation metadata.

## Current status

Tivrex is a public architecture and reference-package release in progress.

The first release pass is intentionally conservative: describe what exists, label what is proposed, preserve the evidence, and invite independent technical review. Production deployment and domain-specific implementation remain the work of an engineering-capable partner.

## Author

**Anthony Cyle Dixon / Tony Dixon**
Contrail Equity Strategies LLC
Tivrex — Accountability and Continuity Architecture
