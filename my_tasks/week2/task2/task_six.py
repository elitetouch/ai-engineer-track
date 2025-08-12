# Task 6: Word Analyze
# created by peter okonmah

# Ask the user to input a word.
word = input("Enter a word: ")

# Print the length of the word.
print("Length of the word:", len(word))

# Check if it is all uppercase, all lowercase, or title case.
if word.isupper():
    print("The word is all uppercase.")
elif word.islower():
    print("The word is all lowercase.")
elif word.istitle():
    print("The word is in title case.")
else:
    print("The word is not in a uniform case.")

# Reverse the word using slicing.
reversed_word = word[::-1]
print("Reversed word:", reversed_word)
