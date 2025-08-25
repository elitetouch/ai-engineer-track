'''
num1 == num2: Checks if  num1 is equal to num2. Returns True if they are equal, False if not.
num1 != num2: Checks if the num1 is not equal to num2. Returns True if they are different.
num1 > num2: Checks if num1 is greater than num2. Returns True if yes.
num1 < num2: Checks if num1 is less than num2. Returns True if yes.

Use Cases
Age Verification System
Compare two ages to check if someone is older, younger, or the same age.

Exam Score Evaluation
Compare a student’s score with the pass mark (e.g., 50) to see if they passed or failed.
Eligibility Checker
check if a student meets certain criteria (e.g., age, score) for a scholarship or admission.
'''

# Exam Score Evaluation

score = int(input("Enter student score: "))
pass_mark = 50

print(f"Score == Pass Mark : {score == pass_mark}")
print(f"Score != Pass Mark : {score != pass_mark}")
print(f"Score > Pass Mark  : {score > pass_mark}")
print(f"Score < Pass Mark  : {score < pass_mark}")

if score >= pass_mark:
    print("Student has passed the exam.")
else:
    print("Student has failed the exam.")
