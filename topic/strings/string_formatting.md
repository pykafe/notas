# How to use Python's templating with `.format()`

# Pass a string and have it inserted at {}
>>> "Hello {}".format("Nando")
'Hello Nando'

# Pass multiple strings like a list
>>> "Hello {0}, how is {0}".format("Nando", "World") 
'Hello Nando, how is Nando'

>>> "Hello {1}, how is {0}".format("Nando", "World")
'Hello World, how is Nando'

>>> "Hello {1}, how is {1}".format("Nando", "World")
'Hello World, how is World'

>>> "Hello {0}, how is {1}".format("Nando", "World")
'Hello Nando, how is World'

# Pass a dictionary as **kwargs. Use the key and see the value
>>> my_dict = {'name':'Nando', 'place': 'World'}
>>> "Hello {name}, how is {place}".format(**my_dict)
'Hello Nando, how is World

# Use like as a template
>>> template = "Hello {}"
>>> template.format("nando")
'Hello nando'

Use like a template with a keyword argument (kwargs).
Don't forget the **
>>> context = {'name': 'Nando', 'place': 'Eraulo'}
>>> context = {'name': 'Nando', 'place': 'Eraulo'}
>>> template = "Hello {name}, where is {place}"
>>> template.format(**context)
'Hello Nando, where is Eraulo'