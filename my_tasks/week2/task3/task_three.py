#Task3: Tuple Operation
#created by peter okonmah

# Create a tuple of 5 Nigerian states entered by the user.
states = (
    input("Enter the name of the first Nigerian state: "),
    input("Enter the name of the second Nigerian state: "),
    input("Enter the name of the third Nigerian state: "),
    input("Enter the name of the fourth Nigerian state: "),
    input("Enter the name of the fifth Nigerian state: ")
)

# Print the first state and last state.
print("First state:", states[0])
print("Last state:", states[-1])

# Check if "Lagos" is in the tuple and print "Yes" or "No".
print("Lagos" in states)

# Print the number of states entered.
print("Number of states entered:", len(states))