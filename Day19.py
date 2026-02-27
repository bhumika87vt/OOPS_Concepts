#Abstraction

from abc import ABC, abstractmethod

class Window(ABC):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @abstractmethod
    def calculate_area(self):
        pass

class SquareWindow(Window):
    def __init__(self, side, **kwargs):
        super().__init__(**kwargs)
        self.side = side
    def calculate_area(self):
        return self.side*self.side
class RectangleWindow(Window):
    def __init__(self, length, width, **kwargs):
        super().__init__(**kwargs)
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length*self.width
sq = SquareWindow(6)
rc = RectangleWindow(3, 9)
print(sq.calculate_area())
print(rc.calculate_area())



from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        return self.side*self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length*self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi*self.radius**2
s = Square(4)
r = Rectangle(3, 5)
c = Circle(7)
print(s.calculate_area())
print(r.calculate_area())
print(c.calculate_area())



from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_speed(self):
        pass

class Car(Vehicle):
    def __init__(self, speed):
        self.speed = speed
    def get_speed(self):
        return f"Car is moving at {self.speed} km/h"
class Bike(Vehicle):
    def __init__(self, speed):
        self.speed = speed
    def get_speed(self):
        return f"Bike is moving at {self.speed} km/h"

c = Car(80)
b = Bike(40)
print(c.get_speed())
print(b.get_speed())