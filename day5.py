# A function that greets a user by name
def greet(name):
    return f"Hello, {name}!"

# A function that adds two numbers
def add_numbers(a, b):
    return a + b

# A function that checks if a number is even
def is_even(number):
    return number % 2 == 0

# A function that formats a profile message
def profile(name, age, city):
    return f"{name} is {age} years old and lives in {city}."

# Call the functions and print the results
message = greet("Harsha")
sum_result = add_numbers(7, 5)
even_check = is_even(19)
profile_text = profile("Harsha", 17, "Medak")

print(message)
print("7 + 5 =", sum_result)
print("Is 19 even?", even_check)
print(profile_text)