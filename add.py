import questionary
from helper_functions import month_year
from datetime import datetime, date
import secrets # better than random for unique ids
from store_data import store_data
from prettytable import PrettyTable

todo_same_day = PrettyTable()
todo_same_day.field_names = ["TaskID", "Task", "Category", "Deadline", "Priority"]
todo_same_day.align = "c"


def add_task(todo_table, data, chars, categories):
    priority = 1
    same_day = []

    # generates 5 random chars one by one and then .join joins them
    task_id = "".join(secrets.choice(chars) for _ in range(5)) # '_' ==> doesn't care about the variable

    while True:
        task = input("Enter the task to do: ").lower().strip()

        if len(task) <= 3:
            print("add task with names greater than 3 characters!")
            continue

        break

    category_choice = questionary.select(
        "Choose Category: ",
        choices= categories
    ).ask()

    print("---------------------------------Enter Deadline---------------------------------")

    deadline_day = questionary.select(
        "Select the Deadline: ",
        choices= ["Today", "Some Other Day"]
    ).ask()

    current_datetime = date.today()
    print(current_datetime)

    if deadline_day != "Today":
        last_date = month_year(current_datetime)

        deadline = datetime.strftime(last_date, "%Y-%m-%d")

        for items in data["todo_tasks"]:
            if items["deadline"] == deadline:
                same_day.append(items.values())

        if same_day:
            todo_same_day.add_rows(same_day)
            print(todo_same_day)
  
    else:
        deadline = datetime.strftime(current_datetime, "%Y-%m-%d")
    
    print()
    while True:
        try:
            priority = int(input("Priority of this task (1 = highest, 10 = lowest): "))
            print()
            break
        except ValueError:
            print("INVALID INPUT!")

    todo_same_day.clear()

    store_data(todo_table, data, task_id, task, category_choice, str(deadline), priority)