student = {
    "name": "Ada",
    "age": 20,
    "course": "Computer Science"
}
print(student)

student_info = dict(name="John", age=25, course="Maths")
print(student_info)

empty_dict = {}
print(empty_dict)

squares = {'J'+str(x): x**2 for x in range(1, 6)}
print(squares)

evens_cube = {x: x**3 for x in range(1, 10) if x % 2 == 0}
print(evens_cube)

odd_cube = {x: x**3 for x in range(1, 10) if x % 2 != 0}
print(odd_cube)

students = {"Ada": 85, "John": 40, "Musa": 65}

# Filter students who passed (score >= 50)

passed_students = {name: score for name, score in students.items() if score >= 50}
print(passed_students)

names = ["Ada", "John", "Musa"]
lengths = {name: len(name) for name in names}
print(lengths)