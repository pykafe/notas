# Variables
a = 1
b = 2 
a = b
a 
b = 3
a


# Scope

A variable defined outside of a function is available inside that function
> variable ne'ebe defini iha funsuan nia liu se bele assesu iha funsaun nia laran

A variable defined inside of a function is NOT available outside of that function
> vabriable ne'ebe define iha funsaun nia lara la bele assesu iha funsaun nia liur


# Mutable or Immutable

> Mutable means it can be added to.
> Immutable means it cannot be added to

## What types are Mutable?
- lists
- dictonaries

```
people = {'ano': 1, 'ony': 2}

In [18]: def add_person(my_dict):
    ...:     my_dict.update({'mario':3})
    ...:     return my_dict
    ...:

In [19]: people
Out[19]: {'ano': 1, 'ony': 2}

In [20]: add_person(people)
Out[20]: {'ano': 1, 'mario': 3, 'ony': 2}

In [21]: people
Out[21]: {'ano': 1, 'mario': 3, 'ony': 2}
```

## What types are Immutable
- tuples 
- ints
- strings

```
In [12]: number = 5

In [13]: def plus_one(value):
    ...:     value = value + 1
    ...:     return value
    ...:

In [14]: number
Out[14]: 5

In [15]: plus_one(number)
Out[15]: 6

In [16]: number
Out[16]: 5
```