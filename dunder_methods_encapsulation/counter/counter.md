## `Counter`

A simple counter that supports `+`, `==`, and `print`.

- `__init__(self, value=0)`
- `increment()` → adds 1
- `__add__` → adds two counters, returns new `Counter`
- `__eq__` → equal if same value
- `__str__` → `"Counter(5)"`
- `__bool__` → `False` if value is 0, `True` otherwise

```python
c1 = Counter()
c1.increment()
c1.increment()
c1.increment()
print(c1)           # Counter(3)

c2 = Counter(7)
c3 = c1 + c2
print(c3)           # Counter(10)
print(c1 == Counter(3))  # True

empty = Counter()
if not empty:
    print("Counter is zero!")  # This prints
```

