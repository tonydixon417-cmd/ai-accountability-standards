# Current Status — Tivrex v2.5.2

**Status date:** August 11, 2026 (America/Chicago)  
**Release classification:** Final bounded reference release / maintenance mode  
**Canonical artifact:** `releases/v2.5.1/TIVREX_CROP_1_VERIFIED_Aug11_2026.zip`  
**SHA-256:** `25310c1d827d7a498ebe7f5016ed2d61ea293cc90f53df2570a68fee8d80c752`

## What Tivrex is

Tivrex is a public accountability and continuity architecture for placing deterministic controls around nondeterministic AI systems. It specifies how to preserve decision evidence, retain corrections and authority state, separate model proposals from external execution, and subject consequential actions to configured approval boundaries.

## What is runnable

Two deliberately bounded reference layers are visible in this repository:

1. `reference_stack/` — the original three-test local baseline covering hash-chain tamper detection, PIL correction retention, and high-risk action blocking.
2. `crop_1_expanded/CROP_1_TRANSFER_PACKAGE_Aug10_2026/03_reference_stack/` — the expanded Crop #1 implementation containing durable SQLite continuity storage, an OpenAI-compatible model adapter, a live-flight-check runner, and a four-test deterministic suite.

Crop #1 also preserves dry-run, failed-run, and successful real-model evidence; raw C0–C3 benchmark outputs; per-run manifests; and the final internal integrity reports. The complete frozen package remains available as the canonical ZIP above.

## Verified bounded results

- Root reference tests: 3/3 passed.
- Crop #1 deterministic tests: 4/4 passed.
- Durable archive reopen: passed in the tested local case.
- Successful bounded live-model run: `gpt-4o-mini-2024-07-18`.
- High-risk external action: blocked pending approval in the tested run.
- External message sent: no.
- Canonical ZIP publication parity: verified across GitHub and Zenodo v2.5.1.

These are internal, bounded reference results. They are not independent external validation.

## What is not implemented or established

Tivrex is not a production platform, hosted service, regulatory certification, or turnkey enterprise deployment. The repository does not establish:

- a production Loop Detector service;
- enterprise authentication, tenancy, scaling, observability, or key management;
- broad adversarial robustness;
- legal, regulatory, clinical, financial, aviation, or security compliance;
- general risk reduction across models and domains;
- market demand, commercial valuation, or buyer adoption;
- independent external technical validation.

## Document precedence

This file is the authoritative current status. Files dated August 8–10, 2026 document earlier release states and may contain historically accurate statements that are now superseded. They are preserved for auditability and are labeled historical rather than rewritten.

The expanded Crop directory is an unchanged extraction of the canonical frozen ZIP. Some internal status files describe the package at intermediate build stages. Those statements remain preserved as part of the artifact history; this file controls current public status.

## Development state

After v2.5.2, active development is frozen unless an outside adopter, reviewer, or implementation partner creates a concrete reason to resume. Bug reports and reproducibility findings may still be recorded. No production-readiness or commercial-success claim is implied.
