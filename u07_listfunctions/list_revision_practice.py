# Python List Exercises: Student Names and Scores
#
# Scenario:
# You have 2 separate lists.
# One list stores student names.
# The other list stores the corresponding scores.
#
# The score at each index belongs to the student name at the same index.
#
# Example:
# names[0] matches scores[0]
# names[1] matches scores[1]
#
# Use the sample lists below for the questions.

names = [
    "Aiden", "Bella", "Charlie", "Daphne", "Ethan", "Fiona", "Grace", "Henry",
    "Isaac", "Jasmine", "Kai", "Lydia", "Mason", "Nora", "Owen", "Priya",
    "Quentin", "Rachel", "Samuel", "Tina", "Uma", "Victor", "Wendy", "Xavier",
    "Yvonne", "Zach", "Aaron", "Bianca", "Caleb", "Denise"
]

scores = [
    78, 92, 85, 92, 67, 88, 75, 81,
    90, 73, 84, 95, 69, 87, 58, 91,
    76, 83, 95, 64, 72, 89, 77, 68,
    94, 80, 61, 86, 74, 79
]


# --------------------------------------------------
# PART 1: Basic list access and membership
# --------------------------------------------------

# Q1
# Print the full names list using a for loop.

# for name in names:
#     print(name)

# # Q2
# # Print the full scores list using a for loop.

# for score in scores:
#     print(score)

# Q3
# Print the first student name in the list.

# print(names[0])

# # Q4
# # Print the last score in the list.

# print(scores[0])

# Q5
# Find out whether "Charlie" exists in the names list.
# Print True or False.

# if "Charlie" in names:
#     print(True)
# else:
#     print(False)

# # Q6
# # Ask the user to enter a student name.
# # Check whether that student exists in the names list.
# # Print "Student found" or "Student not found".

# check_name = input("Who do you want to check ")

# if check_name in names:
#     print("Student found")
# else:
#     print("Student not found")

# --------------------------------------------------
# PART 2: Finding positions and matching data
# --------------------------------------------------

# Q7
# Find the index position of "Daphne" in the names list.
# Print the index.

# print(names.index("Daphne"))

# # Q8
# # Find Charlie's score by first finding Charlie's index in the names list.
# # Then use that same index to get the score from the scores list.

# position = names.index("Charlie")
# mark = scores[position]
# print(mark)

# Q9
# Ask the user to enter a student name.
# If the student exists, print that student's score.
# If not, print "Student not found".

# check_name = input("Who are you checking ")
# if check_name in names:
#     position = names.index(check_name)
#     mark = scores[position]
#     print(f"{check_name} scored {mark} marks")
# else:
#     print("Student not found")

# Q10
# Print every student's name together with their score.
# Example output:
# Aiden : 78
# Bella : 92
# Charlie : 85

# for i in range(len(names)):
#     print(f"{names[i]} : {scores[i]}")

# --------------------------------------------------
# PART 3: Working with highest and lowest values
# --------------------------------------------------

# Q11
# Find the highest score in the scores list.
# Print the highest score only.

# print(max(scores))

# # Q12
# # Find the lowest score in the scores list.
# # Print the lowest score only.

# print(min(scores))

# Q13
# Find the name of the student who scored the highest mark.
# Assume there is only one highest scorer for now.

# highest_score = max(scores)
# position = scores.index(highest_score)
# name = names[position]
# print(name)

# # Q14
# # Find the name of the student who scored the lowest mark.
# # Assume there is only one lowest scorer for now.

# lowest_score = min(scores)
# position = scores.index(lowest_score)
# name = names[position]
# print(name)

# Q15
# Print a sentence like this:
# "Bella scored the highest mark of 92."

# highest_score = max(scores)
# position = scores.index(highest_score)
# name = names[position]
# print(f"{name} scored the highest mark of {highest_score}")

# --------------------------------------------------
# PART 4: Handling ties
# --------------------------------------------------

# Q16
# In the current list, there are 2 students with the highest score.
# Find the highest score first.
# Then print all student names who got that highest score.

# # find the max score
# maxscore = max(scores)
# maxscorers = []
# for i in range(len(scores)):
#     if scores[i] == maxscore:
#         maxscorers.append(names[i])
# # ["Lydia", "Samuel"]
# maxstring = ",".join(maxscorers) # concatenates all the string value in a list to a string
# print(maxstring)

