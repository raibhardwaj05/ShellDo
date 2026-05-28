from prettytable import PrettyTable
import string
from helper_functions import month_year
from add import add_task
from load_data import load

todo = PrettyTable()
todo.field_names = ["TaskID", "Task", "Category", "Deadline", "Priority"]
todo.align = "c"

chars = string.ascii_lowercase + string.digits

categories = [
    "Planning",
    "Work",
    "Personal",
    "Health",
    "Others"
]

todo, data = load(todo)

print(todo)

while True:
    print()
    cmd = input("Enter:\n'add' to create new task\n'read' to read todo list\n'update' to update existing task\n'completed' to mark as completed\n").lower().strip()
    print()

    if cmd not in {'add', 'read', 'update', 'completed', 'exit'}:
        print("INVALID INPUT!")
        continue
    
    if cmd == 'add':
        add_task(todo, data, chars, categories)

    elif cmd == 'read':
        print(todo)

    elif cmd == 'update':
        pass

    elif cmd == 'completed':
        pass

    else:
        break