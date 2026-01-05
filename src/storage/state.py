import json
import os
import time
from dataclasses import dataclass, asdict
from typing import Any


STATE_FILE = "state.json"


@dataclass
class ClaimRecord:
    key: str
    last_claim_ts: float
    meta: dict[str, Any]


class StateStore:
    def __init__(self, path: str = STATE_FILE):
        self.path = path
        self._data: dict[str, Any] = {"claims": {}}
        self.load()

    def load(self) -> None:
        if not os.path.exists(self.path):
            return
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                self._data = json.load(f)
        except Exception:
            # Keep a safe default if file is corrupted
            self._data = {"claims": {}}

    def save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=2, ensure_ascii=False)

    def can_claim(self, key: str, cooldown_seconds: int) -> bool:
        claims = self._data.get("claims", {})
        record = claims.get(key)
        if not record:
            return True
        last_ts = float(record.get("last_claim_ts", 0))
        return (time.time() - last_ts) >= cooldown_seconds

    def mark_claimed(self, key: str, meta: dict[str, Any] | None = None) -> None:
        meta = meta or {}
        self._data.setdefault("claims", {})
        self._data["claims"][key] = {
            "key": key,
            "last_claim_ts": time.time(),
            "meta": meta
        }
        self.save()
