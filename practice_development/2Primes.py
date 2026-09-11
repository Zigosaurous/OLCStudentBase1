def div_2(number):
      halved = int(number/2)
      return halved

# print(div_2(5))

# #Task 1

def odd_or_even(number):
    remainder = number % 2
    if remainder == 1:
        return "Odd"
    else:
        return "Even"

# print(odd_or_even(3)) #test

#Task 2

def prime(number):

    if number < 2:
        return "Not prime"
    elif number == 2:
        return "Prime"
    elif odd_or_even(number) == "Even":
        return "Not prime"
    else:
        for num in range(3, div_2(number)+1):
            check = number % num
            if check == 0:
                return "Not prime"
        return "Prime"

# print(div_2(3)) #test
# print(prime(3))

#Task 3 

while True: # repeat asking for input if it is not valid 
    user_input = input("Please enter a whole number to check if it is prime: ")
    
    if user_input.isdigit():
        number = int(user_input) # convert string to integer
        result = prime(number)  # get the result of the number
        print(f"The number {number} is {result}.")
        break
    else:
        print("Invalid input. Please enter a whole number only.\n") # to let user know the correct input type

    



    
    



     
     