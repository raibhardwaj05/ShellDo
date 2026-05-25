import json
from helper_fun import total_budget

def store(count, expense_table, expense_amount, day, month, year, category_choice, payment_choice, balance, data):
    
    date_format = {
        "Day": day,
        "Month": month,
        "Year": year
    }

    date = day + "-" + month + "-" + year

    new_expense = {
        "date": date,
        "date_format": date_format,
        "amount": expense_amount,
        "category": category_choice,
        "payment": payment_choice
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

    return balance