while True:
    date = input("Enter the date (DD-MM-YYYY): ") #1 indentation 
    test = date
    if len(test) == 10 and test[2]== "-" and test[5]== "-": #2 change = to ==
        day = int(test[0:2])
        month = int(test[3:5]) #6 changed [3:] to [3:5]
        year = int(test[6:])
        check_year = year>1900 and year<=2026 #11 change the year
        check_month = month>=1 and month<=12 #12 change or to and 
        check_day_31 = day<=31 and (month in [1,3,5,7,8,10,12])
        check_day_30 = day<=30 and (month in [4,6,9,11]) #9 change 31 to 30
        check_day_Feb = month == 2 and ((day<=29 and year%4==0) or day<=28) #10 change 0 to 2
        if check_year: #3 added a _
            if check_month:
                if check_day_31 or check_day_30 or check_day_Feb: #4 added a :
                    break
                else:
                    print("Error in day")
            else:
                print("Error in month") #7 change year to month
        else:
            print("Error in year") #8 change month to year
    else:
        print("Error in format") #5 added a "
print("Date accepted")
