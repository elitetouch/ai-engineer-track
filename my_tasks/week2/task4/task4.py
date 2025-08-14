
# created by peter okonmah

# Ask for voter names and store in a set.

voters = set()

voter = input("Enter voter's name: ")
# voters.add(voter)

if voter not in voters:
   voters.add(voter)
   print(f"'{voter}' registered successfully.")
   voter = input("Enter voter's name: ")
  

else:
   print(f"'{voter}' already registered.")
   voter = input("Enter another voter's name: ")
   voters.add(voter)

# After registration, display the total number of unique voters.
print(f"Total unique voters registered: {len(voters)}")
