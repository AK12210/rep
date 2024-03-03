#task1
import os
path = 'C:\Users\Adm\Downloads'
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print([ name for name in os.listdir(path)])

#task2
import os
print(os.access('C:\Users\Adm\Downloads\exampl.txt', os.F_OK))
print(os.access('C:\Users\Adm\Downloads\exampl.txt', os.R_OK))
print(os.access('C:\Users\Adm\Downloads\exampl.txt', os.W_OK))
print(os.access('C:\Users\Adm\Downloads\exampl.txt', os.X_OK))

#task3
import os
path = r'C:\Users\Adm\Downloads'
print(os.path.exists(path))
if os.path.exists(path) == True:
	print(os.path.basename(path))
	print(os.path.dirname(path))

#task4
with open(r"exampl.txt", 'r') as ff:
    lin = len(ff.readlines())
    print(lin)

#task5
s = ["Hello\n", "World\n"]
 
ff = open('Adm\Downloads', 'w')
ff.writelines(s)
ff.close()

#task7
import shutil 

shutil.copyfile('doc1.txt','doc2.txt')

#task8
import os

path = 'C:\Users\Adm\Downloads\exampl.txt'
if os.path.exists(path) and os.access(path, os.X_OK):
    os.remove(path)
