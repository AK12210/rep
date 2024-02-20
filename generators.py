#task1
def func():
    i = 1
    while True:
        yield i * i
        i += 1

n = int(input())
for j in func():
    if j > n * n:
        break
    print(j)

n = int(input())
s = []
for j in func():
    if j >= n:
        break
    s.append(j)
print(*s, sep=', ')

#task3
def func():
    i = 12
    while True:
        yield i
        i += 12

n = int(input())
for j in func():
    if j >= n:
        break
    print(j)

#task4
def squares():
    i = a
    while True:
        yield i * i
        i += 1

a = int(input())
b = int(input())
for j in squares():
    if j > b * b:
        break
    print(j)

#task5
def func():
    i = n
    while True:
        yield i
        i -= 1

n = int(input())
for j in func():
    if j < 0:
        break
    print(j)
