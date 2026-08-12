# Tivrex Partner Reference Kit

## What exists

Tivrex Core is an early, deterministic accountability boundary for AI systems. It receives a proposed AI action, evaluates evidence and authority, returns a decision, and creates an audit record.

It is not a finished AI operating system. It is a reference implementation showing how an accountability layer can become inspectable software.

## The narrow product

A partner can use Tivrex Core as a starting point for building AI systems that need:

- verified versus unverified status handling
- continuity across sessions and decisions
- human approval for consequential actions
- proposal/action separation
- audit-ready records
- bounded failure lessons
- repeated-loop escalation

## Demo

```bash
node tivrex-core/pipeline-demo.mjs
```

The demo evaluates three scenarios:

1. a verified low-risk draft
2. an unverified consequential external claim
3. an approved consequential action

The runtime does not execute external actions. It demonstrates the boundary that an execution system would have to pass through.

## Partner opportunity

The partner supplies production engineering, security, deployment, model adapters, and domain-specific controls. Tivrex supplies the accountability-layer reference architecture, assessment methodology, failure taxonomy, and continuity principles.

## Current evidence level

- deterministic local reference implementation: demonstrated
- full AI-model integration: not yet demonstrated
- reduction in hallucination or drift: unproven
- production security: unproven
- domain deployment: unproven
- commercial demand: requires direct market testing

## Recommended first commercial conversation

Do not sell a universal AI operating system claim. Offer a partner a controlled implementation assessment:

> “We have a reference boundary for separating AI proposals from authorized action, with verification, audit, continuity, and failure-loop controls. We are looking for an engineering partner to adapt and test it in one consequential domain.”

## What funding would enable

Funding would accelerate:

- model adapters
- secure persistence
- independent observer services
- real action-gateway integration
- red-team testing
- domain-specific pilots
- independent validation

The funding case must be based on the working reference architecture and the validation path—not on claiming that the complete platform already exists.
