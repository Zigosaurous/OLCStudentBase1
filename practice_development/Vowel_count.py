vowels = ['a','e','i','o','u'] # initalise the vowels list to check
word_list = [] # initalise table to store the words
max_vowels = 0 # initialise max number of vowels 
max_word = "" # initialise word with max number of vowels
total_vowels= 0 # initalise total vowels in all 5 words
for x in range(5):
    vowel_count = 0 # initalise the vowel count
    while True:
        word = input("Please enter your word: ").lower() # convert the word to lowercase for checking
        if word.isalpha(): # only will be True if there is purely letters and no spacing or special characters
            for char in word: # loop through each character
                if char in vowels: # check if character exists in the vowel list
                    vowel_count += 1 # increase the counter by 1

            total_vowels += vowel_count # add vowel count for this word to the total
            if vowel_count> 2: # only when vowel count more than 2
                word_list.append(word) # it is added to the list
            if vowel_count > max_vowels: # using the max algorithm 
                max_word = word # update the max word
                max_vowels = vowel_count # update the max count  

            break # update the status of the check to break out of the loop

# print the required outputs
print(f"The word with the highest vowel is {max_word}.")
print("The list of words with more than 2 vowels: ", word_list)
print("The total number of vowels in all 5 words: ", total_vowels)



