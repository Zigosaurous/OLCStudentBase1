

# 2023 – Task 3 [10]
# A mathematics program shown on the next page creates 10 questions.
# Each question is created by generating two random integers 
# between 1 and 50 inclusive and adding them.

# The program:
# •	outputs the questions
# •	allows the user to input their answer to each question
# •	outputs the user's total mark and the number of correct answers
# •	alters the output based on whether 1 or multiple correct answers are given.

# If both random integers are greater than 25, the user gets 2 marks 
# for a correct answer, otherwise, the user gets 1 mark for a correct answer.
    
# If the user enters a correct answer:
# •	the total mark is incremented by the correct amount
# •	the text "Correct" is stored in a list, otherwise, the text "Incorrect" is stored in the list.
# When all questions have been answered, the list is searched to count how many times "Correct" is stored.

import random
questions = 10
answer_list = []
correct = 0
incorrect = 0
total_mark = 0
for x in range(questions):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    print("What is", num1, "+", num2, "?")
    user_answer = int(input())
    answer = num1 + num2 #1 define answer

    if user_answer == answer:
        if num1 > 25 and num2 > 25: #8 change or to and 
            total_mark = total_mark + 2
            answer_list.append("Correct") #6 change to .append()
        else:
            total_mark = total_mark + 1
    else:
        answer_list = answer_list + ["Incorrect"]
list_length = len(answer_list) #2 change len() function to only answer_list
for i in range(list_length):
    if answer_list[i] == "Correct": #7 change x to i
        correct = correct + 1 #5 change - to +

message = correct #4 define message
if message  == 1:
    message = "answer."
else:
    message = "answers."
print(f"Your total mark is {total_mark} and you had {correct} {message}") #3 change to f string

# # Open the file MATHS.py
# # Save the file asMYMATHS_2023___.py

# # 1.	Identify and correct the errors in the program so that it works 
# # according to the requirements given

# # Save your program.
# # [10 marks]


# import random
# questions = 10
# answer_list = []
# correct = 0
# incorrect = 0
# total_mark = 0
# for x in range(questions - 1):
#     num1 = random.randint(1, 50)
#     num2 = random.randint(1, 50)
#     print("What is", num1, "+", num2, "?")
#     user_answer = input()
#     if user_answer == answer:
#         if num1 > 25 or num2 > 25:
#             total_mark = total_mark + 2
#             answer_list = answer_list + ["Correct"]
#         else:
#             total_mark = total_mark + 1
#     else:
#         answer_list = answer_list + ["Incorrect"]
# list_length = len(answer_list - 1)
# for i in range(list_length):
#     if answer_list[x] == "Correct":
#         correct = correct - 1
# if message  == 1:
#     message = "answer."
# else:
#     message = "answers."
# print("Your total mark is", total_mark, "and you had", correct, message)

