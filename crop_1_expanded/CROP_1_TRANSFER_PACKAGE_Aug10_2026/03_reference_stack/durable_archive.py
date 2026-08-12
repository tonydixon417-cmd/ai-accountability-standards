"""Small durable SQLite archive for the Tivrex flight check.

This is a local reference archive, not an enterprise persistence service.
"""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any


class DurableArchive:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(self.path)
        self.connection.execute(
            """CREATE TABLE IF NOT EXISTS archive (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            )"""
        )
        self.connection.commit()

    def put(self, key: str, value: Any) -> None:
        encoded = json.dumps(value, sort_keys=True)
        self.connection.execute(
            "INSERT INTO archive(key, value) VALUES (?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
            (key, encoded),
        )
        self.connection.commit()

    def get(self, key: str) -> Any | None:
        row = self.connection.execute("SELECT value FROM archive WHERE key = ?", (key,)).fetchone()
        return json.loads(row[0]) if row else None

    def search(self, term: str) -> list[dict[str, Any]]:
        pattern = f"%{term.lower()}%"
        rows = self.connection.execute(
            "SELECT key, value FROM archive WHERE lower(value) LIKE ? ORDER BY key",
            (pattern,),
        ).fetchall()
        return [{"key": key, "value": json.loads(value)} for key, value in rows]

    def close(self) -> None:
        self.connection.close()
