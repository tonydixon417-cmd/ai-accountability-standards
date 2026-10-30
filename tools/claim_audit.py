#!/usr/bin/env python3
"""Claim audit: no claim ships without a receipt.

The failure this exists to stop: a category check reported as the specific.
"I checked every file against the live secret values" when the check ran with
zero secrets loaded. "I can't publish the version" when the mechanism was never
inspected. Both were fluent, both were false, both reached the operator.

The discipline: while drafting, every factual claim carries an evidence tag
[E1], [E2] in the DRAFT. Each tag resolves to a logged command result. The
auditor refuses the draft if a high-risk claim has no resolving tag, or if a
tag points at a log entry that is missing.

The operator never sees the tags. They see only audited claims.

USAGE
    claim_audit.py log --proves "2.5.3 archive contains no profile file" \
        --method "zipfile namelist grep" --result "profile=False brief=False"

    claim_audit.py audit DRAFT.md [--log LOG]     # exit 1 = do not ship
    claim_audit.py show
    claim_audit.py new                            # start a fresh evidence run
"""
import argparse, json, os, re, sys, datetime

HOME = os.path.expanduser("~")
DEFAULT_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "verify_log.jsonl")
DEFAULT_RUN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "verify_run.txt")

# ---------------------------------------------------------------- claim classes
# (label, regex, severity)  severity: BLOCK = must be evidenced or reworded
CLASSES = [
    ("INABILITY",   r"\b(i can(?:'|no)t|cannot|can not|no way to|not possible|"
                    r"there(?:'|i)s no (?:api|token|route|way)|don(?:'|o)t have access|"
                    r"only (?:you|the owner) can|must be done by)\b", "BLOCK"),
    ("VERIFICATION", r"\b(i (?:checked|verified|ran|confirmed|tested|traced|swept)|"
                    r"verified|confirmed|checked|scanned|zero hits|no matches|"
                    r"0 hits|0 matches|i read|i downloaded)\b", "BLOCK"),
    ("QUANTITY",    r"\b\d+(?:\.\d+)?\s*(?:files?|hits?|matches|values?|records?|"
                    r"versions?|tickets?|weeks?|days?|chars?|characters?|bytes?)\b"
                    r"|\bHTTP \d{3}\b|\b[0-9a-f]{7,40}\b|\b10\.5281/zenodo\.\d+\b", "WARN"),
    ("ABSENCE",     r"\b(no\s+\w[\w\s]{0,30}?(?:leaked|found|exposed|remaining|left|"
                    r"appears?|contains?|shows?|carries)|"
                    r"nothing (?:else )?(?:leaked|remains?|found)|clean of|"
                    r"came back clean|no further action|zero findings)\b", "BLOCK"),
    ("SPECULATION", r"\b(probably|likely|presumably|must have been|i assume|"
                    r"i suspect|scrapers (?:already )?have|no doubt|"
                    r"obviously|clearly they)\b", "WARN"),
    ("CAUSAL",      r"\b(because (?:he|she|they|someone|nobody)|"
                    r"that(?:'|i)s (?:why|how) (?:it|he|she|they)|"
                    r"the reason (?:it|he|she|they)|intended to)\b", "WARN"),
]

TAG = re.compile(r"\[E(\d+)\]")


def log_path(a):
    return a.log or DEFAULT_LOG


def cmd_log(a):
    path = log_path(a)
    entries = []
    if os.path.exists(path):
        with open(path) as f:
            entries = [json.loads(l) for l in f if l.strip()]
    eid = len(entries) + 1
    entry = {
        "id": f"E{eid}",
        "ts": datetime.datetime.now().isoformat(timespec="seconds"),
        "proves": a.proves,
        "method": a.method,
        "result": a.result,
    }
    with open(path, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"logged {entry['id']}: {a.proves}")
    return 0


def load_log(a):
    path = log_path(a)
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        return {json.loads(l)["id"]: json.loads(l) for l in f if l.strip()}


def sentences(text):
    # strip markdown scaffolding, keep prose
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"^#+ .*$", " ", text, flags=re.M)
    parts = re.split(r"(?<=[.!?])\s+|\n{2,}", text)
    return [p.strip() for p in parts if len(p.strip()) > 12]


def cmd_audit(a):
    log = load_log(a)
    try:
        draft = open(a.draft).read()
    except OSError as e:
        print(f"cannot read draft: {e}")
        return 2

    rows, blocked, warned = [], 0, 0
    for s in sentences(draft):
        tags = TAG.findall(s)
        hits = [(lab, sev) for lab, rx, sev in CLASSES if re.search(rx, s, re.I)]
        labels = ",".join(h[0] for h in hits) or "-"

        # 1. any cited receipt must exist, whether or not a class regex fired
        if tags:
            missing = [t for t in tags if f"E{t}" not in log]
            if missing:
                blocked += 1
                rows.append(("BLOCK", labels + ":GHOST",
                             "MISSING " + ",".join("E" + m for m in missing),
                             s[:150].replace("\n", " ")))
            elif hits:
                rows.append(("OK", labels, "OK", s[:150].replace("\n", " ")))
            continue

        # 2. an untagged claim in a risky class
        if not hits:
            continue
        sev = "BLOCK" if any(h[1] == "BLOCK" for h in hits) else "WARN"
        if sev == "BLOCK":
            blocked += 1
        else:
            warned += 1
        rows.append((sev, labels, "NO RECEIPT", s[:150].replace("\n", " ")))

    print(f"draft: {a.draft}   evidence entries available: {len(log)}")
    print(f"{'LEVEL':8} {'CLASS':28} {'RECEIPT':12} CLAIM")
    print("-" * 118)
    for sev, labels, status, s in rows:
        print(f"{sev:8} {labels[:27]:28} {status[:11]:12} {s}")

    print("-" * 118)
    if blocked or warned:
        print(f"REFUSED: {blocked} blocking, {warned} warning. Log a receipt "
              f"(claim_audit.py log --proves ...) or reword the claim so it "
              f"asserts only what was actually run.")
        return 1
    print("PASS: every claim in a risky class carries a resolving receipt.")
    return 0


def cmd_show(a):
    log = load_log(a)
    if not log:
        print("no receipts logged")
        return 0
    for eid in sorted(log, key=lambda x: int(x[1:])):
        e = log[eid]
        print(f"{eid}  {e['ts']}  {e['proves']}")
        print(f"      method: {e['method']}")
        print(f"      result: {e['result'][:200]}")
    return 0


def cmd_new(a):
    path = log_path(a)
    if os.path.exists(path):
        os.remove(path)
    print("evidence run reset")
    return 0


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("log")
    p.add_argument("--proves", required=True)
    p.add_argument("--method", required=True)
    p.add_argument("--result", required=True)
    p.add_argument("--log")
    p.set_defaults(fn=cmd_log)

    p = sub.add_parser("audit")
    p.add_argument("draft")
    p.add_argument("--log")
    p.set_defaults(fn=cmd_audit)

    p = sub.add_parser("show")
    p.add_argument("--log")
    p.set_defaults(fn=cmd_show)

    p = sub.add_parser("new")
    p.add_argument("--log")
    p.set_defaults(fn=cmd_new)

    a = ap.parse_args()
    sys.exit(a.fn(a))


if __name__ == "__main__":
    main()
