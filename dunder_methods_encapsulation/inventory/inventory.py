class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, item, qty=1):
        if item in self.items:
            self.items[item] += qty
        else:
            self.items[item] = qty

    def remove(self, item, qty=1):
        if item in self.items:
            self.items[item] -= qty
            if self.items[item] <= 0:
                del self.items[item]

    def __len__(self):
        return sum(self.items.values())

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, item):
        return self.items.get(item, 0)

    def __add__(self, other):
        new_inv = Inventory()
        for item, qty in self.items.items():
            new_inv.add(item, qty)
        for item, qty in other.items.items():
            new_inv.add(item, qty)
        return new_inv

    def __eq__(self, other):
        return self.items == other.items

    def __str__(self):
        if not self.items:
            return "Inventory is empty"
        return "\n".join(f"{item}: {qty}" for item, qty in self.items.items())


inv1 = Inventory()
inv1.add("Sword")
inv1.add("Potion", 3)
inv1.add("Shield")

print(len(inv1))
print("Potion" in inv1)
print(inv1["Potion"])
print(inv1["Arrow"])

inv2 = Inventory()
inv2.add("Potion", 2)
inv2.add("Arrow", 10)

inv3 = inv1 + inv2
print(inv3["Potion"])
print(inv3["Arrow"])
print(inv3["Sword"])

inv1.remove("Potion", 2)
print(inv1["Potion"])