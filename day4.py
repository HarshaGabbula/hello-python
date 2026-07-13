# day4.py

# Day 4: lists and loops
favorite_foods = ["biryani", "chicken", "dietcoke", "watermelon"]
print("Favorite foods:")
for food in favorite_foods:
    print("-", food)

# Get the number of items in the list
print("I have", len(favorite_foods), "favorite foods.")

# Work with numbers in a list
numbers = [1, 2, 7, 9, 5]
total = 0
for n in numbers:
    total += n
print("Sum of numbers:", total)

# Use range to repeat an action
print("Counting from 1 to 9:")
for i in range(1, 10):
    print(i)

# Add items to a list
pets = []
pets.append("dog")
pets.append("cat")
print("My pets:", pets)

# Loop through a list and show checks
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    if fruit == "banana":
        print("I found a banana!")
    else:
        print("This is a", fruit)
