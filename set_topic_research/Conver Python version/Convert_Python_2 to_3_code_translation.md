# Automated Python 2 to 3 code translation

2to3 is a Python program that reads Python 2.x source code and applies a series of *fixers* to transform it into valid Python 3.x code. The standard library contains a rich set of fixers that will handle almost all code. 2to3 supporting library [`lib2to3`](https://docs.python.org/2/library/2to3.html#module-lib2to3) is, however, a flexible and generic library, so it is possible to write your own fixers for 2to3. [`lib2to3`](https://docs.python.org/2/library/2to3.html#module-lib2to3) could also be adapted to custom applications in which Python code needs to be edited automatically.

## Using 2to3

2to3 will usually be installed with the Python interpreter as a script. It is also located in the `Tools/scripts` directory of the Python root.

2to3’s basic arguments are a list of files or directories to transform. The directories are recursively traversed for Python sources.

Here is a sample Python 2.x source file, `converter_python_version_example.py`:

```python
def greet(name):
    print "Hello, {0}!".format(name)
print "What's your name?"
name = raw_input()
greet(name)
```

It can be converted to Python 3.x code via 2to3 on the command line:

```
$ 2to3 converter_python_version_example.py
```

Or converted to Python 2.x code via 3to2 on the command line:

```
$ 3to2 converter_python_version_example.py
```

A diff against the original source file is printed. 2to3 can also write the needed modifications right back to the source file. (A backup of the original file is made unless `-n` is also given.) Writing the changes back is enabled with the `-w` flag:

```
$ 2to3 -w converter_python_version_example.py
```

After transformation, `converter_python_version_example.py` looks like this:

```python
def greet(name):
    print("Hello, {0}!".format(name))
print("What's your name?")
name = input()
greet(name)
```

Comments and exact indentation are preserved throughout the translation process.