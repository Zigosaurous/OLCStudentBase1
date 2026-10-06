firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
username = firstname[0:3] + lastname
print("Your username is " + username)

while True:
    password = input("Please enter a password: ")

    if len(password) < 8:
        print("Invalid password, Please enter a password with at least 8 characters")
    else:
        print("Valid password")
        break

while True:
    check = input("Please re-enter your password: ")
    if check == password:
        print("Your password has been set.")
        break
    else:
        print("“Password entries do not match. Please repeat the second entry of your password: ")