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
    answer = num1 + num2
    if user_answer == answer: #4
        if num1 > 25 and num2 > 25:
            total_mark = total_mark + 2
            # print(total_mark)
            answer_list.append("Correct") #1 #2
        else:
            total_mark = total_mark + 1
    else:
        answer_list.append("Incorrect")
# print(answer_list)
list_length = len(answer_list) #3
for i in range(list_length):
    if answer_list[i] == "Correct":
        correct = correct + 1
if correct  == 1: #5
    message = "answer."
else:
    message = "answers."
print("Your total mark is", total_mark, "and you had", correct, message)