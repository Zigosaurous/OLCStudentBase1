def square_side(sq_perimeter):
     side_length = sq_perimeter / 4
     return side_length

#Task 1

def square_area(perimeter):
    side = square_side(perimeter) 
    area = side * side
    return area

# print(square_area(16))

#Task 2

def circle_diam(circumference):
    diameter = circumference / 3.14
    return diameter

#Task 3 

def circle_area(circumference):
    radius = circle.diam(circumference) / 2
    area = 3.14 * radius * radius
    return area

#Task 4


while True:
    choice = input("What shape do you want to find the area for (square/circle)? ").lower()
    if choice != "square" and choice != "circle":
        print("Invalid input, please enter either square or circle to continue.")
    else:
        break

if choice == "square":
    perimeter = int(input("What is the perimeter of your square "))
    area = square_area(perimeter)
else:
    circumference = int(input("What is the circumference of your circle "))
    area = circle_area(circumference)

def output_message(shape, answer):
    return f"The area of the {shape} is {answer}"

shape = choice
answer = area

print(output_message(shape, area))