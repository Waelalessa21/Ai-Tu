def add_task(
    task_list, task_name, task_description, task_due_date, task_priority, task_status
):
    task_list.append(
        {
            "task_name": task_name,
            "task_description": task_description,
            "task_due_date": task_due_date,
            "task_priority": task_priority,
            "task_status": task_status,
        }
    )
