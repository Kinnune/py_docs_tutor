#!/usr/local/bin/python3

num_in = int(input("Fibonacci sequence up to: "))

def print_fib(n):
	"""Print fibonacci numbers up to n."""
	a, b = 0, 1
	while a < n:
		print(a, end = ' ')
		a, b = b, a + b
	print()

def return_fib(n):
	"""Return a list of integers from \
	the fibonacci series not exceeding n."""
	a, b = 0, 1
	result = []
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result
print_fib(num_in)
print(return_fib(num_in))
