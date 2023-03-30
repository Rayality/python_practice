# Write a class that meets these requirements.
#
# Name:       Circle
#
# Required state:
#    * radius, a non-negative value
#
# Behavior:
#    * calculate_perimeter()  # Returns the length of the perimater of the circle
#    * calculate_area()       # Returns the area of the circle
#
# Example:
#    circle = Circle(10)
#
#    print(circle.calculate_perimeter())  # Prints 62.83185307179586
#    print(circle.calculate_area())       # Prints 314.1592653589793
#
# There is pseudocode for you to guide you.
import math
class Circle:
    def __init__(self, radius):
        self.r = radius
    def calculate_perimeter(self):
        perimeter = 2*math.pi*self.r
        return perimeter
    def calculate_area(self):
        area = math.pi* pow(self.r,2)
        return area

circle = Circle(10)
print(circle.calculate_perimeter())  # Prints 62.83185307179586
print(circle.calculate_area())       # Prints 314.1592653589793
