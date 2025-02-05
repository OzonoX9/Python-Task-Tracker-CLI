import json
import os
import sys
from datetime import datetime

TASKS_FILE = 'tasks.json'

def initialize_tasks_file():
    # Check if the tasks file exists, if not, create it with an empty list
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as file:
            json.dump([], file)

def load_tasks():
    # Load tasks from the JSON file
    with open(TASKS_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    # Save tasks to the JSON file
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(task_description):
    # Add a new task with the given description
    tasks = load_tasks()
    task_id = len(tasks) + 1
    current_time = datetime.now().isoformat()
    task = {
        'id': task_id,
        'description': task_description,
        'status': 'todo',
        'createdAt': current_time,
        'updatedAt': current_time
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def update_task(task_id, new_description):
    # Update the description of an existing task
    tasks = load_tasks()
    task_found = False
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            task_found = True
            break
    if task_found:
        save_tasks(tasks)
        print(f"Task updated successfully (ID: {task_id})")
    else:
        print(f"Task not found (ID: {task_id})")

def delete_task(task_id):
    # Delete a task by its ID
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task deleted successfully (ID: {task_id})")

def mark_in_progress(task_id):
    # Mark a task as in-progress
    tasks = load_tasks()
    task_found = False
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'in-progress'
            task['updatedAt'] = datetime.now().isoformat()
            task_found = True
            break
    if task_found:
        save_tasks(tasks)
        print(f"Task marked as in-progress (ID: {task_id})")
    else:
        print(f"Task not found (ID: {task_id})")

def mark_done(task_id):
    # Mark a task as done
    tasks = load_tasks()
    task_found = False
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'done'
            task['updatedAt'] = datetime.now().isoformat()
            task_found = True
            break
    if task_found:
        save_tasks(tasks)
        print(f"Task marked as done (ID: {task_id})")
    else:
        print(f"Task not found (ID: {task_id})")

def list_tasks(status=None):
    # List tasks, optionally filtered by status
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")

if __name__ == "__main__":
    # Initialize the tasks file and handle command line arguments
    initialize_tasks_file()
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'add' and len(sys.argv) > 2:
            task_description = sys.argv[2]
            add_task(task_description)
        elif command == 'update' and len(sys.argv) > 3:
            task_id = int(sys.argv[2])
            new_description = sys.argv[3]
            update_task(task_id, new_description)
        elif command == 'delete' and len(sys.argv) > 2:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        elif command == 'mark-in-progress' and len(sys.argv) > 2:
            task_id = int(sys.argv[2])
            mark_in_progress(task_id)
        elif command == 'mark-done' and len(sys.argv) > 2:
            task_id = int(sys.argv[2])
            mark_done(task_id)
        elif command == 'list':
            if len(sys.argv) > 2:
                status = sys.argv[2]
                list_tasks(status)
            else:
                list_tasks()
        else:
            print("Invalid command or missing arguments")
    else:
        print("No command provided")