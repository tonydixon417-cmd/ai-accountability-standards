# PUBLIC VERIFIER — SPECIFICATION VER-1 v0.1
### Anthony Cyle Dixon · October 29, 2026 · working draft
### Companion to INCIDENT_PACKET_SPEC_INC1_v0.1.md

---

## 0. Purpose

A single file a stranger can open on a laptop with no internet connection, drop a packet on, and get one of three verdicts in plain language. No account. No upload. No vendor. Nothing leaves the machine.

**Why this has to be free.** The moment of an incident is the worst moment to be a gatekeeper. A verifier that charges money gets bypassed, distrusted, or replaced by a vendor's own tool. A verifier that is free and open becomes the thing people cite, and citation is the only durable asset in this scenario. The verifier is the wedge precisely because it is not the product.

## 1. Verdicts

Exactly three. No scores, no grades, no percentages.

| Verdict | Meaning |
|---|---|
| **INTACT** | Every hash resolves, the chain is continuous, every anchor verifies, and no published field is unaccounted for. |
| **INTACT WITH GAPS** | The above, plus one or more declared sequence ranges are missing. The gaps are listed with their positions. |
| **FAILED** | At least one hash mismatch, a broken chain, a failing anchor, or content that cannot be reconciled to the committed root. |

A fourth state exists and must be visible: **INCOMPLETE PACKET**, meaning a required member is missing. This is not a failure of integrity, it is a failure to present evidence.

**The verifier never reports a higher verdict than the evidence supports.** No partial credit. No "mostly verified."

## 2. What the verifier checks

1. **Structure.** Required members present, manifest parseable, version recognised.
2. **Canonical re-hash.** Re-canonicalize each event with RFC 8785 and recompute SHA-256. Compare to the recorded `hash`.
3. **Chain continuity.** Each `prev_hash` matches the prior event's `hash`, starting from the genesis constant.
4. **Sequence integrity.** `seq` strictly increasing, no reuse, no reordering.
5. **Anchors.** Verify each RFC 3161 token against its included certificate chain and confirm the message imprint matches the sealed head hash.
6. **Redaction consistency.** Recompute the disclosed subset against the committed Merkle root; confirm every listed redaction corresponds to a committed path.
7. **Gap reconciliation.** Confirm `gaps.json` matches the sequence arithmetic. A gap not listed in `gaps.json` is a FAILED verdict, not a gap.
8. **Report agreement.** Confirm the facts stated in `report.html` (session count, approval counts, review durations, model identifiers) are derivable from `events.jsonl`. A report that contradicts the events is a FAILED verdict.

Item 8 matters more than it looks. It is the check that catches a packet where the prose was written to be persuasive and the data says something else.

## 3. What the verifier does not do

Printed on screen with every verdict, not buried in a readme:

- It does not prove the log is complete. It proves the presented log is unaltered and its gaps are declared.
- It does not prove the events are true. A system can record a lie faithfully and consistently.
- It does not prove the model behaved as recorded, only that the record was not changed after sealing.
- It does not establish who controlled the system at the time.
- It does not substitute for discovery, testimony, or expert examination.

**A verifier that lets a reader believe it proved more than this has done harm.** The limits text is part of the product, and softening it for a customer is disqualifying.

## 4. Interface

Three screens, no navigation.

**Screen one.** Drop target. One line: "This file is checked on your machine. Nothing is uploaded."

**Screen two.** The verdict, in the largest type on the page, one sentence of plain explanation, and the three-line summary: events, sessions, anchors.

**Screen three.** Details, collapsed. Every check with pass or fail and the reason. Then the limits text, always expanded, never behind a click.

Everything renders from the packet itself. No fonts, scripts, or assets fetched from anywhere.

## 5. Durability

A packet must remain verifiable in 2046, when this repository may not exist.

- Single HTML file, inline CSS and JavaScript, no dependencies.
- The hashing and canonicalization logic implemented in the file itself, not imported.
- The packet embeds its own copy of the verifier at the version that validated it.
- No calls to a timestamp authority during verification: the tokens are verified offline against the included certificate chain, with an explicit warning when a certificate has expired but the token predates expiry.

That last point is the difference between a verifier and a subscription. Offline token validation is the hard part and it is worth the work.

## 6. Independent replication

The verifier must be re-implementable by a third party from the specification alone, in any language, and must produce identical verdicts on the same packet. A published corpus of sample packets, at least four:

1. Clean packet.
2. Packet with declared gaps.
3. Packet with one altered byte.
4. Packet with a persuasive report that contradicts its own events.

The fourth is the one that proves the format has teeth. If an independent implementation fails on it, the spec is wrong, not the implementation.

## 7. Trust boundary, stated plainly

The verifier is not a trusted authority. It is a calculator. Its value is that anyone can run it, anyone can re-implement it, and it refuses to say more than it can show. Anyone relying on a packet is relying on the mathematics and on the honesty of the limits page, not on the reputation of the verifier's author.

That is also why the author's name should be on the specification and not on the verdict.
