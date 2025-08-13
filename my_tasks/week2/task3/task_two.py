# Task2: Tuple and Inpu
#created by peter okonmah

# Ask the user for 5 best friends’ names and Store them in a tuple friends
friends = (
    input("Enter the name of your first best friend: "),
    input("Enter the name of your second best friend: "),
    input("Enter the name of your third best friend: "),
    input("Enter the name of your fourth best friend: "),
    input("Enter the name of your fifth best friend: ")
)

# Print the tuple in reverse order.
print(friends[::-1])
