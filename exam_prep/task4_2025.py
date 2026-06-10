
# Task 5

# A company is creating a system to calculate, record and 
# output different information relating to customer sales.

# All code should have appropriate comments and all identifiers 
# should be appropriately named. [4]

# You can assume that all costs will be valid and in dollars.

#========================================================
# Task 5.1
# Write a function total_cost() that calculates the total cost of a sale by:
# •	taking cost as a parameter
# •	calculating the total cost by adding 9% for tax purposes
# •	returning the total cost
# Save your program.
# [3]
# -------------------------------------------------

# Task 5.1

# def total_cost(cost): # define total_cost()
#     new_cost = (cost/100) * 109 # finds the cost after adding 9% for tax
#     return new_cost

# print(total_cost(100)) test










# -------------------------------------------------


#========================================================
# Task 5.2
# Copy and paste your program from sub-task 5.1.
# A discount may be applied to a customer’s purchase.

# Extend the program by writing a function discount() that:
# •	takes cost as a parameter

# •	deducts a discount of 5% from the total cost if the 
#     total cost is between $50 (inclusive) and $100 (exclusive) 

# •	deducts a discount of 10% from the total cost if the 
#     total cost is $100 or greater 
# •	returns the total cost with or without a discount as appropriate 

# Your function must use the function total_cost() to 
# calculate the total cost for the sale.

# Save your program.
# [4]

# -------------------------------------------------
# Task 5.2

# def total_cost(cost): # define total_cost()
#     new_cost = (cost/100) * 109 # finds the cost after adding 9% for tax
#     return new_cost

# def discount(new_cost): # define discount()
#     if new_cost >= 50 and new_cost < 100: # if new_cost is in the range there will be a 5% discount 
#         discounted_cost = (new_cost/100) * 95
#         return discounted_cost
#     elif new_cost >= 100: # if new_cost is in the range there will be a 10% discount 
#         discounted_cost = (new_cost/100) * 90
#         return discounted_cost
#     else:
#         return new_cost # if new_cost < 50 no discount

# print(total_cost(100)) 
# print(discount(total_cost(100))) test












# -------------------------------------------------




#========================================================
# Task 5.3
# Copy and paste your program from sub-task 5.2.
# A customer receives reward points on a purchase.
# Extend your program by writing another function reward_points() that:

# •	takes the total cost with any discount applied as a parameter

# •	calculates the number of reward points received for the purchase. 
#   A customer receives 3 reward points for each whole dollar ($) spent 

# •	returns the number of reward points received. 
# Save your program.
# [3]

# -------------------------------------------------
# Task 5.3

# def total_cost(cost): # define total_cost()
#     new_cost = (cost/100) * 109 # finds the cost after adding 9% for tax
#     return new_cost

# def discount(new_cost): # define discount()
#     if new_cost >= 50 and new_cost < 100: # if new_cost is in the range there will be a 5% discount 
#         discounted_cost = (new_cost/100) * 95
#         return discounted_cost
#     elif new_cost >= 100: # if new_cost is in the range there will be a 10% discount 
#         discounted_cost = (new_cost/100) * 90
#         return discounted_cost
#     else:
#         return new_cost # if new_cost < 50 no discount

# def reward_points(discounted_cost): # define reward_points()
#     num_of_dollar = discounted_cost // 1 # finds how many dollars rounded down
#     num_reward_points = num_of_dollar * 3 # finds how many reward points
#     return num_reward_points














# -------------------------------------------------



#========================================================
# Task 5.4
# Copy and paste your program from sub-task 5.3.
# A customer may receive a voucher code that can be used for a future purchase. 
# Extend your program by writing a function voucher() that:

# •	takes the total cost with any discount applied and the customer’s 
#   first name as parameters

# •	creates a voucher code that is the first three letters of the customer’s name 
#   then the string "05PERCENT", if the total cost is between $25 (exclusive) and $50 (inclusive)

# •	creates a voucher code that is the first three letters of the customer’s name 
#   then the string "10PERCENT", if the total cost is greater than $50

# •	returns the voucher code or None as appropriate.
# Save your program.
# [3]

# -------------------------------------------------
# Task 5.4

def total_cost(cost): # define total_cost()
    new_cost = (cost/100) * 109 # finds the cost after adding 9% for tax
    return new_cost

def discount(new_cost): # define discount()
    if new_cost >= 50 and new_cost < 100: # if new_cost is in the range there will be a 5% discount 
        discounted_cost = (new_cost/100) * 95
        return discounted_cost
    elif new_cost >= 100: # if new_cost is in the range there will be a 10% discount 
        discounted_cost = (new_cost/100) * 90
        return discounted_cost
    else:
        return new_cost # if new_cost < 50 no discount

def reward_points(discounted_cost): # define reward_points()
    num_of_dollar = discounted_cost // 1 # finds how many dollars rounded down
    num_reward_points = num_of_dollar * 3 # finds how many reward points
    return num_reward_points

def voucher(discount(total_cost(cost)), name):
    if discount(total_cost(cost)) > 25 and discount(total_cost(cost)) <= 50:
        







# -------------------------------------------------



#========================================================
# Task 5.5
# Copy and paste your program from sub-task 5.4.
# The company wants an interface for the system.

# Extend your program to create an interface that:
#   •	takes the first name of the customer as input

#   •	takes the cost of the sale as input

#   •	outputs a receipt for the customer, using the correct functions, that shows:
#       o	the title "Receipt" 
#       o	the total cost of the sale (to 2 decimal places)
#       o	the discounted cost of the sale (to 2 decimal places)
#       o	the reward points received
#       o	the voucher code created. If no voucher code is created the text 
#           "You need to spend over $25 for a voucher code." should be output

#   •	writes the voucher code that is created (if any) to the file vouchercode.txt 

# Suitable input and output messages must be used.
# Save your JupyterLab notebook for Task 5.
# [8]

# -------------------------------------------------
# Task 5.5











# -------------------------------------------------








