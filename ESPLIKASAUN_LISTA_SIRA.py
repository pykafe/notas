#python
list ne mamar no tuple ne to'os

iha lian python tau det dalaruma nia simu 	**'four'**

the list use  calibraki the number start with zero.

We find large of list use len.

the last value always -1
oisna atu add list foun ita uza .append ex:
	
	>>> my_list.append('six')
	>>> my_list 
	[1, 2, 3, 'four', 5.0, 'six']

tuple nia difernte ho lista mak:

	>>> my_list .append('six')
	>>> my_list 
	[1, 2, 3, 'four', 5.0, 'six']
	>>> my_list .append('four')
	>>> my_tuple = (1, 2, 3)
	>>> my_tuple.append('four')
	Traceback (most recent call last):
 	File "<stdin>", line 1, in <module>
	AttributeError: 'tuple' object has no attribute 'append'
	>>> 

pop nia funsaun atu foti depois hamos fali ex:
	
	>>> my_list.pop()
	'7'
	
ita bele tau kualker iha list seluk, karik ita append list sira seluk 

oinsa prosseessu liu list ida ?
	
	>>> for item in my_list:
	...     print item
	... 
	1
	2
	3
	four
	5.0
	six
	four
	y
	o
	u
	r
	_
	l
	i
	s
	t
metodu atu check tipu sira

	>>> for item in my_list:
	...     print type(item)
	... 
	<type 'int'>
	<type 'int'>
	<type 'int'>
	<type 'str'>
	<type 'float'>
	<type 'str'>
	<type 'str'>
	<type 'str'>
	<type 'str'>
	<type 'str'>
	<type 'str'>
	<type 'str'>
	<type 'str'>
	<type 'str'>
	<type 'str'>
	<type 'str'>
	>>> 


metodu atu remove kada list sira:

	>>> my_list.remove(3)
	>>> my_list
	[1, 2, 'four', 5.0, 'six', 'four', 'y', 'o', 'u', 'r', '_', 'l', 'i', 's', 't']
	>>> yout_list.remove('four')
	Traceback (most recent call last):
  	File "<stdin>", line 1, in <module>
	NameError: name 'yout_list' is not defined
	>>> my_list.remove('four')
	>>> my_list
	[1, 2, 5.0, 'six', 'y', 'o', 'u', 'r', '_', 'l', 'i', 's', 't']
	>>> 

Add list hamutuk

	>>> my_list.extend([8, 9])
	>>> my_list
	[1, 2, 5.0, 'six', 'y', 'o', 'u', 'r', '_', 'l', 'i', 's', 't', 8, 9]
	>>> 

CSV = comma separated values

muda list to'o csv no csv ba list

	t>>> our_list
	'joanico barros, mariano deus'
	>>> our_list = our_list.split(',')
	>>> our_list
	['joanico barros', ' mariano deus']
	>>> ', '.join(our_list)
	'joanico barros,  mariano deus'
	>>> ' __'.join(our_list)
	'joanico barros __ mariano deus'
	>>> 


