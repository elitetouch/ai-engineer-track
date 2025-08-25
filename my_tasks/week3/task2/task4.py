# Task 1: Student Bio Data Storage
# Created by Peter Okonmah

print("=== Student Bio Data Storage ===\n")

# List to hold multiple student records
students = []

while True:
    # Collect student details
    student = {
        "name": input("Enter student name: "),
        "age": input("Enter student age: "),
        "gender": input("Enter student gender: ")
    }

    # Collect courses (multiple values)
    courses = input("Enter courses separated by commas: ")
    student["courses"] = courses.split(",")

    # Add this student to the list
    students.append(student)

    # Display the bio-data neatly
    print("\n--- Student Bio-Data ---")
    print(f"Name:\t {student['name']}")
    print(f"Age:\t {student['age']}")
    print(f"Gender:\t {student['gender']}")
    print(f"Courses: {', '.join(student['courses'])}")

    # Ask if user wants to continue
    choice = input("\nDo you want to enter another student? (yes/no): ").lower()
    if choice != "yes":
        print("\n--- All Student Records ---")
        for i in range(len(students)):
            s = students[i]
            print(f"\nStudent {i+1}")
            print(f"Name:\t {s['name']}")
            print(f"Age:\t {s['age']}")
            print(f"Gender:\t {s['gender']}")
            print(f"Courses: {', '.join(s['courses'])}")
        print("\nData entry completed. Goodbye!")
        break
