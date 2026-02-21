# single line comment

"""
multiline comment/documentation

documentation: python basic syntax review for interview prep
"""

print(f"floor division: 5 // 3 = {5 // 3}")

print(f"division always returns a float: 5 / 3 = {5 / 3}")

# math commands: +, -, *, /, //, %, **, >, >=, ==, !=, <, <=

print(f"the bool command evaluates None, 0, and empty structs as false: bool([]) = {bool([])}")

print("the print function by default attaches a newline character to the end, we can change this using the end param", end=" ")
print("see")

"""
COMMENTED FOR SIMPLICITY
data = input("we can also recieve input from the terminal:")
print(data)
"""

# unlike in statically typed languages (java, c, cpp, go...), variables can hold any data type since
# the type checking occurs at runtime rather than compile time, meaning we dont have to declare our variables

print(f"we can oneline our evaluations and loops: print({{i for i in [1,2,3]}}) if True else print(\"wrong\")")
print({i for i in [1,2,3]}) if True else print("wrong")

print("\n------------ARRAYS------------")
arr = ["c", 2, "str", 6.2, 5*2, False]
print(f"arr = {arr}")
arr.append({2})
print(f"we can add to an array using the append method: arr.append({{2}}) = {arr}")
popped = arr.pop()
print(f"we can also pop off the end: arr.pop() -> popped {popped} off {arr}")


# COVER LANGUAGE LEVEL STATEMENTS: assignment (=, +=, -=, annotated assignment...), control flow (if, elif, else, for, while, break, continue), definition (def, class, return, yield),
# exceptions (try, except, else, finally, raise, assert), import (import, from, as), scope (global, nonlocal), del (del), context (with), switch stmt (match, case), webdev (async, await)