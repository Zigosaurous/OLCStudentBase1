flag = True
list_name_totals = [] #1 added a = before the []
counter = 1
total = 0
while flag:
    name = input("Please enter the Player's name: ")
    length_string = len(name) #2 changed name.len() to len(name)
    name = name.upper()
    print("You are player " + str(counter)) #
    for x in range(length_string): # 7
        char = name[x]
        value = ord(char) #3 changed num to ord
        total = total + value
    list_name_totals.append(total)
    print("Your total is " + str(total))
    more = input("Would you like to enter another player's name? Enter Yes or No. ")
    if more == "No":
        flag = False
    else:
        counter += 1 #4 changed count to counter

    highest = max(list_name_totals) #5changed ceil to max
    for x in range(len(list_name_totals)): #6 added a len()
        if list_name_totals[x] == highest:
            position = x 

    print ("The highest value is " + str(highest) + " and that is player " + str(position))

