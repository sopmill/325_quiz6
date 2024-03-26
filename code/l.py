from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def set_dimensions(self, *args):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def set_dimensions(self, radius):
        self.radius = radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def set_dimensions(self, base, height):
        self.base = base
        self.height = height


class Polygon(Shape):
    def __init__(self, sides_length):
        self.sides_length = sides_length

    def calculate_area(self):
        # Implement area calculation for polygon (e.g., using Heron's formula)
        # For demonstration purposes, let's assume it's a regular polygon
        num_sides = len(self.sides_length)
        side_length = self.sides_length[0]  # Assuming all sides are equal
        return (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

    def set_dimensions(self, *args):
        self.sides_length = args


def main():
    shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8), Polygon([5, 5, 5, 5])]  # Example of a square

    for shape in shapes:
        print(f"Area of {shape.__class__.__name__}: {shape.calculate_area()}")

    polygon = Polygon([5, 5, 5, 5])  # Square
    print("Before:", polygon.calculate_area())
    polygon.set_dimensions(6, 6, 6, 6)  # Changing dimensions to represent another polygon (e.g., a rhombus)
    print("After:", polygon.calculate_area())


if __name__ == "__main__":
    main()
