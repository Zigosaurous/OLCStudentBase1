def getgradepoint(mark):
    if mark >= 75:
        return "A1"
    elif mark < 75 and mark => 70:
        return "A2"
    elif mark < 70 and mark => 65:
        return "B3"
    elif mark < 65 and mark => 60:
        return "B4"
    elif mark < 60 and mark => 55:
        return "C5"
    elif mark < 55 and mark => 50:
        return "C6"
    elif mark < 50 and mark => 45:
        return "D7"
    elif mark < 45 and mark => 40:
        return "E8"
    elif mark < 40:
        return "F9"