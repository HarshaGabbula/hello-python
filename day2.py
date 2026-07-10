# day2.py

name = "Saiharsha"     # str
age = 17          # int
height = 5.9     # float
is_student = True # bool

# Print values
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Show the data type of each variable
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Simple expressions
next_age = age + 1
double_height = height * 2

print("Next year, age will be:", next_age)
print("Double the height is:", double_height)

# Type conversion
age_str = str(age)
print("age as string:", age_str)

height_int = int(height)
print("Height as integer:", height_int)

is_student_str = str(is_student)
print("Student status as string:", is_student_str)

# Combine text and variables 
print(f"{name} is {age} years old and student status is {is_student}.")

favorite_food = "biryani"  # str
grade = 9.5       # float
is_hungry = False  # bool

print(f"{name} likes {favorite_food}.")
print("Next year , age plus five is:" , age + 5)
print("Half the height is:", height / 2)
print("Grade type is:", type(grade))
print("is hungry?" , is_hungry)
print("is age greater than 18?", age > 18)

