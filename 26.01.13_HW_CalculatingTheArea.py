
"""
ZADANIE: Create a base class Shape with a method for calculating the area. 
Create derived classed: a rectangle, circle, right triangle with their own methods for calculating the area. 
Practicing pomymorphism.
"""

from abc import abstractmethod
from typing import override
import math



class Shape:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

#########################################################################


class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__("rectangle")
        self.width = w
        self.height = h

    @override
    def area(self):
        return self.width * self.height



class Circle(Shape):
    def __init__(self, r):
        super().__init__("circle")
        self.radius = r

    @override
    def area(self):
        return self.radius**2 * math.pi



class RightTriangle(Shape):
    def __init__(self, b, h):
        super().__init__("right angled triangle")
        self.base = b
        self.height = h

    @override
    def area(self):
        return self.base * self.height / 2



shapes = [Rectangle(4, 5), Circle(5), RightTriangle(3, 6)]

for shape in shapes:
    print(f"Area of the {shape.name} is:", shape.area(), "\n")
