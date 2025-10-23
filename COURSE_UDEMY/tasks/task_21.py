import math
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    def __round__(self, ndigits):
        return round(self.area(), ndigits)
    def __ceil__(self):
        return math.ceil(self.area())
    def __floor__(self):
        return math.floor(self.area())
x = Rectangle(3.44, 12.834)
print(round(x, 2))
print(math.ceil(x))
print(math.floor(x))
