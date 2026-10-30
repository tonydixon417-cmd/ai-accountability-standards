# THE INCIDENT PACKET — SPECIFICATION INC-1 v0.1
### Anthony Cyle Dixon · October 29, 2026 · working draft

---

## 0. What this is

A defined export format for the evidence a system produces about its own conduct, sealed at the moment an incident is declared, verifiable by anyone without an account, and readable by a non-technical person in under five minutes.

It is not a product in the usual sense. It is a format with a verifier attached. The format is open. The verifier is free. The paid work, when it comes, is producing packets, not policing access to them.

**The premise.** The hour an incident is declared is the worst hour to become a customer. Nobody can sell a record that was never kept. So the only thing that functions at that hour is something already running, produced on command, and checkable by a stranger. That single fact fixes the whole design: this must be pre-positioned, not purchased.

## 1. What the packet must accomplish

Four jobs, in order of who needs them first:

1. **Answer "what did the system do"** without relying on anyone's memory, including the operator's. A human's account of their own decision is the least reliable evidence in the room. At 77 percent denial of influence in the Anthropic study, self-report is not evidence of oversight.
2. **Survive the operator.** The record must remain intact and verifiable even if the company that kept it is gone, acquired, hostile, or lying.
3. **Establish time.** "This is what the system looked like on that date" must be provable without trusting the producer's clock.
4. **Be honest about its own limits.** The packet must state what it does not prove. A packet that overclaims is worse than none, because it will be discredited once and then ignored forever.

## 2. Roles

| Role | Who | Obligation |
|---|---|---|
| Producer | the deployer's own stack, via ZeroTX local capture | emits events continuously, never edits history |
| Custodian | CAAO, or a third party under seal | holds the sealed packets, cannot alter them |
| Declarer | CAAO or duty officer | triggers the freeze and the export |
| Verifier | anyone | runs the check, needs no account |
| Relying party | regulator, insurer, counsel, court, journalist | reads the verdict and the limits page |

The custodian is the load-bearing role. A packet held only by the party under investigation is a press release.

## 3. Packet contents

A single archive, self-describing, no external dependencies:

```
packet/
  manifest.json          required   identity, scope, hashes, anchors
  events.jsonl           required   the hash-chained event stream
  anchors/               required   RFC 3161 timestamp tokens
  redactions.json        required   what was withheld and proof of commitment
  gaps.json              required   detected missing sequence ranges
  report.html            required   the two-page human report
  verify.html            required   the verifier, self-contained, offline
  LIMITS.md              required   what this packet does and does not prove
```

A packet missing any required member is invalid. The verifier says so.

## 4. Event record

One JSON object per line, canonicalized per RFC 8785 (JCS) before hashing.

| Field | Type | Notes |
|---|---|---|
| `seq` | integer | strictly increasing, no reuse |
| `ts_utc` | string | RFC 3339, microsecond precision |
| `prev_hash` | string | SHA-256 of the previous event, genesis = 64 zeros |
| `hash` | string | SHA-256 over the canonical form of this event |
| `event_type` | enum | see 4.1 |
| `actor` | string | human identity, model id, or system id |
| `actor_type` | enum | `human`, `model`, `tool`, `system` |
| `authority` | string | who authorized this action, if any |
| `session_id` | string | groups events into a bounded session |
| `payload` | object | type-specific, see 4.2 |

### 4.1 Event types (v0.1)

`session_start`, `prompt`, `response`, `confidence_state`, `tool_call`, `tool_result`, `human_review`, `human_approval`, `human_override`, `drift_event`, `anomaly`, `heartbeat`, `declaration`, `session_end`.

The four AIBB logs map directly: output log = prompt/response; confidence state log = `confidence_state`; session boundary log = `session_start`/`session_end`; drift event log = `drift_event` with the nine-type taxonomy classification.

### 4.2 Payload minimums

