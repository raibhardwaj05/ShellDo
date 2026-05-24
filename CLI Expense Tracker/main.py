from prettytable import PrettyTable
from load_data import load
from store_data import store
from filter import filter_expense
import questionary
import calendar

# create table
expense_table = PrettyTable()
expense_table.field_names = ["Sr No.", "Date", "Expense Amt", "Category", "Payment Mode"]
expense_table.align = "c" # everything in table should be in center

# create id
count = 1

# temporary storage list
expense_records = []

# category choices
category_list = ["Groceries", "Medical", "Personal", "Transport", "Food", "Bills", "Shopping", "Entertainment", "Other"]

expense_table, data, balance, count = load(expense_table, count)

print("Balance: ", balance)
print(expense_table)

while(1):
    if balance < 0:
        print("Your Expenses are already Over Budget\n(Do you want to still make more expenses?)\nIF NO TYPE 'EXIT'")

    print()

    expense_OR_exit_OR_filter = input("enter : expense amount or 'filter' dates or 'analyse' expense or 'exit' to get out of this!\n").lower().strip()

    print()

    if expense_OR_exit_OR_filter not in {"analyse", "filter", "exit"}:
        try:
            amt = int(expense_OR_exit_OR_filter)
            if amt <= 0: 
                print("INVALD INPUT")
                print()
                continue
            
        except ValueError:
            print("INVALID INPUT")
            continue

    if expense_OR_exit_OR_filter == "exit":
        print("Balance: ", balance)
        print(expense_table)
        break

    elif expense_OR_exit_OR_filter == "filter": 
        filter_expense(data, category_list)

    elif expense_OR_exit_OR_filter == "analyse":
        pass
    
    else:

        # category of expense
        category_choice = questionary.select(
            "Choose Category: ",
            choices= category_list
        ).ask()

        print()

        # payment mode
        payment_choice = questionary.select(
            "Payment Mode: ",
            choices= ["UPI", "CARD", "NET BANKING", "CASH"]
        ).ask()

        print()
        
        # expense date

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

        print()

        balance = store(count, expense_table, expense_OR_exit_OR_filter, str(day), str(month), str(year), category_choice, payment_choice, balance, data)
        