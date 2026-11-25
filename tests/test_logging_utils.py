import json

from app.logging_utils import log_event


def test_log_event_returns_one_json_line():
    line = log_event("restock", sku="A-1", amount=5)
    data = json.loads(line)
    assert data["event"] == "restock"
    assert data["sku"] == "A-1"
