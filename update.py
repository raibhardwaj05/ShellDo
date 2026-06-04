from helper_functions import month_year, filter_fun
from datetime import datetime, date
import questionary
from load_data import load
import json


def update_task(todo, data, categories):

    current_date = date.today()

    filter_by = input("Filter task by 'date' / 'category' you want to update\n").strip().lower()

    print()

    if filter_by not in {'date', 'category'}:
        print("invalid input!")
        return todo, data 
    
    id_list = filter_fun(filter_by, current_date, data, categories)

    #  ---------------------------------------get the field to be updated----------------------------------------

    while True:
        to_update = input("What you want to update?\n('task' / 'category' / 'deadline' / 'priority' / 'exit' to abort updation)\n").strip().lower()
        print()

        if to_update not in {"task", "category", "deadline", "priority", "exit"}:
            print("invalid input!")
            continue
        else:
            break

    # ------------------------------------------new values-----------------------------------
    
    if to_update == "task":
        new_value = input("Enter the task replacement: ")

    elif to_update == "category":
        new_value = questionary.select(
            "Choose new Category Replacement: ",
            choices= categories
        ).ask()
    
    elif to_update == "deadline":
        print("Enter new deadline")
        new_deadline = month_year(current_date)

        new_value = datetime.strftime(new_deadline, "%Y-%m-%d")

    elif to_update == "priority":
        new_value = int(input("Enter the new priority: "))

    else:
        print("Updation Aborted!")
        return todo, data

#  ---------------------------------------update data permanently----------------------------------------

    for item in data["todo_tasks"]:
        for same_id in id_list:
            if item["task_id"] == same_id:
                item[to_update] = new_value
                break

    with open("data.json", "w") as file:
        json.dump(data, file, indent= 4)

#  ---------------------------------clear the variables and return the data----------------------------------------

    todo.clear_rows()

    todo, data = load(todo)

    return todo, data
