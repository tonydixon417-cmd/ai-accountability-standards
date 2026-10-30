#!/usr/bin/env python3
"""Publish gate: build a Zenodo/GitHub release archive from an explicit file list,
and refuse to build if anything in it looks like personal, health, family,
commercial-transaction, or credential material.

Usage:
    python3 publish_gate.py --src DIR --out release.zip [--include include.txt] [--force]

No --include means every file is a candidate, which is how the August failure
happened: zipping a working directory and calling it a publication.
"""
import argparse, os, re, sys, zipfile

PATTERNS = [
    (r"\bdiabet\w*", "health"),
    (r"\bAlzheimer\w*", "health"),
    (r"\behrlichios\w*", "health"),
    (r"\bessential[- ]tremor\b", "health"),
    (r"\bICU\b", "health"),
    (r"\bhereditary\b", "health"),
    (r"\bAimee\b|\bPlumlee\b|\bDrummond\b|\bBritton\b", "third-party names"),
    (r"\b68[- ]door\w*", "personal finance"),
    (r"\bBonanza\b", "personal finance"),
    (r"\b\d+\s*doors?\b", "personal finance"),
    (r"[\w.+-]+@[\w-]+\.[\w.]{2,}", "email address"),
    (r"sk_live_|rk_live_|whsec_|ghp_[A-Za-z0-9]{20}|AKIA[0-9A-Z]{16}", "credential"),
    (r"BEGIN [A-Z ]*PRIVATE KEY", "credential"),
    (r"\bconfidential\b|\bacquisition brief\b|strategic buyer|what is for sale|exit structure",
     "transaction material"),
    (r"\b(?:TG|telegram)\s*[:@]", "messaging handle"),
]
TEXT_EXT = {".md", ".txt", ".py", ".json", ".yml", ".yaml", ".cff", ".jsonl", ".csv"}


def scan(path):
    try:
        text = open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        return []
    return [(label, m.group(0)[:40]) for rx, label in PATTERNS for m in re.finditer(rx, text, re.I)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--include")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    if a.include:
        wanted = {l.strip() for l in open(a.include) if l.strip() and not l.startswith("#")}
    else:
        wanted = None

    files, blocked = [], []
    for dp, _, fs in os.walk(a.src):
        if "/.git" in dp or dp.endswith("/.git"):
            continue
        for f in fs:
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, a.src)
            if wanted is not None and rel not in wanted:
                continue
            files.append((p, rel))
            if os.path.splitext(f)[1].lower() in TEXT_EXT:
                for label, hit in scan(p):
                    blocked.append((rel, label, hit))

    print(f"candidates: {len(files)}   flagged: {len(blocked)}")
    by_file = {}
    for rel, label, hit in blocked:
        by_file.setdefault(rel, []).append(f"{label}: {hit}")
    for rel, items in sorted(by_file.items()):
        print(f"  BLOCK {rel} -> {'; '.join(sorted(set(items))[:3])}")

    if blocked and not a.force:
        print("\nREFUSED. Remove or redact the flagged files, or rerun with --force after a written decision.")
        return 2

    with zipfile.ZipFile(a.out, "w", zipfile.ZIP_DEFLATED) as z:
        for p, rel in files:
            z.write(p, os.path.join(os.path.basename(a.out).rsplit(".zip", 1)[0], rel))
    print(f"\nbuilt {a.out} ({os.path.getsize(a.out)} bytes, {len(files)} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
