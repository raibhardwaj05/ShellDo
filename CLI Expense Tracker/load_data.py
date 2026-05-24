import json

def load(expense_table, count):
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

    return expense_table, data, balance, count