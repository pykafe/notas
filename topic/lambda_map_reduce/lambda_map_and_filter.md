# Lambda

## a normal function

In [35]: def add_one(x):

```
...:     return x+1
...:
```

In [36]: add_one(2)
Out[36]: 3

## lambda are a short function

In [38]: add_two = lambda x: x+2
In [39]: add_two(2)
Out[39]: 4

# Map

`map` applies a function to each item in a list and returns the result as a list

```
In [38]: my_list = [2, 3, 5]
In [39]: map(lambda x: x * 2, my_list)
Out[39]: [4, 6, 10]
```

# Filter

`filter` tests a condition to each item in a list and returns the result as a list

```
In [46]: my_list = [2, 3, 4, 5]
In [47]: filter(lambda number: number % 2 == 0
    ...: , numbers)

Out[48]: [2, 4,]
```

