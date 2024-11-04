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

def show_tasks(tasks):
    if not tasks:
        print("No tasks available 🤷")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            status = "Completed 😉" if task['done'] else "Pending 😑"
            print(f"{idx}. {task['title']} - {status}")
    print()

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Task '{title}' added.\n")

def update_task(tasks):
    show_tasks(tasks)
    task_num = int(input("Enter the task number to update: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]['title'] = input("Enter new title: ")
        save_tasks(tasks)
        print("Task updated.\n")
    else:
        print("Invalid task number.\n")

def mark_task_done(tasks):
    show_tasks(tasks)
    task_num = int(input("Enter the task number to mark as done: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]['done'] = True
        save_tasks(tasks)
        print("Task marked as done.\n")
    else:
        print("Invalid task number.\n")

def delete_task(tasks):
    show_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' deleted.\n")
    else:
        print("Invalid task number.\n")

def main():
    tasks = load_tasks()
    
    while True:
        print("To-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task Name")
        print("4. Mark task as done")
        print("5. Delete task")go
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_task_done(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Omkay Byeeee 🏃🏃🏃")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
