##############################################################
### ASCII ord() and chr() for password generation
##############################################################

# #Generate a Simple Password
# # Write a Python program that generates a random password of a given length 
#     using ASCII printable characters.
# # Example input: length = 8
# # Expected output: A random password of 8 characters, e.g., 'aB3#xG2!'
# # HINT: ASCII printable characters range from 33 to 126

# Sample solution 

# import random

# length = 8
# password = ""
# for i in range(length):
#     char = chr(random.randint(33, 126))  
#     password += char
# print(f"Generated password: {password}")


###########################################################
# Generate a Password with Specific Character Types
# Scenario 1: Corporate Password Policy - Basic Compliance
# One of your clients, a fintech company, has implemented a basic password policy. 
# All system-generated passwords must:
# - Be of a specific length
# - Include at least 1 uppercase letter, 1 lowercase letter, and 1 digit

# Your task: Write a Python program to generate such a password.
# Example: input = 8 → output = 'aB3xG2#1'

# HINT: Use ASCII:
# - Uppercase letters: 65-90
# - Lowercase letters: 97-122
# - Digits: 48-57


# Write and test your code here
# import random

# length = int(input("How long do you want your password to be? "))  #8

# upper = chr(random.randint(65, 90))
# lower = chr(random.randint(97, 122))
# digits = chr(random.randint(48, 57))

# password = upper + lower + digits
# for i in range(length-3):
#     choice = random.randint(1,3)

#     thischar = ""
#     if choice == 1:
#         thischar = chr(random.randint(65,90))
#     elif choice == 2:
#         thischar = chr(random.randint(97,122))
#     else:
#         thischar = chr(random.randint(48,57))

#     password = password + thischar

# print(password)
       


    





###########################################################
# Exclude Specific Characters in Password
#  Scenario 2: Readability-Enhanced Password Generator
# A logistics firm found that users often confuse similar-looking characters 
# (like 'l', '1', 'I', 'O', and '0') when reading out passwords over the phone.

# To improve usability, you're tasked to generate passwords that:
# - Are of a specific length
# - Exclude these confusing characters: 'l', '1', 'I', 'O', '0'

# Example: input = 8, exclude = 'l1IO0' → output = 'aB3xG#2!'
# Hint: Any character in 33-126 except ASCII codes 48, 49, 73, 79, 108


# Write and test your code here

import random

length = int(input("How long do you want your password to be? "))  #8

upper = chr(random.randint(65, 90))
lower = chr(random.randint(97, 122))
digits = chr(random.randint(48, 57))


for i in range(length):
    choice = random.randint(1,3)

    thischar = ""
    if choice == 1:
        while True:
            thischar = chr(random.randint(65,90))
            if chr(73) in thischar or chr(79) in thischar:
                False
            else:
                break

    elif choice == 2:
        while True:
            thischar = chr(random.randint(97,122))
            if chr(108) in thischar:
                False
            else:
                break
        
    else:
        while True:
            thischar = chr(random.randint(48,57))
            if chr(48) in thischar or chr(49) in thischar:
                False
            else:
                break
    password = thischar
print(password)




###########################################################
# Password with Special Characters
# Scenario 3: System Admin Access Passwords
# System administrators require strong passwords with at least 2 special characters 
# to prevent brute-force attacks.

# Your task:
# - Generate a password of a given length
# - Ensure it includes at least two special characters
#   (characters that are neither letters nor digits, e.g., '@', '#', '$', '%', etc.)

# Example: input = 8 → output = 'aB3@xG#2'
# Hint: ASCII 33-47: ! " # $ % & ' ( ) * + , - . /

# Write and test your code here





###########################################################
# Scenario 4: High-Security Access Control
# A secure military application demands passwords that follow strict composition rules
# The password must contain:
# - At least 2 uppercase letters
# - At least 2 lowercase letters
# - At least 2 digits
# - At least 2 special characters

# Write a Python program that:
# - Accepts the desired password length
# - Ensures the final password follows these rules exactly

# Example: input = 8 → output = 'A1b#C2d!'
# Hint: 
# Uppercase letters: 65-90
# Lowercase letters: 97-122
# Digits: 48-57
# Special characters (non-alphanumeric)
# 33-47, 58-64, 91-96, 123-126


# Write and test your code here






###########################################################