Lists - Review
==============


## How do you change value at index?

    >>> us = ['Peter', 'Niko', 'Mario', 'Nando', 'Ano', 'Anders']
    >>> us[3] = "Onorio"
    >>> us
    ['Peter', 'Niko', 'Mario', 'Onorio', 'Nando', 'Ano', 'Anders']


## How do you add a value at an index?
Lists have a method `insert`.  Insert adds an object before the index: `insert(index, object)`


    >>> us = ['Peter', 'Niko', 'Mario', 'Nando', 'Ano', 'Anders']
    >>> us.insert(3, 'Ony')
    >>> us
    ['Peter', 'Niko', 'Mario', 'Ony', 'Nando', 'Ano', 'Anders']


## What is a lambda?
 A quick way to define a function

    >>> def squared(x):
    ...    return x**2

    >>> squared(3)
    9

    >>> squared2 = lambda x: x**2
    >>> squared2(3)
    9


## How do we currently use lists in our projects
Everywhere


## What is the difference between `.extends` vs. `+` vs. `*`

`.extends` changes the list
`+` returns a new list with the values found in the two lists
`*` returns a new list with the original list's values duplicated a given number of times


## How do you check if a value is in a list?
Use `in`


    >>> 'Anders' in them
    False

    >>> 'Niko' in them
    True


## What does `.index()` do?
`.index()` returns the first index for a given value

    >>> us = ['Peter', 'Niko', 'Mario', 'Peter']

    >>> us.index('Peter')
    0