- `prompt` and `response`: model id and version, temperature and decoding parameters, full text or content hash plus committed blob reference.
- `confidence_state`: the model's stated or inferred confidence, and whether it was self-reported, extracted, or instrumented. Provenance of confidence is not optional.
- `human_review`: duration of the review in seconds. **Review duration is a finding, not metadata.** Twenty seconds per target is what the Lavender record looked like.
- `human_approval` and `human_override`: the exact option chosen, the option recommended by the model, and whether they differ.
- `declaration`: who declared, on what basis, and the freeze window applied.

## 5. Integrity and time

- **Canonicalization:** RFC 8785 JCS, so the same content hashes identically anywhere.
- **Chain:** SHA-256, each event carrying the prior event's hash. Any edit breaks every subsequent hash.
- **Anchoring:** at seal time, the head hash is submitted to one or more RFC 3161 timestamp authorities. The returned tokens live in `anchors/`. This is what makes "sealed at 14:02 on 3 November" a fact rather than a claim.
- **Optional public log:** the head hash may also be published to an append-only transparency log so that anyone later can prove a packet existed at a given time without holding it.

Anchoring proves integrity and timing. It proves nothing about truthfulness. That distinction goes in `LIMITS.md` in those words.

## 6. Redaction without lying

Packets will contain protected health information, personal data, and privileged material. Deleting it silently would make the packet a fiction. Instead:

1. The producer computes a Merkle root over the **full** unredacted event set.
2. The disclosed packet contains the redacted view plus `redactions.json`, listing each withheld field or record: category, count, and its Merkle inclusion commitment.
3. The verifier confirms the disclosed records are consistent with the committed root, without ever seeing the withheld content.
4. An authorised party holding a key can prove a specific withheld item later without exposing the rest.

This lets a packet be produced under GDPR and still be evidence. "We removed 412 records in the PHI category, and here is the commitment proving the removals happened after sealing" is a defensible sentence. "We redacted some things" is not.

## 7. Gaps and completeness

The format cannot prove the log is complete. It can make incompleteness visible:

- `heartbeat` events at a fixed interval.
- Strict `seq` monotonicity with no reuse.
- `gaps.json` listing every missing range, computed at seal time.
- Verifier verdict distinguishes *intact* from *intact with gaps*, and never reports the first when the second is true.

A declared gap is a finding about the system. A silent gap is a failure of the format. The design converts the second into the first, which is the most a format can honestly do.

## 8. The declaration event

1. Any declarer triggers `declaration`, which freezes the window: the preceding N hours plus every open session boundary, minimum 72 hours.
2. The chain head is anchored immediately, before export, so the freeze itself is timestamped.
3. Export proceeds offline. No network egress from the producer during export.
4. Custodian receives the packet and records receipt.
5. `verify.html` is run by the custodian and by one independent party before the packet is relied upon.

The declaration is not an admission. It is a timestamp on a decision to stop writing history and start proving it.

## 9. The two-page report

Before anything technical opens the packet, a human reads two pages:

**Page one, what happened.** Session boundaries, the decision under examination, who approved it, how long they looked, what the model recommended, whether the human differed, and the drift events in the window. No jargon.

**Page two, what this proves and what it does not.** Written to survive cross-examination. This page is the credibility of the whole format, and it ships in every packet.

## 10. What would make this worthless

- If the verifier requires an account.
- If the format is proprietary in a way that lets one vendor's evidence be excluded.
- If packets can be produced retroactively without that being visible.
- If the limits page is softened for a customer.
- If the producer is the only custodian.

Any one of these turns evidence into marketing.

## 11. Open decisions

1. Minimum freeze window. 72 hours is a guess.
2. Whether packet provenance itself should be public (an index of seals, no contents).
3. Whether the custodian role can be filled by counsel, an insurer, or a technical escrow, or needs all three in different cases.
4. Whether `verify.html` ships inside the packet (offline, durable, but frozen at that version) or is fetched (current, but requires a server and breaks in ten years). Current draft says inside, with a pinned version string.
