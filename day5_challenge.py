def calculate_area(length, width):
  return length * width

def is_adult(age):
  if age >= 18:
    return True
  else:
    return False

def greet_user(name, age):
  return f"Hello, {name}! You are {'an adult' if is_adult(age) else 'not an adult'}."

def celsius_to_fahrenheit(celsius):
  return (celsius * 9/5) + 32

calculate_area_result = calculate_area(5, 3)
age_check = is_adult(17)
greeting_message = greet_user("Harsha", 17)
fahrenheit_temp = celsius_to_fahrenheit(25)


print("Area of rectangle (5 x 3):", calculate_area_result)
print("Is 17 an adult?", age_check)
print("Greeting:", greeting_message)
print("25°C in Fahrenheit:", fahrenheit_temp)