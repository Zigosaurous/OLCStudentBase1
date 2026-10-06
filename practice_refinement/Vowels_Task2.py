############################################################
# TASK 2 - REFINEMENT OF PROGRAM
############################################################

# The program allows a user to enter a word and stores the word in a list.


# word_list = []

# word = input("Enter a word containing at least 5 letters: ")
# word_list.append(word)



#------------------------------------------------------------
# Task 2.1 [4]
#------------------------------------------------------------

# Extend the program so that the word entered is validated
# before it is stored in the list.
#
# The program must:
# - check that the word contains at least 5 characters;
# - check that every character in the word is an alphabetic letter;
# - if the word is invalid, output a suitable message explaining why and
#   repeatedly ask the user to enter another word until a
#   valid word is entered;
# - convert the valid word to lower case before storing it
#   into a list named word_list.

# word_list = []
# while True:
#     word = input("Enter a word containing at least 5 letters: ")
#     if len(word) != 5:
#         print("Invalid word, Please enter word with 5 characters. ")
#     elif word.isalpha() == False:
#         print("Invalid word, Please enter characters all being a alphabetic.")
#     else:
#         print("Valid word")
#         word_list.append(word.lower())
#         break

# print(word_list) test



#------------------------------------------------------------
# Task 2.2 [5]
#------------------------------------------------------------

# Copy and paste your program from Task 2.1.
#
# Extend the program so that it:
# - asks the user whether another word is to be entered
#   after each valid word is stored;
# - accepts Y to enter another word and N to stop;
# - continues to apply the validation rules from Task 2.1
#   to every word entered;
# - stores every valid word in word_list;
# - outputs each word from the completed word_list one by one
#   when the user chooses to stop.
#
# You can assume that the user will only enter Y or N when asked
# whether another word is to be entered.

# word_list = []
# while True:
#     word = input("Enter a word containing at least 5 letters: ")
#     if len(word) != 5:
#         print("Invalid word, Please enter word with 5 characters. ")
#     elif word.isalpha() == False:
#         print("Invalid word, Please enter characters all being a alphabetic.")
#     else:
#         print("Valid word")
#         word_list.append(word.lower())
#         check = input("Do you want to add another word? (Y/N) ").upper()
#         if check == "Y":
#             continue
#         else:
#             print(word_list)
#             break

# print(word_list)





#------------------------------------------------------------
# Task 2.3 [6]
#------------------------------------------------------------

# Copy and paste your program from Task 2.2.
#
# A dictionary is required to count the number of times each
# vowel occurs in all the words stored in word_list.
#
# Use the following dictionary:

vowel_count = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}


word_list = []
while True:
    word = input("Enter a word containing at least 5 letters: ")
    if len(word) != 5:
        print("Invalid word, Please enter word with 5 characters. ")
    elif word.isalpha() == False:
        print("Invalid word, Please enter characters all being a alphabetic.")
    else:
        print("Valid word")
        word_list.append(word.lower())
        check = input("Do you want to add another word? (Y/N) ").upper()
        if check == "Y":
            continue
        else:
            print(word_list)
            break

# vowels = []
# count_a = 0
# count_e = 0
# count_i = 0
# count_o = 0
# count_u = 0

for word in word_list:
    for letter in word:
        if letter in vowel_count:
            vowel_count[letter] = vowel_count[letter] + 1

print(vowel_count)

for letter in vowel_count:
    print(f"{letter} has {vowel_count[letter]} in the word_list")
# for x in vowels:
#     if x == "a":
#         count_a += 1
#     elif x == "e":
#         count_e += 1
#     elif x == "i":
#         count_i
# print(vowels)

# Extend the program so that it:
# - checks every character in every word stored in word_list;
# - increases the correct value in vowel_count whenever a
#   vowel is found;
# - outputs the completed vowel_count dictionary;
# - outputs the count for each of the five vowels using
#   suitable output messages.



