# Task 4: Student Record
# created by peter okonmah

# Create empty dictionary
student = {}

# Collect name and age
student["name"] = input("Enter student name: ")
student["age"] = int(input("Enter student age: "))

# Collect scores for specific subjects
maths = int(input("Enter score for Maths: "))
english = int(input("Enter score for English: "))
physics = int(input("Enter score for Physics: "))

# Store scores in a list
student["scores"] = [maths, english, physics]

# Check if passed (average score >= 50)
average_score = sum(student["scores"]) / len(student["scores"])
student["passed"] = average_score >= 50


# Check if teenager (age between 13 and 19)
student["teenager"] = student["age"] >= 13 and student["age"] <= 19   # logical operator

# Print record in a formatted way
print("\nStudent Record:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Scores: {student['scores']}")
print(f"Average Scores: {average_score}")
print(f"Passed: {student['passed']}")
print(f"Teenager: {student['teenager']}")
