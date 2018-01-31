# Planning, Flowcharts for python Loops

It is important to be able to plan code with the use of flowcharts. Even though you can code without a plan, it is not good practice to start coding without a guide to follow.

A good plan:

- creates a guide you can follow
- helps you plan efficient structure
- helps communicate to others what your code will do

Poor planning can result in inefficient, unstructured code known as 'spaghetti code'.

# flowcharts

A standard way to plan code is with flowcharts. Specific parts of the flowchart represent specific parts of your code.

![Screenshot from 2017-07-07 23-31-28](/home/ony/Desktop/Screenshot from 2017-07-07 23-31-28.png)

# Representing loops in flowcharts

The common way to represent **loops** is with a diamond symbol:

![diamond](/home/ony/Desktop/diamond.png)

This is the same way we show a decision (**if, else if/elif** etc).

**For loops** normally repeat a nested block of code a set number of times or for a set range of data.

**while loops** repeat a set block of code while a condition is true.  The diamond symbol is used with **loops** to show the way the computer repeats a nested block of code then moves on to the next step.

For example:

```python
item = 0
while item < 10:
  print(item)
  item += 1
```

```flow
​```flow
st=>start: Start
op=>operation: item = 0
cond=>condition: while i < 10
e=>end

st->op->cond
cond(yes)->e
cond(no)->cond
```

![basic_while_loop (1)](/home/ony/Desktop/basic_while_loop (1).jpg)

==Now, you can Create your own logic code with flowchart  nicer 😉==

