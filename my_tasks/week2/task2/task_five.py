#Task 5: Student Score Tracker
# created by peter okonmah

# Initialize empty lists to store student names and scores.
student_name = []
student_score = []

# Ask the user for 3 student names.
for i in range(3):
    name = input(f"Enter the name of student {i + 1}: ")
    student_name.append(name)

# For each student, ask for their score.
for i in range(3):
    score = float(input(f"Enter the score for {student_name[i]}: "))
    student_score.append(score)

# Store the results in two lists (one for names, one for scores).

# Print a formatted output showing Name — Score, aligned neatly.
print("\nStudent Scores:")
print("{:<20} {:<10}".format("Name", "Score"))
print("-" * 30)
for i in range(3):
    print("{:<20} {:<10}".format(student_name[i], student_score[i]))
