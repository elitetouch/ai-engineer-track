#calculator using input



#Ask the user to enter a sentence and print the number of vowels in it.
# user_sentence = input("Enter a sentence: ").lower()
# vowels = "aeiou"
# vowel_count = user_sentence.count("a") + user_sentence.count("e") + user_sentence.count("i") + user_sentence.count("o") + user_sentence.count("u")
# print(vowel_count)

# user_sentence = input("Enter a sentence: ")
# word = "\n".join(user_sentence.split())
# print(word)



#Check if a given string starts with "https://".
# url = "https://publica.academy"

# check =  url.startswith("https://")
# print(f"Does the URL start with 'https://'? {check}")

user_word = input("Enter your word: ")

print(f"The character count is: {user_word.count('') - 1}")