# Tivrex Prototype Release Manifest

**Manifest date:** August 9, 2026
**Release state:** Public release package v2.4.0 — committed locally; publication verification pending
**Repository:** `ai-accountability-standards`
**Baseline commit before this package:** `3166fbb7ab941afd2b1918268c7b569fa5bf9e82`
**Author:** Anthony Cyle Dixon / Tony Dixon
**Organization:** Contrail Equity Strategies LLC

## Release identity

This manifest records the contents and boundaries of the Tivrex v2.4.0 public release package prepared on August 8–9, 2026.

The package is a Git commit, but GitHub publication, Zenodo status, external review, and production deployment remain separate states that must be verified independently.

## Included public-package documents

| File | Purpose | Status |
|---|---|---|
| `START_HERE.md` | Five-minute orientation | Complete |
| `ARCHITECTURE_MAP.md` | Component relationships and boundaries | Complete |
| `REFERENCE_IMPLEMENTATION_AND_TESTS.md` | Runnable code description and test evidence | Complete |
| `INDEPENDENT_REVIEW_PROTOCOL.md` | External review and reporting method | Complete |
| `CITATION_AND_ATTRIBUTION.md` | Citation, authorship, DOI, and reuse guidance | Complete |
| `PROTOTYPE_RELEASE_NOTE_Aug8_2026.md` | Scope and limitations of this release candidate | Complete |
| `RELEASE_MANIFEST_Aug8_2026.md` | Inventory and release-state record | This file |

## Existing repository materials included in the candidate

- `README.md` — conservatively updated with the new entry point, implementation status, qualified architecture language, and AIBB v2.5 correction;
- `CITATION.cff` — existing machine-readable citation metadata;
- `reference_stack/` — local Python reference instrument;
- `EVALUATION/` — ablation protocol, evaluation cases, regression case, and evaluation guidance;
- versioned standards and architecture documents, including AIBB v2.5, Loop Detector, ZeroTX, PIL, Missing CVR, and Ethics Floor materials;
- existing publication, DOI, book, and assessment links already present in the repository.

## Runnable evidence

The reference test command is:

```bash
python -m unittest reference_stack.test_reference_stack -v
```

Verified result on August 8, 2026:

```text
Ran 3 tests
OK
```

The three tests cover:

1. AIBB hash-chain tamper detection;
2. PIL correction persistence;
3. high-risk Action Gateway blocking without explicit human approval.

This is local reference evidence only. It is not independent validation of the full architecture.

## Status classification

### Demonstrated locally

- AIBB event recording and local tamper detection;
- PIL rules, scars, and decisions retained in the local store;
- risk-tiered action evaluation and explicit approval behavior;
- the three-test reference suite passes.

### Published or documented specifications

- AIBB;
- PIL and PIL Training Layer;
- Loop Detector;
- ZeroTX Architecture and deployment tiers;
- Missing CVR;
- Ethics Floor / Covenant Warning System;
- AI Preflight Briefing, Type Rating, and Check-Ride concepts;
- CAAO and Distributed Oversight models;
- Early Warning Channel;
- related implementation and evaluation protocols.

### Open or not yet demonstrated

- production persistence, retrieval, and indexing;
- model-provider adapters;
- executable production Loop Detector service;
- enterprise ZeroTX deployment;
- security operations, tenancy, and observability;
- independent scoring of preserved benchmark outputs;
- independent technical review;
- domain-specific implementation and validation;
- claims of legal, regulatory, clinical, aviation, or financial compliance.

## Evidence and attribution boundaries

The package must not be described as:

- a finished enterprise product;
- a universal safety solution;
- a guarantee against hallucination or drift;
- independently validated before the review is completed;
- patent-pending or legally compliant without the relevant verified records;
- a replacement for human responsibility or professional review.

Use `CITATION_AND_ATTRIBUTION.md` for the canonical repository and PIL paradigm citations.

## Excluded or private materials

Private patent drafts, filing checklists, personal archives, private database exports, credentials, and withheld implementation details are not part of this public release candidate.

Their existence or status must not be inferred from this manifest.

## Pre-publication checklist

Before publishing this release:

- [ ] review all README links and public URLs;
- [ ] inspect the complete Git diff;
- [ ] remove generated caches such as `__pycache__/` from the release set;
- [ ] run the reference test suite from a clean environment;
- [ ] confirm the intended release version and date;
- [ ] confirm DOI and citation metadata;
- [ ] preserve benchmark raw outputs unchanged;
- [ ] obtain or schedule independent technical review;
- [x] commit and tag after the contents are approved;
- [ ] verify the public repository and release URL after publication.

## Current release decision

The package is structurally coherent enough for public release. Independent technical review, external acceptance, production implementation, and domain-specific validation remain open and are not implied by this release.
