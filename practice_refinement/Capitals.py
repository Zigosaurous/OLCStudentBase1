# Task 3.1 ANS
capital_cities = {
    'singapore':'Singapore',
    'japan':'Tokyo',
    'australia':'Canberra',
    'england':'London',
    'france':'Paris',
    'germany':'Berlin'
}
country = input("Please enter the name of a country: ").lower() # Convert the user input to lowercase
remove = input("Would you like to remove any of the entries? (Y or N): ").upper()

if remove == "Y":
    choice = input("What country would you like to remove? ").lower()
    del capital_cities[choice]
    # print(capital_cities) test
add = input("Would you like to add a new entry? (Y or N): ").upper()

if add == "Y":
    key = input("What country would you like to add? ").lower()
    value = input(f"What is the capital of {key}? ")
    capital_cities[key] = value
    # print(capital_cities) #test

if country in capital_cities: # Checks if the country key exists in the capital_cities dictionary
    print(f"The capital of {country} is {capital_cities[country]}.") # Prints out the value of the key that exists

print(capital_cities) 