# Task 1: Student Bio Data Storage
# Created by Peter Okonmah

print("=== Student Bio Data Storage ===\n")

# List to hold multiple student records
students = []

while True:
    # Collect student details
    name = input("Enter student name: ").strip()
    
    # Age input with try/except to ensure it's a number
    while True:
        age_input = input("Enter student age: ").strip()
        try:
            age = int(age_input)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for age.")

    gender = input("Enter student gender: ").strip()

    # Collect courses (multiple values)
    courses = input("Enter courses separated by commas: ").strip()
    course_list = [c.strip() for c in courses.split(",") if c.strip() != ""]

    # Store student data
    student = {
        "name": name,
        "age": age,
        "gender": gender,
        "courses": course_list
    }
    students.append(student)

    # Display the bio-data neatly
    print("\n--- Student Bio-Data ---")
    print(f"Name:\t {student['name']}")
    print(f"Age:\t {student['age']}")
    print(f"Gender:\t {student['gender']}")
    print(f"Courses: {', '.join(student['courses'])}")

    # Ask if user wants to continue
    choice = input("\nDo you want to enter another student? (yes/no): ").lower()
    while choice not in ["yes", "no"]:
        print("Please enter 'yes' or 'no'.")
        choice = input("Do you want to enter another student? (yes/no): ").lower()

    if choice == "no":
        print("\n--- All Student Records ---")
        for i, s in enumerate(students, start=1):
            print(f"\nStudent {i}")
            print(f"Name:\t {s['name']}")
            print(f"Age:\t {s['age']}")
            print(f"Gender:\t {s['gender']}")
            print(f"Courses: {', '.join(s['courses'])}")
        print("\nData entry completed. Goodbye!")
        break
