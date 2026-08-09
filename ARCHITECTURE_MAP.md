# Tivrex Architecture Map

## Purpose

Tivrex is an external accountability and continuity architecture for AI systems used in consequential settings.

The architecture does not depend on one model provider or one finished application. It separates the system's state, event record, failure detection, authority boundary, and human oversight so those functions can be inspected and governed independently.

## The system in one view

```text
Human / organization
        |
        | identity, rules, authority, approval
        v
PIL — continuity, corrections, scars, operating context
        |
        | context supplied to the AI interaction
        v
AI model or agent runtime
        |
        | proposal, output, uncertainty, requested action
        v
AIBB — event and accountability record
        |
        +--> Loop Detector — recurring failure and drift patterns
        |
        +--> ZeroTX / Action Gateway — risk and authority boundary
                              |
                              +--> human approval before consequential action

Evaluation protocols and independent review examine the behavior of the full boundary.
```

This diagram is a functional map, not a claim that every box is currently a production service.

## Component map

| Component | Function | Current status |
|---|---|---|
| **PIL — Persistent Identity / Reliability Layer** | Carries human-authored identity, operating rules, corrections, and failure scars across interactions and model resets. | Published standard plus local reference store; tested locally. |
| **AI model / agent runtime** | Generates proposals, answers, classifications, or requested actions. | Supplied by the implementation environment; Tivrex does not replace or retrain the model. |
| **AIBB — AI Black Box** | Records material events, session boundaries, outputs, approvals, and outcomes for later review. | Published standard plus local hash-chained recorder; tested locally. |
| **Loop Detector** | Identifies recurring human-AI failure patterns such as abdication, responsibility diffusion, automation bias, and optimization-driven drift. | Published standard/specification; no complete production engine claimed. |
| **ZeroTX architecture** | Defines controlled data and action boundaries, including limits on external transmission and execution. | Published architecture/specification; broader production deployment remains open. |
| **Action Gateway** | Evaluates requested actions by risk tier and blocks high-risk action without explicit human approval. | Local reference implementation; tested locally. |
| **Human authority boundary** | Separates AI assistance from authorization and preserves responsibility for consequential decisions. | Architectural invariant demonstrated in the local Gateway behavior; organizational deployment remains open. |
| **Ethics Floor / Covenant Warning System** | Defines warning and escalation patterns for ethical or operational boundary conditions. | Published standards/specifications; executable production service not claimed. |
| **Missing CVR** | Defines the reasoning and context record that ordinary output logs do not capture. | Published standard/specification. |
| **Distributed Oversight Model** | Separates accountability roles and reduces dependence on one person or one point of failure. | Published governance model/specification. |
| **AI Preflight Briefing / Type Rating / Check-Ride** | Makes system capability, limitations, operator qualification, and recurrent evaluation visible. | Published standards/specifications. |
| **Early Warning Channel** | Captures operator concerns before they become formal incidents. | Published standard/specification. |
| **External archive and retrieval** | Preserves the longer-term professional record and retrieves relevant history into active context. | Proposed implementation path; production archive/indexing service not claimed. |
| **Independent Observer / Flight Engineer** | Provides a separate review perspective for memory, verification, and system-state checks. | Working hypothesis/prototype direction; no independent production engine claimed. |
| **Evaluation and ablation materials** | Tests whether continuity and accountability interventions change observed behavior, while preserving raw outputs and limitations. | Protocols and benchmark materials exist; independent scoring/review remains open. |

## How the pieces work together

### 1. State before output

The PIL supplies the current operating context: who the human is, what rules apply, what was previously corrected, and which failure scars remain relevant.

### 2. Proposal before authority

The model generates a proposal. A proposal is not automatically an authorized action. The system must preserve that distinction.

### 3. Record before memory fades

AIBB records the material event and relevant approval or outcome data. This creates a reviewable history rather than relying on the model's next answer or a person's recollection.

### 4. Pattern before repetition

The Loop Detector is intended to identify repeated failures across interactions and people—not just isolated bad outputs.

### 5. Gate before consequence

The Action Gateway evaluates the requested action. Higher-risk actions require explicit human approval before execution.

### 6. Review before confidence

Evaluation protocols, independent review, and preserved raw outputs test whether the architecture performs as described. The system is not treated as proven merely because the design is coherent.

## What is operational in the current reference instrument

The local Python reference stack currently demonstrates three interfaces:

- `aibb.py` — append-only, hash-chained event records;
- `pil.py` — human-authored rules, scars, and decisions;
- `gateway.py` — risk-tiered action approval.

The repository test command is:

```bash
python -m unittest reference_stack.test_reference_stack -v
```

The verified repository result is **3 tests passed**: tamper detection, correction persistence, and high-risk action blocking without approval.

## What remains open

The reference instrument is not a production platform. The following remain open implementation or validation work:

- enterprise persistence, retrieval, and indexing;
- production model adapters;
- executable Loop Detector service;
- production ZeroTX deployment boundary;
- security, tenancy, observability, and operations;
- domain-specific compliance and workflow integration;
- independent scoring and technical review of preserved benchmark outputs.

## Architectural boundary

Tivrex provides the architecture, standards, reference instrument, evaluation materials, and transfer documentation. An engineering-capable partner would build the production system and the finished domain application.

**The architecture is intentionally broader than the current reference code. The public status labels keep that difference visible.**
