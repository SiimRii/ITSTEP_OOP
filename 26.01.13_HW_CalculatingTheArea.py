
"""
ZADANIE: Create a base class Shape with a method for calculating the area. 
Create derived classed: a rectangle, circle, right triangle with their own methods for calculating the area. 
Practicing pomymorphism.
"""

from abc import ABC, abstractmethod
from typing import override
import abc
import math



class Shape(ABC):
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
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be non-negative as well as non-zero numbers.")
        return self.width * self.height
        


class Circle(Shape):
    def __init__(self, r):
        super().__init__("circle")
        self.radius = r

    @override
    def area(self):
        if self.radius <= 0:
            raise ValueError("Radius must be non-negative as well as non-zero number.")
        return self.radius**2 * math.pi



class RightTriangle(Shape):
    def __init__(self, b, h):
        super().__init__("right angled triangle")
        self.base = b
        self.height = h

    @override
    def area(self):
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be non-negative as well as non-zero numbers.")
        return self.base * self.height / 2





shapes = [Rectangle(-4, 5), Circle(5), RightTriangle(3, 6)]

for shape in shapes:
    try:
        print(f"Area of the {shape.name} is:", shape.area(), "\n")
    except ValueError as e:
        print(f"Error while calculating area of {shape.name}: {e}\n")
