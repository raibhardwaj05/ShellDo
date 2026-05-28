import calendar
from prettytable import PrettyTable

monthly_calender = PrettyTable()
monthly_calender.field_names = ["Mon", "Tue", "Wed", "Thrus", "Fri", "Sat", "Sun"]
monthly_calender.align = "c"

def month_year():
    while True:
        month = input("Month (MM): ")

        try:
            month = int(month)

            if month < 1 or month > 12:
                print("Invalid Input!")
                continue

            break

        except ValueError:
            print("Invalid Input!")

    
    while True:
        year = input("Year (YYYY): ")

        try:
            if len(year) != 4:
                print("Invalid Input!")
                continue

            year = int(year)

            break

        except ValueError:
            print("Invalid Input!")


    dates = calendar.monthcalendar(year, month)
    date_rows = len(dates)
    date_cols = len(dates[0])

    for j in range(date_cols):
        if dates[0][j] == 0:
            dates[0][j] = ""

    for i in range(date_rows):
        monthly_calender.add_row(dates[i])

    print(monthly_calender)
    print()

    no_of_days = calendar.monthrange(year, month)[1]
    days = [day for day in range(1, no_of_days+1)]
    
    while True:
        try:
            date = int(input("Enter Date: "))

            if date not in days:
                print("Invalid Input!")
                continue

            break

        except ValueError:
            print("Invalid Input!")

    return date, month, year