class Task:
    def __init__(self, task_id, description, due_date, priority,
                 status="Pending"):
        """
        Initialize a new Task object.

        Parameters:
        task_id (int): The unique identifier for the task.
        description (str): The description of the task.
        due_date (str): The due date of the task.
        priority (str): The priority of the task.
        status (str): The status of the task (default is "Pending").
        """
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def to_dict(self):
        """
        Convert the Task object to a dictionary.
        """
        return {
            "task_id": self.task_id,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, task_dict):
        """
        Create a Task object from a dictionary.

        Parameters:
        task_dict (dict): A dictionary containing task data.
        """
        return cls(
            task_id=task_dict["task_id"],
            description=task_dict["description"],
            due_date=task_dict["due_date"],
            priority=task_dict["priority"],
            status=task_dict["status"]
        )
