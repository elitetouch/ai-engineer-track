# Task4: Tuple Unpackin
# created by peter okonmah

# Ask a user for their First name, Age, Favorite color, Home town Store them in a tuple profile and unpack into variables.
profile = (
    input("Enter your first name: "),
    input("Enter your age: "),
    input("Enter your favorite color: "),
    input("Enter your home town: ")
)

# Store the tuple into variables.
first_name = profile[0]
age = profile[1]
favorite_color = profile[2]
home_town = profile[3]

# Print and use  escape sequence to align each piece of information nicely.
print(f"First Name: {first_name} \t Age: {age} \t Favorite Color: {favorite_color} \t Home Town: {home_town}")    
