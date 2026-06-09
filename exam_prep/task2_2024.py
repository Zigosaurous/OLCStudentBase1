######### LOGIN.py #########
list_username = ["StudentNo1", "JaneJones", "ABC123"] 
username = input("Please enter a username: ")
password = input("Please enter a password: ") 


# Task 1.1 #######################
# 4 MARKS
while True:

    check = input("What is your username? ")
    if check in list_username:
        print("Your username exist")
    
    else:
        list_username.append(check)
        break







# Task 1.2 #######################

password = input("Please enter a password: ") 


number = ["1","2","3","4","5","6","7","8","9"]
special = ["@","!","/","?"]

while True:
    if number not in password:
        print("Invalid password")
    elif special not in password:
        print("Invalid password")
    elif len(password) <= 8:
        print("Invalid password")
    else:
        print("Valid password")
        break
    


