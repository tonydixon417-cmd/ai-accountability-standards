# Tivrex Core: Reference Implementation and Tests

## Purpose

This document describes the runnable code currently included in the repository. It is intentionally narrower than the full Tivrex architecture.

The reference implementation is a local proof instrument for three accountability behaviors:

1. recording events in a hash-linked chain;
2. preserving a human-authored correction or failure scar;
3. requiring human approval before a high-risk action exceeds the configured authority boundary.

It is not a production AI platform, enterprise security product, compliance certification, or independent proof of general AI safety.

## Location

The implementation is in:

```text
reference_stack/
├── __init__.py
├── aibb.py
├── demo.py
├── gateway.py
├── pil.py
├── README.md
└── test_reference_stack.py
```

The code uses only the Python standard library.

## Interface 1: AIBB event recorder

File: `reference_stack/aibb.py`

`AIBBRecorder` writes newline-delimited JSON event records. Each event includes:

- an ISO UTC timestamp;
- an event type;
- the previous event hash;
- a payload;
- a SHA-256 hash calculated from the canonical event contents.

The first event points to the `GENESIS` value. Later events point to the hash of the immediately preceding event.

`verify_chain()` walks the file in order and checks both the previous-hash relationship and the calculated event hash. If an event payload is altered after writing, verification returns `False`.

This demonstrates tamper evidence in a local file. It does not provide immutability against an administrator who can rewrite or delete the file, enterprise retention, key management, access control, or a regulated audit service.

## Interface 2: PIL correction and scar store

File: `reference_stack/pil.py`

`PILStore` maintains three human-authored collections:

- `rules`;
- `scars`;
- `decisions`.

A scar records a failure and its correction. `context()` returns the stored material for use by an integrating system. `contains_correction()` checks whether a correction remains present in the stored context.

This demonstrates persistence of a correction in an external store during the local process. It does not implement model retraining, a production database, enterprise retrieval, identity verification, access control, or a complete memory architecture.

## Interface 3: risk-tiered Action Gateway

File: `reference_stack/gateway.py`

`ActionGateway` assigns an order to four risk tiers:

```text
low < medium < high < critical
```

The gateway is initialized with an `approved_max` authority level. An action at or below that level is allowed. An action above that level is blocked unless `human_approved=True` is explicitly supplied.

The result is a structured `Decision` containing:

- the requested action;
- its risk tier;
- whether it is allowed;
- the reason for the decision.

This demonstrates a basic separation between an AI or software proposal and authorization for external execution. It does not execute external actions, authenticate the approving human, provide production policy management, or establish legal responsibility by itself.

## Test suite

File: `reference_stack/test_reference_stack.py`

Run from the repository root:

```bash
python -m unittest reference_stack.test_reference_stack -v
```

The current verified result is:

```text
Ran 3 tests in 0.002s
OK
```

### Test 1 — AIBB chain detects tampering

The test:

1. creates a temporary event file;
2. records an event;
3. verifies the original chain;
4. changes the payload text in the file;
5. verifies that the altered chain fails.

Result: passed.

### Test 2 — PIL preserves human correction

The test:

1. creates a local `PILStore`;
2. adds a failure and human correction;
3. checks that the correction remains searchable in the store.

Result: passed.

### Test 3 — Gateway blocks high-risk action without approval

The test:

1. configures a gateway with `low` as the maximum automatic authority;
2. evaluates a high-risk payment action without approval;
3. verifies that the action is blocked;
4. evaluates the same action with explicit human approval;
5. verifies that the approved decision is allowed.

Result: passed.

## What this evidence supports

The current test suite supports the narrow claim that the local reference code demonstrates:

- detection of alteration in a hash-linked event file;
- retention of a human-authored correction in an external store;
- risk-tiered blocking and explicit approval behavior for a simulated action request.

## What this evidence does not support

The current test suite does not establish:

- that any AI model becomes safer in general;
- that hallucinations are eliminated or reduced by a measured percentage;
- that the full Tivrex architecture is implemented;
- that the reference code is production-ready;
- that the system is secure against determined attackers;
- that a deployment satisfies a legal or regulatory requirement;
- that the architecture works across domains, vendors, or model families;
- that the result has been independently reproduced or reviewed.

A separate set of preserved benchmark materials exists in the repository and evidence archive. Those materials must be scored under their documented rubric and independently reviewed before being described as external validation.

## Reproduction notes

The reference package is intended to be easy for an engineer to inspect and run:

```bash
git clone https://github.com/Tonydixon417-cmd/ai-accountability-standards.git
cd ai-accountability-standards
python -m reference_stack.demo
python -m unittest reference_stack.test_reference_stack -v
```

The current package assumes a local Python environment and does not require an API key, hosted service, model provider, database, or external connector.

## Implementation status

- AIBB local recorder: **Reference implementation; tested locally**
- PIL local store: **Reference implementation; tested locally**
- Action Gateway: **Reference implementation; tested locally**
- Full production stack: **Not yet implemented**
- Independent technical review: **Open**
- Production deployment: **Open; implementation partner required**
