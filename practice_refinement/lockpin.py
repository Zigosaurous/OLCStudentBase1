arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]

while True:
    locker = int(input("Please enter the locker you would like to open: "))

    if locker >= 1 and locker <= 10:
        print("Valid locker")
        break
    else:
        print("locker number not in the range")

while True:
    pin = int(input("Please enter the PIN for the locker: "))
    if len(str(pin)) != 4:
        print("Invalid length, Please enter a 4 characters for your pin")

    elif pin == arraypins[locker-1]:
        print("The locker is open.")
        break

    else:
        print("Incorrect PIN for that locker")


