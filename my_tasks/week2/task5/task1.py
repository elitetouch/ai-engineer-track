# Task1: Student Bio Data Storage
# created by peter okonmah

# Collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary
student = {
    "name": input("Enter student name: "),
    "age": input("Enter student age: "),
    "gender": input("Enter student gender: ")
}

# Collect courses (multiple values)
courses = input("Enter courses separated by commas: ")

# Courses should be stored as a list.
student["courses"] = courses.split(",")

# Display the bio-data neatly using escape sequences
print("\n--- Student Bio-Data ---")
print(f"Name:\t {student['name']}")
print(f"Age:\t {student['age']}")
print(f"Gender:\t {student['gender']}")
print(f"Courses: {', '.join(student['courses'])}")
  