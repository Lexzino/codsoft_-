import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found. Add some tasks!")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks, new_task):
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{new_task}' added successfully!")

def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task index. Please enter a valid index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == '3':
            display_tasks(tasks)
            task_index = int(input("Enter the task index to remove: "))
            remove_task(tasks, task_index)
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()