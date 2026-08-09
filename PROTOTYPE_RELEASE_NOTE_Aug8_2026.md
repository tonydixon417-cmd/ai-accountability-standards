# Tivrex Public Prototype Release Note

**Date:** August 8, 2026
**Status:** Public release package v2.4.0 — committed locally; publication verification pending
**Project:** Tivrex AI Accountability and Continuity Architecture
**Author:** Anthony Cyle Dixon / Tony Dixon
**Organization:** Contrail Equity Strategies LLC

## What this release is

This release candidate makes the Tivrex accountability architecture easier for an outside technical reader to inspect, reproduce, cite, and challenge.

It combines published standards and specifications with a small local Python reference instrument. The package is intentionally conservative: it describes what exists, labels what is proposed, preserves evidence, and identifies the work required for production implementation.

This is not a finished enterprise platform or a claim that AI systems using the architecture are automatically safe.

## What is included

The release candidate includes:

- `START_HERE.md` — five-minute orientation;
- `ARCHITECTURE_MAP.md` — component relationships and status boundaries;
- `REFERENCE_IMPLEMENTATION_AND_TESTS.md` — runnable code and evidence limits;
- `INDEPENDENT_REVIEW_PROTOCOL.md` — repeatable external review method;
- `CITATION_AND_ATTRIBUTION.md` — authorship, citation, DOI, and reuse guidance;
- the `reference_stack/` local Python proof instrument;
- the `EVALUATION/` protocols and preserved evaluation materials;
- the versioned accountability standards and architecture documents;
- the repository README and citation metadata.

## Reference implementation

The local reference stack demonstrates three narrow behaviors:

1. AIBB event records form a hash-linked chain and detect the supplied tampering case.
2. The PIL store preserves a human-authored correction or failure scar during the local process.
3. The Action Gateway blocks a high-risk action above the configured authority boundary unless explicit human approval is supplied.

Run from the repository root:

```bash
python -m reference_stack.demo
python -m unittest reference_stack.test_reference_stack -v
```

The verified current result is:

```text
Ran 3 tests
OK
```

## Evidence boundary

The local tests support only the narrow behaviors they execute. They do not establish that:

- hallucinations are eliminated or reduced by a measured percentage;
- the full Tivrex architecture is implemented;
- the code is production-ready or secure against determined attackers;
- a legal, regulatory, clinical, aviation, financial, or government requirement is satisfied;
- the architecture generalizes across all models, vendors, or domains;
- independent external validation has been completed.

Broader benchmark materials are preserved separately. They require independent scoring and review before being presented as independent validation.

## Current implementation status

**Runnable and locally tested:** AIBB recorder, PIL store, and risk-tiered Action Gateway.

**Published standards/specifications:** Loop Detector, ZeroTX Architecture, Missing CVR, Ethics Floor, oversight models, preflight/type-rating/check-ride standards, and related components.

**Open implementation work:** production persistence and retrieval, model adapters, executable Loop Detector service, enterprise deployment, domain-specific integration, independent scoring, and independent technical review.

## Intended use

The package is intended for:

- technical readers evaluating the architecture;
- implementation partners assessing transfer potential;
- researchers designing reproducible tests;
- organizations considering accountability and continuity requirements for AI deployment;
- reviewers who want to challenge the distinction between a coherent architecture and a demonstrated system.

It is not intended to replace professional legal, regulatory, security, clinical, aviation, or engineering review.

## Review invitation

An independent reviewer should begin with `INDEPENDENT_REVIEW_PROTOCOL.md`, run the local tests from a clean environment, inspect the reference code, and report both supporting and contradictory findings.

A negative or limited result is useful. The purpose of this release candidate is not to manufacture a green score; it is to make the claims and boundaries inspectable.

## Attribution

When reusing the architecture or reference code, cite:

> Dixon, Anthony Cyle. *AI Accountability Standards: An Aviation-Grade Governance Stack for AI Audit Trails, Drift Detection, Human Oversight, and Data Sovereignty*. Version 2.4.0. Zenodo, 2026. DOI: https://doi.org/10.5281/zenodo.21322039.

For the PIL paradigm specifically, cite:

> Dixon, Anthony Cyle. *The PIL Training Layer: Behavioral Conditioning of AI Systems Without Weight Modification*. Zenodo, 2026. DOI: https://doi.org/10.5281/zenodo.21465514.

See `CITATION_AND_ATTRIBUTION.md` for reuse boundaries and component-level attribution.

## Release state

This document records the v2.4.0 public release package prepared on August 8–9, 2026. It does not imply independent review, external acceptance, or production readiness.

Those events should be recorded separately when they occur and verified from the relevant repository, DOI, or review record.
