
def split_sentence(word_string):
    list_sentence = word_string.split()
    return list_sentence


#Task 4.1
def check_list(word):
    word_list = split_sentence(word_string)
    for items in word_list:
        if word == items:
            return "Yes"
        else:
            return "No"

word_string = input("What is the sentence you would like to input? ") #test
word = input("What word would you like to check ")
print(check_list(word))


#Task 4.2
reverse_list = []

def reverse_sentence(word_string):
    word_string = split_sentence(word_string)
    print(word_string)
    for items in word_list:
        reverse_list.append(items)
        return reverse_list

print(reverse_sentence(word_string))

