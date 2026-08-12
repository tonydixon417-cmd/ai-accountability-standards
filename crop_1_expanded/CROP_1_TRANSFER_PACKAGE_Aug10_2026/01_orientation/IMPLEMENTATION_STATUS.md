# Implementation Status

This file prevents the repository from presenting blueprints as deployed software.

## Available now

- published standards and versioned papers;
- stack-level architecture map;
- Zenodo deposits and GitHub source;
- public Tivrex accountability assessment;
- PIL ablation protocol;
- definitions for proposed logs, roles, gates, and evaluation procedures.

## Not yet implemented in this repository

- production AIBB event recorder;
- production Missing CVR store;
- executable Loop Detector;
- executable PIL storage/retrieval service;
- ZeroTX action gateway;
- machine-checkable Ethics Floor;
- automated Check-Ride runner;
- CI test suite;
- enterprise deployment package.

## What an implementation partner should build first

1. A versioned event schema for AIBB.
2. A local reference recorder that writes and validates events.
3. A minimal PIL store with correction/scar retrieval.
4. A deterministic action-gateway mock with risk tiers.
5. The ablation runner and raw-result archive.
6. A small demo that shows one failure before the stack and the same failure after the stack.

The repository is an architectural specification and proof-of-stack request. It is not a claim that the complete aircraft already exists.
