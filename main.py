# Define the task list
tasks = []

# Function to add a task
def add_task(task):
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

# Function to mark a task as completed
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"Task ID {task_id} marked as completed!")
            return
    print("Task not found!")

# Function to display tasks
def show_tasks():
    print("\nTo-Do List:")
    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        print(f"{task['id']}: {task['task']} [{status}]")

# Function to save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['id']},{task['task']},{task['completed']}\n")
    print("Tasks saved to file!")

# Usage
add_task("Buy groceries")
add_task("Clean the house")
show_tasks()
complete_task(1)
show_tasks()
save_tasks()


help("modules")
