# the purpose of object oriented programming is to build modular applications

# oop hinges on classes
class Class:
    class_attr = True # class attributes are shared by all instances
    def __init__(self, attr): # constructor method, handles initialization of properties, automaticlly invoked
        self.attr = attr # instance attributes are unique to each instance

obj = Class(True) # an object is an instance of a class
assert obj.attr and obj.class_attr and Class.class_attr

# we have four fundamental concepts in oop: encapsulation, inheritance, abstraction, and polymorphism

# inheritance allows a child class to inherit attributes and methods from a parent class, all classes inherit from Object
class Parent:
    parent_attr = 1
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def parent_method():
        return True
class Child(Parent):
    def __init__(self, a, b, c): # by implementing init again, we are overriding the parent implementation
        self.c = c
        super().__init__(a, b) # super() returns a proxy object representing the parent class
child = Child('a', 'b', 'c')
assert child.parent_method and child.parent_attr == 1 # child may use parent attributes and methods

# python also allows for multiple inheritance
class ParentOne:
    def method(self):
        return 1
class ParentTwo:
    def method(self): # now we have two method implementations that the child could inherit..
        return 2
class Child(ParentOne, ParentTwo): # the order is relevant, more on this..
    def __init__(self):
        super().__init__() # calling super() will return the next class in the method resolution order
        # in the mro, child classes take precedence and the order of parent classes defined in a class definition is respected
child = Child()
assert child.method() == 1 # python will opt to choose the next implementation in the mro
assert Child.__mro__ == (Child, ParentOne, ParentTwo, object) # here we can see the full mro for the Child class

# we also have multilevel inheritance, where a class can inherit from another derived class

# polymorphism refers to the idea of having a method behave differently according to the object
# compile time polymorphism: method overloading (doesnt exist in python as we resolve method calls at runtime, but we can replicate)
class Class:
    # default arguments and variable length arguments can simulate overloading in that the same method can recieve differing params
    def method(self, a, b, c=1, *args, **kwargs):
        try: return (a + b) / sum(args)
        except: return c
obj = Class()
assert obj.method(2, 4) == 1
assert obj.method(2, 4, 2) == 2
assert obj.method(2, 4, 2, 1) == 6
assert obj.method(2, 4, 2, 1, 7) == 6 / 8

# runtime polymorphism: method overriding
class Parent:
    def method(self):
        return 0
class ChildOne(Parent):
    def method(self): # we override the parent behavior of method
        return 1
class ChildTwo(Parent):
    def method(self): # we override the parent behavior of method
        return 2
obj1 = Parent(); obj2 = ChildOne(); obj3 = ChildTwo()
# method() behaves differently according to the object we call it from
assert (obj1.method(), obj2.method(), obj3.method()) == (0, 1, 2)

# built in functions like len() and max() are polymorphic as they behave according to the type of object passed
assert len("str") == 3 and len((1,2,3)) == 3 # string length vs tuple length

# encapsulation refers to the idea of grouping data and methods together (into classes) and hiding internal 
# details of a class and only allowing interaction with a controlled public interface
class Class:
    def __init__(self, public, protected, private):
        self.public = public # accessed anywhere outside class
        self._protected = protected # python does not enforce this, hint for developer for internal use
        self.__private = private # python does not strictly enforce this, instead converts the name to ._Class__private to discourage use
    def method(self): # public method
        return 0
    def _method(self): # protected method
        return 1
    def __method(self): # private method
        return 2
    def set_var(self, arg): # its good practice to utilize getter and setter methods to safely update private data
        self.__private = arg
    def get_var(self):
        self.__private
obj = Class(0, 1, 2)
assert obj.public == 0 and obj._protected == 1 and obj._Class__private == 2
assert obj.method() == 0 and obj._method() == 1 and obj._Class__method() == 2
obj.set_var(False)
assert not obj.get_var()

# data abstraction refers to the idea of hiding implementation details and only showing high-level features
from abc import ABC, abstractmethod # we have to import the abstract base classes module to use the abstractmethod decorator
class Blueprint(ABC): # our 'blueprint' class must inherit from ABC to enforce rules
    @abstractmethod # decorator that means subclasses MUST override this method
    def method(self):
        pass # we dont implement abstract methods, but of course python doesnt enforce this either

    # we can also force subclasses to have properties by combining the property and abstractmethod decorators
    @property # the property decorator allows us to access the class using the standard dot operator without parenthesis
    @abstractmethod
    def attr(self):
        pass
class Class(Blueprint):
    # we wont be able to instantiate any instances of class without implementing method() and attr()
    def method(self): # we now make a concrete implementation of method() in the child class
        return True
    
    @property
    def attr(self):
        return True
# bp = Blueprint() will return a TypeError, we cant instantiate abstract classes
obj = Class()
assert obj.method() and obj.attr
# abstraction in python is not required or very useful for that matter...