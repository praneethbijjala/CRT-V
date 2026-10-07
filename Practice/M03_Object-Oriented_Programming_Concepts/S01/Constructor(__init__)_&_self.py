'''
What is __init__()?
__init__() is a special method that is automatically called when an object is created.
It is commonly used to initialize object attributes.

Types of Constructors:
1. Default constructor
2. Parameterized constructor

self refers to the current object.

Without self, the value would only exist as a local variable inside the constructor.
self.name stores the value inside the object.

Leetcode problems:
1603. Design Parking System
1845. Seat Reservation Manager
'''

#Count no.of objects created for a class
class A:
    count = 0
    def __init__(self):
        A.count += 1

a = A()
b = A()
c = A()
print("Object count is:",A.count)


from math import pi
class Circle:
    def __init__(self,r):
        self.r = r
    def Area(self):
        return pi * self.r * self.r
    def Perimeter(self):
        return 2 * pi * self.r

c = Circle(7)
c1 = Circle(10)
c2 = Circle(15)
print(c.Area())
print(c.Perimeter())
print(c1.Area())
print(c1.Perimeter())
print(c2.Area())
print(c2.Perimeter())

#1603. Design Parking System
#Solution - 1 

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
        if carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
        if carType == 3:
            if self.small > 0:
                self.small -= 1
                return True
        return False
#Solution - 2
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [0,big,medium,small]

    def addCar(self, carType: int) -> bool:
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        return False