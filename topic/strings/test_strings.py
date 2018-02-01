# Strings

def hello_world():
    ''' This function returns 'Hello World' '''
    return 'Hello World'


def test_hello_world():
    assert hello_world() == 'Hello World'


def string_to_list(my_string):
    ''' This function takes a string and returns that string as a list.
        If a the given value is not a string. The function returns None.
        return list(my_string)'''
    if type(my_string) is str:
        return list(my_string)
    else:
        return None


def test_string_to_list():
    assert string_to_list('hello world') == ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    assert string_to_list(5) == None
    assert string_to_list({'hello': 'world'}) == None
