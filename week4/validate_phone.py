# Function to collect and validate a Nigerian phone number
def collect_nigerian_phone_number():
    while True:
        # Ask for the user's phone number
        phone_number = input("Enter your Nigerian phone number: ")

        # Clean up the input by removing any spaces or dashes
        phone_number = phone_number.replace(" ", "").replace("-", "")

        # Check if the phone number starts with '0' or '+234' and has exactly 11 digits
        if phone_number.startswith('0') and len(phone_number) == 11 and phone_number[1:].isdigit():
            print(f"Phone number '{phone_number}' is valid.")
            break
        elif phone_number.startswith('+234') and len(phone_number) == 13 and phone_number[4:].isdigit():
            print(f"Phone number '{phone_number}' is valid.")
            break
        else:
            print("Invalid phone number. Please enter a valid Nigerian phone number.")

# Call the function
collect_nigerian_phone_number()
