#Task4: Create a Unique Voters Registration System
# created by peter okonmah

# initialize voters as set
voters = set()

# Ask user how many voters you want to register
number_of_voter = int(input("How many voters do you want to register? "))

# Loop to register voters in range of number of voters
for i in range(number_of_voter):
  
    # Ask for voter name.
    name = input(f"Enter name of voter {i+1}: ")
    
    # Check if the voter is already registered, display a warning
    if name in voters:
        print("This voter is already registered!")
        
        # Ask for another voter name.
        name = input(f"Enter another name of voter {i+1}: ")
        voters.add(name)
    else:
      
      # store in a set if not already registered
        voters.add(name)
        print(f"{name} has been registered successfully.")

# After registration, display the total number of unique voters.
print(f"Registration complete.\n Total unique voters: {len(voters)}")
