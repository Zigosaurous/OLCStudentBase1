flag = True #1
while flag:
	length = float(input("What is the length of the parcel?"))
	width = float(input("What is the width of the parcel?"))
	depth = float(input("What is the depth of the parcel?"))
	if length > 50 and width > 50 and depth > 50: #6
		parcel_size = "large"
		print(parcel_size) #8
	elif length > 50 and width > 50 and depth <= 50: #11 #12
		parcel_size = "medium" #7
		print(parcel_size) #9
	else:
		parcel_size = "small"
		print(parcel_size) #10
	more_parcel = input("Do you want to enter another parcel? Y or N") 
	if more_parcel == "N": #3 #4
		flag = False #5