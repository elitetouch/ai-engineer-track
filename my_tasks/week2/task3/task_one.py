# Task1:  Create and Display
# created by peter okonmah

# Ask the user to enter three favorite Nigerian dishes (one at a time) and store them in a tuple called dishes.
dishes = (
    input("Enter your first favorite Nigerian dish: "),
    input("Enter your second favorite Nigerian dish: "),
    input("Enter your third favorite Nigerian dish: ")
)

# Print the tuple in a single line, separating items with commas.
print(dishes)

# Use the \n escape sequence to print each dish on a new line.
print("\n".join(dishes))
