import calendar
from prettytable import PrettyTable
from datetime import date, datetime
import questionary

monthly_calender = PrettyTable()
monthly_calender.field_names = ["Mon", "Tue", "Wed", "Thrus", "Fri", "Sat", "Sun"]
monthly_calender.align = "c"

list_task = PrettyTable()
list_task.field_names = ["TaskID", "Task", "Category", "Deadline", "Priority"]
list_task.align = "c"

def month_year(current_datetime):

#  ------------------------------------------input month----------------------------------------

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

    
    year = current_datetime.year

#  ------------------------------------------print calender----------------------------------------

    dates = calendar.monthcalendar(year, month)
    date_rows = len(dates)
    date_cols = len(dates[0])

    for i in range(date_rows):
        for j in range(date_cols):
            if dates[i][j] == 0:
                dates[i][j] = ""

    for i in range(date_rows):
        monthly_calender.add_row(dates[i])

    print(monthly_calender)
    print()

#  ---------------------------------------------input date----------------------------------------

    no_of_days = calendar.monthrange(year, month)[1]
    days = [day for day in range(1, no_of_days+1)]
    
    while True:
        try:
            day = int(input("Enter Date: "))

            if day not in days:
                print("Invalid Input!")
                continue
            
            check_date = date(year, month, day)
            print(check_date)

            break

        except ValueError:
            print("Invalid Input!")

#  ---------------------------------clear the variables and return the data----------------------------------------

    monthly_calender.clear_rows()

    return check_date

# -----------------------------------------filter function---------------------------------------------

def filter_fun(filter_by, current_date, data, categories):
    tasks = []
    id_list = []

    #  ---------------------------------------filter-by date----------------------------------------
    while True: 
        if filter_by == 'date':

            deadline_day = questionary.select(
                "Select the Deadline: ",
                choices= ["Today", "Some Other Day"]
            ).ask()

            if deadline_day != "Today": 
                task_on_date = month_year(current_date)

                task_on_date_format = datetime.strftime(task_on_date, "%Y-%m-%d")
            else:
                task_on_date_format = datetime.strftime(current_date, "%Y-%m-%d")

            for items in data["todo_tasks"]:
                if task_on_date_format == items["deadline"]:
                    tasks.append(items.values())

        #  ---------------------------------------filter-by category----------------------------------------

        if filter_by == 'category':
            category_choice = questionary.select(
                "Choose Category: ",
                choices= categories
            ).ask()
        
            for items in data["todo_tasks"]:
                if category_choice == items["category"]:
                    tasks.append(items.values())

        if not tasks:
            print("no task matched!")
            continue

        if tasks:
            list_task.add_rows(tasks)
            print(list_task)
            break

    #  ---------------------------------------get the id to be updated----------------------------------------

    while True:

        id_to_update = input("enter task_id of that task: ")

        if any(item.get("task_id") == id_to_update for item in data["todo_tasks"]):
            id_list.append(id_to_update)

            while True:
                more = input("Do you want to update same field for more task ids with same values?\n(Yes: 'y' / No: 'n'): ").strip().lower()

                if more not in {"y", "n"}:
                    print("invalid input!")
                    continue

                break

            if more == "y":
                continue

            break

        else:
            print("invalid input!")
            continue

    list_task.clear_rows()

    return id_list