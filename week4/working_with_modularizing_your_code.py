# Defining a function
# def greet():
#     print("Hello, welcome to AI Fellowship!")

# # When you want to use a function, this is how to call it.
# # And you can call it as many times as possible.
# greet()
# greet()
# greet()

# def greet(name):
#     print(f"Hello {name}, welcome to AI Fellowship!")
#     print("We're glad to have you here.")

# greet("peter")

# def greet(name):
#     print("Hello", name)


# # Function call
# result = greet("Esther")

# # You will notice that it did not store the name
# print("Result:", result)

# def add(a, b):
#     return a + b

# # Function call

# result = add(4, 6)
# print("The sum is:", result)

# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i   # pause and return i
#         i += 1

# # Using the generator
# for number in count_up_to(5):
#     print(number)

# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track, ".")

# # function call
# introduce("Ngozi", "AI Engineering")   # Correct order

# # Change the arrangment and watch the output

# introduce("AI Engineering","Ngozi")   # Incorrect order, this will throw a semantic error

# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track,".")

# # function call
# introduce(name = "Ngozi", track = "AI Engineering")

# # Change the arrangment and watch the output

# introduce(track = "AI Engineering",name = "Ngozi")   # HEre you notice that order does not batter

# def introduce(name, track = "AI Engineering"):
#     print("My name is", name)
#     print(f"I am learning {track}.")

# # function call
# # Without specifying the default argument, but watch the ouput
# introduce("Paul")  

# def add_number(*args):
#     total = sum(args)
#     print("The sum is:", total)


# number = (3, 5)
# add_number(*number)

students = {    
   ' name' : 'peter okonmah',
   'score' : 90
}

def print_user(**args):
    # print(args)
    return args

user =  print_user(**students)

print(user)
