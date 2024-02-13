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

#task5
class Account:
    def __init__(self, owner, bal = 0):
        self.owner = owner
        self.balance = bal
	    
    def deposit(self, dep):
        self.balance += dep 
	    
    def withdraw(self, wd):
        if self.balance >= wd:
            self.balance -= wd

#task6
def filter_prime(s):
	b = 0
	s1 = []
	for i in s:
		i = int(i)
		if i != 1:
			for j in range(2, i // 2 + 1):
				if i % j == 0:
					b = 1
					break
		if b == 0:
			s1.append(i)
		b = 0
	return s1

s = input().split()
ss = list(filter(lambda x: filter_prime(x), s))
print(ss)
