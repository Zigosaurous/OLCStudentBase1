# num_members = 15
#   for x in range(num_members):
#       sport = input("What is the member's preferred sport?")

# Task 5.1
# [3 marks]
# Edit the program to repeatedly prompt the organizer to enter a member's preferred sport. 
# The loop should stop when the organizer enters 'done'

# num_members = 15
# for x in range(num_members):

# good to put a space whenever using input()
# remember to use .lower() to make it case insensitive

# while True:
#     sport = input("What is the member's preferred sport? ")
#     if sport == "done":
#         break




# Task 5.2
# [2 marks]
# Edit your program to convert each sport to lowercase and then store it into a list.

while True:
    sport = input("What is the member's preferred sport? ")
    if sport == "done":
        break


# Task 5.3
# [5 marks]
# Edit your program to display the number of members that prefer a specific sport. The program must:

# Ask the organizer to input a sport to search for in the list.
# Output an appropriate message if the sport does not exist in the list. (i.e. nobody likes it)
# Output the sport and the number of members who prefer that specific sport.
# Your program must handle upper and lower case search queries 
# (i.e. users can type "SOCCER" to search for "Soccer"). Suitable input and output messages must be used.