# main.py

# Import the whole package
import my_package as package

print(package.add(5, 3))           # 8
print(package.subtract(10, 4))     # 6
print(package.capitalize_text("python"))  # Python

# OR import specific modules
from my_package import string_utils

print(string_utils.reverse_text("hello"))  # olleh