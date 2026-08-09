# Citation and Attribution

## Canonical project identity

**Project:** AI Accountability Standards / Tivrex
**Author:** Anthony Cyle Dixon
**Public name:** Tony Dixon
**Organization:** Contrail Equity Strategies LLC
**Repository:** <https://github.com/tonydixon417-cmd/ai-accountability-standards>
**License listed in `CITATION.cff`:** CC-BY-4.0

Use **Anthony Cyle Dixon** for formal citation, authorship, and legal or archival records. Use **Tony Dixon** for public-facing biography and ordinary communications.

## Recommended repository citation

Dixon, Anthony Cyle. *AI Accountability Standards: An Aviation-Grade Governance Stack for AI Audit Trails, Drift Detection, Human Oversight, and Data Sovereignty*. Version 2.4.0. Zenodo, 2026. DOI: <https://doi.org/10.5281/zenodo.21322039>.

The repository's `CITATION.cff` file is the machine-readable citation source for this release.

## Preferred citation for the PIL paradigm paper

Dixon, Anthony Cyle. *The PIL Training Layer: Behavioral Conditioning of AI Systems Without Weight Modification*. Zenodo, 2026. DOI: <https://doi.org/10.5281/zenodo.21465514>.

Use this citation when referring specifically to the PIL paradigm or the claim that external behavioral conditioning can shape interaction behavior without modifying model weights.

## Suggested short attribution

> Tivrex AI accountability architecture by Anthony Cyle Dixon, Contrail Equity Strategies LLC. See the canonical repository and DOI record for version and source materials.

## Suggested attribution when reusing a component

> This work uses [component name] from the Tivrex AI Accountability Standards architecture by Anthony Cyle Dixon, Contrail Equity Strategies LLC. Source: [repository URL or DOI]. Licensed under the terms stated in the repository release.

Include the specific component, version, source URL, DOI where applicable, and any modifications made.

## Component naming

The public architecture may refer to these named components:

- AI Black Box Standard (AIBB);
- Loop Detector;
- ZeroTX Architecture;
- Persistent Identity Layer (PIL);
- Missing CVR;
- Ethics Floor / Covenant Warning System;
- AI Preflight Briefing Standard;
- AI Type Rating Framework;
- Chief AI Accountability Officer (CAAO) role;
- Distributed Oversight Model;
- Early Warning Channel;
- ZeroTX Deployment Tiers;
- Check-Ride Protocol;
- Tivrex Core reference stack.

Named components should not be described as independently validated, production-deployed, or regulatory-certified unless a separate source specifically establishes that status.

## Reference implementation attribution

The local reference stack is part of the Tivrex public repository and contains the following interfaces:

- `reference_stack/aibb.py` — local AIBB event recorder;
- `reference_stack/pil.py` — local PIL correction/scar store;
- `reference_stack/gateway.py` — local risk-tiered Action Gateway.

The current repository test suite verifies three local behaviors: hash-chain tamper detection, correction persistence, and high-risk action blocking without explicit human approval.

## Related public materials

- Canonical repository: <https://github.com/tonydixon417-cmd/ai-accountability-standards>
- Repository DOI: <https://doi.org/10.5281/zenodo.21322039>
- PIL paradigm DOI: <https://doi.org/10.5281/zenodo.21465514>
- Tivrex AI Accountability Assessment: <https://tivrex-flight-check.base44.app>
- *The Becoming* companion book: <https://www.amazon.com/dp/B0H9CX7CQ7>

The assessment application and companion book are related public materials. They are not substitutes for the technical repository or evidence package.

## Authorship and reuse boundaries

Attribution does not imply that the author has reviewed, approved, certified, or is responsible for a third party's implementation. A reuse notice should identify modifications and should not present a derivative deployment as the original Tivrex reference implementation.

The architecture, whitepapers, local reference code, assessment application, book, and external publication records are separate assets. Cite the particular asset being used.

Do not state that a component is patented, patent-pending, legally compliant, or independently validated unless the relevant filing, legal review, compliance assessment, or independent report is available and specifically supports that statement.

## Metadata reconciliation notes

The repository currently contains older metadata that should be reconciled during the README cleanup pass:

- `CITATION.cff` identifies the release as version 2.4.0 and dates it August 9, 2026.
- The README's paper table still lists AIBB as v2.4 even though `AIBB_Whitepaper_v2.5.md` is present in the repository.
- The current local repository commit inspected for this document is `3166fbb7ab941afd2b1918268c7b569fa5bf9e82`, dated July 25, 2026.

These are editorial/version-control reconciliation items, not grounds for inventing a new version number. Resolve them in the README and release manifest after checking the canonical release records.

## Citation status

- Citation file present: yes.
- Repository DOI recorded: yes.
- PIL paradigm DOI recorded: yes.
- Author and organization identified: yes.
- Reuse license recorded in `CITATION.cff`: CC-BY-4.0.
- Independent validation citation: not available yet.
- Production deployment citation: not available yet.
