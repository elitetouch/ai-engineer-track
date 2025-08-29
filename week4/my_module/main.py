# my_module/main.py

import first as f
import second as s

# lets use the functions in the first.py file


print("=== Math Functions ===")
print("5 + 3 =", f.add(5, 3))
print("10 - 4 =", f.subtract(10, 4))
print("6 * 7 =", f.multiply(6, 7))
print("20 / 5 =", f.divide(20, 5))

# Lets us the functions in the second.py file
print("\n=== String Functions ===")
print(s.greet("Ridwan"))
print("Reverse of 'Python' =", s.reverse_string("Python"))
print("Character count in sentence =", s.count_characters("Python modules are powerful"))
print("Word count in sentence =", s.count_words("Python modules are powerful"))