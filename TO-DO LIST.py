todo_list = []

def show_menu():
    print("\n----- TO-DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")       

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added.")

def view_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def update_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to update: ")) - 1
        new_task = input("Enter the updated task: ")
        todo_list[task_no] = new_task
        print("Task updated.")
    except:
        print("Invalid input.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: ")) - 1
        todo_list.pop(task_no)
        print("Task deleted.")
    except:
        print("Invalid input.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == '1':
         add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting... Bye!")
        break
    else:
        print("Invalid choice.")

