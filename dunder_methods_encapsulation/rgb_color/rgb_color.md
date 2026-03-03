## `RGBColor`

A color class that supports `+` (mixing), `==`, and `print`.

- `__init__(self, r, g, b)` → values 0–255
- `__str__` → `"rgb(255, 128, 0)"`
- `__repr__` → `"RGBColor(255, 128, 0)"`
- `__eq__` → same r, g, b
- `__add__` → mix two colors by averaging each channel (integer division)
- `__contains__(channel_name)` → returns `True` if that channel is > 0. Accepts `"red"`, `"green"`, `"blue"`

```python
red = RGBColor(255, 0, 0)
blue = RGBColor(0, 0, 255)

print(red)              # rgb(255, 0, 0)
print(repr(blue))       # RGBColor(0, 0, 255)
print(red == RGBColor(255, 0, 0))  # True

purple = red + blue
print(purple)           # rgb(127, 0, 127)

print("red" in red)     # True
print("green" in red)   # False
print("blue" in blue)   # True
```

```python
class RGBColor:

    def __init__(self, r, g, b):
        pass
        
    def __str__(self):
        pass

    def __repr__(self):
        return f"RGBColor({self.r}, {self.g}, {self.b})"

    def __eq__(self, other):
        pass

    def __add__(self, other):
        pass

    def __contains__(self, channel):
        mapping = {"red": self.r, "green": self.g, "blue": self.b}
        return mapping.get(channel, 0) > 0

```