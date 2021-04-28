#!/usr/local/bin/python3

# standard_arg(1), standard_arg(arg=1)
def standard_arg(arg):
    print(arg)

# pos_only_arg(1)
def pos_only_arg(arg, /):
    print(arg)

# kwd_only_arg(arg=1)
def kwd_only_arg(*, arg):
    print(arg)

# combined(1, 2, kwd_only=3), combined(1, standard=2, kwd_only=3)
def combined(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# here key_words dictionary allows key named name
def no_clash(name, /, **key_words):
    pass

# *name and **name may be used to create a variadict function
# that receives a tuple and a dictionary respectively