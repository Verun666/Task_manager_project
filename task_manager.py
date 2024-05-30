import json
from class_task import Task

"""
I decided to use '.json' files to support the application.
The readability of the tasks is better than regular '.txt' file,
as .json stores data in a dictionary format.
"""


class TaskManager:
    def __init__(self, filename="tasks.json"):
        """
        Initialize a new TaskManager object.

        Parameters:
        filename (str): The name of the file to save/load tasks.
        """
        self.tasks = []  # List to store tasks.
        self.next_id = 1  # To keep track of the next task ID to assign.
        self.filename = filename  # File to save/load tasks.
        self.load_tasks()  # Load tasks from file if it exists.

    def save_tasks(self):
        """
        Save all tasks to a file.
        """
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def load_tasks(self):
        """
        Load tasks from a file.
        """
        try:
            with open(self.filename, "r") as file:
                tasks = json.load(file)
                self.tasks = [Task.from_dict(task) for task in tasks]
                if self.tasks:
                    self.next_id = max(task.task_id for task in self.tasks) + 1
        except FileNotFoundError:
            # If the file is not found, initialize an empty list.
            self.tasks = []

    def add_task(self, description, due_date, priority):
        """
        Add a new task to the task manager.

        Parameters:
        description (str): The description of the task.
        due_date (str): The due date of the task.
        priority (str): The priority of the task.
        """
        task = Task(self.next_id, description, due_date, priority)
        self.tasks.append(task)
        self.next_id += 1  # Increment the ID for the next task.
        self.save_tasks()  # Save tasks to file.

    def remove_task(self, task_id):
        """
        Remove a task from the task manager.

        Parameters:
        task_id (int): The unique identifier of the task to remove.
        """
        self.tasks = [task for task in self.tasks if
                      task.task_id != int(task_id)]
        self.save_tasks()  # Save tasks to file.

    def update_task(self, task_id, new_description, new_due_date,
                    new_priority):
        """
        Update an existing task in the task manager.

        Parameters:
        task_id (int): The unique identifier of the task to update.
        new_description (str): The new description of the task.
        new_due_date (str): The new due date of the task.
        new_priority (str): The new priority of the task.
        """
        for task in self.tasks:
            if task.task_id == int(task_id):
                task.description = new_description
                task.due_date = new_due_date
                task.priority = new_priority
                break
        self.save_tasks()  # Save tasks to file.

    def mark_task_as_complete(self, task_id):
        """
        Mark a task as complete.

        Parameters:
        task_id (int): The unique identifier of the task to mark as complete.
        """
        for task in self.tasks:
            if task.task_id == int(task_id):
                task.status = "Completed"
                break
        self.save_tasks()  # Save tasks to file.

    def list_tasks(self):
        """
        List all tasks in the task manager.
        """
        for task in self.tasks:
            print(
                f"ID: {task.task_id}, Description: {task.description}, "
                f"Due Date: {task.due_date}, Priority: {task.priority}, "
                f"Status: {task.status}"
            )
