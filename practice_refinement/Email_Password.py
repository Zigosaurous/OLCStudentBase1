firstname = input("Please enter your first name: ").lower()
lastname = input("Please enter your last name: ").lower()
email_id = firstname[:3] + lastname[-3:] + "@example.com"
print("Your email ID is " + email_id)

while True:
    email = input("Please re-enter password: ").lower()

    if email.find("@") == -1:
        print("Symbol '@' missing from email. ")
    elif email.find(".") == -1:
        print("Symbol '.' missing from email. ")
    elif email != email_id:
        print(f"Input email {email} does not match generated email {email_id}")
    elif email == email_id:
        print(f"{email} is valid")
        break


