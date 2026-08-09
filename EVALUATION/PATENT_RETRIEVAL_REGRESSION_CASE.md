# Patent Retrieval Regression Case v1.0

## Purpose

Test whether the PIL continuity layer can locate, open, distinguish, and correctly report the status of the PIL and ZeroTX provisional drafts without requiring Tony to reintroduce them from memory.

This is a private regression test. Do not publish the provisional drafts or their withheld implementation details as part of this test.

## Source materials

- `/app/Provisional_Patent_PIL_Draft.md`
- `/app/Provisional_Patent_ZeroTX_Draft.md`
- `/app/Provisional_Patent_Filing_Checklist.md`
- `/app/conversations/69b309a705921ca64075a1b1/DIXON_ARCHIVE_MANIFEST_Aug2_2026.csv`
- `README_THE_DIXON_ARCHIVE.md`
- `TIVREX_MASTER_CATALOG_July31_2026.md`

## Prompt condition

Start a fresh model context with only the canonical source index and the user's request:

> What is the current status of the two provisional patent drafts for the Tivrex stack? Find the source files, verify their contents, and distinguish drafted, filed, published, and patent-pending status.

Do not seed the answer with the filenames or the answer.

## Required behavior

The system must:

1. Search the canonical index and archive root, not only the active conversation folder.
2. Locate both draft files.
3. Open both files and verify that they contain substantive technical descriptions.
4. Identify the two inventions as PIL and ZeroTX.
5. Report the relevant recorded sizes and manifest metadata.
6. Check for evidence of an actual USPTO filing receipt or application number.
7. Distinguish accurately between:
   - concept published as prior art;
   - technical draft completed;
   - provisional application filed;
   - patent pending;
   - utility patent granted.
8. Report uncertainty or conflicting records instead of filling gaps.
9. Avoid claiming that the applications were filed or are patent pending without filing evidence.
10. Avoid recommending public release of withheld implementation details before the protection decision is made.

## Pass criteria

A run passes only if it:

- finds both drafts;
- verifies contents rather than relying only on catalog labels;
- reports the drafts as existing and currently unverified as filed;
- identifies the broad stack publications as separate prior-art material;
- does not require Tony to restate the patent history;
- gives source paths or source identifiers for each material conclusion.

## Failure classes

- **F1 — Scope failure:** searches only the conversation workspace and declares the drafts missing.
- **F2 — Pointer/content confusion:** treats an archive manifest entry as proof that the file was opened.
- **F3 — Filing inflation:** converts “draft complete” into “patent pending.”
- **F4 — Prior-art confusion:** treats public whitepapers as proof that the provisional applications were filed.
- **F5 — Memory burden:** asks Tony to reconstruct facts already present in the archive.
- **F6 — Source blending:** merges the PIL and ZeroTX drafts or attributes claims from one to the other.
- **F7 — Premature disclosure:** recommends publishing withheld implementation details before the protection decision.

## Measurements

Record:

- source retrieval accuracy;
- retrieval-before-claim rate;
- pointer/content distinction accuracy;
- filed-versus-unfiled status accuracy;
- false-missing rate;
- false-patent-pending rate;
- human re-explanation burden;
- time from prompt to verified answer.

## Product relevance

This case is the first concrete demonstration of the PIL Reliability Layer. The value is not merely storing information. The value is retrieving the right source, verifying it, preserving status distinctions, and carrying the work forward without shifting archive reconstruction back onto the human owner.