# # string = ""
# # for name in maxscorers:
# #     string += name
# Q17
# Print the result in this format:
# "Top scorer(s): Lydia, Samuel with 95 marks."
# maxscore = max(scores)
# maxscorers = []
# for i in range(len(scores)):
#     if scores[i] == maxscore:
#         maxscorers.append(names[i])

# maxstring = ", ".join(maxscorers) 
# print(f"Top score(s): {maxstring} with {maxscore}")


# Q18
# Find all students who got the lowest score.
# Print their names and the score.

# minscore = min(scores)
# minscorers = []
# for i in range(len(scores)):
#     if scores[i] == minscore:
#         minscorers.append(names[i])

# minstring = ", ".join(minscorers) 
# print(f"lowest score(s): {minstring} with {minscore}")

# Q19
# Count how many students got the highest score.
# Print the number.

# maxscore = max(scores)
# maxscorers = []
# for i in range(len(scores)):
#     if scores[i] == maxscore:
#         maxscorers.append(names[i])

# print(len(maxscorers))

# Q20
# Count how many students scored above 80.

# maxscorers = []
# for i in range(len(scores)):
#     if scores[i] > 80:
#         maxscorers.append(names[i])

# print(len(maxscorers))


# --------------------------------------------------
# PART 5: Searching and filtering
# --------------------------------------------------

# Q21
# Create a new list that stores the names of students who scored above 80.
# Print the new list using a for loop.

# maxscorers = []
# for i in range(len(scores)):
#     if scores[i] > 80:
#         maxscorers.append(names[i])

# print(maxscorers)

# Q22
# Create a new list that stores the names of students who failed.
# Assume fail means score below 50.
# Print the new list using a for loop.

failscorers = []
for i in range(len(scores)):
    if scores[i] < 50:
        failscorers.append(names[i])

print(failscorers)

# Q23
# Create a new list that stores the scores of students whose names start with the letter "B" or "D".

new_names = []
for i in range(len(names)):
    if names[i] == "B" or names[i] == "D":
        new_names.append(names[i])
print(new_names)

# Q24
# Ask the user to enter a min_score and a max_score
# Print all student names who are within the range of the min and max score.

# Q25
# Ask the user to enter a student name.
# Print whether the student passed or failed.
# Assume pass mark is 50.


# --------------------------------------------------
# PART 6: Ranking-style questions
# --------------------------------------------------

# Q26
# Find the top 3 highest scores only.
# Print the 3 scores.

# Q27
# Find the names of the top 3 highest scorers together with their scores.
# Example output:
# Lydia : 95
# Samuel : 95
# Yvonne : 94

# Q28
# Print the top 3 highest scorers in ranking format.
# Example:
# 1. Lydia : 95
# 2. Samuel : 95
# 3. Yvonne : 94

# Q29
# Handle ties properly.
# If 2 students share the highest score, both should appear before the next lower score.

# Q30
# Find the 2nd highest score in the list.
# Then print all students who got that 2nd highest score.

# Q31
# Find the 3rd highest unique score in the list.
# Then print all students who got that score.


# --------------------------------------------------
# PART 7: Data changes and updates
# --------------------------------------------------

# Q32
# Add a new student name "Elena" into the names list.
# Add her score 93 into the scores list.
# Then print both updated lists.

# Q33
# Ask the user to enter a new student name and score.
# Add both into the correct lists.

# Q34
# Change Ethan's score to 74.
# Print the updated scores list.

# Q35
# Remove "Grace" from the names list.
# Also remove her matching score from the scores list.

# Q36
# Ask the user for a student name.
# If the student exists, remove that student and the matching score.
# If not, print "Student not found".


# --------------------------------------------------
# PART 8: Slightly more advanced list logic
# --------------------------------------------------

# Q37
# Calculate the average score of all students.
# Print the average.

# Q38
# Find out how many students scored above the average.

# Q39
# Print the names of students who scored above the average.

# Q40
# Find the difference between the highest score and the lowest score.

# Q41
# Sort the scores from highest to lowest.
# Print the sorted scores only.



# --------------------------------------------------
# CHALLENGE QUESTIONS
# --------------------------------------------------

# Q42
# Create a new list of grades based on the scores.
# Use this grading system:
# 75 and above = A
# 65 to 74 = B
# 50 to 64 = C
# below 50 = F
# Print each student's name, score, and grade.

# Q43
# Find all students who got grade A.

# Q44
# Print the class leaderboard from highest to lowest.
# Include ranking number, student name, score, and grade.

# Q45
# If a student name appears more than once in the names list,
# print a warning message saying "Duplicate student name found".