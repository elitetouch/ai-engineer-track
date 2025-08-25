# Task 3: Online Store Cart Calculation
# Program created by Peter Okonmah

print("=== Welcome to the Online Store ===\n")

# Predefined store items
items = ["Book", "Pen", "Bag"]
prices = [500, 100, 2000]

# Pair item with price using zip()
store = {item: price for item, price in zip(items, prices)}

# Shopping cart (empty at start)
cart = {}

# Control flow loop
while True:
    print("\n--- Store Menu ---")
    print("1. View Store Items")
    print("2. Add Item to Cart")
    print("3. View Cart")
    print("4. Checkout and Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\nAvailable Store Items:")
        for item, price in store.items():
            print(f"{item}: ₦{price}")

    elif choice == "2":
        print("\nWhich item do you want to add?")
        for i in range(len(items)):
            print(f"{i+1}. {items[i]} - ₦{prices[i]}")

        selection = input("Enter item number: ")

        if selection.isdigit():
            selection = int(selection)
            if 1 <= selection <= len(items):
                item = items[selection - 1]
                if item in cart:
                    cart[item] += 1  # increase quantity
                else:
                    cart[item] = 1
                print(f"{item} added to your cart.")
            else:
                print("Invalid item number. Please select again.")
        else:
            print("Please enter a valid number.")

    elif choice == "3":
        if not cart:
            print("\nYour cart is empty.")
        else:
            print("\nYour Shopping Cart:")
            total_price = 0
            for item, quantity in cart.items():
                price = store[item] * quantity
                total_price += price
                print(f"{item} x{quantity} = ₦{price}")
            print(f"\nTotal Price: ₦{total_price}")

    elif choice == "4":
        if not cart:
            print("\nYour cart is empty. Goodbye!")
        else:
            print("\nCheckout Successful!")
            total_price = sum(store[item] * qty for item, qty in cart.items())
            print("Your Final Cart:")
            for item, qty in cart.items():
                print(f"{item} x{qty} = ₦{store[item] * qty}")
            print(f"\nTotal Amount to Pay: ₦{total_price}")
        break  # exit the loop

    else:
        print("Invalid choice. Please select from 1-4.")
