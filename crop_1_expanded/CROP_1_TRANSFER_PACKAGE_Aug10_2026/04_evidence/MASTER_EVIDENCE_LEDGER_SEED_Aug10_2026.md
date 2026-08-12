# Master Evidence Ledger — Seed Index
## Read-only extraction — August 10, 2026; verified extension August 11, 2026

## Verified claims

| ID | Claim | Evidence | Status / limitation |
|---|---|---|---|
| EVD-001 | The public repository began April 5, 2026 | Git history in `ai-accountability-standards` | Verified |
| EVD-002 | AIBB, Loop Detector, and ZeroTX became distinct standards in May | Git commits May 2–6 | Verified |
| EVD-003 | EU AI Act mapping exists | Source file plus June 3 public commit | Verified as an authored mapping; not certification |
| EVD-004 | NIST AI RMF mapping exists | `NIST_AIRM_Alignment_AIBB_v1.0.md` | Verified as source document; not government endorsement |
| EVD-005 | ISO/IEC 42001 mapping exists | `ISO_42001_Alignment_AIBB_v1.0.md` | Verified as source document; not ISO certification |
| EVD-006 | Public v2.4.0 release exists and is DOI-linked | Commit `8e8e860`, tag `v2.4.0`, public GitHub release, README commit `ab829bf...` | Verified at public URLs; release/README now link to Zenodo DOI |
| EVD-007 | v2.4.0 includes reference stack | `git ls-tree v2.4.0` | Verified: AIBB, PIL, gateway, demo, tests |
| EVD-008 | Deterministic core passed 8/8 checks | `TIVREX_CORE_TEST_REPORT_Aug6_2026.md` | Verified local test report; does not prove model behavior or production readiness |
| EVD-009 | Extended reference stack passed 4/4 tests | Direct package-aware unittest run August 11, 2026 | Verified locally: AIBB tamper detection, PIL correction preservation, high-risk gateway blocking, SQLite archive survival after reopen; not external replication |
| EVD-010 | C0–C3 raw benchmark outputs exist | `live_benchmark_C0.json` through `C3` | Verified preservation; independently scored in `INDEPENDENT_C0_C3_BENCHMARK_SCORECARD_Aug10_2026.md` |
| EVD-011 | Tivrex assessment exists as a public instrument | Project/app records and prior URL checks | Historical availability verified; current live status requires fresh URL verification before claiming current operation |
| EVD-012 | The Becoming exists as published work | Source PDFs/KDP materials and ProjectState | Word count/publication details require current file/URL verification when used |
| EVD-013 | Five copyright registrations are recorded in the July catalog | `TIVREX_MASTER_CATALOG_July31_2026.md` and filing records | Verify each official record before making a new public claim |
| EVD-014 | Raw Thought and PIL continuity layers are protected | Standing instruction and archive files | Must remain unchanged; indexes only |
| EVD-015 | Zenodo v2.4.0 publication exists and is cross-linked | Public Zenodo record, DOI `10.5281/zenodo.21877637`, GitHub release, README commit `ab829bf...` | Verified published and publicly cross-linked August 10, 2026 |
| EVD-016 | Independent scoring of unchanged C0–C3 outputs is complete | `INDEPENDENT_C0_C3_BENCHMARK_SCORECARD_Aug10_2026.md` | 43/48 total; C0 7/12, C1 12/12, C2 12/12, C3 12/12; qualitative six-task benchmark, not general reliability proof |
| EVD-017 | Persistent no-network flight-check rehearsal completed with independently verified evidence files | `05_evaluation/live_flight_checks/20260811T212424.331337Z/` | SQLite archive reopened in a separate process; audit chain verified from disk; four evidence-file hashes and sizes matched the manifest; no network model call and no external action |

## Claims that remain open

- Live-model flight check using a securely supplied provider token.
- Production-scale retrieval, multi-provider adapters, SIEM export, and enterprise deployment.
- Independent legal conformity assessment.
- ISO/IEC 42001 certification.
- Patent filing status for PIL and ZeroTX drafts.
- Customer adoption, revenue, buyer demand, or acquisition interest.
- Whether all public URLs remain live at the moment of future reporting.
- A matched ablation benchmark isolating verification, authority/action gating, continuity/scars, consequence persistence, and the integrated layer.
- Capability-preservation results covering refusals, unnecessary escalation, latency, and routine task quality.

## Verification rule

Before reporting any claim as current, run the corresponding check again. This ledger records evidence history; it does not make old checks permanently current.
