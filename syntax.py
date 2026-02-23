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
    return local_v
assert func(1,2) == 2 # type hinting does not force static typing, rather serves as hints for developing

# python does not support function overloading (overwritten), but we can use default arguments to replicate varying arguments
def eligibility(name, tent, age=20, eligible=False): # nondefault args must come before default args
    tent += 1
    return f"{name} is {"not " if age < 15 or not eligible else ""}eligible"
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
ahh = [2,5,1,7,3,10]
assert args_example(*ahh) == 21
agg = {"v1": 2, "v2":1, "mog":True, "job":None}
assert kwargs_example(**agg) # ** operator must unpack a mapping

# functions in python are treated as first class objects (assignable, passable, returnable, storable)
def zyn_vending_machine_factory(id):
    def zyn_vending_machine(count):
        return f"id {id}, {count} zyns"
    return zyn_vending_machine # return a function
zvm = zyn_vending_machine_factory("wef0ngdfb") # assign function to a variable
assert zvm(0) == "id wef0ngdfb, 0 zyns"

# lambda functions in python allow us to create anonymous temporary functions, lambda args: expression
assert (lambda x: x + 2)(2) == 4
# lambda functions can be a powerful tool for functions that accept other functions as arguments
d = [1, 4, 7, 3, 4]
assert list(map(lambda x: x / 2, d)) == [0.5, 2.0, 3.5, 1.5, 2.0]
# also very useful in sorting complicated collections
ed = {"ima hogg":23, "amillion buggs":19, "olive garden":27, "apple":2}
assert sorted(ed, key=lambda x: ed[x]) == ['apple', 'amillion buggs', 'ima hogg', 'olive garden']

#-----------------------------MODULE-----------------------------
# we import modules using the import keyword, we can examine the functions/attributes in a module with dir()
# most useful standard modules in python (installation not required)...
import os
import sys
import math # standard math functions
import re
import collections # data structures, queue/stack and heap implementations in particular
import unittest

#------------------------------CLASS------------------------------


# COVER LANGUAGE LEVEL STATEMENTS: assignment (=, +=, -=, annotated assignment...), control flow (if, elif, else, for, while, break, continue), definition (def, class, return, yield),
# exceptions (try, except, else, finally, raise, assert), import (import, from, as), scope (global, nonlocal), del (del), context (with), switch stmt (match, case), webdev (async, await)\

# cover common development practices (type hinting)

# cover function decorators, *args, **kwargs, lambda functions
