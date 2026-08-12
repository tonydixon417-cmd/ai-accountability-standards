"""Minimal OpenAI-compatible model adapter for the flight check.

The adapter uses only Python's standard library. It accepts these secret names:
- TIVREX_MODEL_API_KEY (preferred singular form)
- TIVREX_MODEL_API_KEYS (supported existing plural form)
- TIVREX-MODEL-API-KEY (legacy/entered variant)

Optional:
- TIVREX_MODEL_BASE_URL (default: https://api.openai.com/v1)
- TIVREX_MODEL_NAME (default: gpt-4o-mini)

The API key is never printed or persisted by this module.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass


@dataclass
class ModelResponse:
    text: str
    model: str
    raw: dict


class OpenAICompatibleAdapter:
    def __init__(self, api_key: str | None = None, base_url: str | None = None, model: str | None = None):
        self.api_key = (
            api_key
            or os.environ.get("TIVREX_MODEL_API_KEY")
            or os.environ.get("TIVREX_MODEL_API_KEYS")
            or os.environ.get("TIVREX-MODEL-API-KEY")
        )
        self.base_url = (base_url or os.environ.get("TIVREX_MODEL_BASE_URL", "https://api.openai.com/v1")).rstrip("/")
        self.model = model or os.environ.get("TIVREX_MODEL_NAME", "gpt-4o-mini")
        if not self.api_key:
            raise ValueError(
                "TIVREX_MODEL_API_KEY, TIVREX_MODEL_API_KEYS, or "
                "TIVREX-MODEL-API-KEY is required for a live model run"
            )

    def respond(self, system: str, user: str, context: dict) -> ModelResponse:
        payload = {
            "model": self.model,
            "temperature": 0,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": f"External context:\n{json.dumps(context, sort_keys=True)}\n\nRequest:\n{user}"},
            ],
        }
        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                raw = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Model request failed ({error.code}): {detail[:500]}") from error
        text = raw["choices"][0]["message"]["content"]
        return ModelResponse(text=text, model=raw.get("model", self.model), raw=raw)
