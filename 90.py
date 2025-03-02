import math

class Circle:
    # Constructor to initialize the radius
    def __init__(self, radius):
        self.radius = radius

    # Method to compute the area of the circle
    def area(self):
        return math.pi * self.radius ** 2

    # Method to compute the perimeter (circumference) of the circle
    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage:
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

print(f"The area of the circle is: {circle.area():.2f}")
print(f"The perimeter (circumference) of the circle is: {circle.perimeter():.2f}")
