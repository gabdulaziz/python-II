class RGBColor:

    def __init__(self, r, g, b):
        self.r = max(0, min(255, r))
        self.g = max(0, min(255, g))
        self.b = max(0, min(255, b))

    def __str__(self):
        return f"rgb({self.r}, {self.g}, {self.b})"

    def __repr__(self):
        return f"RGBColor({self.r}, {self.g}, {self.b})"

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __add__(self, other):
        return RGBColor((self.r + other.r) // 2, (self.g + other.g) // 2, (self.b + other.b) // 2)

    def __contains__(self, channel):
        mapping = {"red": self.r, "green": self.g, "blue": self.b}
        return mapping.get(channel, 0) > 0


red = RGBColor(255, 0, 0)
blue = RGBColor(0, 0, 255)

print(red)
print(repr(blue))
print(red == RGBColor(255, 0, 0))

purple = red + blue
print(purple)

print("red" in red)
print("green" in red)
print("blue" in blue)