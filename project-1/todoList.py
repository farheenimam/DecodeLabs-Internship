import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, title):
    title = title.strip()
    if not title:
        return None

    new_id = max((t["id"] for t in tasks), default=0) + 1  
    task = {"id": new_id, "task": title}
    tasks.append(task)  
    return task


def view_tasks(tasks):
    """Display step: the 'read operation' using enumerate()."""
    print("\n===== YOUR TO-DO LIST =====")
    if not tasks:
        print("No tasks yet. Add one to get started!")
    else:
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task['task']}")
    print("===========================\n")


def show_menu():
    print("--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Exit")


def main():
    my_tasks = load_tasks()  

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            title = input("Enter your task: ")
            if add_task(my_tasks, title):
                save_tasks(my_tasks)
                print("Task added!\n")
            else:
                print("Task cannot be empty.\n")

        elif choice == "2": 
            view_tasks(my_tasks)

        elif choice == "3":
            print("Goodbye! Your tasks have been saved.")
            break

        else:
            print("Invalid choice. Please enter 1, 2 or 3.\n")


if __name__ == "__main__":
    main()