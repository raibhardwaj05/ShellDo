import calendar
import questionary

def total_budget(balance, expense):
    return (balance - expense)

def month_year():
    # valid month
    while True: 
        try: 
            month = input("Enter month (MM): ")

            if not month.isdigit():
                print("INVALID MONTH")
                continue

            month = int(month)

            if month < 1 or month > 12:
                print("INVALID MONTH")
                continue

            break
            
        except ValueError:
            print("INVALID MONTH")

        # valid year
    while True: 
        try: 
            year = input("Enter year (YYYY): ")

            if not year.isdigit() or len(year) != 4:
                print("INVALID YEAR")
                continue

            year = int(year)

            break
            
        except ValueError:
            print("INVALID YEAR")

    
            # valid days in the month => (first day of the month, total days)(0 to 6 =>> monday to sunday)
    no_of_days = calendar.monthrange(year, month)[1]

    days = [str(day) for day in range(1, no_of_days + 1)]

    day = questionary.select(
        "DATE: ",
        choices= days
    ).ask()


    return (day, month, year)

