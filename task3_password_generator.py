# Task 3 - Password Generator

import random
import string

print("Password Generator")

try:
    length = int(input("Enter desired password length: "))
    if length <= 0:
        print("Length must be greater than 0.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
