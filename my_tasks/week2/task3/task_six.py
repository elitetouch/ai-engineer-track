

# created by peter okonmah

# Stores the days of the week in a tuple.
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# Stores the months of the year in another tuple.
months_of_year = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# Asks the user to enter:
# Student’s name, Gender, Course Track
student_name = input("Enter the student's name: ")
gender = input("Enter the student's gender: ")
course_track = input("Enter the student's course track: ")

# Current month number (1-12)
current_month = int(input("Enter the current month (1-12): "))

# Current day number (1-7)
current_day = int(input("Enter the current day (1-7): "))

# print all the information collected
print("Student's Name:", student_name)
print("Gender:", gender)
print("Course Track:", course_track)
print("Current Month:", months_of_year[current_month - 1])
print("Current Day:", days_of_week[current_day - 1])
