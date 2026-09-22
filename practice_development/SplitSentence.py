
def split_sentence(word_string):
    list_sentence = word_string.split()
    return list_sentence


#Task 4.1
def check_list(word, word_string):
    word_list = split_sentence(word_string) #   black , the cat is black
    # for items in word_list:
    # if word == items:
    if word in word_list:
        return "Yes"
    else:
        return "No"

# word_string = input("What is the sentence you would like to input? ") #test
# word = input("What word would you like to check ")
# print(check_list("cat","the cat is black"))


#Task 4.2
# reverse_list = []

def reverse_sentence(word_string):
    word_string = split_sentence(word_string)

    output = ""

    for w in word_string:  ##the cat is black
        output = w + " " + output   #the 

    return output



    print(word_string)
    # for items in word_list:
    #     reverse_list.append(items)
        # return reverse_list

print(reverse_sentence(word_string))

