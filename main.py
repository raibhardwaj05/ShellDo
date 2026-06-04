from prettytable import PrettyTable
import string
from delete import delete_task
from add import add_task
from update import update_task
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
    cmd = input("Enter:\n'add' to create new task\n'read' to read todo list\n'update' to update existing task\n'delete' task from the list\n'completed' to mark as completed\n'exit' to get out of this\n").lower().strip()
    print()

    if cmd not in {'add', 'read', 'update', 'delete', 'completed', 'exit'}:
        print("INVALID INPUT!")
        continue
    
    if cmd == 'add':
        add_task(todo, data, chars, categories)
        print()
        print("Task Added Successfully!!\n")

    elif cmd == 'read':
        print(todo)
        print()

    elif cmd == 'update':
        todo, data = update_task(todo, data, categories)
        print()
        print("Task Updated Successfully!!\n")

    elif cmd == 'delete':
        todo, data = delete_task(todo, data, categories)
        print()
        print("Task Deleted Successfully!!\n")

    elif cmd == 'completed':
        todo, data = delete_task(todo, data, categories)
        print()
        print("Whoa!! Congratulations\nYou Completed a Task!!\n")

    else:
        break