import json

def load(todo):

    with open("data.json", 'r') as file:
        data = json.load(file)

    for items in data["todo_tasks"]:
        task_id = items['task_id']
        task = items["task"]
        category_choice = items["category"]
        deadline = items["deadline"]
        priority = items["priority"]

        todo.add_row([task_id, task, category_choice, deadline, priority])
    

    return todo, data