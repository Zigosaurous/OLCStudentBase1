def split_sentence(word_string):
    list_sentence = word_string.split()
    return list_sentence


def check_list(word):
    word_list = split_sentence(word_string)
    for x in word_list: 
        if x == word:
            return "Yes" 
        
    return "No"
    

def reverse_sentence():
    word_list = split_sentence(word_string)
    reversed_string=""
    for x in range(len(word_list)-1,0,-1): 
        reversed_string += word_list[x] + " " 

    return reversed_string

word_string = input("Please enter a string of words: ")
word_search = input("Please enter a word to search for in the string: ")


print("Words as a list: ", split_sentence(word_string))
print("Reversed: ",reverse_sentence())
print("Is there the word in the string? ",check_list(word_search))
