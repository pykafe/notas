## How to use `lambda`
## How to use `map()`
In [39]: map(lambda x: x * 2, [2, 3, 5])
Out[39]: [4, 6, 10]

## How to use list comprehension
In [40]: [x * 2 for x in [2, 3, 5]]
Out[40]: [4, 6, 10]


## How to use `for` loop
In [41]: lista = []

In [42]: for x in [2, 3, 5]:
    ...:     lista.append(x * 2)
    ...:

In [43]: lista
Out[43]: [4, 6, 10]

# How to use filter
In [11]: [0, 4, 8, 12, 16]
Out[11]: [0, 4, 8, 12, 16]

In [12]: filtered = filter(lambda x: x % 2 == 0, lista)

In [13]: filtered
Out[13]: [0, 2, 4, 6, 8]

# How to filter in a list comprehension
In [16]: [ x * 2 for x in lista if x % 2 == 0]
Out[16]: [0, 4, 8, 12, 16]
