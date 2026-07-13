from add_task import add_task
from view_tasks import view_tasks
from delete_task import delete_task


def todolist():
    task_list = []
    while True:
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Delete a task")
        print("4. Exit")
        print("")
        user_input = input("Select an option:")

        match user_input:
            case "1":
                add_task(task_list)
            case "2":
                view_tasks(task_list)
            case "3":
                delete_task(task_name, task_list)
            case "4":
                break


print("Welcome to the To-Do List")
todolist()
