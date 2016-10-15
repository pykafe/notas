(notas)➜  dictionaries git:(onys_notas) python
Python 2.7.3 (default, Jun 22 2015, 19:43:34) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>
>>> def add(value_1, value_2):
...     return value_1 + value_2
...     print value_1, value_2
... 
>>> value_1 = 8
>>> value_2 = 4
>>> 
>>> def add(value_1, value_2):
...     return value_1 + value_2
...     print value_1, value_2
... 
>>> add(2, 4)
6
>>>  
>>> 
>>> def hello(name):
...     print "hello" + name
... 
>>> hello("ony")
helloony
>>> hello('ony')
helloony
>>> 
>>> 
>>> hello("ano")
helloano
>>> hello("nando")
hellonando
>>> hello("Ony")
helloOny
>>> 
>>> 
>>> 
>>> hi = hello('Peter')
helloPeter
>>> hi
>>>
>>> hi == None
True
>>> type(hi)
<type 'NoneType'>
>>> 
>>>  
>>> 
>>> def add(this, that):
...     pass
... 
>>> def add(this, that):
...     if type(this) != int:
...             pass
...     else:
...             return this + that
... 
>>> add('Mario', 1)
>>> add(3, 1)
4
>>> def add(this, that):
...     pass
...     return this + that
... 
>>> add(1, 3)
4
>>> koko1 = 2
>>> koko2 = 5
>>> add(koko1, koko2)
7
>>> 

================
SCOPE EXPLAIN:
>>> def scope(x):
...     x = x + 1
...     return x
... 
>>> x = 2
>>> scope(x)
3
>>> x
2
>>> 