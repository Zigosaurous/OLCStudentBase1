# The following program takes in 2 user entries and verifies if the users are Singaporeans 
# by checking if the first letter of each entry is "S". 
# If the user is a Singaporean, the program prints a welcome home message. 
# Otherwise, it prints a welcome to Singapore message.

# ID = ""
# for i in range(2):
#     ID = input("Enter ID: ")
#     if ID[0] == "S":
#         print("Welcome home!")
#     else:
#         print("Welcome to Singapore!")
      
# Task 2.1
# Edit the program so that
# 1.   It takes in 5 entries,[1]

# ID = ""
# for i in range(5):
#     ID = input("Enter ID: ")
#     if ID[0] == "S":
#         print("Welcome home!")
#     else:
#         print("Welcome to Singapore!")

# 2.   It prints the same welcome home message if the first letter of the entry is either "S" or "T".[2]

# ID = ""
# for i in range(5):
#     ID = input("Enter ID: ")
#     if ID[0] == "S" or ID[0] == "T":
#         print("Welcome home!")
#     else:
#         print("Welcome to Singapore!")

# 3.   The program counts the total number of Singaporeans in the list.[3]

# num_people = []

# ID = ""
# for i in range(5):
#     ID = input("Enter ID: ").upper()
#     if ID[0] == "S" or ID[0] == "T":
#         print("Welcome home!")
#         num_people.append("Singaporean")
#     else:
#         print("Welcome to Singapore!")

# print("Number of Singaporeans in the list is", len(num_people))
# Copy the Code Above. Write Your Code Here.




# Task 2.2
# Edit the program so that it
# 4.   Checks that the length of the ID is 9 characters. 
# 5.   Otherwise, it will produce an error message and keep asking the user to re-enter the ID.[2]
# 6.   Works for any number of entries.[2]

# Copy the Code Above. Write Your Code Here.

num_people = []

ID = ""
num_entries = int(input("How many entries? "))
for i in range(num_entries):
    while True:
        ID = input("Enter ID: ").upper()
        if len(ID) == 9:
            break
        else:
            print("ID must be 9 characters long.")

    if ID[0] == "S" or ID[0] == "T":
        print("Welcome home!")
        num_people.append("Singaporean")
    else:
        print("Welcome to Singapore!")

print("Number of Singaporeans in the list is", len(num_people))