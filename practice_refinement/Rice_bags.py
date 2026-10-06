bags_rice = int(input("How many rice bags would you like to check? "))
upper_bound = 5.1
lower_bound = 4.9
over_count = 0
under_count = 0

for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
        over_count += 1
    elif bag_weight < lower_bound:
        print("The bag of rice is underweight")
        under_count += 1
    else:
        print("The bag of rice is the correct weight")

print(f"The number of bags that were underweight is {under_count}")
print(f"The number of bags that were overweight is {over_count}")
      