'''
What is a Class?
A class is a blueprint/template for creating objects.
It defines:

Attributes → data/properties
Methods → behavior/functions

What is an Object?
An object is an instance of a class.
'''

class Example:
    x = 100 #data
    def display(self):
        print("This is Example class display method")

obj = Example()
print(obj.x)
obj.display()

#class Circle with 2 methods
from math import pi
class Circle:
    r = 7
    def Area(self):
        return pi * self.r * self.r
    def Perimeter(self):
        return 2 * pi * self.r

c = Circle()
print(c.Area())
print(c.Perimeter())