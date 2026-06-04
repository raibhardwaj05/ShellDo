from helper_functions import month_year
from datetime import datetime, date
from prettytable import PrettyTable
import questionary
from load_data import load
import json

list_task = PrettyTable()
list_task.field_names = ["TaskID", "Task", "Category", "Deadline", "Priority"]
list_task.align = "c"

def update_task(todo, data, categories):
    tasks = []
    current_date = date.today()

    filter_by = input("Filter task by 'date' / 'category' you want to update\n").strip().lower()

    print()

    if filter_by not in {'date', 'category'}:
        print("invalid input!")
        return
    
    if filter_by == 'date':
        task_on_date = month_year(current_date)

        task_on_date_format = datetime.strftime(task_on_date, "%Y-%m-%d")

        for items in data["todo_tasks"]:
            if task_on_date_format == items["deadline"]:
                tasks.append(items.values())

    if filter_by == 'category':
        category_choice = questionary.select(
            "Choose Category: ",
            choices= categories
        ).ask()
    
        for items in data["todo_tasks"]:
            if category_choice == items["category"]:
                tasks.append(items.values())

    if tasks:
        list_task.add_rows(tasks)
        print(list_task)

    while True:
        id_to_update = input("enter task_id to update that task: ")

        if any(item.get("task_id") == id_to_update for item in data["todo_tasks"]):
            break
        else:
            print("invalid input!")
            continue
    
    while True:
        to_update = input("What you want to update?\n('task' / 'category' / 'deadline' / 'priority' / 'exit' to abort updation)\n").strip().lower()
        print()

        if to_update not in {"task", "category", "deadline", "priority", "exit"}:
            print("invalid input!")
            continue
        else:
            break
    
    if to_update == "task":
        new_value = input("Enter the task replacement: ")

    elif to_update == "category":
        new_value = questionary.select(
            "Choose new Category Replacement: ",
            choices= categories
        ).ask()
    
    elif to_update == "deadline":
        new_deadline = month_year(current_date)

        new_value = datetime.strftime(new_deadline, "%Y-%m-%d")

    elif to_update == "priority":
        new_value = int(input("Enter the new priority: "))

    else:
        print("Updation Aborted!")
        return
    

    for item in data["todo_tasks"]:
        if item["task_id"] == id_to_update:
            item[to_update] = new_value
            break

    with open("data.json", "w") as file:
        json.dump(data, file, indent= 4)

    todo.clear_rows()
    tasks.clear()
    list_task.clear_rows()

    todo, data = load(todo)

    return todo, data
