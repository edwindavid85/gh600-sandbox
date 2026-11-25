import pytest

from app.inventory import Inventory


def make():
    inv = Inventory()
    inv.add("A-1", "Widget", quantity=10, unit_price=2.50)
    inv.add("B-2", "Gadget", quantity=3, unit_price=10.00)
    return inv


def test_add_rejects_duplicates():
    inv = make()
    with pytest.raises(ValueError):
        inv.add("A-1", "Again")


def test_restock_and_remove():
    inv = make()
    assert inv.restock("A-1", 5) == 15
    assert inv.remove("A-1", 4) == 11


def test_remove_more_than_stock_fails():
    inv = make()
    with pytest.raises(ValueError):
        inv.remove("B-2", 4)


def test_total_value():
    assert make().total_value() == 55.0


def test_low_stock():
    assert make().low_stock() == ["B-2"]
