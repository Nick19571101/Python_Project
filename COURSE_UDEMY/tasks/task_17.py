"""Написати клас, що описує прямокутник і має метод з обчислення площі
"""

class Rectangle:
    def __init__(self ,length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

x = Rectangle(16, 10)
y = Rectangle(2.5, 4)
print(x.area())
print(y.area())
