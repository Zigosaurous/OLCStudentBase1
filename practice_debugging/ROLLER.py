
age = 0
height = float(0) 
rejected = 0 #7
rider = 0
age = int(input("Please enter your age ")) #1
height = float(input("Please enter your height ")) 
while age > 0 and height != 0: #2
    if age < 7 or age > 70 or height <= 1.3: 
        if age < 7:
            print("You are too young to ride") 
        if age > 70: #5
            print("You are too old to ride") 
        if height <= 1.3:
            print("You are too short to ride") 
        rejected = rejected + 1 #8
    else: #3
        print("You can ride the Roller Coaster") 
        rider = rider + 1 #4
        age = int(input("Please enter your age "))
        height = float(input("Please enter your height ")) 
print("Number of people rejected ", rider) 
print("Number of riders ", rejected)