name = input("Enter your name: ")


print("Welcome to python programming", name)

#converting int, float
age = int(input("Enter your age: "))
print("Your age is", age)
print(f"You will be {age + 2} years old in 2 years.")

exam_score = float(input("Enter your exam score: "))
print("Your exam score is", exam_score)


#calculator using input

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter an operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    result = None

if result is not None:
    print(f"The result of {num1} {operation} {num2} = {result}")
else:
    print("Invalid operation")