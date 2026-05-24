import calendar
import questionary
from prettytable import PrettyTable
from datetime import datetime

filter_table = PrettyTable()
filter_table.field_names = ["Sr No.", "Date", "Expense Amt", "Category", "Payment Mode"]
filter_table.align = "c"

def filter_expense(data, category_list):
    expense_list = []
    count = 1

    filter_by = input("Filter By ('date' / 'category' / 'payment mode'): ")

    if filter_by not in {"date", "category", "payment mode"}:
        print("INVALID INPUT")
        return
    
    print()

    # filter by date
    if filter_by == 'date':
        print("--------------------ENTER STARTING DATE--------------------")

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

        start_date = str(day) + "-" + str(month) + "-" + str(year)

        # convert end_date into datetime for filtering
        start_datetime = datetime.strptime(start_date, "%d-%m-%Y")

        print()

        print("---------------------ENTER ENDING DATE----------------------")

        # valid month
        while True: 
            try: 
                month1 = input("Enter month (MM): ")

                if not month1.isdigit():
                    print("INVALID MONTH")
                    continue

                month1 = int(month1)

                if month1 < 1 or month1 > 12:
                    print("INVALID MONTH")
                    continue

                break
            
            except ValueError:
                print("INVALID MONTH")

        # valid year
        while True: 
            try: 
                year1 = input("Enter year (YYYY): ")

                if not year1.isdigit() or len(year1) != 4:
                    print("INVALID YEAR")
                    continue

                year1 = int(year1)

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

        end_date = str(day) + "-" + str(month1) + "-" + str(year1)

        # convert end_date into datetime for filtering
        end_datetime = datetime.strptime(end_date, "%d-%m-%Y")

        print()

        for items in data["expenses"]:
            start_match = start_datetime <= datetime.strptime(items["date"], "%d-%m-%Y")
            end_match = end_datetime >= datetime.strptime(items["date"], "%d-%m-%Y")

            if start_match and end_match:
                expense_list.append(items)

        print(f"Expenses from {start_datetime} - {end_datetime}")

    # filter by category
    if filter_by == 'category':
        category_choice = questionary.select(
            "Choose Category: ",
            choices= category_list
        ).ask()

        print()

        for items in data["expenses"]:
            if category_choice == items["category"]:
                expense_list.append(items)

    if filter_by == 'payment mode':
        payment_choice = questionary.select(
            "Payment Mode: ",
            choices= ["UPI", "CARD", "NET BANKING", "CASH"]
        ).ask()

        print()

        for items in data["expenses"]:
            if payment_choice == items["payment"]:
                expense_list.append(items)


    # show table
    for item in expense_list:
        filter_table.add_row([str(count), item["date"], item["amount"], item["category"], item["payment"]])
        count = count + 1

    print(filter_table)

    # clear expense list
    expense_list.clear

    # clear pretty table
    filter_table.clear_rows()