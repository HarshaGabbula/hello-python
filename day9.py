# Day 9: Tuples and sets

# Tuple example
colors = ("red", "green", "blue", "yellow")
print("tuple:", colors)

print("First color:", colors[0])
print("Last color:", colors[-1])
print("Slice first two colors:", colors[:2])

colors_list = list(colors)
colors_list[0] = "orange"
colors = tuple(colors_list)
print("Changed tuple:", colors)

print("Tuple length:", len(colors))

print("\nloop through tuple:")
for colors in colors:
    print("-", colors)

# Set eample
numbers = {1, 2, 3, 4, 5, 2, 3}
print("\nset:", numbers)

numbers.add(6)
print("After add 6:", numbers)

numbers.discard(2)
print("After discard 2:", numbers)

if 3 in numbers:
    print("3 is in the set")
else:
    print("3 is not in the set")

fruits = ["apple", "banana", "apple", "orange", "banana"]
unique_fruits = set(fruits)
print("\nOriginal list:", fruits)
print("Unique fruits:", unique_fruits)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\nset1:", set1)
print("set2:", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric difference:", set1 ^ set2)

empty_set = set()
print("\nEmpty set:", empty_set)
