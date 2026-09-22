
def div_2(number):
      halved = int(number/2)
      return halved

def odd_or_even(number):
    check = number % 2
    if check == 0:
        return "Even"
    else:
        return "Odd"

# print(odd_or_even(3))


def prime(number):
    count = 0
    if number < 3 and number > 1 :
        return "Prime"
    elif number == 1:
        return "Not prime"
    
    elif odd_or_even(number) == "Even" :
        return "Not prime"

    else:
        for i in range(3, div_2(number) + 1):
            check = number % i
            if check == 0:
                count += 1
            if count == 0:
                return "Prime"
            else:
                return "Not prime"

# for i in range(1,100):
#     print(prime(f"{i} is {prime(i)}"))

print(prime(1))    

    