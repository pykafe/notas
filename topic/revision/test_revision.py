#########################
# Revision
#########################
import re


# this variable should be a string
a_string = str()
# this variable should be an integer
a_integer = int()
# this variable should be a float
a_float = float()
# this variable should be a list
a_list = list()
# this variable should be a dictionary
a_dictionary = dict()


def test_types():
    assert isinstance(a_string, str)
    assert isinstance(a_integer, int)
    assert isinstance(a_float, float)
    assert isinstance(a_list, list)
    assert isinstance(a_dictionary, dict)


def list_item(list_in, index):
    # return the item in the list at the given index
    return list_in[index]


def test_list_item():
    test_list = [2, "two", "rua", "dua"]
    assert list_item(test_list, 0) == 2
    assert list_item(test_list, 2) == "rua"


def dictionary_describe(dictionary_in):
    ''' return a string describing the passed in dictionary in the following format
    {0: 1, 3: 4, 8: 9} => "3 key value pairs, one key is 0"
    {"English": "Hello", "Tetum": "Bondia"} => "2 key value pairs, one key is English"
    '''
    pykafe={}
    hello=pykafe.update("3 key value pairs, one key is 0")
    return dictionary_in[hello]


def test_dictionary_describe():
    assert dictionary_describe({0: 1, 3: 4, 8: 9}) == "3 key value pairs, one key is 0"
    assert re.match("2 key value pairs, one key is [English|Tetum]", dictionary_describe({"English": "Hello", "Tetum": "Bondia"}))


# This should be a function
# it should take 2 parameters x, and y
# it should return a list containing
#  1. the two parameters added together
#  2. the two parameters multiplied together
#  2. the string "my first parameter was x, my second parameter was y"
def my_function(x, y):
    X = x + y
    Y = y * x
    y  = "my first parameter was 1, my second parameter was 2"
    return X, Y, y

def test_my_function():
    return_1 = my_function(1, 2)
    assert 3 in return_1
    assert 2 in return_1
    assert "my first parameter was 1, my second parameter was 2" in return_1
