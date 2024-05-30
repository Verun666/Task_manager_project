
from task_manager import TaskManager


def main():
    """
    Main function to run the task manager application.
    """
    task_manager = TaskManager()

    while True:
        # Display menu options.
        print("\nTask Manager Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. List Tasks")
        print("4. Remove Task")
        print("5. Mark task as complete")
        print("6. Quit application")

        # Get user's choice.
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new task.
            task_description = input("Enter task description: ")
            task_due_date = input("Enter due date (YYYY-MM-DD): ")
            task_priority = input("Enter task priority (low, medium, high): ")
            task_manager.add_task(task_description, task_due_date,
                                  task_priority)
            print("Task saved succesfully!")
        elif choice == "2":
            # Update an existing task.
            task_id = input("Enter task ID: ")
            task_description = input("Enter new description of the task: ")
            task_due_date = input("Enter new due date (YYYY-MM-DD): ")
            task_priority = input("Enter new task priority\
                                   (low, medium, high): ")
            task_manager.update_task(task_id, task_description, task_due_date,
                                     task_priority)
            print("Task updated succesfully!")
        elif choice == "3":
            print("\nYour current tasks: ")
            # List all tasks.
            task_manager.list_tasks()
        elif choice == "4":
            # Remove a task.
            task_to_remove = input("Enter ID of the task you wish to remove: ")
            task_manager.remove_task(task_to_remove)
            print("Task removed succesfully!")
        elif choice == "5":
            # Mark task as complete.
            task_id = input("Enter task ID to mark as complete: ")
            task_manager.mark_task_as_complete(task_id)
            print(f"Task {task_id} succesfully marked as complete!")
        elif choice == "6":
            # Quit the application.
            print("Application closed. See you again soon!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
