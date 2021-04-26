#!/usr/local/bin/python3

x = int(input("Please enter a number: "))

if x < 0:
	x = 0
	print("Negative changed to 0")
elif x == 42:
	print("You have the answer")
else:
	print("You entered", x)
