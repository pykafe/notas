# Functions

## What is a function?

A piece of code that we can define in one place and reuse.  It can take arguments and can also return values.


## How do you create a function in Python?
Use `def`. It creates functions. 
Follow the example below:

    >>> def my_function(parameter_1, parameter_2):
    ....:    return parameter_1 + parameter_2

    >>> def add(value_1, value2):
    ....:    return value_1 + value_2

    >>> def divide(numerator, denominator):
    ....:    return numerator / denominator


## How do I use a function?

    >>> my_function(1, 45)
    46
    >>> divide(8, 2)
    4


## What is `return` and what does it do?
- `return` gives back one or more values from a function.
- It is a reserved word in Python. It is Python's, you cannot use it for variables or function names.

        >>> return = "Hello World"
        SyntaxError: invalid syntax

- No code within the function is executed after you call `return`.

        >>> def add(value_1, value_2):
        ....:     print value_1, value_2
        ....:     return value_1 + value_2
        >>> add(3, 4)
        3 4
        7
        >>> def add(value_1, value_2):
        ....:     return value_1 + value_2
        ....:     print value_1, value_2
        >>> add(3, 4)
        7


## What is the difference between `print` and `return`?
`return` gives back one or more values from a funciton.
`print` shows you a value.


## What gets returned when you don't use `return`?
By default a function returns `None`


    >>> def hello(name):
    ....:    print "Hello " + name
    >>> hello('Mario')
    Hello Mario
    >>> hi = hello('Peter')
    >>> hi

    >>> hi == None
    True


## What is `pass`?
`pass` is a place holder which does nothing.
It is a reserved word in Python, so don't use `pass` for variable or function names.

   >>> def add(this, that):
   ....:     if type(this) != int:
   ....:         pass
   ....:     else:
   ....:         return this + that
   >>> add('Mario', 1)

   >>> add(3, 1)
   4


## What is an Argument (aka Parameter)?
An Argument is a value passed to a function.

    >>> def add(this, that):
    ....:    return this + that

`this` and `that` are the arguments in this function.

    >>> Macs = 2
    >>> PCs = 5
    >>> add(Macs, PCs)
    7

    >>> this = 0
    >>> that = 8
    >>> add(this, that)
    8

The name of the variable passed to the function can be the same as the arguments or different.


## What is a Optional Argument?
An optional argument is an argument which is not required.
You define an optional argument by giving it a default value:

    >>> def add(this=0, that=0):
        return this + that

    >>> add(1)
    1
    >>> add(3, 4)
    7

## What is a Named Argument?
A named argument is an argument which you can refer to when calling the function.
If you use named arguments, you can change the order of the arguments.
The name is optional, but then the order is very important.
You define an optional argument by giving it a default value:


    >>> def divide(numerator=0, denominator=1):
    ....:    return numerator / denominator

    >>> divide(numerator=8, denominator=2)
    4
    >>> divide(denominator=2, numerator=8)
    4
    >>> divide(8, 2)
    4
    >>> divide(8, 2)  # remember we are dividing `int`
    0


## What are `*args`?
`*args` is an optional way of passing values to a function. You can pass a list to a function using `*` and the values in the list will be passed to the function in the order they appear in the list or tuple.

    >>> def add(this=0, that=0):
    ....:    return this + that

    >>> add(1, 2)
    3
    >>> values = [1, 2]
    >>> add(*values)
    3

## What are `**kwargs`?
`**kwargs` are keyword arguments. Similar to `*args` but uses Named Arguments defined in a dictionary.

    >>> def add(this=0, that=0):
    ....:    return this + that

    >>> keyword_values = {'this': 1, 'that':2}
    >>> add(**keyword_values)
    3

## What is Scope?
It is the difference between inside and outside. What you define outside of a function is separate from what is defined within a function.

    >>> def scope(x):
    .....:     x = x + 1
    .....:     return x

    >>> x = 3
    >>> x
    3
    >>> scope(x)
    4
    >>> x
    3
    >>> y = 8
    >>> scope(y)
    9
    >>> x
    3


## Functions can return multiple values via tuples.

    >>> def counter(index):
    ....:     new_index = index + 1
    ....:     return index, new_index
    >>> counter(1)
    (1, 2)
    >>> this, that = counter(5)
    >>> this
    5
    >>> that
    6

## What is the difference between a method and a function?

### What is a Function?
A piece of code that we can define in one place and reuse.  It can take arguments and can also return values.

### What is a Method?
A method is a special kind of Function which is bound to a Class.
