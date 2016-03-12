# give this base class a method called hello
class BaseClass(object):
    pass


# Make this class inherit from BaseClass
class ClassOne(object):
    pass


def test_inheritance():
    """ ClassOne should inherit from BaseClass """
    class_one = ClassOne()

    # this assert will fail the test if the class_one instance is not an instance of the class BaseClass
    assert isinstance(class_one, BaseClass)


def test_method():
    """ BaseClass should have a method called hello """
    base = BaseClass()
    class_one = ClassOne()

    # this line will throw an exception if the base object does not have a hello method
    base.hello()
    # this line will throw an exception if the class_one object does not have a hello method
    class_one.hello()


def test_property():
    """ ClassOne should have an instance variable 'name' """

    class_one = ClassOne()
    assert hasattr(class_one, 'name')
    assert not hasattr(ClassOne, 'name'), "You have created a class variable, not an instance variable"


# A new class
Dog = 'this is a string, you must make it a class'


def test_dog():
    dog = Dog()
    assert isinstance(dog, Dog)


# A class with a constructor that takes a name paramter
# in teh constructor create an instance variable 'name' and assign the name parameter value to it
Cat = 'this is a string, you must make it a class'


def test_cat():
    cat = Cat('Busa')
    assert isinstance(cat, Cat)
    assert cat.name == 'Busa'
