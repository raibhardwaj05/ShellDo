import calendar
import questionary
from prettytable import PrettyTable
from datetime import datetime
from helper_fun import month_year

filter_table = PrettyTable()
filter_table.field_names = ["Sr No.", "Date", "Expense Amt", "Category", "Payment Mode"]
filter_table.align = "c"

def filter_expense(data, category_list):
    expense_list = []
    count = 1

    filter_by = input("Filter By ('date' / 'category' / 'payment mode'): ").strip().lower()
    filter_by = filter_by.replace(" ", "")

    if filter_by not in {"date", "category", "payment mode"}:
        print("INVALID INPUT")
        return
    
    print()

    # filter by date
    if filter_by == 'date':
        print("--------------------ENTER STARTING DATE--------------------")

        day, month, year = month_year()

        start_date = str(day) + "-" + str(month) + "-" + str(year)

        # convert end_date into datetime for filtering
        start_datetime = datetime.strptime(start_date, "%d-%m-%Y")

        print()

        print("---------------------ENTER ENDING DATE----------------------")

        day1, month1, year1 = month_year()

        end_date = str(day1) + "-" + str(month1) + "-" + str(year1)

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

    if filter_by == 'paymentmode':
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