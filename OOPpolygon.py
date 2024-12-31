class Polygon:
    def area(self):
        return 0

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.142 * (self.radius ** 2)

if __name__ == "__main__":
    rect = Rectangle(width=15, height=5)
    print(f"Rectangle Area: {rect.area()}")

    tri = Triangle(base=13, height=14)
    print(f"Triangle Area: {tri.area()}")

    circ = Circle(radius=13.5)
    print(f"Circle Area: {circ.area()}")