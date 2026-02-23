import json
import os
from typing import Any

from config import STATE_FILE


def load() -> dict[str, Any]:
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save(state: dict[str, Any]) -> None:
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def clear() -> None:
    if os.path.exists(STATE_FILE):
        os.remove(STATE_FILE)
        print(f"State file '{STATE_FILE}' removed.")
