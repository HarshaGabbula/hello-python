# Day 7 : Lists and slicing

fruits = ["apple", "banana", "mango", "orange", "grape", "kiwi"]
print("Full list", fruits)

# Indexing
print("First item:", fruits[0])
print("Second item:", fruits[1])
print("Last item:", fruits[-1])

# Slicing
print("First three:", fruits[:3])
print("Middle items:", fruits[1:4])
print("From third to end:", fruits[2: ])
print("Every second item:", fruits[::2])

# List operations 
fruits.append("pineapple")
print("After append:", fruits)

fruits.insert(2, "strawberry")
print("After insert:", fruits)

fruits.remove("banana")
print("After remove banana:", fruits)

popped = fruits.pop()
print("Popped item:", popped)
print("List now:", fruits)

print("Number of fruits:", len(fruits))

# More work with numbers
numbers = [5, 10, 15, 20, 25 ]
print("Numbers list:", numbers)
print("First two numbers:", numbers[:2])
print("Last three numbers:", numbers[-3:])

numbers[1] = 12
print("After change:", numbers)

print("Sum of numbers:", sum(numbers))
print("Average of numbers:", sum(numbers)/len(numbers))

# Slicing with step
print("Every other number:", numbers[::2])

# Use a loop to print each fruit
print("\nLooping through fruits:")
for fruit in fruits:
    print("-", fruit)