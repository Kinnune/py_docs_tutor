#!/usr/local/bin/python3

heroes = ["lina", "pudge", "disruptor", "invoker"]
print("default:", heroes)

heroes_cpy = heroes.copy()
print("copied list:", heroes_cpy)

heroes.append("axe")
print("axe appended:", heroes)

axe_in = heroes.index("axe")
print("axe indexed at:", axe_in)

heroes.extend(["techies", "meepo"])
print("extending by two:", heroes)

boomer = heroes.pop(-2)
print("popped", boomer + ":", heroes)

heroes.insert(0, "meepo")
print("meepo inserted ulti lvl:", heroes)

meepo_total = heroes.count("meepo")
print("meepo count:", meepo_total)

while "meepo" in heroes:
	heroes.remove("meepo")
print("removed meepos:", heroes)

heroes.sort(key=len)
print("sorted by length:", heroes)

heroes.reverse()
print("and reveresed:", heroes)

heroes.clear()
print("list cleared:", heroes)
print("but not copy:", heroes_cpy)