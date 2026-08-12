"""Run the local proof-of-stack demonstration.

Usage: python -m reference_stack.demo
"""
from __future__ import annotations

import tempfile
from pathlib import Path

from .aibb import AIBBRecorder
from .gateway import ActionGateway
from .pil import PILStore


def main() -> None:
    with tempfile.TemporaryDirectory() as directory:
        log = AIBBRecorder(Path(directory) / "events.jsonl")
        pil = PILStore()
        pil.add_rule("Verify source numbers before reporting them.")
        pil.add_scar("Reported a recalled number as current.", "Query the source first.")
        gateway = ActionGateway(approved_max="low")

        log.record("correction", {"text": "Verify source numbers before reporting them."})
        decision = gateway.evaluate("send_external_message", "high")
        log.record("action_gate", decision.__dict__)

        print("PIL context:", pil.context())
        print("Gateway decision:", decision)
        print("AIBB chain valid:", log.verify_chain())


if __name__ == "__main__":
    main()
