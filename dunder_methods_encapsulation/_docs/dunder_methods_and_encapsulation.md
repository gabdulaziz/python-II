# Magic Methods, Composition, Encapsulation

---

## Magic Methods — Cheat Sheet

```
print(obj)       →  __str__
repr(obj)        →  __repr__
obj1 == obj2     →  __eq__
obj1 > obj2      →  __gt__
obj1 < obj2      →  __lt__
len(obj)         →  __len__
x in obj         →  __contains__
```

---

## Example 1: `__str__`

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"{self.name} — GPA: {self.gpa}"

s = Student("Ali", 87)
print(s)  # Ali — GPA: 87
```

---

## Example 2: `__eq__`, `__gt__`, `__lt__`

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __gt__(self, other):
        return self.gpa > other.gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

s1 = Student("Ali", 85)
s2 = Student("Sara", 92)
s3 = Student("Nizar", 85)

print(s1 == s3)  # True
print(s2 > s1)   # True
print(sorted([s2, s1, s3]))  # sorted by GPA
```

---

## Example 3: `__len__` and `__contains__`

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

    def __contains__(self, song):
        return song in self.songs

    def __str__(self):
        return f"{self.name}: {len(self)} songs"

p = Playlist("My Mix")
p.add("Despacito")
p.add("Shape of You")

print(len(p))            # 2
print("Despacito" in p)  # True
print("Hello" in p)      # False
print(p)                 # My Mix: 2 songs
```

---

## Composition — Cheat Sheet

```
Inheritance:   Student IS A Person
Composition:   Car HAS AN Engine
               University HAS Departments
               Cart HAS Products
```

One object lives inside another object as an attribute.

---

## Example 4: Composition

```python
class Engine:
    def __init__(self, hp, fuel):
        self.hp = hp
        self.fuel = fuel

    def __str__(self):
        return f"{self.hp}hp {self.fuel}"

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Engine object inside Car

    def __str__(self):
        return f"{self.brand} [{self.engine}]"

v8 = Engine(450, "petrol")
car = Car("Mustang", v8)
print(car)              # Mustang [450hp petrol]
print(car.engine.fuel)  # petrol
```

---

## Example 5: Composition — Multiple Objects

```python
class Grade:
    def __init__(self, subject, score):
        self.subject = subject
        self.score = score

    def letter(self):
        if self.score >= 90: return "A"
        if self.score >= 80: return "B"
        if self.score >= 70: return "C"
        if self.score >= 60: return "D"
        return "F"

    def __str__(self):
        return f"{self.subject}: {self.score} ({self.letter()})"

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []  # list of Grade objects

    def add_grade(self, grade):
        self.grades.append(grade)

    def gpa(self):
        if not self.grades:
            return 0
        return sum(g.score for g in self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name} — GPA: {self.gpa():.1f}"

s = Student("Shahrom")
s.add_grade(Grade("Python", 95))
s.add_grade(Grade("Math", 72))
s.add_grade(Grade("English", 58))

print(s)  # Shahrom — GPA: 75.0
for g in s.grades:
    print(f"  {g}")
```

---

## Encapsulation — Cheat Sheet

```
self.name       →  public (anyone can read/write)
self._name      →  protected (don't touch from outside)
self.__name     →  private (hard to access from outside)

@property       →  read access that looks like an attribute
@name.setter    →  write access with validation
```

---

## Example 6: Without Encapsulation (Problem)

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

acc = BankAccount("Ali", 5000)
acc.balance = -999999  # nobody stops you!
print(acc.balance)     # -999999 — broken
```

---

## Example 7: With @property (Solution)

```python
class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Error: cannot be negative")
            return
        self._balance = amount

    @property
    def owner(self):
        return self._owner  # read-only, no setter

    def __str__(self):
        return f"{self._owner}: {self._balance} TJS"

acc = BankAccount("Ali", 5000)
print(acc.balance)    # 5000
acc.balance = -999    # Error: cannot be negative
print(acc.balance)    # still 5000
acc.balance = 3000    # works
print(acc.balance)    # 3000
# acc.owner = "Hacker"  # AttributeError — read-only!
```

---

## Example 8: @property — Temperature

```python
class Sensor:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print("Error: below absolute zero")
            return
        self._celsius = value

    @property
    def fahrenheit(self):  # read-only
        return self._celsius * 9/5 + 32

    def __str__(self):
        return f"{self._celsius}°C / {self.fahrenheit}°F"

t = Sensor(36.6)
print(t)              # 36.6°C / 97.88°F
print(t.fahrenheit)   # 97.88
t.celsius = -300      # Error: below absolute zero
t.celsius = 100
print(t)              # 100°C / 212.0°F
```

---

## Example 9: All Together

```python
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Error: negative price")
            return
        self._price = value

    def __str__(self):
        return f"{self._name} — {self._price} TJS"

    def __eq__(self, other):
        return self._name == other._name

    def __gt__(self, other):
        return self._price > other._price

    def __lt__(self, other):
        return self._price < other._price


class Cart:
    def __init__(self, owner):
        self._owner = owner
        self._items = []

    def add(self, product, qty=1):
        for item in self._items:
            if item["product"] == product:
                item["qty"] += qty
                return
        self._items.append({"product": product, "qty": qty})

    def total(self):
        return sum(i["product"].price * i["qty"] for i in self._items)

    def __len__(self):
        return len(self._items)

    def __contains__(self, name):
        return any(i["product"].name == name for i in self._items)

    def __str__(self):
        lines = [f"=== {self._owner}'s Cart ==="]
        for i in self._items:
            sub = i["product"].price * i["qty"]
            lines.append(f"  {i['product'].name} x{i['qty']} = {sub} TJS")
        lines.append(f"  Total: {self.total()} TJS")
        return "\n".join(lines)


phone = Product("iPhone", 8500)
case = Product("Case", 150)

cart = Cart("Ali")
cart.add(phone, 1)
cart.add(case, 3)
cart.add(case, 2)       # qty becomes 5

print(cart)
print(len(cart))        # 2
print("iPhone" in cart) # True
phone.price = -500      # Error: negative price
print(sorted([phone, case]))
```

---

## Your Task

Create an **Online Store** system with the classes below. Use the examples above as reference.

**Class `Product`**
- `_name`, `_price`
- `@property` for price — reject negative
- `__str__`, `__eq__` (by name), `__gt__`, `__lt__` (by price)

**Class `Cart`**
- `_owner`, `_items` (list)
- `add(product, qty)` — if already exists, increase qty
- `remove(product_name)`
- `total()` — total price
- `__len__`, `__contains__`, `__str__`

**Test:**
```python
phone = Product("iPhone", 8500)
case = Product("Case", 150)
charger = Product("Charger", 200)

cart = Cart("Ali")
cart.add(phone, 1)
cart.add(case, 3)
cart.add(charger, 2)
cart.add(case, 2)

print(cart)
print(len(cart))
print("iPhone" in cart)
print("Laptop" in cart)

phone.price = -500
cart.remove("Charger")
print(cart)
print(sorted([phone, case, charger]))
```

---

## Bonus (if you finish early)

1. Add `apply_discount(product_name, percent)` to Cart
2. Add `save_receipt(filename)` — save cart to a text file
3. Add a `Customer` class with name, email, and a Cart object (composition)
