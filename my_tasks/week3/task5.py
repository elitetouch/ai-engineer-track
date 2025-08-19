# Task 5: Store Inventory 
# created by peter okonmah

# a dictionary of a store inventory
store = {"Book": 10, "Pen": 20, "Bag": 5}

# show the store inventory before purchase
print("Before purchase:", store)

item = input("Enter the item you want to buy (Book, Pen, Bag): ")
quantity = int(input(f"Enter quantity of {item} you want to purchase: "))

# Directly subtract using -=
store[item] -= quantity  

# Ensure the quantity does not go below zero
if store[item] < 0:
    store[item] = 0
    print(f"Not enough {item} in stock. Setting quantity to 0.")    
print("After purchase:", store)
