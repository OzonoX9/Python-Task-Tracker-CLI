# Task Tracker

This is a project from the [roadmap.sh](https://roadmap.sh/projects/task-tracker) page of Python.

## Description

The project is a Task-tracker made in Python. It allows users to manage tasks from the command line, including adding, updating, deleting, and listing tasks. Tasks can also be marked as in-progress or done.

## Instructions to run

1. Clone the repository:

    ```sh
    git clone https://github.com/OzonoX9/Python-Task-Tracker-CLI
    ```

2. Navigate to the project directory:

    ```sh
    cd Python-Task-Tracker-CLI
    ```

3. Create a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

5. Run the application with the following commands:

    - **Adding a new task**:

        ```sh
        python main.py add "Buy groceries"
        ```

        Output: `Task added successfully (ID: 1)`

    - **Updating a task**:

        ```sh
        python main.py update 1 "Buy groceries and cook dinner"
        ```

        Output: `Task updated successfully (ID: 1)`

    - **Deleting a task**:

        ```sh
        python main.py delete 1
        ```

        Output: `Task deleted successfully (ID: 1)`

    - **Marking a task as in progress**:

        ```sh
        python main.py mark-in-progress 1
        ```

        Output: `Task marked as in-progress (ID: 1)`

    - **Marking a task as done**:

        ```sh
        python main.py mark-done 1
        ```

        Output: `Task marked as done (ID: 1)`

    - **Listing all tasks**:

        ```sh
        python main.py list
        ```

    - **Listing tasks by status**:

        ```sh
        python main.py list done
        python main.py list todo
        python main.py list in-progress
        ```

## Project link

[https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)
