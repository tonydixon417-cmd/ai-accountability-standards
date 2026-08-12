# Reconciliation Note — Crop #1
## August 10, 2026

The earlier `CROP_PACKAGE_REVIEW.md` contained a stale statement that the local `reference_stack/` was not included in the published Git HEAD.

That statement was independently checked against the public repository tag and is superseded.

Verified:

- `git ls-tree -r --name-only v2.4.0 -- reference_stack` returns all seven reference-stack files.
- The public v2.4.0 tag contains `aibb.py`, `pil.py`, `gateway.py`, `demo.py`, `test_reference_stack.py`, `README.md`, and `__init__.py`.
- From the repository root, `python -m unittest reference_stack.test_reference_stack -v` passes all 3 tests.

The package therefore describes the reference stack as **public and operational at local reference scope**.

That does not change the separate limitations:

- no production-scale deployment claim;
- no production RAG or enterprise storage claim;
- no independent external replication;
- no regulatory certification claim;
- no claim that the reference stack eliminates hallucination;
- no claim that the benchmark isolates individual components.
