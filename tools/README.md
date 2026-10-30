# Two gates

Both tools are small, dependency-free Python 3, and solve problems that anyone
running an AI agent in public eventually hits. Public domain, CC0.

## claim_audit.py — no claim ships without a receipt

An agent writes "I verified all 40 files" and it is fluent, confident, and wrong.
This gate makes that failure visible to the agent instead of the reader.

While drafting, every risky claim in the draft carries an evidence tag. Each tag
resolves to a logged command result. The auditor refuses the draft if a
high-risk claim has no resolving tag, or if a tag points at a log entry that
does not exist.

```bash
python3 claim_audit.py new
python3 claim_audit.py log --proves "archive contains no profile file" \
    --method "zipfile namelist grep" --result "profile=False"
python3 claim_audit.py audit DRAFT.md      # exit 1 = do not ship
```

It matches patterns, not meaning. A claim wearing words outside the class list
passes untouched. It is a speed bump for the fluent lie, not a proof of
truthfulness, and the README says so because the author needed reminding.

## publish_gate.py — build the release from a list, not from a directory

The failure this exists to stop: zipping a working directory, calling it a
publication, and shipping someone's private material inside it.

```bash
python3 publish_gate.py --src DIR --out release.zip --include include.txt
```

No `--include` means every file is a candidate, which is exactly how the mistake
happens. On a hit it refuses to build and names the file and the pattern.

It scans for health data, third-party names, personal finance, email addresses,
credentials, and transaction material. `--force` exists and requires a written
decision, which is the point: overriding it is a documented act, not a reflex.

It has already caught a real leak in this repository's own example packet, which
is the only credential a lint tool needs.

## A note on the gate's own source

Run `publish_gate.py` on itself and it refuses: the credential patterns it
searches for (`sk_live_`, `rk_live_`, `whsec_`) appear literally inside its own
source. Overridden with `--force`, deliberately, once, for that reason. A tool
that contains the patterns it hunts will always flag itself, and pretending
otherwise would have meant weakening the patterns.
