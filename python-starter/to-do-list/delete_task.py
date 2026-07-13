def delete_task(task_name, task_list):
    for task in task_list:
        if task["task_name"] == task_name:
            task_list.remove(task)
            print(f"Task {task_name} has been deleted")
            break
        else:
            print(f"Task {task_name} not found")
