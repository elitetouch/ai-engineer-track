'''
Task3: Online Store Cart Calculation
program created by Peter Okonmah
Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).
'''
items = ["Book", "Pen", "Bag"]
prices = [500, 100, 2000]




# Pair item with price  using zip() 
cart_item = {item: price for item, price in zip(items, prices)}

print("Your shopping cart:")
print(cart_item)

total_price = sum(cart_item.values())
print(f"Total Price: {total_price}")
