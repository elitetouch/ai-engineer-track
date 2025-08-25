# USSD Application
# This is a USSD application with control flow and input validation
# Created by Peter Okonmah

print("=== Welcome to the USSD Application ===")

balance = 1000  # starting balance

while True:
    print("\n--- Main Menu ---")
    print("1. Check Balance")
    print("2. Buy Airtime")
    print("3. Pay Bill")
    print("4. Exit")

    option = input("Please enter the option number: ")

    if option == '1':
        print("\nChecking balance...")
        print(f"Your balance is N{balance}.")

    elif option == '2':
        print("\nYou selected Buy Airtime.")
        airtime = input("Enter the amount of airtime to buy: ")

        try:
            airtime = int(airtime)
            if airtime <= balance:
                balance -= airtime
                print(f"You bought airtime worth N{airtime}.")
                print(f"Your new balance is N{balance}.")
            else:
                print("Insufficient balance.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif option == '3':
        print("\nYou selected Pay Bill.")
        bill = input("Enter the bill amount to pay: ")

        try:
            bill = int(bill)
            if bill <= balance:
                balance -= bill
                print(f"You paid a bill of N{bill}.")
                print(f"Your new balance is N{balance}.")
            else:
                print("Insufficient balance.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif option == '4':
        print("\nYou selected Exit.")
        print("Thank you for using the USSD application. Goodbye!")
        break  # exit loop

    else:
        print("\nInvalid option. Please select from 1 - 4.")
