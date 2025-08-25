# Task 2: Government Scholarship Eligibility Checker
# Program created by Peter Okonmah

print("=== Government Scholarship Eligibility Checker ===\n")

while True:
    # Collect student details
    student_detail = {
        "name": input("Enter your full name: "),
        "age": int(input("Enter your age: ")),  # assumes user enters a number
        "country": input("Enter your country: ").strip().lower(),
        "university": input("Enter your university or 'non' if not enrolled: ").strip(),
        "scholarship": input("Have you received scholarship from an oil & gas company? (yes/no): ").strip().lower(),
        "subjects": ['Maths', 'English', 'Physics', 'Chemistry', 'Biology']
    }

    # Format details
    name = student_detail["name"].title()
    age = student_detail["age"]
    country = student_detail["country"]
    university = student_detail["university"].title()
    scholarship = student_detail["scholarship"]

    # Collect WAEC/WASSCE scores
    student_detail["score"] = {
        subject: input(f"Enter {subject} score in WAEC/WASSCE (e.g A,B,C, F, ): ").upper()
        for subject in student_detail["subjects"]
    }

    score = student_detail["score"]

    # Eligibility checks added control flow
    eligible = True
    reasons = []

    if country != "nigeria":
        eligible = False
        reasons.append("- Applicant must be a Nigerian citizen.")

    if university.lower() == "non" or university.strip() == "":
        eligible = False
        reasons.append("- Applicant must be enrolled in a Nigerian university.")

    if scholarship == "yes":
        eligible = False
        reasons.append("- Applicant must not have received scholarship from an oil & gas company.")

    for subject in ["Maths", "English", "Physics", "Chemistry", "Biology"]:
        if score[subject] not in ["A", "B"]:
            eligible = False
            reasons.append(f"- Must have at least a B in {subject}.")

    # Output results
    print("\n--------------------------------")
    print("Scholarship Eligibility Checker")
    print("--------------------------------")
    print(f"Candidate:   {name}")
    print(f"Age:         {age}")
    print(f"Country:     {country}")
    print(f"University:  {university}")
    print(f"Scholarship: {scholarship}")
    print("\nWAEC/WASSCE Results:")
    for subject, grade in score.items():
        print(f"{subject}: {grade}")

    print("\nResult:")
    if eligible:
        print("Congratulations! You are eligible for the scholarship.\n")
    else:
        print("Sorry, you are NOT eligible for the scholarship.")
        print("Reason(s):")
        for reason in reasons:
            print(reason)
        print()

    # Ask if user wants to check another candidate
    retry = input("\nDo you want to check another candidate? (yes/no): ").lower()
    if retry != "yes":
        print("\n Thank you for using the Scholarship Eligibility Checker. Goodbye!")
        break
