
################ SET 1: Country and Capital ################

################ Define a dictionary ###############
# Define a dictionary named countries which will store a country and its capital city.

# 'Singapore' has capital 'Singapore'
# 'Malaysia' has capital 'Kuala Lumpur'
# 'Thailand' has capital 'Bangkok'
# 'Japan' has capital 'Tokyo'
# '''
# # write and test your code here
# '''

# countries = {"Singapore" : "Singapore",
#              "Malaysia" : "Kuala Lumpur",
#              "Thailand" : "Bangkok",
#              "Japan" : "Tokyo"
# }

# print(countries)

# ################ Retrieve values from a dictionary ###############
# # Print out the capital city of Malaysia only.
# # Print out the capital city of Japan only.
# '''

# # write and test your code here

# '''
# print(countries["Malaysia"]) # value
# print(countries["Japan"])

# ########### Change the value of a dictionary key ###############
# # Change the capital city of Thailand to 'Phuket'.
# # Change the capital city of Singapore to 'Toa Payoh'.
# '''
# # write and test your code here
# '''
# countries["Thailand"] = "Phuket"
# countries["Singapore"] = "Toa Poyah"
# print(countries)


# ############ Add a new key / value to the dictionary #####################
# # Add a new country => Indonesia with capital Jakarta.
# # Add a new country => South Korea with capital Seoul.
# '''

# # write and test your code here

# '''

# countries["Indonesia"] = "Jakarta"
# countries["South Korea"] = "Seoul"

# print(countries)

# ############ Delete a key / value from the dictionary #####################
# # Delete the country Singapore from the dictionary.
# '''

# # write and test your code here

# '''

# del countries["Singapore"]
# print(countries)


# ########### Loop through to Retrieve Keys ##################
# # Write a for loop, and only display the name of each country.
# # Only display the keys.
# '''

# # write and test your code here

# '''
# for names in countries:
#     print(names)
# ########### Loop through to Retrieve Values ##################
# # Write a for loop, and only print out the capital cities.
# '''

# # write and test your code here

# '''

# for names in countries:
#     print(countries[names])

# ########### Loop through to Retrieve Key and Values ##################
# # Write a for loop, and print out the country and its capital city.

# # Example:
# # Malaysia has capital city Kuala Lumpur
# # Japan has capital city Tokyo

# for names in countries:
#     print(f"{names} has a capital city {countries[names]}")
'''

# write and test your code here

################ SET 2: Student and Marks ################

################ Define a dictionary ###############
Define a dictionary named marks which will store a student name and the marks they scored.

'Alice' scored 78
'Ben' scored 64
'Chloe' scored 89
'Daniel' scored 55
'''

marks = {"Alice" : 78,
         "Ben" : 64,
         "Chloe" : 89,
         "Daniel" : 55

}

print(marks)

# write and test your code here

'''
################ Retrieve values from a dictionary ###############
Print out the marks scored by Alice only.
Print out the marks scored by Daniel only.
'''

print(marks["Alice"])
print(marks["Daniel"])

# write and test your code here

'''
########### Change the value of a dictionary key ###############
Change Ben's marks to 70.
Change Daniel's marks to 60.
'''

marks["Ben"] = 70
marks["Daniel"] = 60

print(marks)

# write and test your code here

'''
############ Increase the value of a dictionary key ############
Increase Chloe's marks by 5.
Decrease Alice's marks by 3.
'''

marks["Chloe"] = marks["Chloe"] + 5
marks["Alice"] = marks["Alice"] - 3

print(marks)

# write and test your code here

'''
############ Add a new key / value to the dictionary #####################
Add a new student => Ethan who scored 82.
Add a new student => Fiona who scored 91.
'''

marks["Ethan"] = 82
marks["Fiona"] = 91

print(marks)

# write and test your code here

'''
############ Delete a key / value from the dictionary #####################
Delete Daniel from the dictionary.
'''

del marks["Daniel"]

print(marks)

# write and test your code here

'''
########### Loop through to Retrieve Keys ##################
Write a for loop, and only display the name of each student.

Only display the keys.
'''

for names in marks:
    print(names)

# write and test your code here

'''
########### Loop through to Retrieve Values ##################
Write a for loop, and only print out the marks.
'''
for names in marks:
    print(marks[names])
# write and test your code here


'''



########### Loop through to Retrieve Key and Values ##################
Write a for loop, and print out the student name and marks.

Example:
Alice scored 78 marks
Ben scored 64 marks
'''

for names in marks:
    print(f"{names} scored {marks[names]} marks")

# write and test your code here

################ SET 3: Game Item and Quantity ################

################ Define a dictionary ###############
# Define a dictionary named inventory which will store a game item 
# and the quantity owned by the player.

# 'potion' quantity is 5
# 'sword' quantity is 1
# 'shield' quantity is 1
# 'arrow' quantity is 20
'''

# write and test your code here

'''
################ Retrieve values from a dictionary ###############
# Print out the quantity of potion only.
# Print out the quantity of arrow only.
'''

# write and test your code here

'''
########### Change the value of a dictionary key ###############
# Change the quantity of sword to 2.
# Change the quantity of shield to 3.
'''

# write and test your code here

'''
############ Increase the value of a dictionary key ############
# Increase the quantity of potion by 10.
# Decrease the quantity of arrow by 5.
'''

# write and test your code here

'''
############ Add a new key / value to the dictionary #####################
# Add a new item => bow with quantity 1.
# Add a new item => apple with quantity 8.
'''

# write and test your code here

'''
############ Delete a key / value from the dictionary #####################
# Delete apple from the dictionary.
'''

# write and test your code here

'''
########### Loop through to Retrieve Keys ##################
# Write a for loop, and only display the name of each item.

# Only display the keys.
'''

# write and test your code here

'''
########### Loop through to Retrieve Values ##################
# Write a for loop, and only print out the quantities.
# '''

# # write and test your code here

'''
########### Loop through to Retrieve Key and Values ##################
# Write a for loop, and print out the item and quantity.

# Example:
# potion quantity: 5
# arrow quantity: 20
# '''

# write and test your code here