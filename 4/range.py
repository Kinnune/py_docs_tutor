#!/usr/local/bin/python3

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
song = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(song)):
    print(i, song[i])

# sum iterates and adds the elements found from the
# object returned by range which is not in fact a list
print("\n" + str(sum(range(4))))
