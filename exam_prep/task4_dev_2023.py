
# Task 4 - 2023 Paper - Development of Program
# Open the file SPLIT_SENTENCE.py. You will see the following function that 
# takes a string of words, passed as the parameter word_string, splits it 
# into individual words and stores these words in a list. 
# It returns the list of words. 

# You can assume the string does not contain punctuation marks.

# def split_sentence(word_string):
#     list_sentence = word_string.split(" ")
#     return list_sentence



# # Task 4.1
# 10.	Save the program as CHECK_LIST_2023_<your name>_<centre number>_<index number>.py [7 marks]
# Extend the program by writing another function check_list() that searches 
# through the list of words to find a certain word. 

# If it finds the word in the list, it returns "Yes", otherwise it returns "No". 
# The variable word needs to be passed to the function. 
# The function you write must use the function split_sentence() already provided.
# Save your program.

#---------------------------------------
# Task 4.1 [7]
#---------------------------------------
# write your code here

# def split_sentence(word_string): 
#     list_sentence = word_string.split() 
#     return list_sentence
    


# def check_list(word): # defining check_list() function
#     if word in split_sentence(word_string):
#         return "Yes"
#     else:
#         return "No"

# # # Task 4.2
# # 11.	Save your program as REVERSE_2023_<your name>_<centre number>_<index number>.py [7 marks]
# # Extend your program by writing another function reverse_sentence() 
# # that reverses the words in the string and returns the whole string reversed, 
# # with spaces between the words. 

# # For example, 
# # "the cat sat on the mat" would return: "mat the on sat cat the". 

# # The function you write must use the function split_sentence() already provided. 
# # You must not use the slice operator or the reverse function available in Python. 
# # Your program does not need to consider any spaces before or after 
# # the reversed sentence. Save your program.

# # write your code here


# def reverse_sentence(sentence):
#     # use the function split_sentence() already provided.
#     list_sentence = split_sentence(sentence) ###
#     output = ""

#     for word in list_sentence:
#         output = word + " " + output
#     return output


# print(reverse_sentence("the cat sat on the mat"))



#---------------------------------------
# Task 4.2 [7]
#---------------------------------------






# # Task 4.3
# 12.	Save your program as FUNCTIONS_2023_<your name>_<centre number>_<index number>.py [6 marks]

# Extend your program by using the functions created such that it:
# •	allows the user to input a string of words (validation of this is not necessary)
# •	allows the user to input a word to search for in the string of words
# •	outputs the string of words, split into a list
# •	outputs the string of words, reversed
# •	outputs whether the word input is found in the string of words.
# Save your program.


#---------------------------------------
# Task 4.3 [7]
#---------------------------------------



def split_sentence(word_string): 
    list_sentence = word_string.split() 
    return list_sentence
    

def check_list(word): # defining check_list() function
    if word in split_sentence(word_string):
        return "Yes"
    else:
        return "No"
    
def reverse_sentence(sentence):
    # use the function split_sentence() already provided.
    list_sentence = split_sentence(sentence) ###
    output = ""

    # this for loop reverses the string
    for word in list_sentence:
        output = word + " " + output
    return output

word_string = input("Input a string of words ") # ask the user for the string of words
word = input("What word do you want to check ") # Finds out which word does the user want to find in the string of words
print(split_sentence(word_string)) # calls split_sentence()
print(reverse_sentence(word_string))# calls reverse_sentence()
print(f"{check_list(word)} the word is found in the string of words") # calls check_list() 





