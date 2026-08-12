# Start Here — Tivrex in Five Minutes

## Sixty-second description

Tivrex is a public accountability and continuity architecture for AI systems. It places deterministic controls around nondeterministic models: preserving decision evidence, carrying human-authored corrections and authority state across sessions, separating model proposals from real-world execution, and blocking configured high-risk actions until explicit approval.

This repository contains specifications and a bounded reference implementation. It is **not** a production operating platform.

## Inspect the current implementation

1. Read [`CURRENT_STATUS.md`](./CURRENT_STATUS.md) for the authoritative maturity and claim boundary.
2. Browse the expanded Crop at [`crop_1_expanded/CROP_1_TRANSFER_PACKAGE_Aug10_2026/`](./crop_1_expanded/CROP_1_TRANSFER_PACKAGE_Aug10_2026/).
3. Inspect the current reference code in [`03_reference_stack/`](./crop_1_expanded/CROP_1_TRANSFER_PACKAGE_Aug10_2026/03_reference_stack/).
4. Inspect preserved evidence in [`04_evidence/`](./crop_1_expanded/CROP_1_TRANSFER_PACKAGE_Aug10_2026/04_evidence/) and [`05_evaluation/`](./crop_1_expanded/CROP_1_TRANSFER_PACKAGE_Aug10_2026/05_evaluation/).

The canonical frozen archive is [`releases/v2.5.1/TIVREX_CROP_1_VERIFIED_Aug11_2026.zip`](./releases/v2.5.1/TIVREX_CROP_1_VERIFIED_Aug11_2026.zip), SHA-256 `25310c1d827d7a498ebe7f5016ed2d61ea293cc90f53df2570a68fee8d80c752`.

## Run the tests

Root baseline:

```bash
python -m unittest reference_stack.test_reference_stack -v
```

Expected bounded result: 3 tests pass.

Expanded Crop #1:

```bash
cd crop_1_expanded
python -m unittest CROP_1_TRANSFER_PACKAGE_Aug10_2026.03_reference_stack.test_reference_stack -v
```

Expected bounded result: 4 tests pass.

GitHub Actions runs both suites and verifies that the expanded Crop files match the frozen ZIP.

## What the reference artifact demonstrates

Within its tested local scope, Crop #1 demonstrates:

- hash-chained event recording and detection of the supplied tampering case;
- durable SQLite continuity records surviving process reopen;
- retention and retrieval of a human-authored correction;
- an OpenAI-compatible model adapter and preserved bounded live-model run;
- separation of model proposal from external action execution;
- blocking of a configured high-risk action without explicit approval.

## What it does not demonstrate

It does not establish production security, enterprise deployment, broad adversarial robustness, legal or regulatory compliance, universal safety, general hallucination reduction, independent external validation, commercial value, or buyer demand.

## Architecture map

Read [`ARCHITECTURE_MAP.md`](./ARCHITECTURE_MAP.md) for the component relationships. Read [`REFERENCE_IMPLEMENTATION_AND_TESTS.md`](./REFERENCE_IMPLEMENTATION_AND_TESTS.md) for the code and evidence guide. Read [`INDEPENDENT_REVIEW_PROTOCOL.md`](./INDEPENDENT_REVIEW_PROTOCOL.md) if reproducing or challenging the results.
