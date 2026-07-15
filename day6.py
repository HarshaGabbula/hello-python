# A dictionary that stores a student record
student = {
    "name": "Harsha",
    "age": 17,
    "city": "Medak",
    "is_student": True,
    "subjects": ["Math", "Python", "Science"],
    "scores": {
        "Math": 90,
        "Python": 95,
        "Science": 88 
    }    
}

# Print the full record
print("Student Record:", student)

# Access values by key 
print("Name:", student["name"])
print("City:", student["city"])
print("Is student:", student["is_student"])

# Add a new field to the dictionary
student["grade"] = "12th"

# Update a nested value 
student["scores"]["English"] = 92

# Loop through the dictionary
print("\nstudent info:")
for key, value in student.items():
    print(f"{key}: {value}")

# Loop through the subject list inside the dictionary
print("\nSubjects:")
for subject in student["subjects"]:
    print("-" , subject)

# Calculate the average score
score_values = student["scores"].values()
average_score = sum(score_values) / len(score_values)
print("\nAverage Score:", average_score)

# Check a condition using dictionary data
if student["age"] >= 18:
    print("The student is an adult.")
else:
    print("This student is not an adult yet.")
    