## `Inventory`

An RPG inventory system with full dunder support.

- `__init__(self)` → empty dict `items` (key: item name, value: quantity)
- `add(item, qty=1)` → adds item or increases quantity
- `remove(item, qty=1)` → decreases quantity, removes if 0
- `__len__` → total number of items (sum of all quantities)
- `__contains__(item)` → is the item in inventory
- `__getitem__(item)` → returns quantity of that item (0 if not found)
- `__add__` → merges two inventories into a new one
- `__eq__` → same items and quantities
- `__str__` → formatted inventory list

```python
inv1 = Inventory()
inv1.add("Sword")
inv1.add("Potion", 3)
inv1.add("Shield")

print(len(inv1))           # 5
print("Potion" in inv1)    # True
print(inv1["Potion"])      # 3
print(inv1["Arrow"])       # 0

inv2 = Inventory()
inv2.add("Potion", 2)
inv2.add("Arrow", 10)

inv3 = inv1 + inv2
print(inv3["Potion"])      # 5
print(inv3["Arrow"])       # 10
print(inv3["Sword"])       # 1

inv1.remove("Potion", 2)
print(inv1["Potion"])      # 1
```

```python
class Inventory:

    def __init__(self):
        self.items = {}

    def add(self, item, qty=1):
        pass

    def remove(self, item, qty=1):
        pass

    def __len__(self):
        pass

    def __contains__(self, item):
        pass

    def __getitem__(self, item):
        pass

    def __add__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __str__(self):
        pass

```
