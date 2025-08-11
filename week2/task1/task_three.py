#Given "apple,banana,orange", split the string into a list of fruits.

#Ask the user for a sentence and print each word on a new line.

#Replace all spaces in a string with underscores (_).

#Count how many times the letter "a" appears in "Banana".

#Check if a given string starts with "https://".

#Answer by Peter Okonmah

#Given "apple,banana,orange", split the string into a list of fruits.
fruits = "apple,banana,orange"
fruit_list = fruits.split(",")
print(fruit_list)

#Ask the user for a sentence and print each word on a new line.
user_sentence = input("Enter a sentence: ")
for word in user_sentence.split():
    print(word)

#Replace all spaces in a string with underscores (_).
text = "Hello World"
text = text.replace(" ", "_")
print(text)

#Count how many times the letter "a" appears in "Banana".
text = "Banana"
count = text.count("a")
print(f"The letter 'a' appears {count} times in '{text}'.")

#Check if a given string starts with "https://".
url = "https://publica.academy"

check =  url.startswith("https://")
print(f"Does the URL start with 'https://'? {check}")

