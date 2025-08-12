

#  Create a list of five cities.
cities = ["Abuja", "Kaduna", "Jos", "Lagos", "Port Harcourt"]

# Replace the third city with a new one (entered by the user).
new_city = input("Enter a new city for the third position: ")
cities[2] = new_city

# Remove the last city.
cities.pop()

# Add a new city to the beginning of the list.
new_city = input("Enter a new city for the beginning of the list: ")
cities.insert(0, new_city)

# Print the updated list.
print("Updated list of cities:")
for city in cities:
    print("-", city)