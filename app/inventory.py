"""A tiny inventory service. It is the code your agents will work on in every GH-600 lab."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Item:
    sku: str
    name: str
    quantity: int = 0
    unit_price: float = 0.0


@dataclass
class Inventory:
    items: dict[str, Item] = field(default_factory=dict)

    def add(self, sku: str, name: str, quantity: int = 0, unit_price: float = 0.0) -> Item:
        """Add a new item. Raises ValueError if the SKU exists or values are negative."""
        if sku in self.items:
            raise ValueError(f"SKU already exists: {sku}")
        if quantity < 0 or unit_price < 0:
            raise ValueError("quantity and unit_price must be non-negative")
        item = Item(sku, name, quantity, unit_price)
        self.items[sku] = item
        return item

    def restock(self, sku: str, amount: int) -> int:
        """Increase stock for an item and return the new quantity."""
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.items[sku].quantity += amount
        return self.items[sku].quantity

    def remove(self, sku: str, amount: int) -> int:
        """Take stock out. Raises ValueError if there is not enough stock."""
        item = self.items[sku]
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > item.quantity:
            raise ValueError(f"not enough stock for {sku}: have {item.quantity}, need {amount}")
        item.quantity -= amount
        return item.quantity

    def total_value(self) -> float:
        """Total value of all stock, rounded to cents."""
        return round(sum(i.quantity * i.unit_price for i in self.items.values()), 2)

    def low_stock(self, threshold: int = 5) -> list[str]:
        """SKUs at or below the threshold, sorted."""
        return sorted(s for s, i in self.items.items() if i.quantity <= threshold)
