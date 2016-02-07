########################
# tests for functions
########################
import pytest

# make my_function a function that can be called with no variables
# it does not need to do anything, just be callable
my_simple_function = "this is not a function. Tenki troka"


def test_my_function():
    # this line will raise an error if my_function is not callable
    my_simple_function()


# make my_returning_function a function that returns a value that does not evaluate to false
my_function_returns_something = "this is not a function. Tenki troka"


def test_my_function_returns_something():
    # this line will assert, fail the test, if my_returning_function returns a non true value
    returned_value = my_function_returns_something()
    assert returned_value


# make my_function_with_parameter a function that takes a parameter
my_function_with_parameter = "this is not a function. Tenki troka"


def test_my_function_with_parameter():
    # this line will assert if your function does not accept a parameter
    my_function_with_parameter("a value")


# make my_function_three_parameters a function that takes three parameters
my_function_three_parameters = "this is not a function. Tenki troka"


def test_my_function_three_parameters():
    # this line will assert if your function does not accept a parameter
    my_function_three_parameters("a value", 23, ["this", "is", "a", "list"])


# make my_function_optional_parameter a function which can take a parameter, or not
my_function_optional_parameter = "this is not a function. Tenki troka"


def test_my_function_optional_parameter():
    # this line checks we can call the function without a parameter
    my_function_optional_parameter()
    # this line checks we can call the function with a parameter
    my_function_optional_parameter("a value")


# make a function with 1 required parameter and 1 optional parameter
my_function_one_required_one_optional = "this is not a function. Tenki troka"


def test_my_function_one_required_one_optional():
    # this line will assert if your function does not accept a parameter
    my_function_one_required_one_optional("first")
    # this line will assert if your function does not accept 2 parameters
    my_function_one_required_one_optional("first", "second")
    # this will fail if your function accepts more than 2 parameters
    with pytest.raises(TypeError):
        my_function_one_required_one_optional("first", "second", "third")


# make a function that takes two named parameters - name your parameters param_a and param_b
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


# make a function that changes the value of the parameter passed to it
my_function_changes_parameter_value = "this is not a function. Tenki troka"


def test_my_function_changes_parameter_value():
    # set a variable to a value
    my_variable = 5
    # pass that variable into our function
    my_function_changes_parameter_value(my_variable)
    # fail the test if the value of the variable has not changed
    assert my_variable != 5


# This function accepts any number of unnamed arguments
my_function_many_arguments = "this is not a function. Tenki troka"


def test_my_function_many_arguments():
    my_function_many_arguments()
    my_function_many_arguments(3, 4)
    my_function_many_arguments(3, 4, 5)
    my_function_many_arguments(3, 4, 5, 6, 7, 8, 23, "heello", "any number of arguments can be passed to this function")


my_function_many_keyword_arguments = "this is not a function. Tenki troka"


def test_my_function_many_keyword_arguments():
    my_function_many_keyword_arguments()
    my_function_many_keyword_arguments(a_keyword=3, another_keyword=4)
    my_function_many_keyword_arguments(a_keyword=3, another_keyword=4, idatan_keyword=5)
