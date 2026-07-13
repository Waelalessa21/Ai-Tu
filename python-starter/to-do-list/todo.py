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
                task_name = input("Enter the task name:")
                task_description = input("Enter the task description:")
                task_due_date = input("Enter the task due date:")
                task_priority = input("Enter the task priority:")
                task_status = input("Enter the task status:")
                task_list.append(
                    {
                        "task_name": task_name,
                        "task_description": task_description,
                        "task_due_date": task_due_date,
                        "task_priority": task_priority,
                        "task_status": task_status,
                    }
                )

            case "2":
                print(task_list)
            case "3":
                task_name = input("Enter the task name to delete:")
                task_list.remove(task_name)
            case "4":
                break


print("Welcome to the To-Do List")
todolist()
