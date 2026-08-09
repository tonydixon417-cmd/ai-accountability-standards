# Reference Stack

This is the smallest runnable proof instrument in the repository. It demonstrates three interfaces:

- `aibb.py` — append-only, hash-chained event records;
- `pil.py` — human-authored rules, scars, and decisions;
- `gateway.py` — risk-tiered action approval.

Run the demo from the repository root:

```bash
python -m reference_stack.demo
python -m unittest reference_stack.test_reference_stack -v
```

This is not production security, a compliance product, or a complete AI agent. It is a concrete starting point for an implementation partner.
