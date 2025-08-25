# Admission Eligibility Checker
#created by Peter Okonmah

print("===  Admission Eligibility Checker (2025/2026) ===")

# Collect user inputs
age = int(input("Enter your age: "))
utme_score = int(input("Enter your UTME score: "))
first_choice = input("Did you choose UNILAG as your first choice? (yes/no): ").lower()
o_level_passes = int(input("How many O'Level credits do you have at one sitting?: "))
english = input("Do you have a credit in English Language? (yes/no): ").lower()
maths = input("Do you have a credit in Mathematics? (yes/no): ").lower()
post_utme_score = int(input("Enter your Post-UTME score (out of 400): "))

# Check admission conditions

# Check for  Age
age_ok = age >= 16  

# Check for the UTME score
utme_ok = utme_score >= 200  

# Check for First choice
first_choice_ok = first_choice == "yes"  

# Check O'Level (5 credits at one sitting + English + Maths)
olevel_ok = o_level_passes >= 5 and english == "yes" and maths == "yes"

# Check for Post-UTME (score will be used for departmental cut-off)
# for  departmental cut-off range (200–320)
post_utme_ok = 200 <= post_utme_score <= 320  

# print eligibility results
if age_ok and utme_ok and first_choice_ok and olevel_ok and post_utme_ok:
    print("\nCongratulations! You are eligible for admission consideration at UNILAG.")
else:
    print("\nSorry, you are NOT eligible for admission.")
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
