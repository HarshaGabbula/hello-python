# day3.py

# Day 3: if statements and decision making
age = 18

if age >= 18:
    print("You are an adult and can vote.")
else:
    print("You are not an adult yet. Keep learning!")

# Check if a number is even or odd
number = 20
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# Score grading using if / elif / else
score = 98
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"

print("Score:", score)
print("Grade:", grade)

# Logical operators
is_student = True
has_id = False
if is_student and has_id:
    print("You can get a student discount.")
elif is_student and not has_id:
    print("You are a student, but you need your ID.")
else:
    print("No student discount for you today.")
