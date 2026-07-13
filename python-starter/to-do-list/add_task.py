def add_task(task_list):
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
