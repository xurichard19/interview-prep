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
assert [i for i in "str"] if edit else print("failed") == ['s','t','r']

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
# declare with {}, o(1) search, keys must be immutable, items maintain order post-python3.7
dict = {"f":1, 3:0, "s":10, False:True}

# we can create an iterable for the keys and values of a dict using the keys() and values() methods
assert list(dict.keys()) == ['f', 3, 's', False]
assert list(dict.values()) == [1, 0, 10, True]

# we can unpack dictionaries using the ** operator
assert "s" in {'9':9, "t":False, **dict, "f":None}

#-------------------------------SET-------------------------------
# declare with {}, o(1) search, elements must be immutable
s = set()
s.add(1)
assert 1 in s

try:
    s.add([2,3])
except:
    pass
assert(len(s) == 1)

# we can perform operations on sets
assert {2, 6, 3, 1} & {4, 2, 1} == {2, 1} # intersection
assert {2, 6, 3, 1} | {4, 2, 1} == {2, 6, 3, 1, 4} # union
assert {2, 6, 3, 1} - {4, 2, 1} == {6, 3} # difference
assert not {2, 6, 3, 1} <= {4, 2, 1} # is subset of

#---------------------------CONTROL FlOW---------------------------
# indentation is necessary in python since we do not use ;

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







# COVER LANGUAGE LEVEL STATEMENTS: assignment (=, +=, -=, annotated assignment...), control flow (if, elif, else, for, while, break, continue), definition (def, class, return, yield),
# exceptions (try, except, else, finally, raise, assert), import (import, from, as), scope (global, nonlocal), del (del), context (with), switch stmt (match, case), webdev (async, await)\

# cover common development practices (type hinting)

# cover function decorators, *args, **kwargs, lambda functions
