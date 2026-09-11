
# Task 3
# The following program converts a range of Fahrenheit temperature readings
# to Celsius and vice versa. It begins by allowing the user to choose between
# an “F” for Fahrenheit to Celsius conversion or “C” for Celsius to Fahrenheit conversion.
# The program will print out the chosen conversions from the start value to the end value (inclusive).
# The formula for converting Fahrenheit to Celsius is:
#        C = 5/9 x ( F – 32 )
# The formula for converting Celsius to Fahrenheit is:
#        F = 32 + ( C * 9/5 )


def displayWelcome():
    print("This program will convert a range of temperatures")
    print("Enter (F) to convert Fahrenheit to Celsius")
    print("Enter (C) to convert Celsius to Fahrenheit\n")

def getConvertTo():
    which = input("Enter selection: ") #1
    if which != "F" and which != "C": #3
        which = input("Enter selection: ") #2
    return which

def displayFahrenToCelsius(start, end):
    print("\n Degrees", " Degrees")
    print("Fahrenheit", "Celsius")

    for temp in range(start, end + 1):
        converted_temp = temp - 32 * 5/9
        print("{:4.1f}      {:4.1f}".format(temp, temp))

def displayCelsiusToFahren(start, end):
    print("\n Degrees", "Degrees")
    print(" Celsius", "Fahrenheit")

    for temp in range(start, end):
        converted_temp = 9/5 * temp * 32
        print("{:4.1f}      {:4.1f}".format(temp, converted_temp))

# --- main

#Display program welcome
displayWelcome()

# Get which conversion from user
which = getConvertTo()

print(which)

# Get range of temperatures to convert
temp_start = int(input("Enter starting temperature to convert: "))
temp_end = int(input("Enter ending temperature to convert: "))

# Display range of converted temperatures
if which == "F":
    displayFahrenToCelsius(temp_start, temp_end)
elif which == "C": #3
    displayCelsiusToFahren(temp_start, temp_end)


# Open the file TEMPCONV_BUGS.py
# Save the file as TEMPCONV_DEBUG__
# 12 Identify and correct the errors in the program so 
# that it works correctly according to the rules above.
# [10]
# Save your program.
