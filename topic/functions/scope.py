# this variable is global scope
name = "Peter"


# this function is in global scope
def say_my_name(name="Anders"):
    # the variable, or parameter name is in the functions local scope
    print "Hello", name


# this prints the global variable name
print "Hello", name

# this calls the function say_my_name
say_my_name()
say_my_name("David")
