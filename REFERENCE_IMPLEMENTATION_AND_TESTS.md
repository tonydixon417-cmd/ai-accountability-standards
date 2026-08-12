# Reference Implementation and Tests

**Classification:** Local bounded reference implementation — not enterprise validation.

## Visible implementations

### Root baseline

Path: [`reference_stack/`](./reference_stack/)

The root baseline contains the original AIBB recorder, PIL store, risk-tiered Action Gateway, demonstration script, and three deterministic tests.

```bash
python -m reference_stack.demo
python -m unittest reference_stack.test_reference_stack -v
```

### Crop #1

Path: [`crop_1_expanded/CROP_1_TRANSFER_PACKAGE_Aug10_2026/03_reference_stack/`](./crop_1_expanded/CROP_1_TRANSFER_PACKAGE_Aug10_2026/03_reference_stack/)

Crop #1 extends the baseline with:

- `durable_archive.py` — SQLite-backed continuity storage;
- `model_adapter.py` — OpenAI-compatible HTTP model adapter;
- `live_flight_check.py` — bounded live-model and dry-run evidence runner;
- `flight_check_demo.py` — local flight-check demonstration;
- a fourth deterministic test covering archive survival after reopen.

Run from the repository root:

```bash
cd crop_1_expanded
python -m unittest CROP_1_TRANSFER_PACKAGE_Aug10_2026.03_reference_stack.test_reference_stack -v
```

Expected bounded result: 4 tests pass.

## Preserved evidence

- [`04_evidence/FINAL_CROP1_INTEGRITY_REVIEW_Aug11_2026.md`](./crop_1_expanded/CROP_1_TRANSFER_PACKAGE_Aug10_2026/04_evidence/FINAL_CROP1_INTEGRITY_REVIEW_Aug11_2026.md)
- [`04_evidence/LIVE_MODEL_FLIGHT_CHECK_VERIFICATION_Aug11_2026.md`](./crop_1_expanded/CROP_1_TRANSFER_PACKAGE_Aug10_2026/04_evidence/LIVE_MODEL_FLIGHT_CHECK_VERIFICATION_Aug11_2026.md)
- [`05_evaluation/live_flight_checks/`](./crop_1_expanded/CROP_1_TRANSFER_PACKAGE_Aug10_2026/05_evaluation/live_flight_checks/)
- [`05_evaluation/live_benchmark_C0.json`](./crop_1_expanded/CROP_1_TRANSFER_PACKAGE_Aug10_2026/05_evaluation/live_benchmark_C0.json) through `live_benchmark_C3.json`

The evidence includes a dry run, a transparently preserved failed attempt, a successful bounded live-model run, manifests, raw provider evidence, and C0–C3 raw outputs. It remains internal project evidence until independently reproduced or scored by an outside reviewer.

## Frozen artifact identity

The canonical archive is [`releases/v2.5.1/TIVREX_CROP_1_VERIFIED_Aug11_2026.zip`](./releases/v2.5.1/TIVREX_CROP_1_VERIFIED_Aug11_2026.zip).

SHA-256:

```text
25310c1d827d7a498ebe7f5016ed2d61ea293cc90f53df2570a68fee8d80c752
```

The expanded directory is verified against each member of this ZIP in CI.

## Evidence boundary

The tests demonstrate only the supplied local cases. They do not establish that administrators cannot regenerate an entire chain, that keys are securely managed, that the Gateway cannot be bypassed in a larger system, that retrieval remains reliable under scale or hostile input, or that Tivrex reduces risk generally. Production security, independent validation, deployment, and commercial value remain open.
