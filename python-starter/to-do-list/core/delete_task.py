def delete_task(task_name, task_list):
    for task in task_list:
        if task["task_name"] == task_name:
            task_list.remove(task)
            return True
    return False
