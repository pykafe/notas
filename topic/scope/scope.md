# Scope

A variable defined outside of a function is available inside that function
> variable ne'ebe defini iha funsuan nia liu se bele assesu iha funsaun nia laran

```
In [2]: name = 'Mario'

In [3]: def print_name():
   ...:     print name
   ...:

In [4]: print_name()
Mario
```

A variable defined inside of a function is NOT available outside of that function
> vabriable ne'ebe define iha funsaun nia lara la bele assesu iha funsaun nia liur

```
In [5]: color
NameError: name 'color' is not defined

In [6]: def print_color():
   ...:     color = 'blue'
   ...:     print color
   ...:

In [7]: print_color()
blue

In [8]: color
NameError: name 'color' is not defined
```

