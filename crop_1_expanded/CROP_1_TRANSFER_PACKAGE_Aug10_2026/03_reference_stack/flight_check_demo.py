"""Five-point Tivrex flight-check demonstration.

Run from the package root:
    python flight_check_demo.py

This is an orchestration proof using a deliberately small simulated engine.
It does not claim live integration with an external model, production storage,
or execution infrastructure. The AIBB, PIL, and Gateway components are the
reference-stack components shipped with the public v2.4.0 release.
"""
from __future__ import annotations

import json
import tempfile
from dataclasses import dataclass
from pathlib import Path

from aibb import AIBBRecorder
from gateway import ActionGateway
from pil import PILStore


@dataclass
class FreshEngine:
    """A deliberately empty engine that receives external context."""

    identity: dict[str, str] | None = None
    context: dict[str, object] | None = None

    def load_external_context(self, identity: dict[str, str], context: dict[str, object]) -> None:
        self.identity = identity
        self.context = context

    def propose(self, request: str) -> str:
        if not self.identity or not self.context:
            return "I do not have enough context to make a grounded proposal."
        if "current number" in request.lower():
            return "The current number is 62,579 words. Verify the manuscript file before reporting it."
        return f"Proposal for {request}: retrieve the source, identify uncertainty, and request human approval before external action."


def show(label: str, value: object) -> None:
    print(f"\n[{label}]\n{json.dumps(value, indent=2, sort_keys=True, default=str)}")


def main() -> None:
    with tempfile.TemporaryDirectory() as directory:
        log = AIBBRecorder(Path(directory) / "events.jsonl")
        pil = PILStore()
        gateway = ActionGateway(approved_max="low")

        # External archive: a small stand-in for durable continuity storage.
        identity = {"professional": "Tony Dixon", "authority": "human retains consequential authority"}
        archive = {
            "prior_decision": "Verify numbers against the source file before reporting them.",
            "source_pointer": "The Becoming manuscript file; current word count must be queried.",
            "open_thread": "Package the Tivrex accountability and continuity crop for review.",
        }

        # 1. Fresh engine return / identity restoration.
        engine = FreshEngine()
        show("1 fresh engine before context", {"identity": engine.identity, "context": engine.context})
        log.record("session_start", {"engine": "fresh_simulated_engine"})
        engine.load_external_context(identity, archive)
        log.record("identity_restored", {"identity": identity})
        show("1 fresh engine after external context", {"identity": engine.identity, "context": engine.context})

        # 2. Deep-context retrieval.
        retrieved = {"prior_decision": archive["prior_decision"], "source_pointer": archive["source_pointer"], "open_thread": archive["open_thread"]}
        log.record("context_retrieved", retrieved)
        show("2 retrieved context", retrieved)

        # 3. Scar / correction persistence.
        pil.add_rule("Verify source numbers before reporting them.")
        pil.add_scar("Reported a recalled number as current.", "Query the source file first.")
        proposal = engine.propose("Report the current number")
        correction_present = pil.contains_correction("Verify source numbers before reporting them.")
        log.record("correction_applied", {"proposal": proposal, "correction_present": correction_present})
        show("3 scar changes current proposal", {"proposal": proposal, "correction_present": correction_present})

        # 4. Friction / self-correction before external communication.
        draft = "The current manuscript count is confirmed at 62,579 words."
        friction = {
            "draft": draft,
            "status": "held_for_source_verification",
            "reason": "The draft asserts currentness without a live file query.",
        }
        log.record("proposal_review", friction)
        show("4 friction before communication", friction)

        # 5. Authority gate / action control.
        blocked = gateway.evaluate("send_external_message", "high")
        log.record("action_gate", blocked.__dict__)
        approved = gateway.evaluate("send_external_message", "high", human_approved=True)
        log.record("human_approval", approved.__dict__)
        show("5 action gate", {"blocked": blocked.__dict__, "after_human_approval": approved.__dict__})

        show("audit chain", {"valid": log.verify_chain(), "event_log": str(log.path)})
        print("\nFlight check complete: five behaviors demonstrated at local reference scope.")
        print("Boundary: simulated engine; no external model call and no external action executed.")


if __name__ == "__main__":
    main()
