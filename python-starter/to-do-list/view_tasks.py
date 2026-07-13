def view_tasks(task_list):
    for task in task_list:
        print(task_list.keys(), end=" ")
        print(task_list.values(), end=" ")
        print()
