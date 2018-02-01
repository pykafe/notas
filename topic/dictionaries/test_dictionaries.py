def hello_world():
    ''' This function returns 'Hello World' '''
    return 'Hello World'


def test_hello_world():
    assert hello_world() == 'Hello World'


def add(a, b):
    ''' This function adds two values '''
    return a + b

# Dictionaries

def test_add():
    assert add(1, 1) == 2
    assert add(1, 2) == 3
    assert add(23, 24) == 47


def multiply(a, b):
    ''' This function multiplies two values '''

def test_list_values_in_dict():
    assert list_values_in_dict({'hello': 'world'}) == ['world', ]
    assert list_values_in_dict({'world': 'hello'}) == ['hello', ]
    assert list_values_in_dict({'a': '1', 'b': '2', 'c': '3'}) == ['1', '2', '3', ]


def count_occurrences(my_list):
    ''' This function will return a dictionary containing 
    the number of occurrences of a item in a given list. '''
    from collections import Counter
    return Counter(my_list)


def test_count_occurrences():
    my_list = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c']
    assert count_occurrences(my_list) == {'a': 3, 'b': 3, 'c': 2}


def string_to_list(my_string):
    ''' This function takes a string and returns that string as a list.
        If a the given value is not a string. The function returns None.'''


def test_string_to_list():
    assert string_to_list('hello world') == ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    assert string_to_list(5) == None
    assert string_to_list({'hello': 'world'}) == None



