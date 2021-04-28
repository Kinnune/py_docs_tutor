#!/usr/local/bin/python3

args = [3, 6]
print(list(range(*args)))
# same as calling the function with ALL indexes
print(list(range(args[0], args[1])))

# * is the operator for lists and tuples
# ** for dictionaries (1st star for key second for value)
