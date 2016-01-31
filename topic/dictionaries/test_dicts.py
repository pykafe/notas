######################################################
# Dicts
# https://docs.python.org/2/library/stdtypes.html#dict
#######################################################
import pytest


def empty_dict():
    """ Return an empty dict """
    pass


def test_empty_dict():
    # check the value returned from empty_dict is a dictionary
    assert isinstance(empty_dict(), dict)
    # check that the dictionary is empty
    assert len(empty_dict()) == 0


def dict_with_one_keyvalue():
    """ Return a dictionary with only one key value pair
    the key and value can be anything you like"""
    pass


def test_dict_with_one_keyvalue():
    # check the value returned from dict_with_one_keyvalue is a dictionary
    assert isinstance(dict_with_one_keyvalue(), dict)
    # check that the dictionary is empty
    assert len(dict_with_one_keyvalue()) == 1


def value_from_dict(dictionary, key):
    """ return the value in the dictionary for the key given """
    pass


def test_value_from_dict():
    dict1 = {0: 5, 1: 50, 2: 500}
    dict2 = {0: "five", 1: "fifty", 2: "five hundred"}

    # check the method returns the correct value
    assert value_from_dict(dict1, 1) == 50
    assert value_from_dict(dict1, 2) == 500
    assert value_from_dict(dict2, 0) == "five"


def is_key_in_dict(key, dictionary):
    """ return True if the key is in the dictionary, False if not """
    pass


def test_is_key_in_dict():
    test_dict = {
        "hello": "world",
        "Michael": "Jackson",
        "Barack": "Obama"
        }

    assert is_key_in_dict("Michael", test_dict) is True
    assert is_key_in_dict("Barack", test_dict) is True
    assert is_key_in_dict("Anders", test_dict) is False


def dictionary_length(dictionary):
    """ Return the length of the dictionary, the number of key/value pairs """
    pass


def test_dictionary_length():
    test_dict = {
        "hello": "world",
        "Michael": "Jackson",
        "Barack": "Obama"
        }
    assert dictionary_length(test_dict) == 3


def add_key_value(dictionary, key, value):
    """ Add a key value pair to a dictionary """
    pass


def test_add_key_value():
    test_dict = {
        "hello": "world",
        "Michael": "Jackson",
        "Barack": "Obama"
        }

    add_key_value(test_dict, "Rui", "Araujo")
    assert test_dict["Rui"] == "Araujo"
    assert test_dict["Michael"] == "Jackson"
    assert len(test_dict) == 4


def get_dictionary_keys(dictionary):
    """ should return a list of all keys in a dictionary """
    pass


def test_get_dictionary_keys():
    test_dict = {
        "hello": "world",
        "Michael": "Jackson",
        "Barack": "Obama"
        }

    assert get_dictionary_keys(test_dict) == ['hello', 'Michael', 'Barack']


def get_dictionary_values(dictionary):
    """ should return a list of all values in a dictionary """
    pass


def test_get_dictionary_values():
    test_dict = {
        "hello": "world",
        "Michael": "Jackson",
        "Barack": "Obama"
        }

    assert get_dictionary_values(test_dict) == ['world', 'Jackson', 'Obama']


def value_from_dictionary(dictionary, key):
    """ Return the value from the dictionary stored under the key given """
    pass


def test_value_from_dictionary():
    test_dict = {
        "hello": "world",
        "Michael": "Jackson",
        "Barack": "Obama"
        }

    assert value_from_dictionary(test_dict, "Barack") == "Obama"

    # check that an assertion is raised when we try to get a key that is not in the dictionary
    with pytest.raises(KeyError):
        value_from_dictionary(test_dict, "keynotpresent")


def value_with_default(dictionary, key, default=None):
    """ return the value from the dictionary stored under the key given, if it is not present return the default supplied """
    pass


def test_value_with_default():
    test_dict = {
        "hello": "world",
        "Michael": "Jackson",
        "Barack": "Obama"
        }

    assert value_with_default(test_dict, "Barack") == "Obama"
    assert value_with_default(test_dict, "notpresent") is None
    assert value_with_default(test_dict, "notpresent", "default") == "default"
