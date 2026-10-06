def getgradepoint(mark):
    if mark >= 75:
        return "1"
    elif mark >= 70 and mark < 75:
        return "2"
    elif mark >= 65 and mark < 70:
            return "3"
    elif mark >= 60 and mark < 65:
            return "4"
    elif mark >= 55 and mark < 60:
            return "5"
    elif mark >= 50 and mark < 55:
            return "6"
    elif mark >= 45 and mark < 50:
            return "7"
    elif mark >= 40 and mark < 45:
            return "8"
    else:
        return "9"

# print(getgradepoint(60))
def calL1R5(result):
    if "English" in result:
        eng_score = result["English"]
    if "Higher Chinese" in results:
        hcl_score = result["Higher Chinese"]
    if eng_score > hcl_score:
        L = getgradepoint(eng_score)
    else:
        L = getgradepoint(hcl_score)

    for i in result:
        if i != "English" and i != "Higher "


      

