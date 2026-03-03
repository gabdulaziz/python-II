
## `Fraction`

A simple fraction class with `+`, `==`, and `print`.

- `__init__(self, numerator, denominator)`
- `__str__` → `"3/4"`
- `__eq__` → `1/2 == 2/4` should be `True` (compare cross-multiplied)
- `__add__` → adds two fractions, returns new `Fraction`
- `__lt__` → compare fractions

Hint: use `from math import gcd` to simplify fractions.

```python
a = Fraction(1, 2)
b = Fraction(1, 3)
c = Fraction(2, 4)

print(a)          # 1/2
print(a == c)     # True  (1/2 == 2/4)
print(a < b)      # False (1/2 > 1/3)

d = a + b
print(d)          # 5/6
```
