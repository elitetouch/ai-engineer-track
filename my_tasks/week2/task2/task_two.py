#Task1: Your Favorite Life Quote
# created by peter okonmah

# Create an empty list.
shopping_list = []

# Ask the user to enter 3 shopping items (one by one).
for i in range(3):
    item = input(f"Enter shopping item {i+1}: ")
    shopping_list.append(item)

# Display the list as a single string, separated by commas.
print("Shopping List:")
print([item for item in shopping_list])