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


def sum_of_integers(maximum):
    ''' return the sum of all the integers up to maximum
    hint: create a total_sum variable value 0, and a counter variable value 1
    WHILE the counter is less than OR EQUAL TO the maximum, add the counter to the total_sum, add 1 to the counter
    after the while loop has exited, return the total_sum
    '''
    total_sum = 0
    print "total sum is ", total_sum
    counter = 1
    print "counter is ", counter
    while counter <= maximum:
        print "now counter is less than or equal to maximum {counter} <= {max} == True".format(counter=counter, max=maximum)
        print "adding counter({}) to total sum".format(counter)
        total_sum = total_sum + counter
        print "total sum is ", total_sum
        print "adding 1 to counter"
        counter = counter + 1
        print "counter is ", counter
    print "now counter is not less than or equal to maximum {counter} <= {max} == False".format(counter=counter, max=maximum)
    print "returning total value", total_sum
    return total_sum

sum_of_integers(5)
total sum is  0
counter is  1
now counter is less than or equal to maximum 1 <= 5 == True
adding counter(1) to total sum
total sum is  1
adding 1 to counter
counter is  2
now counter is less than or equal to maximum 2 <= 5 == True
adding counter(2) to total sum
total sum is  3
adding 1 to counter
counter is  3
now counter is less than or equal to maximum 3 <= 5 == True
adding counter(3) to total sum
total sum is  6
adding 1 to counter
counter is  4
now counter is less than or equal to maximum 4 <= 5 == True
adding counter(4) to total sum
total sum is  10
adding 1 to counter
counter is  5
now counter is less than or equal to maximum 5 <= 5 == True
adding counter(5) to total sum
total sum is  15
adding 1 to counter
counter is  6
now counter is not less than or equal to maximum 6 <= 5 == False
returning total value 15
15

>> x = 10
>>> while x > 0:
...     print x, "is greater than 0"
...     x = x - 1
...
10 is greater than 0
9 is greater than 0
8 is greater than 0
7 is greater than 0
6 is greater than 0
5 is greater than 0
4 is greater than 0
3 is greater than 0
2 is greater than 0
1 is greater than 0

>> name = "Peter"
>>> while len(name) < 20:
...     name = name + "p"
...     print name
...
Peterp
Peterpp
Peterppp
Peterpppp
Peterppppp
Peterpppppp
Peterppppppp
Peterpppppppp
Peterppppppppp
Peterpppppppppp
Peterppppppppppp
Peterpppppppppppp
Peterppppppppppppp
Peterpppppppppppppp
Peterppppppppppppppp

>>> numbers = range(0,20)
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> while len(numbers) > 5:
...     print numbers.pop()
...
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
>>> numbers
[0, 1, 2, 3, 4]
>>> len(numbers)
5
