class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print(f"{task} not found in ToDo list!")

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks in ToDo list.")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
