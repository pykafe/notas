# Iteration
A piece of code that loops.


## `while` loops
A while loop takes a condition and continues to loop if that condition returns `True`.
 
    >>> x = 0
    >>> while x < 5:
    ....:    x = x + 1
    ....:    print x
    1
    2
    3
    4

## !!! INFINITE LOOPS !!!!
An infinite loop will iterate forever and ever:
    
    >>> x = 0
    >>> while True:
    ....:    x = x + 1
    ....:    print x


Or until it finds `break`.


## How do you stop a loop from inside? Use `break`.
`break` is a special word in python.  `break` will stop loops from continuing to iterate.

    >>> x = 0
    >>> while True:
    ....:    x = x + 1
    ....:    print x
    ....:    if x == 100:
    ....:       break


## What is `continue`?
`continue` is a special word in Python.  From inside a loop it will return you to the top of the loop.

    >>> while x < 10:
    ....: x = x + 1
    ....:     if x % 2 == 0:
    ....:         continue
    ....:     print x, 'is odd'
    1 is odd
    3 is odd
    5 is odd
    7 is odd
    9 is odd


## `for` loops, another kind of loop!
A for loop will loop through an iterable like lists, dictionaries, sets, and tuples.

    >>> for x in [1, 3, 4]:
    ....:     print x
    1
    3
    4

    >>> for x in "Hello world":
    ....:     print x
    H
    e
    l
    l
    o

    w
    o
    r
    l
    d


`for` loops over a dictionary's keys

    >>> ages = {"Ony": 34,
    ....:       "Ano": 83,
    ....:       "Mario": 16,
    ....:       "Nando": 15,
    ....:       "Niko": 22,}

    >>> for person in ages:
    ....:     print person
    ....:
    Mario
    Ony
    Niko
    Nando
    Ano


## How do you use `range()`?
`range()` is a built-in function that takes an integer and returns a list of integers up until that value.

    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> for x in range(5):
    ....:    print x
    0
    1
    2
    3
    4


## How do you get the index and the value? Use `enumerate()`.

    >>> for i, name in enumerate(names):
    ...:    print i, name
    0 Mario
    1 Ony
    2 Niko
    3 Nando


