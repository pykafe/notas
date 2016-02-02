######################################################
# Dicts
# https://docs.python.org/2/library/stdtypes.html#dict
# all functions can be completed using ONE LINE ONLY
#######################################################
import pytest


def empty_dict():
    """ Return an empty dict """
    empty_dict = dict()
    return empty_dict


def test_empty_dict():
    # check the value returned from empty_dict is a dictionary
    assert isinstance(empty_dict(), dict)
    # check that the dictionary is empty
    assert len(empty_dict()) == 0


def dict_with_one_keyvalue():
    """ Return a dictionary with only one key value pair
    the key and value can be anything you like"""
    my_dict = {'my_name': 'niko'}
    return my_dict


def test_dict_with_one_keyvalue():
    # check the value returned from dict_with_one_keyvalue is a dictionary
    assert isinstance(dict_with_one_keyvalue(), dict)
    # check that the dictionary is empty
    assert len(dict_with_one_keyvalue()) == 1


def value_from_dict(dictionary, key):
    """ return the value in the dictionary for the key given """
    if key in dictionary:
        return dictionary[key]
    else:
        return dictionary[key, "keynotpresent"]


def test_value_from_dict():
    test_dict = {
        "hello": "world",
        "Michael": "Jackson",
        "Barack": "Obama"
        }

    # check the method returns the correct value
    assert value_from_dict(test_dict, 'hello') == 'world'
    assert value_from_dict(test_dict, 'Michael') == 'Jackson'
    with pytest.raises(KeyError):
        value_from_dict(test_dict, "keynotpresent")


def is_key_in_dict(key, dictionary):
    """ return True if the key is in the dictionary, False if not """
    return key in dictionary


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
    return len(dictionary)


def test_dictionary_length():
    test_dict = {
        "hello": "world",
        "Michael": "Jackson",
        "Barack": "Obama"
        }
    assert dictionary_length(test_dict) == 3


def add_key_value(dictionary, key, value):
    """ Add a key value pair to a dictionary """
    return dictionary.update({key: value})


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
    return dictionary.keys()


def test_get_dictionary_keys():
    test_dict = {
        "hello": "world",
        "Michael": "Jackson",
        "Barack": "Obama"
        }

    assert 'hello' in get_dictionary_keys(test_dict)
    assert 'Michael' in get_dictionary_keys(test_dict)
    assert 'Barack' in get_dictionary_keys(test_dict)
    assert isinstance(get_dictionary_keys(test_dict), list)
    assert len(get_dictionary_keys(test_dict)) == 3


def get_dictionary_values(dictionary):
    """ should return a list of all values in a dictionary """
    return dictionary.values()


def test_get_dictionary_values():
    test_dict = {
        "hello": "world",
        "Michael": "Jackson",
        "Barack": "Obama"
        }

    assert 'world' in get_dictionary_values(test_dict)
    assert 'Jackson' in get_dictionary_values(test_dict)
    assert 'Obama' in get_dictionary_values(test_dict)
    assert isinstance(get_dictionary_values(test_dict), list)
    assert len(get_dictionary_values(test_dict)) == 3


def value_with_default(dictionary, key, default=None):
    """ return the value from the dictionary stored under the key given, if it is not present return the default supplied """
    if key in dictionary:
        return dictionary[key]
    else:
        return default


def test_value_with_default():
    test_dict = {
        "hello": "world",
        "Michael": "Jackson",
        "Barack": "Obama"
        }

    assert value_with_default(test_dict, "Barack") == "Obama"
    assert value_with_default(test_dict, "notpresent") is None
    assert value_with_default(test_dict, "notpresent", "default") == "default"


def remove_key(dictionary, key):
    """ Remove a key value pair from the dictionary """
    remove_key = dictionary.pop(key)
    return remove_key


def test_remove_key():
    test_dict = {
        "hello": "world",
        "Michael": "Jackson",
        "Barack": "Obama"
        }

    remove_key(test_dict, 'hello')
    assert 'hello' not in test_dict


def return_and_remove_key(dictionary, key):
    """ remove a key from the dictionary and return it's value """
    remove_value = dictionary.pop(key)
    return remove_value


def test_remove_and_return_key():
    test_dict = {
        "hello": "world",
        "Michael": "Jackson",
        "Barack": "Obama"
        }

    value = return_and_remove_key(test_dict, 'hello')
    assert value == 'world'
    assert 'hello' not in test_dict
