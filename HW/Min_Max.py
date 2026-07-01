###############################################################
# Scenario: Employee Performance Review

# Finding Maximum, Minimum, and Average Performance Scores 
# Without Built-in Functions
# YOU CANNOT USE ANY PYTHON INBUILT FUNCTIONS TO DO THIS.

# A company conducts annual performance reviews for employees. 
# Each employee is given a performance score out of 100. 
# The HR department wants to:

# - Identify the top-performing employee (highest score).
# - Identify the lowest-performing employee (lowest score).
# - Calculate the average performance score, rounded to 2 decimal places.
# - Identify underperforming employees (those with scores below 50) 
#    -> save them into another dictionary called non_performers.
#   and print a performance warning message to all of these employees.

performance_scores = {
    'Alice': 88, 'Benny': 75, 'Charlie': 92, 'David': 85,
    'Emma': 78, 'Farah': 81, 'George': 66, 'Hassan': 94,
    'Ivy': 71, 'Jack': 88, 'Liam': 45, 'Jessica': 98,
    'Samir': 23, 'Jimmy': 5, 'Bryan': 78, 'Estelle': 9}

# write your code here

first = True
total = 0
count = 0
non_performers = {}

for people in performance_scores:
    score = performance_scores[people]

    if first:
        highest_score = score
        lowest_score = score 
        highest_employee = people 
        lowest_employee = people
        first = False
    else:
        if score > highest_score:
            highest_score = score 
            highest_employee = people 

        if score < lowest_score:
            lowest_score = score
            lowest_employee = people

    total += score 
    count += 1 

    if score < 50:
        non_performers[people] = score

average = round(total / count, 2)

for people in non_performers:
    print(people, ", you have scored less than 50")
    print("You have been given a warming")

# print(highest_employee)
# print(highest_score)
# print(lowest_employee)
# print(lowest_score)