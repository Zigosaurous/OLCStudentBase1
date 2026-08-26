
def div_2(number):
    halved = int(number/2)
    return halved

def odd_or_even(number):
    remainder = number%2 # even number are divisible by 2
    if remainder == 1: # if there is remainder from dividing 2, it is an odd number
        return "Odd" 
    else:
        return "Even"
    
def prime(number):
    if number < 2: # 0 and 1 are not considered prime numbers as they cannot follow the rule where it can only: 1 * itself = itself0
        return "Not prime"
    if number == 2: # 2 is the smallest prime number, that is even
        return "Prime"
    
    if odd_or_even(number) == "Even": # Other than 2, all other even numbers are not prime
        return "Not prime"
    
    for i in range(3, div_2(number) + 1): # to check if it is divisible by any number from 3 to half of the number
        if number % i == 0: # if it is fully divisible by any number, it will have remainder of 0.
            return "Not prime"
    
    return "Prime"  # All other even numbers are not prime
    
while True: # repeat asking for input if it is not valid 
    user_input = input("Please enter a whole number to check if it is prime: ")
    
    if user_input.isdigit():
        number = int(user_input) # convert string to integer
        result = prime(number)  # get the result of the number
        print(f"The number {number} is {result}.")
        break
    else:
        print("Invalid input. Please enter a whole number only.\n") # to let user know the correct input type

