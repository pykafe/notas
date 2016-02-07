########################
# tests for functions
# ALL your functions, except one should have only one line 'pass' in them
########################
import pytest

# make my_function a function that can be called with no variables
# the body of your function should be one line: pass
my_simple_function = "this is not a function. Tenki troka"


def test_my_function():
    # this line will raise an error if my_function is not callable
    my_simple_function()
    # if your function accepts any variables, this test will fail
    with pytest.raises(TypeError):
        my_simple_function(1)


# make my_returning_function a function that returns a value that does not evaluate to false
# this function is the only one you need to write a body for - you must return something
my_function_returns_something = "this is not a function. Tenki troka"


def test_my_function_returns_something():
    # this line will assert, fail the test, if my_returning_function returns a non true value
    returned_value = my_function_returns_something()
    assert returned_value
    # if your function accepts any variables, this test will fail
    with pytest.raises(TypeError):
        my_function_returns_something(1)


# make my_function_with_parameter a function that takes a parameter
# the body of your function should be one line: pass
my_function_with_parameter = "this is not a function. Tenki troka"


def test_my_function_with_parameter():
    # this line will assert if your function does not accept a parameter
    my_function_with_parameter("a value")
    # if your function accepts no variables, or more than one variable this test will fail
    with pytest.raises(TypeError):
        my_function_with_parameter()
        my_function_with_parameter("a value", "another value")


# make my_function_three_parameters a function that takes three parameters
# the body of your function should be one line: pass
my_function_three_parameters = "this is not a function. Tenki troka"


def test_my_function_three_parameters():
    # this line will assert if your function does not accept a parameter
    my_function_three_parameters("a value", 23, ["this", "is", "a", "list"])
    # if your function accepts anythin else expect 3 variables this test will fail
    with pytest.raises(TypeError):
        my_function_three_parameters()
        my_function_three_parameters("a value", "another value")
        my_function_three_parameters("a value", "another value", 2, 5)


# make my_function_optional_parameter a function which can take a parameter, or not
# the body of your function should be one line: pass
my_function_optional_parameter = "this is not a function. Tenki troka"


def test_my_function_optional_parameter():
    # this line checks we can call the function without a parameter
    my_function_optional_parameter()
    # this line checks we can call the function with a parameter
    my_function_optional_parameter("a value")
    # if your function accepts more than 1 parameter this test will fail
    with pytest.raises(TypeError):
        my_function_optional_parameter(1, 2)


# make a function with 1 required parameter and 1 optional parameter
# the body of your function should be one line: pass
my_function_one_required_one_optional = "this is not a function. Tenki troka"


def test_my_function_one_required_one_optional():
    # this line will assert if your function does not accept a parameter
    my_function_one_required_one_optional("first")
    # this line will assert if your function does not accept 2 parameters
    my_function_one_required_one_optional("first", "second")
    # this will fail if your function accepts no parameters, or more than 2 parameters
    with pytest.raises(TypeError):
        my_function_one_required_one_optional()
        my_function_one_required_one_optional("first", "second", "third")


# make a function that takes two named parameters - name your parameters param_a and param_b
# the body of your function should be one line: pass
my_function_two_named = "this is not a function. Tenki troka"


def test_my_function_two_named():

    # your function should have default values so can be called with no parameters
    my_function_two_named()
    # your function should have default values so can be called with one parameter
    my_function_two_named(1)
    # your function can decide which parameter is which based on the prder they are given
    my_function_two_named(1, 2)
    # your function can decide which parameter is which based on the names given
    my_function_two_named(param_a=1, param_b=2)
    # your function can decide which parameter is which based on the names given
    my_function_two_named(param_b=1, param_a=2)
    # this will fail if your function accepts more than 2 parameters
    with pytest.raises(TypeError):
        my_function_two_named(1, 2, param_b=1, param_a=2)


# This function accepts any number of unnamed arguments
# the body of your function should be one line: pass
my_function_many_arguments = "this is not a function. Tenki troka"


def test_my_function_many_arguments():
    my_function_many_arguments()
    my_function_many_arguments(3, 4)
    my_function_many_arguments(3, 4, 5)
    my_function_many_arguments(3, 4, 5, 6, 7, 8, 23, "heello", "any number of arguments can be passed to this function")


# This function accepts any number of keyword arguments
# the body of your function should be one line: pass
my_function_many_keyword_arguments = "this is not a function. Tenki troka"


def test_my_function_many_keyword_arguments():
    my_function_many_keyword_arguments()
    my_function_many_keyword_arguments(a_keyword=3, another_keyword=4)
    my_function_many_keyword_arguments(a_keyword=3, another_keyword=4, idatan_keyword=5)
