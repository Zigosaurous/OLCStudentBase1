
# Task 3
# The following program should read a denary non-negative integer from the user. 
# The program will then convert the denary integer to its 
#    binary value and print it to the screen. 
# The “division by 2” method is employed to carry out the conversion. 
# There are several syntax errors and logical errors in the program.

NEW_BASE = 2 #4 #5
num = input("Enter a non-negative integer: ") #1 and #2
num = int(num) #7
result = ""
q = num
r = q % NEW_BASE 
result = str(r) + result
q = q // NEW_BASE
while q > 0: #3
    r = q % NEW_BASE
    result = result + str(r)
    q = q // NEW_BASE 
print(num, "in Decimal is", result , "in Binary.") #6


# Open the file D2B.py
# Save the file as MYD2B___
# 
# Identify and correct the errors in the program so that it 
# works correctly according to the description above. Save your program.
#  [10] 
