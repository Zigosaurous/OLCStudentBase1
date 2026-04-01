import random
secret_code = ""
for i in range(3):
    digit = str(random.randint(1, 5))
    secret_code = secret_code + digit

# print(secret_code) # remember to comment off later  

print("Guess the 3-digit number. Each digit is from 1 to 5: ")
print("You have 5 tries. Enter your guess (e.g. 123). ")

#ask the user to guess 

for j in range(5):
    guess = input("Enter your guess: ")

    #count how many correct 

    count = 0
    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            count += 1
    print(f"You have {count} correct digits in the correct position.")

    # stop the user after 5 tries

    if guess == secret_code:
        print("You have guessed the code")
        break
    else:
        print("You did not guess it")
else:
    # code here will run on successful completion of loop
    print(f"The correct answer is {secret_code}")



