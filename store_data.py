import json

def store_data(todo_table, data, task_id, task, category, deadline, priority):
    new_task = {
        "task_id": task_id,
        "task": task,
        "category": category,
        "deadline": deadline,
        "priority": priority
    }

    todo_table.add_row([new_task["task_id"], new_task["task"], new_task["category"], new_task["deadline"], new_task["priority"]])

    data["todo_tasks"].append(new_task)

    with open("data.json", "w") as file:
        json.dump(data, file, indent= 4)