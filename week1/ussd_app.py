# USSD Application
# this is a ussd application
# print the options on the screen
# add input to enter the option number
# created by peter okonmah

print("Welcome to the USSD application")
print("1. Check Balance")
print("2. Buy Airtime")
print("3. Pay Bill")
print("4. Exit")
balance = 1000
option = input("Please enter the option number: ")

if option == '1':
    print("checking balance..")
    print(f"Your balance is N{balance}.")
elif option == '2':
    print("you selected buy airtime.")
    airtime = int(input("Enter the amount of airtime to buy: "))
    print(f"you are buying airtime worth N{airtime}")
    print(f"Your new balance is N{balance + airtime}.")
elif option == '3':
    print("you selected pay bill.")
    bill = int(input("Enter the amount to pay: "))
    print("you are paying a bill of N", bill)
elif option == '4':
    print("you selected exit.")
    print("Thank you for using the USSD application. Goodbye!")
else:
    print("Invalid option")

   
