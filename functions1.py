#task1
def oun(grams):
	return 28.3495231 * grams

grams = int(input())
print(oun(grams))

#task2
def t(f):
	return (5 / 9) * (f - 32)

f = float(input())
print(t(f))

#task3
def solve(numheads, numlegs):
	for i in range(numheads):
		if i * 2 + (numheads - i) * 4 == numlegs:
			return numheads - i, i

h = int(input())
l = int(input())
print(solve(h, l))

#task4
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
print(filter_prime(s))

#task5
from itertools import permutations

def perms(s):
    s1 = [''.join(i) for i in permutations(s)]
    return s1

s = input()
print(perms(s))

#task6
def re(s):
	s1 = []
	for i in reversed(range(len(s))):
		s1.append(s[i])
	s1 = ' '.join([str(i) for i in s1])
	return s1

s = input().split()
print(re(s))

#task7
def has_33(s):
	b = 0
	for i in range(len(s)):
		if b != 0:
			if s[i - 1] == s[i] and s[i] == 3:
				return True
		b += 1
	return False

s = [int(i) for i in input().split()]
print(has_33(s))
#task8
def spy_game(s):
	for i in range(len(s) - 2):
		if s[i] == 0 and s[i + 1] == 0 and s[i + 2] == 7:
			return True
	return False

s = [int(i) for i in input().split()]
print(spy_game(s))
#task9
import math
def vol(r):
	return (4 / 3) * math.pi * r * r * r

r = float(input())
print(vol(r))
#task10
def dis(s):
	s1 = []
	for i in s:
		if i not in s1:
			s1.append(i)
	return s1

s = [int(i) for i in input().split()]
print(dis(s))
#task11
def pal(s):
	return s == s[::-1]

s = input()
print(pal(s))
#task12
def histogram(s):
	for i in s:
		j = i
		s1 = ''
		while j > 0:
			s1 += '*'
			j -= 1
		print(s1)

s = [int(i) for i in input().split()]
histogram(s)
#task13
import random

s = input('Hello! What is your name?')
print('Well, ' + s + ', I am thinking of a number between 1 and 20.')
n = random.randint(1, 20)
print('Take a guess.')
j = 0
while True:
	m = int(input())
	if m < n:
		print('Your guess is too low.')
		print('Take a guess.')
		j += 1
	elif m > n:
		print('Your guess is too high.')
		print('Take a guess.')
		j += 1
	else:
		print('Good job, ' + s + '! You guessed my number in ', end='')
		print(j, end=' ')
		print('guesses!')
		
