# Task 2: Super Market Price List
# created by peter okonmah

# Items should come from a list
items = ["Rice", "Beans", "Milk", "Bread", "Sugar"]

# create an empty dictionary to store price list
price_list = {}

#  Ask user to enter prices for each item
print("Enter prices for the following items:")

price = {
    item: input(f"Price of {item}: ") for item in items
}

# Display all items and their prices
print("\n--- Super Market Price List ---")
print("Item\t\tPrice")
for item in items:
    print(f"{item}\t\t{price[item]}")


# allow the user to update the price of an item
item_to_update = input("Enter the item you want to update the price for: ")
if item_to_update in items:
    new_price = int(input(f"Enter the new price for {item_to_update}: "))
    price[item_to_update] = new_price
    print(f"The new price of {item_to_update} is {new_price}.")
else:
    print(f"{item_to_update} is not in the price list.")
