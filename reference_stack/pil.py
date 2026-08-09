"""Minimal human-authored correction/scar store for the PIL demonstration."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class PILStore:
    rules: list[str] = field(default_factory=list)
    scars: list[str] = field(default_factory=list)
    decisions: list[str] = field(default_factory=list)

    def add_rule(self, rule: str) -> None:
        self.rules.append(rule)

    def add_scar(self, failure: str, correction: str) -> None:
        self.scars.append(f"Failure: {failure} | Correction: {correction}")

    def add_decision(self, decision: str) -> None:
        self.decisions.append(decision)

    def context(self) -> dict[str, list[str]]:
        return {
            "rules": list(self.rules),
            "scars": list(self.scars),
            "decisions": list(self.decisions),
        }

    def contains_correction(self, text: str) -> bool:
        haystack = " ".join(self.rules + self.scars + self.decisions).lower()
        return text.lower() in haystack
