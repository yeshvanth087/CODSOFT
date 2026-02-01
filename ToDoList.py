import json
import os

FILE_NAME = "tasks.json"
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "status": "Pending"})
    save_tasks(tasks)
    print("Task added successfully!\n")
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
        return

    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['task']} - {task['status']}")
    print()
def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        tasks[task_num - 1]["status"] = "Completed"
        save_tasks(tasks)
        print("Task marked as completed!\n")
    except:
        print("Invalid task number!\n")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        tasks.pop(task_num - 1)
        save_tasks(tasks)
        print("Task deleted successfully!\n")
    except:
        print("Invalid task number!\n")
def main():
    tasks = load_tasks()

    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
