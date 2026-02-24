# single line comment

"""
multiline comment/documentation

python basic syntax review for interview prep
"""

# data types (at least the common ones)...
# immutable
str, int, float, tuple, range, bool, bytes, None
# mutable
list, dict, set

"""
important built-in functions (that i use):

abs(numeric) - return absolute value
dir(object) - return list of attributes and/or methods associated with the object (or current scope when no arg)
enumerate(iterable) - return an iterator that maps each element to its index
hash(object) - return hash value of object
input(prompt) - accept command line input from user
isinstance(object, class) - return bool of if object is an instance of class
len(object) - return size of object (str, collection)
max(iterable) - return max element of iterable
min(iterable) - return min element of iterable
open(file, mode) - return file object (r - reading, w - writing, a - append)
print(string) - print string, commonly use string formatting like so: print(f"..{data}..")
range(start(op), stop, step(op)) - return range object with sequence of integers from start to stop (exclusive)
round(numeric, precision) - return number rounded to a precision
sorted(iterable) - return a new o(nlogn) powersorted list
sum(iterable) - return sum of elements in an iterable
type(object) - return type of object
zip(iterables) - return iterator with tuples containing elements from each iterable at each index
"""

# type 'casting' in python creates a new object rather than modifying the actual datatype
bool(), dict(), float(), int(), list(), set(), str(), tuple()

# unlike in statically typed languages (java, c, cpp, go...), variables can hold any data type since
# the type checking occurs at runtime rather than compile time, meaning we dont have to declare our variables

# we can write our loops and conditionals in one line
edit = True # edit this variable to False
assert ([i for i in "str"] if edit else print("failed")) == ['s','t','r']

#------------------------------LIST------------------------------
# declare with [], mutable (and therefore dynamic), overallocates memory
arr = ["c", 2, "str", 6.2, 5*2, False]

# we can add to a list by using the append method or concatenating
arr.append({2})
assert arr == ["c", 2, "str", 6.2, 5*2, False, {2}]

# we can remove from a list at an index using pop (defaults to -1)
popped = arr.pop()
assert arr == ["c", 2, "str", 6.2, 5*2, False]

# slicing works like [start : end(op) : step(op)], start moves towards end with step
assert arr[5:1:-1] == [False, 10, 6.2, 'str']

#------------------------------TUPLE------------------------------
# declare with (), immutable, faster indexing
# operations largely remain the same as lists (ex. indexing, len, slicing...) with the exception of in-place modifications

# we can unpack all iterables (but usually tuples) like so...
a, b, c = (1,2,3)
assert a == 1 and b == 2 and c == 3

#----------------------------DICTIONARY----------------------------
# declare with {}, o(1) search average, keys must be hashable (immutable), items maintain order post-python3.7
d = {"f":1, 3:0, "s":10, False:True}

# we can create an iterable for the keys and values of a dict using the keys() and values() methods
assert list(d.keys()) == ['f', 3, 's', False]
assert list(d.values()) == [1, 0, 10, True]

# we can unpack dictionaries using the ** operator (this has many more uses, more on this later)
assert "s" in {'9':9, "t":False, **d, "f":None}

#-------------------------------SET-------------------------------
# declare with set() or {...}, o(1) search average, elements must be hashable (immutable)
s = set()
s.add(1)
assert 1 in s

try:
    s.add([2,3])
except TypeError:
    pass
assert(len(s) == 1)

# we can perform operations on sets
assert {2, 6, 3, 1} & {4, 2, 1} == {2, 1} # intersection
assert {2, 6, 3, 1} | {4, 2, 1} == {2, 6, 3, 1, 4} # union
assert {2, 6, 3, 1} - {4, 2, 1} == {6, 3} # difference
assert not {2, 6, 3, 1} <= {4, 2, 1} # is subset of

#---------------------------CONTROL FlOW---------------------------
# indentation is necessary in python since we are not required to use ; (can optionally be used as a separator)

# we have an equivalent to switch statements in python...
m = 2
a = None
match m:
    case 1:
        raise ValueError
    case 2:
        a = True
    case _: # default case
        raise ZeroDivisionError
assert a

# loops can take any iterable/iterator...
assert [i for i in enumerate([3,5,1])] == [(0, 3), (1, 5), (2, 1)]
assert [i for i in "str"] == ["s", "t", "r"]

# we handle exceptions in try except else blocks
try:
    raise IndentationError("message")
except (TimeoutError, NameError):
    raise BufferError
except IndentationError as e:
    pass
else: pass

# the with keyword allows python to automatically manage setup and cleanup operations
with open("README.md", "r", encoding="utf-16") as f:
    assert f.readlines()[1] == 'i review python, dsa, oop, testing, django, react, and sql\n'

#----------------------------FUNCTION----------------------------
# we create using def keyword, pass in arguments as parameters, variables are contained in the local scope (unless we use the global keyword)
def func(param1: int, param2: str) -> bool: # type hinting is a good coding practice
    local_v: int = param1 + 1 # typed assignment
    return local_v > 1
assert func(1,2) # type hinting does not force static typing, rather serves as hints for developing

# python does not support function overloading (overwritten), but we can use default arguments to replicate varying arguments
def eligibility(name, tent, age=20, eligible=False): # nondefault args must come before default args
    tent += 1
    return f"{name} is {'not ' if age < 15 or not eligible else ''}eligible"
