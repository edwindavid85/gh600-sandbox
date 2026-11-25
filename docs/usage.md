# Using the inventory service

```python
from app.inventory import Inventory

inv = Inventory()
inv.add("A-1", "Widget", quantity=10, unit_price=2.50)
inv.restock("A-1", 5)
inv.remove("A-1", 2)
print(inv.total_value())
print(inv.low_stock(threshold=5))
```

`remove` raises `ValueError` when there is not enough stock.
Note: quantities are whole units.
