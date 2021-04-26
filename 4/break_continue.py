#!/usr/local/bin/python3

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, "is not prime", x, "*", n//x)
			break
	else:
		print(n, "is prime")

for num in range(1, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
	print("Found an odd number", num)
