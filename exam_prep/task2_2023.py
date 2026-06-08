
### The below are the starter codes provided for 
### the questions on Refinement of Program
### Copy and Paste this as part of the start of Your Question.

######### ANIMALGAME.py #########
# num_of_animals = 5
# for x in range(num_of_animals):
# 	p1_animal = input("Player 1, please enter an animal: ")
# 	p1_animal = p1_animal.lower()
# 	p2_guess = input("Player 2, please enter your guess: ")
# 	p2_guess = p2_guess.lower()

#-----------------------------------------------

# Task 1.1
#---------------------------------

# 4 marks - good
# animals = []
# while True:
# 	p1_animal = input("Player 1, please enter an animal: ")
# 	p1_animal = p1_animal.lower()
# 	animals.append(p1_animal)
	
# 	another = input("Do you want to continue? (Y/N) ")
# 	if another.upper() == "N":
# 		break
		
# p2_guess = input("Player 2, please enter your guess: ")
# p2_guess = p2_guess.lower()



# Task 1.2
#---------------------------------
# 2 marks (-1) for indentation. fatal error
# animals = []
# while True:
# 	p1_animal = input("Player 1, please enter an animal: ")
# 	p1_animal = p1_animal.lower()
# 	animals.append(p1_animal)
	
# 	another = input("Do you want to continue? (Y/N) ")
# 	if another.upper() == "N":
# 		break
		
# score = 0
# while True:
#     p2_guess = input("Player 2, please enter your guess: ")
#     p2_guess = p2_guess.lower()

#     if p2_guess in animals:
#         score += 1 
#         animals.remove(p2_guess)
#     else:
#          break # indentation issue here...

# Task 1.3
#---------------------------------
# 3 marks

animals = []
while True:
	p1_animal = input("Player 1, please enter an animal: ")
	p1_animal = p1_animal.lower()
	animals.append(p1_animal)
	
	another = input("Do you want to continue? (Y/N) ")
	if another.upper() == "N":
		break
		
score = 0
while True:
    p2_guess = input("Player 2, please enter your guess: ")
    p2_guess = p2_guess.lower()

    if p2_guess in animals:
        score += 1 
        animals.remove(p2_guess)
    else:
        print(f"Game Over your score is {score}")
        print(f"The remaining animals are {animals}")
        break
    
    if len(animals) == 0:
          print("Player two is the winner!") # indentation error...
          break