'''
Task 2: Government scholarship eligibility checker
program created by Peter okonmah
This is a government scholarship eligibility checker.
check if student is a Nigerian citizen,
it check if the student is registered in a nigerian university.
it also check if the student has received scholarship from any oil and gas company.
student must have  A's or B's in 5 WAEC/WASSCE subjects


''' 

student_detail = {
    "name": input("Enter your full name: "),
    "age": int(input("Enter your age: ")),
    "country": input("Enter your country: ").strip().lower(),
    "university": input("Enter your university or non if you are not enrolled: "),
    "scholarship": input("Enter your scholarship status: ").strip().lower(),
    "subjects" : ['Maths', 'English', 'Physics', 'Chemistry', 'Biology']
}

name = student_detail["name"].title()
age = student_detail["age"]
country = student_detail["country"]
university = student_detail["university"].title()
scholarship = student_detail["scholarship"]


student_detail["score"] = {
    subject: input(f"Enter {subject} score in WAEC or WASSCE: ").upper() for subject in student_detail["subjects"]
}

score = student_detail["score"]

eligibility = (score["Maths"] == 'A' or score["Maths"] == 'B') and (score["Physics"] == 'A' or score["Physics"] == 'B') and (score["Chemistry"] == 'A' or score["Chemistry"] == 'B') and (score["Biology"] == 'A' or score["Biology"] == 'B') and (country == "nigeria") and (university != "") and (university != "non") and (scholarship == "no")

print("--------------------------------\nScholarship Eligibility Checker\n--------------------------------\n")
print(f"Candidate: \t{name}\nAge: \t\t{age}\nCountry: \t{country}\nUniversity: \t{university}\nScholarship: \t{scholarship}\n\nWAEC/WASSCE Results:\n{student_detail['subjects'][0]}: {student_detail['score']['Maths']}\n{student_detail['subjects'][1]}: {student_detail['score']['Physics']}\n{student_detail['subjects'][2]}: {student_detail['score']['Chemistry']}\n{student_detail['subjects'][3]}: {student_detail['score']['Biology']}\nEligible: {eligibility}")
