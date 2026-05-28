from prettytable import PrettyTable
import secrets # better than random for unique ids
import string
import questionary
from helper_functions import month_year

todo = PrettyTable()
todo.field_names = ["TaskID", "Task", "Category", "Deadline", "Completed?"]
todo.align = "c"

chars = string.ascii_lowercase + string.digits

categories = [
    "Planning",
    "Work",
    "Personal",
    "Health",
    "Others"
]

while True:

    # generates 5 random chars one by one and then .join joins them
    task_id = "".join(secrets.choice(chars) for _ in range(5)) # '_' ==> doesn't care about the variable

    task = input("Enter the Task you want to add or 'exit' to get out of this\n").lower()

    if task.strip() == 'exit':
        print(todo)
        break
    
    if len(task.strip()) <= 2:
        print("add task with names greater than 2 characters!")
        continue

    category_choice = questionary.select(
        "Choose Category: ",
        choices= categories
    ).ask()

    print("---------------------------------Enter Deadline---------------------------------")

    date, month, year = month_year()

    print(str(date)+ "-" +str(month) + "-" + str(year))
