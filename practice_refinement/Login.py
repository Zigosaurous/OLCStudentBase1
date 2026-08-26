list_username = ["StudentNo1", "JaneJones", "ABC123"]
username = input("Please enter a username: ")
password = input("Please enter a password: ")

#username 
while True:
    if username in list_username:
        print("Username already exists. Please enter another username.")
    else:
        list_username.append(username)
        print("Username has been added to the list.")
        break

special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?"]

#password
if len(password) <= 8:
    print("Password is at least 8 characters long.")
    
elif: 
    for char in password:
        if char in special:

