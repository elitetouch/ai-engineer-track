

# created by peter okonmah

# Store all seat numbers (1 to 50) in a set.
seat_numbers = set(range(1, 51))

# Ask users to "book" a seat by entering the number.
book_seat = int(input("Enter the seat number you want to book (1-50): "))
seat_booked = seat_numbers.remove(book_seat)

print(f"Seat {book_seat} {'booked successfully.'}")

print(f"Remaining seats: {seat_numbers}")
