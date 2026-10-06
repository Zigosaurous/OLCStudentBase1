############################################################
# TASK 3 - DEBUGGING OF PROGRAM
############################################################

# Open the file:
# EMAILCHECK.ipynb
#
# Save the file as:
# TASK3___.ipynb
#
# The following program is intended to validate email
# addresses entered by the user.
#
# The program should work according to the following rules:
#
# - Prompt the user to enter an email address.
#
# - An email is considered valid if:
#       - it is at least 10 characters long;
#       - it contains exactly one '@' symbol;
#       - it does not contain '@' as the first or last
#         character;
#       - it contains a dot ('.') after the '@' symbol;
#       - the dot is not immediately after the '@' symbol.
#
# - The program should display:
#
#       Valid Email!
#
#   if all conditions are met.
#
# - If the email fails any of the above checks, a suitable
#   error message should be shown.
#
# - The program should keep asking for new email addresses
#   until the user types:
#
#       exit
#
#   The word "exit" may be entered in any case format,
#   for example:
#       exit
#       Exit
#       EXIT
#
# - At the end of the program, it should display:
#       - the total number of valid emails entered;
#       - the total number of invalid emails entered.
#
# There are several syntax errors and logic errors in the
# program.
#
# Identify and correct the errors so that the program works
# correctly according to the rules above. [10]


valid = 0
invalid = 0 #10 changed 1 to 0

print("Welcome to the Email Validator!")
print("Type 'exit' to quit the program.\n")

while True: #1 added a :
    email = input("Enter an email address: ").strip()

    if email.lower() == "exit": #9 added ()
        break #8 changed continue to break

    if len(email) < 10: #3 changed >= to <
        print("Email is too short.\n")
        invalid += 1
        continue

    at_index = email.find("@") #4 changed == to =

    if at_index == -1 or email.find("@", at_index + 1) != -1:
        print("Email must contain exactly one '@' symbol.\n")
        invalid += 1
        continue

    if at_index == 0 or at_index == len(email): #5 changed len.email to len(email)  #6 removed -1
        print("'@' cannot be at the start or end of the email.\n")
        invalid += 1
        continue

    dot_index = email.find(".", at_index + 1)

    if dot_index == -1 or dot_index == at_index + 1:
        print("There must be a '.' after the '@' symbol, and not immediately after it.\n")
        invalid += 1 #7 changed one to 1
        continue

    print("Valid Email!\n")
    invalid += 1


print("\nTotal valid emails entered: ", valid) #2 added a ) at the end
print("Total invalid emails entered: ", invalid)