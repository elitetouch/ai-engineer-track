# Task5: Modify Tuple Indirectly
# created by peter okonmah

# Ask a user to enter three items for their shopping list and store in a tuple shopping_list.
shopping_list = (
    input("Enter the first item for your shopping list: "),
    input("Enter the second item for your shopping list: "),
    input("Enter the third item for your shopping list: ")
)

# Convert it to a list, then ask for two more items to add.
shopping_list = list(shopping_list)
shopping_list.append(input("Enter the fourth item for your shopping list: "))
shopping_list.append(input("Enter the fifth item for your shopping list: "))

# Convert back to a tuple and print the updated list using join() to display items separated by " | ".
shopping_list = tuple(shopping_list)
print("Updated shopping list:")
print(" | ".join(shopping_list))