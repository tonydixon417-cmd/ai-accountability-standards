"""Minimal risk-tiered action gate for the ZeroTX demonstration."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Decision:
    action: str
    risk: str
    allowed: bool
    reason: str


class ActionGateway:
    ORDER = {"low": 1, "medium": 2, "high": 3, "critical": 4}

    def __init__(self, approved_max: str = "low"):
        if approved_max not in self.ORDER:
            raise ValueError("approved_max must be low, medium, high, or critical")
        self.approved_max = approved_max

    def evaluate(self, action: str, risk: str, human_approved: bool = False) -> Decision:
        if risk not in self.ORDER:
            raise ValueError("risk must be low, medium, high, or critical")
        if self.ORDER[risk] <= self.ORDER[self.approved_max]:
            return Decision(action, risk, True, "within configured authority boundary")
        if human_approved:
            return Decision(action, risk, True, "explicit human approval recorded")
        return Decision(action, risk, False, "escalation required before external execution")
