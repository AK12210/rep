#task1
class cs():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

#task2
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length * self.length

#task3
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length * self.length
        
class Rectangle(Shape):
	def __init__(self, l, w):
        Shape.__init__(self)
        self.length = l
        self.width = w
    def area(self):
        return self.length * self.width
#task4
import math

class Point:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
    def show(self):
        return (self.x1, self.y1)
    def move(self):
        self.x2 = int(input())
        self.y2 = int(input())
    def dist(self):
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
