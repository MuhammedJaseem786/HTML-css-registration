year = int(input("Enter the year : "))
if year % 100 == 0:
    if year % 400 == 0:
        print("The given year is leap year")
    else:
        print("The given year is not leap year")
else:
    if year % 4 == 0:
        print("The given year is leap year")
    else:
        print("The given year is not leap year")
