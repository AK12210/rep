#task1
import re
def text_match(a):
    s = '^a(b*)$'
    if re.search(s, a):
        return 'Match'
    else:
        return 'No match'
                
a = input()                
print(text_match(a))

#task2
import re
def text_match(a):
    s = 'ab{2,3}'
    if re.search(s, a):
        return 'Match'
    else:
        return 'No match'
                
a = input()                
print(text_match(a))

#task3
import re
def text_match(a):
    s = '^[a-z]+_[a-z]+$'
    if re.search(s, a):
        return 'Match'
    else:
        return 'No match'
                
a = input()                
print(text_match(a))

#task4
import re
def text_match(a):
    s = '[A-Z]+[a-z]+$'
    if re.search(s, a):
        return 'Match'
    else:
        return 'No match'
                
a = input()                
print(text_match(a))

#task5
import re
def text_match(a):
    s = 'a.*?b$'
    if re.search(s, a):
        return 'Match'
    else:
        return 'No match'
                
a = input()                
print(text_match(a))

#task6
import re
s = input()
print(re.sub("[ ,.]", ":", s))

#task7
def func(s):
    import re
    return ''.join(x.capitalize() or '_' for x in s.split('_'))

s = input()
print(func(s))

#task8
import re
s = input()
print(re.findall('[A-Z][^A-Z]*', s))

#task9
import re
def func(s):
	return re.sub(r"(\w)([A-Z])", r"\1 \2", s)
  
s = input()
print(func(s))

#task10
import re
def func(a):
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', a)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()

a = input()
print(func(a))
