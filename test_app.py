import unittest
import os
from task_manager import TaskManager
from class_task import Task


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Create a temporary TaskManager instance with a test file.
        self.task_manager = TaskManager("test_tasks.json")

    def tearDown(self):
        """
        This function ensures the '.json' file is deleted once all the
        tests are completed, otherwise the tests are fully dependant on the
        file and when ran again/updated they won't work.
        """
        if os.path.exists("test_tasks.json"):
            os.remove("test_tasks.json")

    def test_task_creation(self):
        task = Task(1, "Test Task", "2024-05-19", "high")
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.description, "Test Task")
        self.assertEqual(task.due_date, "2024-05-19")
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.status, "Pending")

    def test_remove_task(self):
        self.task_manager.add_task("Test Task", "2024-05-19", "high")
        self.task_manager.remove_task(1)
        self.assertEqual(len(self.task_manager.tasks), 0)

    def test_update_task(self):
        self.task_manager.add_task("Test Task", "2024-05-19", "high")
        self.task_manager.update_task(1, "Updated Task", "2025-01-01",
                                      "medium")
        task = self.task_manager.tasks[0]
        self.assertEqual(task.description, "Updated Task")
        self.assertEqual(task.due_date, "2025-01-01")
        self.assertEqual(task.priority, "medium")

    def test_add_task(self):
        self.task_manager.add_task("Test Task", "2023-12-31", "high")
        self.assertEqual(len(self.task_manager.tasks), 1)
        task = self.task_manager.tasks[0]
        self.assertEqual(task.description, "Test Task")
        self.assertEqual(task.due_date, "2023-12-31")
        self.assertEqual(task.priority, "high")

    def test_mark_task_as_complete(self):
        self.task_manager.add_task("Test Task", "2024-05-19", "high")
        self.task_manager.mark_task_as_complete(1)
        task = self.task_manager.tasks[0]
        self.assertEqual(task.status, "Completed")


if __name__ == "__main__":
    unittest.main()
