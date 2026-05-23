from prettytable import PrettyTable
from budget import total_budget
import json

# date = "", amount = 0, catego = "", payment

# create table
expense_table = PrettyTable()
expense_table.field_names = ["Sr No.", "Date", "Expense Amt", "Category", "Payment Mode"]
expense_table.align = "c" # everything in table should be in center

# create id
count = 1

# temporary storage list
expense_records = []

# load data
with open("data.json", "r") as records:
    data = json.load(records)


# if no data is there in the PrettyTable or storage get the budget input as it is set once
if not data["expenses"] and data["Balance_Budget"] == 0:
    balance = int(input("Your monthy Budget: $"))
    data["Balance_Budget"] = balance
else:
    # reflect data into table
    balance = data["Balance_Budget"]

    for items in data["expenses"]:
        date = items["date"]
        amount = items["amount"]
        category = items["category"]
        payment = items["payment"]

        expense_table.add_row([count, date, amount, category, payment])
        count = count + 1

print("Balance: ", balance)
print(expense_table)

while(1):
    cmd = input("enter command: (date (DD/MM/YYYY), expense, category, payment mode) or 'exit' to get out of this!\n").lower().strip()

    if cmd == "exit":
        print("Balance: ", balance)
        print(expense_table)
        break

    try:
        expense_records = cmd.split(",")
        date = expense_records[0]

        date_split = expense_records[0].split("/")
        date_format = {
            "Day": date_split[0],
            "Month": date_split[1],
            "Year": date_split[2]
        }
        amount = expense_records[1]
        category = expense_records[2]
        payment = expense_records[3]

        new_expense = {
            "date": date,
            "date_format": date_format,
            "amount": amount,
            "category": category,
            "payment": payment
        }
        
        # fill table row with new data
        expense_table.add_row([str(count), new_expense["date"], new_expense["amount"], new_expense["category"], new_expense["payment"]])
        count = count + 1

        # update with new records
        balance = total_budget(balance, int(new_expense["amount"]))
        data["Balance_Budget"] = balance
        data["expenses"].append(new_expense)

        # store data in json
        with open("data.json", "w") as records:
            json.dump(data, records, indent= 4) # indent is spacing for readability
    
    except IndexError:
        print("Please enter data in valid format")




