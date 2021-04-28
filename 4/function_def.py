#!/usr/local/bin/python3

num_in = int(input("Fibonacci sequence up to: "))

def print_fib(n):
    """Print Fibonacci numbers up to n"""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()
print_fib(num_in)

def return_fib(n):
    """Return a list of integers from the Fibonacci series never exceeding n."""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
print(return_fib(num_in))

# help(return_fib)