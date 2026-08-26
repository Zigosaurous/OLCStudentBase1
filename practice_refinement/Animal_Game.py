animal_list = []
count = 0

#player 1
while True:
    p1_animal = input("Player 1, please enter an animal: ").lower()
    animal_list.append(p1_animal)
    add = input("Do you want to add anymore? (Y/N) ").lower()
    if add == "n":
        break
    
#player 2
while True:

    if len(animal_list) == 0:
        print("Game over!")
        print("You have guessed all the animals.")
        print(f"You have scored a total of {count} points.")
        break

    else:
        guess = input("Player 2 please make your guess: ").lower()

        if guess in animal_list:
            count += 1
            animal_list.remove(guess)

        else:
            print("Game over!")
            print(f"You have scored a total of {count} points.")
            print(f"The animals left were {animal_list}.")
            break
    