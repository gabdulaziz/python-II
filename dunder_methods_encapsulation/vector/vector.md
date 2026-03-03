## `Vector`

A mathematical 2D vector with full operator support.

- `__init__(self, x, y)`
- `__str__` → `"Vector(3, 4)"`
- `__repr__` → same as `__str__`
- `__eq__` → same x and y
- `__add__` → vector addition `(x1+x2, y1+y2)`
- `__sub__` → vector subtraction `(x1-x2, y1-y2)`
- `__mul__(scalar)` → scalar multiplication `(x*n, y*n)`
- `__abs__` → returns the magnitude (length) of the vector: `sqrt(x² + y²)`
- `__lt__` → compare by magnitude
- `__bool__` → `False` if both x and y are 0

```python
v1 = Vector(3, 4)
v2 = Vector(1, 2)
v0 = Vector(0, 0)

print(v1)              # Vector(3, 4)
print(v1 + v2)         # Vector(4, 6)
print(v1 - v2)         # Vector(2, 2)
print(v1 * 3)          # Vector(9, 12)
print(abs(v1))         # 5.0
print(v1 == Vector(3, 4))  # True
print(v2 < v1)         # True

if not v0:
    print("Zero vector!")   # This prints

vectors = [Vector(5, 0), Vector(1, 1), Vector(3, 4)]
print(sorted(vectors))  # [Vector(1, 1), Vector(3, 4), Vector(5, 0)]
```

```python
class Vector:
    def __init__(self, x, y):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, scalar):
        pass

    def __abs__(self):
        pass

    def __lt__(self, other):
        pass

    def __bool__(self):
        pass
```