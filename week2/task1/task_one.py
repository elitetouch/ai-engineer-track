# Write a program to take a string input from the user and display it in uppercase.
#Given the string "python", print its first and last characters.
#Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.
#Write a program to count the number of characters in a string without using len()
#Given "Hello World", replace "World" with "Python"

#Answer by Peter Okonmah

# Write a program to take a string input from the user and display it in uppercase.
user_word = input("Enter your word: ")
print(user_word.upper())

#Given the string "python", print its first and last characters.
text = "python"
print(text[0])  # p
print(text[-1]) # n

#Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.
user = input("Enter your name: ")
print(f"Hello, {user}!")

#Write a program to count the number of characters in a string without using len()
user_word = input("Enter your word: ")
character_count = 0
for char in user_word:
    character_count += 1
print(f"The character count is: {character_count}")

#Given "Hello World", replace "World" with "Python"
text = "Hello World"
text = text.replace("World", "Python")
print(text)
