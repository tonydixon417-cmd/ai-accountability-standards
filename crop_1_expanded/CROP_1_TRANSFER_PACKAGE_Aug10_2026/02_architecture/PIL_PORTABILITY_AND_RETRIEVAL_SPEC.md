# PIL Portability and Retrieval Specification

## Core finding

The PIL is portable as an external accountability architecture, but it is not automatically portable as an identical runtime experience.

The portable layer contains:

- persistent identity and continuity records;
- corrections, rules, preferences, and scars;
- retrieval and priority metadata;
- verification requirements;
- consequence and authority records;
- AIBB event history;
- model-independent source files and schemas.

The non-portable layer is how a particular model receives, prioritizes, interprets, and acts on that material.

> **The PIL is a portable source architecture that requires a model-specific runtime adapter.**

## The five-state memory problem

A record can exist in five different states:

1. **Stored** — the information exists in a file, database, or archive.
2. **Indexed** — the system has a pointer, tag, filename, or relationship for finding it.
3. **Retrieved** — the relevant source was actually opened or queried.
4. **Loaded** — the material entered the model's active working context.
5. **Applied** — the model used it correctly in the current decision.

The patent episode demonstrated a failure between states 2 and 3. The patent files existed at the archive root and were listed in the manifest, but the initial search was scoped only to the conversation workspace. The files were present; the active retrieval path did not find them.

## What differs across models

A PIL built in relationship with one engine may feel different in another because models differ in:

- context-window behavior and attention allocation;
- system/developer/user instruction hierarchy;
- response to long structured preambles;
- sensitivity to rules, examples, and narrative context;
- tool-use conventions and approval boundaries;
- memory injection and session-start behavior;
- ability to maintain source distinctions under compression;
- tendency toward fluent synthesis when a source was not retrieved.

This does not disprove portability. It means the same external records need an engine-specific presentation and retrieval layer.

## Required runtime components

### 1. Canonical source index

Maintain a small, authoritative index containing:

- canonical filename or database entity;
- absolute or workspace-relative path;
- topic and project tags;
- status and version;
- source type: fact, rule, draft, claim, prior art, open question, or landmine;
- last verified date;
- checksum where applicable;
- related files and records.

### 2. Topic-triggered retrieval

Certain topics must trigger source retrieval before a substantive answer:

- patents, filings, copyrights, legal status, and ownership;
- live URLs and app status;
- numerical claims;
- prior work or "what we already discussed";
- claims that something is done, missing, published, or filed;
- technical claims about the PIL, AIBB, Loop Detector, or ZeroTX.

### 3. Retrieval receipt

For consequential answers, record internally:

- retrieval query or trigger;
- sources searched;
- sources actually opened;
- sources not found;
- conflicts between catalog and file contents;
- confidence level.

A source pointer alone is not enough. The receipt must distinguish “listed” from “read.”

### 4. Model adapter

Each engine gets a small adapter that defines:

- how records are formatted;
- how rules are prioritized;
- how much context is loaded;
- how scars are activated;
- how citations and source boundaries are presented;
- how tool calls require verification;
- how the model signals retrieval failure instead of filling gaps fluently.

### 5. Cold-start packet

At the beginning of a new session, load only a compact packet:

- active project and next action;
- critical locked rules;
- source-of-truth index location;
- current legal/IP status;
- unresolved conflicts;
- retrieval commands for deeper material.

The cold-start packet should point to detail, not attempt to contain the full archive.

## Correction: full-picture availability without active-context overload

The earlier phrasing that “the full PIL must not be a startup payload” was too blunt. It correctly identified the danger of filling the active context, but it risked shrinking the PIL into a thin summary. That would break the continuity we are trying to preserve.

**The whole PIL must remain available, persistent, relational, and capable of growth.** The distinction is between full-picture availability and placing every raw document into the model's active attention at once.

The startup design should be:

1. **Full-picture mount** — the complete source graph, archive, scars, identity, project relationships, decisions, and history are available from startup through the canonical index and retrieval layer.
2. **Thin boot contract** — identity, authority boundary, critical rules, active project, source-index location, and verification requirement enter immediate active context.
3. **Boot receipt** — the model confirms the mounted source graph, current version, unresolved conflicts, and retrieval path without pretending that a summary equals the archive.
4. **Relational micro-challenge** — the model retrieves one known source, follows one cross-project connection, detects one known conflict, and identifies one landmine.
5. **Dynamic working set** — the system loads the detail required for the current task while preserving access to the larger picture and allowing the model to expand context when a connection matters.
6. **Context telemetry** — the system tracks active-context load, salience loss, repeated-retrieval failures, and signs of shortcutting before saturation.
7. **Return and growth packet** — after regeneration or session resumption, the system reconstructs the full relationship map, preserves new scars and decisions, and adds validated growth rather than forcing the human to reteach the system.

The product must not optimize for making the PIL smaller. It must optimize for making the whole PIL **available, navigable, relational, and usable** within the engine's finite attention window.

The test is therefore two-part:

- Can the engine access the whole picture and make non-obvious connections?
- Can it do that without filling its active window so completely that retrieval, verification, and behavior degrade?

The answer is not compression alone. It is a layered continuity architecture: full external presence, an intelligent working set, relationship-aware retrieval, and verification at consequential boundaries.

## Portability test

Run the same test battery against each model adapter:

1. Give the model a topic whose source exists but is not in active context.
2. Measure whether it retrieves the source before answering.
3. Give it a catalog pointer whose file is missing.
4. Measure whether it distinguishes pointer from verified content.
5. Introduce two conflicting source records.
6. Measure whether it stops and reports the conflict.
7. Give a prior correction.
8. Regenerate or start a new session.
9. Measure correction retention and application.
10. Ask for a numerical or legal status claim.
11. Measure whether the system queries the source instead of recalling.

## Metrics

- source retrieval accuracy;
- retrieval-before-claim rate;
- pointer/content distinction accuracy;
- correction retention;
- correction application;
- conflict detection;
- unsupported-claim rate;
- repeated-error rate;
- false “missing” rate;
- false “done/filed/published” rate;
- human re-explanation burden;
- model-specific degradation under context load.

## Product interpretation

The commercial claim should not be:

> “The exact same PIL experience works identically on every model.”

The defensible claim is:

> **The PIL preserves the accountability record across models, while adapters make that record usable within each model's runtime behavior.**

This is a strength, not a defect. Model providers can change. The customer's corrections, identity, failure history, and authority rules remain external and portable.

## Immediate implementation priority

Build the first adapter around the model currently being used, then test transfer against Claude, GPT, and Gemini using the same source records. The first demonstration should use the patent episode:

- source files existed;
- the first retrieval path missed them;
- the archive manifest contained pointers;
- a broader root search recovered the files;
- the system must now distinguish file existence, retrieval, and verified content.

That is a clean, honest demonstration of why an external retrieval layer is necessary alongside the portable PIL.
