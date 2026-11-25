import json

from app.logging_utils import record_event


def test_record_event_returns_one_json_line():
    line = record_event("restock", sku="A-1", amount=5)
    data = json.loads(line)
    assert data["event"] == "restock"
    assert data["sku"] == "A-1"
