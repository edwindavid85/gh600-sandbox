"""Logging helper. Every module must log through this helper (see .github/copilot-instructions.md)."""
from __future__ import annotations

import json
import time


def log_event(event: str, **fields) -> str:
    """Return (and print) one structured JSON log line."""
    line = json.dumps({"ts": round(time.time(), 3), "event": event, **fields}, sort_keys=True)
    print(line)
    return line
