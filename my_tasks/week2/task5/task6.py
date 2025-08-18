# Task 6: Student Profile Builder
# created by peter okonmah

# Collect personal student details
student_detail = {
    "fullname": input("Enter student fullname: "),
    "age": int(input("Enter student age: ")),
    "gender": input("Enter student gender: "),
    "hobbies": input("Enter student hobbies separated with commas: ").split(", "),
    "guardian": {
        "name": input("Enter guardian name: "),
        "phone": input("Enter guardian phone number: ")
    },
    "subjects": ["math", "science", "english", "history"]
}

# Now collect scores after subjects are defined
student_detail["score"] = {
    subject: float(input(f"Enter {subject} score: ")) for subject in student_detail["subjects"]
}

# Display the result
print("--------------------\nStudent Profile\n--------------------")
for key, value in student_detail.items():
    print(f"{key}\t\t {value}")
