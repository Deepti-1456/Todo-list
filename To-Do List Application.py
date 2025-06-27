# To-Do List Application in Python (Terminal-Based)
# This app uses a simple menu to add, remove, and view tasks

# Initialize an empty list to store the tasks
tasks = []

# Function to display the main menu
def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

# Function to add a new task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)  # Add task to the list
    print(f"Task '{task}' added successfully!")

# Function to remove a task
def remove_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)  # Remove task by index
                print(f"Task '{removed}' removed successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to remove.")

# Function to view all tasks
def view_tasks():
    print("\n=== CURRENT TASKS ===")
    if not tasks:
        print("No tasks added yet.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Main loop to run the application
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
