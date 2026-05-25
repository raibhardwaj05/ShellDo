from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from helper_fun import month_year



def analyse_expense(data):
    totals = {}
    cmd = input("Do you want to analyse based on 'category' or 'payment mode'?\n").strip().lower()
    cmd = cmd.replace(" ", "")
    print(repr(cmd))

    if cmd not in {"category", "paymentmode"}:
        print("INVALID INPUT")
        return
    
    print("--------------------ENTER STARTING DATE--------------------")
    day, month, year = month_year()

    start_date = str(day) + "-" + str(month) + "-" + str(year)
    start_datetime = datetime.strptime(start_date, "%d-%m-%Y")

    print("---------------------ENTER ENDING DATE----------------------")
    day1, month1, year1 = month_year()

    end_date = str(day1) + "-" + str(month1) + "-" + str(year1)
    end_datetime = datetime.strptime(end_date, "%d-%m-%Y")

    if cmd == 'category':
        for items in data["expenses"]:
            # conditions to search for
            start_match = start_datetime <= datetime.strptime(items["date"], "%d-%m-%Y")
            end_match = end_datetime >= datetime.strptime(items["date"], "%d-%m-%Y")

            if start_match and end_match:
                if items["category"] in totals:
                    totals[items["category"]] += int(items["amount"])
                else:
                    totals[items["category"]] = int(items["amount"])


    if cmd == "paymentmode":

        for items in data["expenses"]:
            # conditions to search for
            start_match = start_datetime <= datetime.strptime(items["date"], "%d-%m-%Y")
            end_match = end_datetime >= datetime.strptime(items["date"], "%d-%m-%Y")

            if start_match and end_match:
                if items["payment"] in totals:
                    totals[items["payment"]] += int(items["amount"])
                else:
                    totals[items["payment"]] = int(items["amount"])


    sns.barplot(x= list(totals.keys()), y = list(totals.values()), palette="rainbow", hue= list(totals.keys()), legend= False)

    if cmd == "paymentmode":
        plt.xlabel('Payment Mode')
    else:
        plt.xlabel("Category")

    plt.ylabel("Expense")
    plt.title("Expense Analysis")
    plt.show()

    totals.clear()