assert "bart is eligible" == eligibility("bart", eligible=True, tent=2) # keyword args (pass explicitly with param name) can be written in any order

# we can create functions that use a variable number of arguments using *args and **kwargs
def args_example(v1, v2, *vn: int): # we arent strictly required to name it args, the functionality hinges on the * operator
    assert type(vn) == tuple # the * operator will combine the remaining arguments into a tuple
    return sum(vn)
assert args_example(1,2,43,2,4,32) == 81
def kwargs_example(v1, v2, **args): # we also do not need to name kwargs
    assert type(args) == dict # the ** operator creates a dictionary using the remaining keyword arguments
    return {i for i in args.values()}
assert "forex" in kwargs_example("mr beats contestant", 1, indoor_shrimp_farming=True, occupation="forex")
# we can use *args and **kwargs in the same function but i didnt for a clearer explanation

# we can also use the * and ** operators in reverse to unpack arguments into a function...
a = [2,5,1,7,3,10]
assert args_example(*a) == 21
b = {"v1": 2, "v2":1, "v3":True, "v4":None}
assert kwargs_example(**b) # ** operator must unpack a mapping

# functions in python are treated as first class objects (assignable, passable, returnable, storable)
def create(id):
    def f(count):
        return f"id {id}, {count} zyns"
    return f # return a function
zvm = create(12) # assign function to a variable
assert zvm(0) == "id 12, 0 zyns"

# lambda functions in python allow us to create anonymous temporary functions, lambda args: expression
assert (lambda x: x + 2)(2) == 4
# lambda functions can be a powerful tool for functions that accept other functions as arguments
d = [1, 4, 7, 3, 4]
assert list(map(lambda x: x / 2, d)) == [0.5, 2.0, 3.5, 1.5, 2.0]
# also very useful in sorting complicated collections
ed = {"c":23, "b":19, "olive garden":27, "a":2}
assert sorted(ed, key=lambda x: ed[x]) == ['a', 'b', 'c', 'olive garden']

#-----------------------------MODULE-----------------------------
# we import modules using the import keyword, we can examine the functions/attributes in a module with dir()
# most useful standard modules in python (installation not required)...
import os # interact with operating system
import sys # interact with python interpreter and runtime env
import math # standard math functions
import collections # data structures, queue/stack and heap implementations in particular
import unittest # standard testing module

# we can import under an alias or import specific functions from a module
import json as j
from keyword import iskeyword

#------------------------------CLASS------------------------------
# declare with class keyword, classes can have attributes methods and dunder methods (like __init__)
class Example:
    count = 0 # class variable, associated with the class
    
    # we can describe how our object behaves upon initialization
    def __init__(self, id: str, arg: int=0) -> None: # dunder methods dictate how the class interacts with built-in python operations
        self.arg = arg # instance variable, is tied to the instance of Example
        Example.count += 1
        self._key = hash(id) # convention representing internal use, python does not enforce this (it rarely enforces anything for that matter)

    # instance methods operate on a specific instance of a class, take self as a param
    def imethod(self):
        return self.arg
    
    # class methods is shared between all instances, 
    @classmethod # function decorators modify the behavior of a function
    def cmethod(cls): # cls is equivalent as self, class methods automatically take cls as a parameter
        return cls.count
    
    # static methods have no implicit first arg like self or cls
    @staticmethod
    def smethod(x, y):
        return max(x,y)

ex1 = Example('7')
ex2 = Example('4', 1)
ex3 = Example('8')
assert Example.cmethod() == 3 # weve initialized 3 instances of Example, incrementing count 3 times
assert Example.smethod(2,6) == 6 # static methods are still required to be called using the class or an instance of the class

# python supports object oriented programming concepts (but also procedural, etc.) like inheritance, polymorphism, and abstraction...
# inheritance: child class inherits attributes and methods from parent class
class MiniExample(Example):

    # the child with automatically inherit the parent constructor, and overriding it by writing a new __init__ allows us to add new fields or scrap it entirely
    def __init__(self, id, st, arg=0, fault=True):
        self.st = st
        self.fault = fault
        super().__init__(id, arg) # super() returns a proxy parent object

    # polymorphism: functions with the same name can be executed differently across different objects (like len() works differently for a str vs a list)
    # an example of this is overriding a function from the parent class
    def imethod(self):
        return self.arg + 3

mex = MiniExample("2", "g")
assert isinstance(mex, MiniExample) and isinstance(mex, Example)

# child instances may use functions implemented in the parent class
assert mex.cmethod() == 4 # our inherited init function updates count in Example from 3 -> 4
assert mex.imethod() == 3 and not mex.imethod() == 0 # imethod() has been overwritten

# python also supports multiinheritance...
class Parent1:
    def __init__(self, a):
        self.a = a
    def num(self):
        return 1
class Parent2:
    def __init__(self, b):
        self.b = b
    def num(self):
        return 2
class Child(Parent2, Parent1):
    def __init__(self, a, b):
        # super only works in the next base class in the method resolution order, meaning we have to explicitly call init for each parent
        Parent1.__init__(self, a)
        Parent2.__init__(self, b)
child = Child('a', 'b')
# to resolve the diamond problem, python has a method resolution order that dictates which implementation of a method it uses
assert Child.__mro__ == (Child, Parent2, Parent1, object)
# the order is based on the order in which the parent classes are listed in the child class definition, hence the implementation in parent2 takes precedence
assert child.num() == 2
