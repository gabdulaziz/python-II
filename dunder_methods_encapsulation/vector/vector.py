import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __bool__(self):
        return self.x != 0 or self.y != 0


v1 = Vector(3, 4)
v2 = Vector(1, 2)
v0 = Vector(0, 0)

print(v1)
print(v1 + v2)
print(v1 - v2)
print(v1 * 3)
print(abs(v1))
print(v1 == Vector(3, 4))
print(v2 < v1)

if not v0:
    print("Zero vector!")

vectors = [Vector(5, 0), Vector(1, 1), Vector(3, 4)]
print(sorted(vectors))