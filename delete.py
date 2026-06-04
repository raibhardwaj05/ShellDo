from helper_functions import filter_fun
from datetime import date
from load_data import load
import json

def delete_task(todo, data, categories):
    
    current_date = date.today()

    filter_by = input("Filter task by 'date' / 'category' you want to update\n").strip().lower()

    print()

    if filter_by not in {'date', 'category'}:
        print("invalid input!")
        return todo, data 
    
    id_list = filter_fun(filter_by, current_date, data, categories)

    for ids in id_list:
        for index, items in enumerate(data["todo_tasks"]):
            if items["task_id"] == ids:
                del data["todo_tasks"][index]

    with open("data.json", "w") as file:
        json.dump(data, file, indent= 4)

    todo.clear_rows()

    todo, data = load(todo)

    return todo, data