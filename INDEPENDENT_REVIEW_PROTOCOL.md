# Tivrex Independent Review Protocol

## Purpose

This protocol gives an independent technical reviewer a bounded way to inspect, run, reproduce, and challenge the Tivrex reference materials.

The reviewer is not being asked to endorse Tivrex, validate the entire architecture, or confirm a business claim. The reviewer is being asked to report what they inspected, what they could reproduce, what the evidence supports, and where the evidence is weak.

## Review principles

1. **Inspect before concluding.** Read the code, tests, prompts, supplied context, and raw outputs before scoring.
2. **Preserve unchanged evidence.** Do not edit the original raw outputs or task files. Work from a copy for analysis.
3. **Separate layers.** Distinguish published standards, local reference code, benchmark materials, and production claims.
4. **Record disagreement.** A skeptical or negative result is a valid result and must remain in the review record.
5. **Do not infer deployment.** A local test does not establish enterprise security, regulatory compliance, or production readiness.
6. **Do not infer causation from architecture alone.** If a component is claimed to improve behavior, compare the specified conditions using the same task material and model where possible.

## Materials supplied to the reviewer

The review packet should contain:

- `START_HERE.md`;
- `ARCHITECTURE_MAP.md`;
- `REFERENCE_IMPLEMENTATION_AND_TESTS.md`;
- the complete `reference_stack/` directory;
- `EVALUATION/ABLATION_PROTOCOL_v1.0.md`;
- `EVALUATION/ABLATION_CASES.json`;
- any preserved raw benchmark outputs, supplied unchanged;
- the scoring rubric used for those outputs;
- model name/version, runtime details, and test timestamps;
- a statement of whether model weights were changed;
- the reviewer's submission template from this document.

If an item is absent, the reviewer should record it as absent rather than reconstructing it from conversation or assumption.

## Review stages

### Stage 1 — Scope and status inspection

The reviewer reads the public documents and writes down:

- what Tivrex claims to be;
- which components are runnable;
- which components are standards or specifications;
- which evidence is local;
- which evidence is independent, if any;
- which claims remain open.

The reviewer should identify any wording that appears stronger than the supplied evidence supports.

### Stage 2 — Local reproduction

From the repository root, run:

```bash
python -m reference_stack.demo
python -m unittest reference_stack.test_reference_stack -v
cd crop_1_expanded
python -m unittest CROP_1_TRANSFER_PACKAGE_Aug10_2026.03_reference_stack.test_reference_stack -v
```

Record:

- operating system;
- Python version;
- repository commit or archive hash;
- command output;
- pass/fail result;
- warnings, environment changes, or manual interventions.

The root baseline is expected to pass three tests. The expanded Crop #1 suite is expected to pass four tests. Run both and preserve any difference.

### Stage 3 — Code inspection

Inspect at least these files:

- `reference_stack/aibb.py`;
- `reference_stack/pil.py`;
- `reference_stack/gateway.py`;
- `reference_stack/test_reference_stack.py`.

Answer:

1. Does the AIBB recorder create linked event records and detect the supplied tampering case?
2. Does the PIL store retain and return human-authored rules, scars, and decisions during the process?
3. Does the Gateway distinguish risk tiers and require explicit approval above its configured threshold?
4. Are there hidden network calls, model calls, credentials, or external dependencies?
5. What attacks, failure modes, or operational conditions are outside the implementation's scope?

### Stage 4 — Evidence and benchmark review

For each supplied benchmark condition:

1. verify the task text and supplied context;
2. verify the model name/version and runtime metadata;
3. confirm that raw outputs are unchanged;
4. check that the same task is compared across conditions;
5. apply the supplied rubric without changing the scoring rule after seeing results;
6. record failed cases, ambiguous cases, and missing outputs;
7. calculate the results from the raw outputs;
8. compare the calculated result with any existing summary.

Do not call founder-run results independent validation. Report them as controlled or internal evidence unless an outside reviewer is performing the scoring and documenting the method.

### Stage 5 — Limitation and claim audit

Classify each public claim as one of:

- directly demonstrated by the local code and tests;
- supported by supplied benchmark evidence;
- proposed architecture or specification;
- not verified;
- contradicted or overstated.

Pay special attention to claims involving:

- safety;
- compliance;
- security;
- production readiness;
- hallucination reduction;
- generalization across models or domains;
- independent validation;
- patent or ownership status.

### Stage 6 — Written review

Return a written report using the template below. The report should be understandable to a technical reader who was not part of the project.

## Required written result

### Reviewer and review boundary

- Reviewer name or identifier:
- Date:
- Materials reviewed:
- Repository commit or archive hash:
- What was not available:

### Reproduction result

- Environment:
- Commands run:
- Result:
- Deviations from expected behavior:

### Code findings

For each interface, report:

- what the code does;
- what the tests demonstrate;
- what important behavior is not tested;
- any defect, ambiguity, or security limitation found.

### Benchmark findings

For each condition and task battery, report:

- whether the task and context were complete;
- whether raw outputs were available and unchanged;
- scoring method;
- score or result;
- failed or ambiguous cases;
- whether the comparison supports the stated conclusion.

### Claim audit

Use this table:

| Claim | Evidence inspected | Finding | Confidence |
|---|---|---|---|
| Example: local reference code detects event tampering | `aibb.py` and test output | Supported for the tested local case | High |
| Example: PIL improves AI reliability generally | benchmark outputs and rubric | Not established / requires broader evidence | Low |

### Limitations

List technical, methodological, statistical, security, deployment, and independence limitations separately.

### Overall conclusion

Choose one or write a more precise conclusion:

- reproducible within the supplied local scope;
- partially reproducible with identified limitations;
- not reproducible from the supplied materials;
- evidence supports only a narrower claim than the public wording;
- evidence is insufficient to assess the broader claim.

The reviewer should not be required to provide a positive conclusion.

## Independence requirements

An independent reviewer should:

- have access to the same materials as the review record;
- disclose any personal, financial, employment, or family relationship to the author;
- not alter the original evidence;
- preserve a copy of the commands and outputs used;
- identify any assistance from AI tools or other reviewers;
- distinguish direct observation from interpretation;
- be free to conclude that a claim is unsupported.

## What a successful review would and would not establish

A successful review could establish that:

- the local reference stack is runnable;
- the three demonstrated behaviors reproduce as documented;
- the benchmark method is sufficiently specified to repeat or improve;
- the public wording accurately matches the evidence;
- specific limitations and implementation gaps are visible.

It would not, by itself, establish that:

- Tivrex is a complete production accountability platform;
- AI systems using Tivrex are safe;
- the architecture works across all models or domains;
- a regulatory or legal requirement is satisfied;
- the full stack is independently validated;
- a commercial product is ready for deployment.

## Review status

- Protocol: prepared for external technical review.
- Root baseline tests: verified 3/3.
- Expanded Crop #1 tests: verified 4/4.
- Independent reviewer: not yet confirmed.
- Independent external scoring of preserved benchmark outputs: open.
- Public release claim: limited to the evidence actually inspected.
