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
