while True:
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")

    user_input = input("Enter Your Choice:")

    match user_input:
        case "1":
            print("You Have added a task")
        case "2":
            print("You Have viewed all tasks")
        case "3":
            print("You Have deleted a task")
        case "4":
            print("You Have exited the program")
        case _:
            print("nothing to do")
