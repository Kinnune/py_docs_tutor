#!/usr/local/bin/python3

i = 0
# demonstrates when the evaluation for default arguments happens
# notice that i gets a new value right after the function
# and before it is called
def eval_demo(num = i):
    print(num)
i = 5
eval_demo()

# empty on the 1st call but keeps appended values on subsequent ones
def list_def_demo(num, empty=[]):
    empty.append(num)
    return empty
print(list_def_demo(1))
print(list_def_demo(2))
print(list_def_demo(5, []))
print(list_def_demo(3))
print("----------")
# here there is no default list and a empty one is created
# everytime one is not provided
def list_def_demo2(num, empty=None):
    if empty == None:
        empty = []
    empty.append(num)
    return empty
print(list_def_demo2(1))
print(list_def_demo2(2))

def ask_ok(prompt, retries=4, reminder="Please try again"):
    while True:
        ok = input(prompt)
        if ok in ("y", "ye", "yes"):
            return True
        if ok in ("n", "no", "nop", "nope"):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)
print(ask_ok("yes or nope: "))
print(ask_ok("yes or nope round 2: ", reminder = "fail"))
