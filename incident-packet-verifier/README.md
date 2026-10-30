# Incident Packet Verifier (INC-1)

**A tamper-evident record format for AI incidents, and a single-file verifier you can open in a browser.**

When an AI system does something consequential, the question after the fact is always the same: *what actually happened, and can we prove it?* Logs are written by the system that failed, kept by the vendor under review, and edited under pressure. There is no equivalent of an aviation black box that an outside party can hold.

This repository is a minimal answer. A packet is a folder of files. A manifest seals it. Anyone with the folder can verify that nothing changed after the fact, without trusting the party that produced it.

## Try it in 30 seconds

1. Download `verifier.html`.
2. Open it in any browser. No install, no build, no network.
3. Drop the `examples/packet` folder on it.

A valid packet prints `INTACT`. Edit one character in `events.jsonl` and drop it again. It prints `FAILED` and tells you which check broke.

## What it checks

| Check | What a failure means |
|---|---|
| Event hashes | A record was edited after it was written |
| Hash chain | Records were removed or reordered |
| Sequence numbers | Events are missing from the sequence |
| Heartbeat gaps | The system went quiet, or stopped logging |
| Companion files | An attachment was swapped |
| Human approvals | A decision in the log has no recorded approval |
| Seal imprint | The manifest does not cover the file you are holding |

## What it does not do

It does not tell you whether the original recording was honest. A packet proves that what you are reading is what was sealed. It cannot prove the sealed thing was complete, or that the system logged everything it did.

It does not stop a party from refusing to produce a packet at all.

It is not a blockchain, not a service, and not a product. It is a file format and a verifier, both in the public domain.

## Repository layout

```
verifier.html          single-file verifier (open in a browser)
spec/                  the packet format and the verifier's requirements
examples/packet/       a valid sample packet, 6 events
tests/test_verifier.mjs  headless test: one valid packet, four tampered
```

## Running the tests

```bash
node tests/test_verifier.mjs
```

Expect one `INTACT`, then four `FAILED` results, each naming the check that caught the tampering.

## License

Public domain. CC0 1.0 Universal. No attribution required, no permission needed.

---

Anthony Cyle Dixon · 30 October 2026
