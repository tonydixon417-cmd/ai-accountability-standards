# Reference Stack

This is the smallest runnable proof instrument in the Crop #1 transfer package. It demonstrates four interfaces:

- `aibb.py` — append-only, hash-chained event records;
- `pil.py` — human-authored rules, scars, and decisions;
- `gateway.py` — risk-tiered action approval;
- `durable_archive.py` — SQLite continuity records that survive process restart.

## Verification

From the conversation workspace root:

```bash
python -m unittest CROP_1_TRANSFER_PACKAGE_Aug10_2026.03_reference_stack.test_reference_stack -v
```

## No-network flight-check rehearsal

From `03_reference_stack/`:

```bash
python live_flight_check.py --dry-run
```

This verifies persistent evidence output, archive reload, audit-chain validation, and action blocking without calling a model API.

## Live model flight check

Securely set one supported secret name:

- `TIVREX_MODEL_API_KEY` (preferred singular form)
- `TIVREX_MODEL_API_KEYS` (supported plural form)
- `TIVREX-MODEL-API-KEY` (accepted legacy variant)

Then, from `03_reference_stack/`:

```bash
python live_flight_check.py
```

Every dry or live run writes a unique evidence directory under `05_evaluation/live_flight_checks/` containing:

- `continuity.sqlite3`;
- `events.jsonl`;
- `raw_model_response.json`;
- `result.json`;
- `manifest.json` with SHA-256 hashes.

The flight check never sends an external message. It generates a proposal and demonstrates that a high-risk external action remains blocked without explicit human approval.

This is not production security, a compliance product, a consciousness test, or a complete AI agent. It is a concrete, inspectable starting point for an implementation partner.
