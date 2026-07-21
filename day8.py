# Day 8: tuples and sets

# Tuple - immutable lists (cannot change after creation)
colors = ("red", "green", "blue", "yellow")
print("Tuple:", colors)

# Access items in a tuple (like lists)
print("First colour:", colors[0])
print("Last colour:", colors[-1])

# Slice a tuple
print("First two colors:", colors[:2])

# Get length 
print("Number of colours:", len(colors))

# Loop through tuple 
print("Colors in order:")
for color in colors:
    print("-", color)

# Convert tuple to list and back
colors_list = list(colors)
colors_list[0] = "orange"
colors = tuple(colors_list)
print("After change:", colors)

# Sets - unique values, unordered
numbers = {1, 2, 3, 4, 5, 2, 3}
print("\nset:", numbers)

numbers.add(6) 
print("After add 6:", numbers)

numbers.discard(2)
print("After discard 2:", numbers)

# Check membership
if 3 in numbers:
    print("3 is in the set")
else:
    print("3 is not in thr set")

# Get unique values from a list using set
fruits = ["apple", "banana", "apple", "orange", "banana", "apple",]
unique_fruits = set(fruits)
print("\nOrginal list:", fruits)
print("Unique fruits:", unique_fruits)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\nSet operations:")
print("set1:", set1)
print("set2:", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# Create an empty set
empty_set = set()
print("\nEmpty set:", empty_set)
