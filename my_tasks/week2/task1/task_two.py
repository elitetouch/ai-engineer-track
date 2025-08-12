# Task
#Check if a given string contains the substring "python" (case-insensitive).

#Write a program to reverse a string without using slicing ([::-1]).

#Given a string with extra spaces, remove the leading and trailing spaces.

#Ask the user to enter a sentence and print the number of vowels in it.

#Convert a string "1234" to an integer and multiply it by 2.

#Answer by Peter Okonmah

#Check if a given string contains the substring "python" (case-insensitive).
text = input("Enter any word: ")

print("python" in text.lower()) 

#Write a program to reverse a string without using slicing ([::-1]).
my_word = input("Enter a word to reverse: ")
text_to_reverse = "".join(reversed(my_word))
print(text_to_reverse)

#Given a string with extra spaces, remove the leading and trailing spaces.
text_with_spaces = "   Hello World   "
print(text_with_spaces.strip())

#Ask the user to enter a sentence and print the number of vowels in it.
user_sentence = input("Enter a sentence: ").lower()
vowels = "aeiou"
vowel_count = user_sentence.count("a") + user_sentence.count("e") + user_sentence.count("i") + user_sentence.count("o") + user_sentence.count("u")
print(vowel_count)

#Convert a string "1234" to an integer and multiply it by 2.
number_str = "1234"
number = int(number_str)
print(number * 2)
