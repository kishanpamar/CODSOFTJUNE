# Task 1 - To-Do List with Completed Task Feature

pending_tasks = []
completed_tasks = []

def add_task():
    task = input("Enter task to add: ")
    pending_tasks.append(task)
    print("Task added successfully.")

def view_tasks():
    if not pending_tasks and not completed_tasks:
        print("No tasks added yet.")
    else:
        print("\n--- Pending Tasks ---")
        for i, task in enumerate(pending_tasks, 1):
            print(f"{i}. {task}")
        print("\n--- Completed Tasks ---")
        for i, task in enumerate(completed_tasks, 1):
            print(f"{i}. {task} ✅")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter task number to remove (from pending only): "))
        if 1 <= index <= len(pending_tasks):
            removed = pending_tasks.pop(index - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def mark_completed():
    if not pending_tasks:
        print("No pending tasks to mark as completed.")
        return
    view_tasks()
    try:
        index = int(input("Enter task number to mark as completed (from pending): "))
        if 1 <= index <= len(pending_tasks):
            completed_task = pending_tasks.pop(index - 1)
            completed_tasks.append(completed_task)
            print(f"✅ Marked as completed: {completed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Mark Task as Completed\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_completed()
    elif choice == "5":
        print("Exiting... Stay productive!")
        break
    else:
        print("Invalid choice.")
