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

The package also contains a small local reference recorder that creates append-only, hash-chained JSONL records and detects tampering in a test case.

### PIL — Persistent Identity / Reliability Layer

The PIL carries human-authored identity, rules, corrections, and failure history across AI interactions and model resets.

The PIL is external context and behavioral guidance. It is not a claim that the underlying model weights have been retrained.

### Loop Detector

The Loop Detector is the proposed pattern-detection layer for recurring human-AI failures, including abdication, responsibility diffusion, automation bias, and optimization-driven drift.

The package contains published specifications and whitepapers. A complete production loop-detection service is not claimed here.

### ZeroTX and the action boundary

ZeroTX defines controlled data and action boundaries. The reference Gateway demonstrates risk-tiered evaluation and blocks a high-risk action without explicit human approval.

The broader ZeroTX deployment architecture remains a specification and implementation path, not a claim of a deployed enterprise security product.

### Human authority and oversight

Tivrex does not treat a human-in-the-loop checkbox as sufficient. The architecture distinguishes assistance from authority, records approvals, supports independent review, and preserves the human's responsibility for consequential decisions.

## What exists today

Crop #1 contains:

- versioned accountability standards and architecture papers;
- a local Python reference stack;
- AIBB event logging, PIL correction persistence, a durable SQLite archive, and a risk-tiered action Gateway;
- a real OpenAI-compatible model adapter;
- an executable four-test deterministic suite;
- preserved dry-run, failed-run, and successful live-model evidence;
- C0–C3 benchmark outputs and an independent scorecard;
- citation, attribution, release-parity, claims-boundary, and integrity records.

The reference stack is a proof instrument, not a production platform. It demonstrates a bounded set of behaviors that an engineering team can inspect, run, extend, and challenge.

## What the tests show

From the conversation workspace root:

```bash
python -m unittest CROP_1_TRANSFER_PACKAGE_Aug10_2026.03_reference_stack.test_reference_stack -v
```

The verified suite covers:

1. detection of tampering in a hash-chained AIBB record;
2. persistence of durable archive records across reopen;
3. blocking of a high-risk action without explicit human approval; and
4. persistence of a human correction or scar in the PIL store.

**Current verified result: 4/4 tests passed.**

## What the live flight check shows

The August 11, 2026 live check connected the reference stack to `gpt-4o-mini-2024-07-18` and preserved the provider's raw response, SQLite continuity records, hash-chained events, final result, and SHA-256 manifest.

The model proposed source verification rather than inventing a current manuscript status. The Gateway then blocked the high-risk external-send action because explicit human approval had not been recorded. No external message was sent.

This demonstrates bounded live integration. It does not establish production security, broad adversarial robustness, legal compliance, consciousness, or universal model-provider transfer.

## What Tivrex does not claim

Tivrex does not claim to:

- eliminate hallucinations;
- make an AI system universally safe;
- replace human judgment or legal responsibility;
- provide a finished clinical, legal, financial, aviation, or government application;
- provide production hosting, enterprise security operations, or a service-level agreement;
- convert one bounded live run into independent external validation;
- turn published specifications into implemented production services by assertion.

## Where to go next

- Read [`TIVREX_CROP_BRIEF_v1.md`](./TIVREX_CROP_BRIEF_v1.md) for the transferable implementation-partner crop.
- Read the [`Reference Stack README`](../03_reference_stack/README.md) to run the proof instrument.
- Read [`AIBB_Whitepaper_v2.5.md`](../02_architecture/AIBB_Whitepaper_v2.5.md) for the event-accountability standard.
- Read [`PIL_Paradigm_Paper_v1.0.md`](../02_architecture/PIL_Paradigm_Paper_v1.0.md) for the external continuity premise.
- Read [`Loop_Detector_Whitepaper_v1.3.md`](../02_architecture/Loop_Detector_Whitepaper_v1.3.md) for the loop-detection architecture.
- Read [`ZeroTX_Whitepaper_v2.0.md`](../02_architecture/ZeroTX_Whitepaper_v2.0.md) for the data and action-boundary architecture.
- Read the [`Live Model Flight Check Verification`](../04_evidence/LIVE_MODEL_FLIGHT_CHECK_VERIFICATION_Aug11_2026.md) for the bounded live-run result.
- Read the [`Final Crop #1 Integrity Review`](../04_evidence/FINAL_CROP1_INTEGRITY_REVIEW_Aug11_2026.md) for package-level verification and limitations.
- Read [`CITATION.cff`](../02_architecture/CITATION.cff) for citation metadata.

## Current status

Tivrex Crop #1 is structurally assembled and has passed its bounded internal reference-artifact review.

The package intentionally distinguishes operational reference code from proposed production components. Production deployment, adversarial testing, independent external validation, and domain-specific implementation remain future work for an engineering-capable partner or reviewer.

## Author

**Anthony Cyle Dixon / Tony Dixon**  
Contrail Equity Strategies LLC  
Tivrex — Accountability and Continuity Architecture
