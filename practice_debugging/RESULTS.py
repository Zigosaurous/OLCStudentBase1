name_list = []
mark_list = []
dist_list = []
pass_list = []
fail_list = []
count = 0 #9

flag = True
while flag == True: #3
    name = input("Enter student's name: ") #1
    name_list += [name]
    while True:
        mark = int(input('Enter score of student: '))
        if mark >= 0 and mark <= 100: #8
            break
        else:
            print('Invalid mark!')
    mark_list += [mark] #6
    count += 1
    if mark >= 75: #7
        dist_list += [name]
    elif mark >= 50:
        pass_list += [name]
    else:
        fail_list += [name]
    more = (input('Would you like to enter another score, Y or N?: ')).upper() #4 #5
    if more == 'N':
        flag = False
average = round(sum(mark_list)/len(mark_list), 2) #2
num_dist = len(dist_list)
num_fail = len(fail_list)
print("You entered " + str(count) + " scores.")
print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
print("Average score is " + str(average))