Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = range(6)
>>> for n in x:
	print(n)

	
0
1
2
3
4
5
>>> x = range(4)
>>> for n in x:
	print(n)

	
0
1
2
3
>>> x = range(step,4)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x = range(step,4)
NameError: name 'step' is not defined
>>> x = range(4,0)
>>> for n in x:
	print(n)

	
>>> 
>>> x = range(1, 4)
>>> for n in x:
	print(n)

	
1
2
3
>>> x = range(4, -1)
>>> for n in x:
	print(n)

	
>>> x = range([start4], [stop-1])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    x = range([start4], [stop-1])
NameError: name 'start4' is not defined
>>> for i in range(4, -1, -1):
	print(i)

	
4
3
2
1
0
>>> for i in range(3, -1, -1):
	print(i)

	
3
2
1
0
>>> for x in range(8, 1, -2)
SyntaxError: invalid syntax
>>> for x in range(8, 1, -2):
	print(x)

	
8
6
4
2
>>> 