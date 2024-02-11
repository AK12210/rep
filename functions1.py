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
		print(s[i])
		if b != 0:
			if s[i - 1] == s[i] and s[i] == 3:
				return True
		b += 1
	return False

s = [int(i) for i in input().split()]
print(has_33(s))

