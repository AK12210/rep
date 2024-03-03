#task1
s = [1, 2, 3]
sm = 1
for i in s:
	sm *= i
print(sm)

#task2
s = input()
upp = 0
lw = 0
for i in s:
	if i.isupper():
		upp += 1
	elif i.islower():
		lw += 1
print(upp)
print(lw)

#task3
s = input()
rs = ''.join(reversed(s))
if s == rs:
	print("Yes")
else:
	print("No")

#task4
from time import sleep
import math

def delay(lmb, ms, *args):
    sleep(ms / 1000)
    return lmb(*args)


print(delay(lambda x: math.sqrt(x), 1000, 25))

#task5
s = (True, True, True, True)
print(all(s))
