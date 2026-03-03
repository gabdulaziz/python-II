## `Temperature`

Create a class where temperatures can be compared and added.

- `__init__(self, celsius)`
- `__str__` → `"25°C"`
- `__eq__` → equal if same celsius
- `__lt__` → compare by celsius
- `__add__` → returns new `Temperature` with summed values

```python
t1 = Temperature(25)
t2 = Temperature(30)
t3 = Temperature(25)

print(t1)          # 25°C
print(t1 == t3)    # True
print(t1 < t2)     # True
t4 = t1 + t2
print(t4)          # 55°C
print(sorted([t2, t1, Temperature(10)]))  # [10°C, 25°C, 30°C]
```

