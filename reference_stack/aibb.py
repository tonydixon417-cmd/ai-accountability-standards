"""A minimal hash-chained event recorder for local demonstrations."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class AIBBRecorder:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _last_hash(self) -> str:
        if not self.path.exists():
            return "GENESIS"
        lines = [line for line in self.path.read_text().splitlines() if line.strip()]
        return json.loads(lines[-1])["event_hash"] if lines else "GENESIS"

    def record(self, event_type: str, payload: dict[str, Any]) -> dict[str, Any]:
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event_type": event_type,
            "previous_hash": self._last_hash(),
            "payload": payload,
        }
        canonical = json.dumps(event, sort_keys=True, separators=(",", ":"))
        event["event_hash"] = hashlib.sha256(canonical.encode()).hexdigest()
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(event, sort_keys=True) + "\n")
        return event

    def verify_chain(self) -> bool:
        if not self.path.exists():
            return True
        previous = "GENESIS"
        for line in self.path.read_text().splitlines():
            event = json.loads(line)
            claimed = event.pop("event_hash")
            if event["previous_hash"] != previous:
                return False
            canonical = json.dumps(event, sort_keys=True, separators=(",", ":"))
            if hashlib.sha256(canonical.encode()).hexdigest() != claimed:
                return False
            previous = claimed
        return True
