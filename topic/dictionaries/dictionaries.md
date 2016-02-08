# Dictionaries

## What is a dictionary?
Stores key / value pairs

## How do we make a new dictionary?
Dictionaries use curly brackets `{}`

    >>> ages = {'Nando': 26, 'Peter': 36, 'Ano': 25}


## How do you add a key / value to a dictionary?

    >>> ages['Niko'] = 25

    >>> ages
    {'Ano': 25, 'Nando': 26, 'Niko': 25, 'Peter': 36}


## How do you changes a value for a given key?
Keys are unique.

    >>> ages['Ano'] = 26
    >>> ages
    {'Ano': 26, 'Nando': 26, 'Niko': 25, 'Peter': 36}


<<<<<<< HEAD
## How doe we get a value for a key?
=======
## How do we get a value for a key?
>>>>>>> master

    >>> ages.get('Peter')
    36

Can also have a default value

    >>> ages.get('Peter', 'Unknown')
    36

    >>> ages.get('Anders', 'Unknown')
    'Unknown'


Access the key directly

    >>> ages['Peter']
    36

This might cause a KeyError

    >>> ages['Anders']
    KeyError


## How do you remove a key?
Use `del` to remove a key / value pair from a dictionary

    >>> ages = {'Ano': 25, 'Nando': 26, 'Niko': 25, 'Peter': 36}
    >>> del ages['Niko']

    >>> ages
    {'Ano': 25, 'Nando': 26, 'Peter': 36}


## How can you find the size of a dictionary?

Use `len()` to get the number of key / value pairs in a dictionary

    >>> len(ages)
    3



## How do you check if a value is in a dictionary?
Use `in` to see if a given key is in a dictionary


    >>> 'Anders' in ages
    False

    >>> 'Peter' in ages
    True

## How do we get a list of keys?
Use the `.keys()` method

    >>> ages.keys()
    ['Nando', 'Peter']


## How do we get a list of values?
Use the `.values()` method

    >>> ages.values()
    [26, 36, 25]
<<<<<<< HEAD

=======
>>>>>>> master
