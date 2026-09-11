#Task 1 

list = ['TSt01']

while True:
    check = input("Do you want to add a password? (Y/N) ").upper()

    if check == "Y":
        password = ""
        first = input("What is your first name? ")
        last = input("What is your last name? ")
        year = str(input("What year were you born in? "))

        start = first[:1]
        password += start
        next = last[:2]
        password += next
        num = year[-2:]
        password += num

        if password in list:
            print("Password already in the password list. ")
        else:
            list.append(password)
            print("Password added")

    elif check == "N":
        print(f"What passwords entered are {list}")
        break

    else:
        print("Invalid input, please enter either Y or N")


    # output = print(f"Your created password is {password}")
