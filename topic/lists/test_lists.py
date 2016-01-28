from collections import Counter
# Lists
# This is how you write a funciton and a test with py.test


def hello_world():
    ''' This function returns 'Hello World' '''
    return 'Hello World'


def test_hello_world():
    assert hello_world() == 'Hello World'


# Add to the List

def add_to_list(my_value, my_list):
    '''
    Given a value and a list this function
    returns a list with the value added to it
    '''
    '''
    a_list = []
    a_list.append(my_value)
    my_value = a_list
    return my_list + my_value
    '''
    return my_list + [my_value]


def test_add_to_list():
    my_value = 5
    my_list = [1, 2, 3, 4]

    assert add_to_list(my_value, my_list) == [1, 2, 3, 4, 5]


# Get Item from a List

def get_index_from_list(my_index, my_list):
    '''
    Given an index (integer) and a list this function will
    return the item at that index in the given list.
    If index is not an integer return None
    Remember Python indexes starts at 0
    '''
    '''
    if isinstance(my_index, int):
        return my_list[my_index]
    else:
        return None
    '''
    if isinstance(my_index, int):
        return my_list[my_index]


def test_get_index_from_list():
    my_list = ['1', 'Baucau', 'Aileu', 5, 'Cars']

    assert get_index_from_list(2, my_list) == 'Aileu'
    assert get_index_from_list('hello', my_list) == None


# Check list for value

def is_in_list(my_value, my_list):
    '''
    Given a value and a list this function checks if the value can be found in the list
    and returns True or False
    '''
    '''
    if my_value in my_list:
        return True
    else:
        return False
   '''
    return my_value in my_list


def test_is_in_list():
    my_value = 3
    not_my_value = 4
    my_list = [1, 2, 3]
    assert is_in_list(my_value, my_list) == True
    assert is_in_list(not_my_value, my_list) == False


# List Length

def get_length(my_list):
    '''
    Given a list this function
    returns the number of items in the list
    '''
    get_length = len(my_list)
    return get_length


def test_get_length():
    my_list = [1, 2, 3]
    assert get_length(my_list) == 3


# Merge two lists

def merge_lists(first_list, second_list):
    '''
    Given two list this function returns a single list which contains the items of the
    first list followed by the items of the second list
    '''
    merge_lists = first_list + second_list
    return merge_lists


def test_merge_lists():

    first_list = [1, 2, 3]
    second_list = [4, 5, 6]
    assert merge_lists(first_list, second_list) == [1, 2, 3, 4, 5, 6]


# Converting a list to string

def list_to_string(my_list):
    '''
    Given a list the is funciton returns a string which includes the items of the list
    separated by single spaces
    '''
    return ' '.join(my_list)


def test_list_to_string():
    my_list = ['one', 'two', 'three']
    assert list_to_string(my_list) == "one two three"


# Count items in list

def count_occurrences(my_list):
    '''
    This function will return a dictionary containing
    the number of occurrences of a item in a given list.
    '''
    return Counter(my_list)


def test_count_occurrences():
    my_list = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c']
    assert count_occurrences(my_list) == {'a': 3, 'b': 3, 'c': 2}


# Strings and lists

def string_to_list(my_string):
    '''
    This function takes a string and returns that string as a list.
    If a the given value is not a string. The function returns None.
    '''
    if isinstance(my_string, str):
        return list(my_string)


def test_string_to_list():
    assert string_to_list('hello world') == ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    assert string_to_list(5) == None
    assert string_to_list({'hello': 'world'}) == None
