#########################
# Revision
#########################
import re


# this variable should be a string
a_string = None
# this variable should be an integer
a_integer = None
# this variable should be a float
a_float = None
# this variable should be a list
a_list = None
# this variable should be a dictionary
a_dictionary = None


def test_types():
    assert isinstance(a_string, str)
    assert isinstance(a_integer, int)
    assert isinstance(a_float, float)
    assert isinstance(a_list, list)
    assert isinstance(a_dictionary, dict)


def list_item(list_in, index):
    # return the item in the list at the given index
    pass


def test_list_item():
    test_list = [2, "two", "rua", "dua"]
    assert list_item(test_list, 0) == 2
    assert list_item(test_list, 2) == "rua"


def dictionary_describe(dictionary_in):
    ''' return a string describing the passed in dictionary in the following format
    {0: 1, 3: 4, 8: 9} => "3 key value pairs, one key is 0"
    {"English": "Hello", "Tetum": "Bondia"} => "2 key value pairs, one key is English"
    '''
    pass


def test_dictionary_describe():
    assert dictionary_describe({0: 1, 3: 4, 8: 9}) == "3 key value pairs, one key is 0"
    assert re.match("2 key value pairs, one key is [English|Tetum]", dictionary_describe({"English": "Hello", "Tetum": "Bondia"}))


# This should be a function
# it should take 2 parameters x, and y
# it should return a list containing
#  1. the two parameters added together
#  2. the two parameters multiplied together
#  2. the string "my first parameter was x, my second parameter was y"
my_function = "this is a string, not a function. please change it"


def test_my_function():
    return_1 = my_function(1, 2)
    assert 3 in return_1
    assert 2 in return_1
    assert "my first parameter was 1, my second parameter was 2" in return_1
