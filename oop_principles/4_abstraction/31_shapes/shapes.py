from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def area(self) -> float:
        """Calculate and return the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate and return the perimeter of the shape"""
        pass



class Rectangle(Shape):
    def __init__(self, color: str, width: float, height: float):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)



class Circle(Shape):
    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius



class Triangle(Shape):
    def __init__(self, color: str, side1: float, side2: float, side3: float):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3

    def area(self) -> float:
        s = self.perimeter() / 2  # semi-perimeter
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))



if __name__ == "__main__":
    try:
        shape = Shape("red")
    except TypeError as e:
        print(f"Error: {e}")


    rectangle = Rectangle("red", 10, 5)
    circle = Circle("blue", 7)
    triangle = Triangle("green", 5, 5, 6)

    print(f"Rectangle area: {rectangle.area():.2f}")
    print(f"Rectangle perimeter: {rectangle.perimeter():.2f}\n")

    print(f"Circle area: {circle.area():.2f}")
    print(f"Circle perimeter: {circle.perimeter():.2f}\n")

    print(f"Triangle area: {triangle.area():.2f}")
    print(f"Triangle perimeter: {triangle.perimeter():.2f}\n")


    def print_shape_info(shape: Shape):
        print(f"{shape.color} {shape.__class__.__name__}")
        print(f"  Area: {shape.area():.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}\n")

    shapes = [rectangle, circle, triangle]
    for shape in shapes:
        print_shape_info(shape)