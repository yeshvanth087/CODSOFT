import random
import string

# Take password length from user
length = int(input("Enter desired password length: "))

# Define character set
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display password
print("Generated Password:", password)
