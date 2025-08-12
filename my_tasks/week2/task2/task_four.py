# Task 4: Name Organize
# created by peter okonmah

# Ask the user to enter 5 names (separated by spaces).
names = input("Enter 5 names (separated by spaces): ").split()

# Convert all names to lowercase.
names = [name.lower() for name in names]

# Sort the list alphabetically.
names.sort()

# Display them one name per line using for
for i in range(len(names)):
    print(names[i])
