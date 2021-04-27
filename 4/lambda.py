#!/usr/local/bin/python3

def make_incrementor(plus):
    """Returns a function that increments its argument by plus."""
    return lambda number : number + plus
plus_two = make_incrementor(2)
plus_hundred = make_incrementor(100)
print(plus_two(2))
print(plus_hundred(-98))

print_stuff = lambda stuff : print(stuff)
print_stuff("things")