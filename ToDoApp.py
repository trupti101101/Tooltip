class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            old_task = self.tasks[task_number - 1]
            self.tasks[task_number - 1] = new_task
            print(f"Task '{old_task}' updated to '{new_task}'.")
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            print("\n==| Welcome To 'TO DO App' |==")
            print("Options:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task") 
            print("4. Update Task")
            print("5. Exit")
            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == '1':
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                try:
                    task_number = int(input("Enter the task number to delete: "))
                    self.delete_task(task_number)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '4':
                try:
                    task_number = int(input("Enter the task number to update: "))
                    new_task = input("Enter the new task: ")
                    self.update_task(task_number, new_task)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '5':
                print("Exiting the To-Do app!")
                break
            else:
                print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    todo_app = ToDoApp()
    todo_app.run()
