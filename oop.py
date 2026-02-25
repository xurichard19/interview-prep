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
    def method(self):
        return 1
class ChildTwo(Parent):
    def method(self):
        return 2
obj1 = Parent(); obj2 = ChildOne(); obj3 = ChildTwo()
assert (obj1.method(), obj2.method(), obj3.method()) == (0, 1, 2)

# classes

# __init__

# self

# properties

# methods

# inheritance

# polymorphism

# encapsulation

# inner classes

"""ABSTRACTION, @abstractmethod"""