#!/usr/local/bin/python3

a = ["Mary", "had", "a", "little", "lamb"]
i = 0

for i in range(5):
	print(i)

i = 0
for i in range(5, 10):
	print(i)

print()
i = 0
for i in range(5, 10, 2):
	print(i)

print()
i = 0
for i in range(0, -5, -1):
	print(i)

print()
i = 0
for i in range(len(a)):
	print(i, a[i])

print("\n" + str(sum(range(4))))
