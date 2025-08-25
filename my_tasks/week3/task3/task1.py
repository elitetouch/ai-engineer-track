# Admission Eligibility Checker updated with input validation and retry option
# created by Peter Okonmah

print("=== Admission Eligibility Checker (2025/2026) ===\n")

while True:
    try:
        # Numeric inputs
        age = int(input("Enter your age: "))
        utme_score = int(input("Enter your UTME score: "))
        o_level_passes = int(input("How many O'Level credits do you have at one sitting?: "))
        post_utme_score = int(input("Enter your Post-UTME score (out of 400): "))
    except ValueError:
        print("\n Invalid input! Please enter numbers where required.\n")
        continue  # restart the loop if wrong type entered

    # Text inputs with simple validation
    first_choice = input("Did you choose UNILAG as your first choice? (yes/no): ").lower()
    while first_choice not in ["yes", "no"]:
        first_choice = input("Please answer 'yes' or 'no': ").lower()

    english = input("Do you have a credit in English Language? (yes/no): ").lower()
    while english not in ["yes", "no"]:
        english = input("Please answer 'yes' or 'no': ").lower()

    maths = input("Do you have a credit in Mathematics? (yes/no): ").lower()
    while maths not in ["yes", "no"]:
        maths = input("Please answer 'yes' or 'no': ").lower()

    # Admission Checks
    age_ok = age >= 16
    utme_ok = utme_score >= 200
    first_choice_ok = first_choice == "yes"
    olevel_ok = o_level_passes >= 5 and english == "yes" and maths == "yes"
    post_utme_ok = 200 <= post_utme_score <= 320

    # Print eligibility results
    if age_ok and utme_ok and first_choice_ok and olevel_ok and post_utme_ok:
        print("\n Congratulations! You are eligible for admission consideration at UNILAG.\n")
    else:
        print("\n Sorry, you are NOT eligible for admission.")
        print("Reason(s):")
        if not age_ok:
            print("- You must be at least 16 years old.")
        if not utme_ok:
            print("- You must score at least 200 in UTME.")
        if not first_choice_ok:
            print("- You must choose UNILAG as your first choice.")
        if not olevel_ok:
            print("- You must have at least 5 O'Level credits at one sitting including English and Maths.")
        if not post_utme_ok:
            print("- Your Post-UTME score is outside the departmental cut-off range (200–320).")
        print()

    # Ask if user wants to check again
    retry = input("Do you want to check another candidate? (yes/no): ").lower()
    if retry != "yes":
        print("\n Thank you for using the Admission Eligibility Checker. Goodbye!")
        break
