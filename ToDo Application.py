import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []
        self.completed_tasks = []

        # Task input fields
        self.task_description_var = tk.StringVar()
        self.due_date_var = tk.StringVar()
        self.priority_var = tk.StringVar()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Task input labels and entry fields
        tk.Label(self.root, text="Task Description:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        tk.Entry(self.root, textvariable=self.task_description_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Due Date:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        tk.Entry(self.root, textvariable=self.due_date_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Priority:").grid(row=1, column=2, padx=10, pady=5, sticky=tk.E)
        tk.Entry(self.root, textvariable=self.priority_var).grid(row=1, column=3, padx=10, pady=5)

        # Buttons
        tk.Button(self.root, text="Add Task", command=self.add_task).grid(row=2, column=0, columnspan=4, pady=10)
        tk.Button(self.root, text="Display Tasks", command=self.display_tasks).grid(row=3, column=0, columnspan=4, pady=10)
        tk.Button(self.root, text="Mark as Completed", command=self.mark_as_completed).grid(row=4, column=0, columnspan=4, pady=10)
        tk.Button(self.root, text="Update Task", command=self.update_task).grid(row=5, column=0, columnspan=4, pady=10)
        tk.Button(self.root, text="Remove Task", command=self.remove_task).grid(row=6, column=0, columnspan=4, pady=10)

    def add_task(self):
        description = self.task_description_var.get()
        due_date = self.due_date_var.get()
        priority = self.priority_var.get()

        if description:
            task = {"description": description, "due_date": due_date, "priority": priority, "completed": False}
            self.tasks.append(task)
            messagebox.showinfo("Task Added", "Task added successfully!")
        else:
            messagebox.showwarning("Error", "Task description cannot be empty.")

    def display_tasks(self):
        task_list = ""
        for i, task in enumerate(self.tasks, 1):
            task_list += f"{i}. {task['description']} - Due Date: {task['due_date']} - Priority: {task['priority']} - Completed: {task['completed']}\n"

        messagebox.showinfo("To-Do List", task_list)

    def mark_as_completed(self):
        task_index = self.get_task_index("Mark as Completed")
        if task_index is not None:
            task = self.tasks.pop(task_index)
            task["completed"] = True
            self.completed_tasks.append(task)
            messagebox.showinfo("Task Completed", "Task marked as completed.")

    def update_task(self):
        task_index = self.get_task_index("Update Task")
        if task_index is not None:
            description = self.task_description_var.get()
            due_date = self.due_date_var.get()
            priority = self.priority_var.get()

            self.tasks[task_index]["description"] = description
            self.tasks[task_index]["due_date"] = due_date
            self.tasks[task_index]["priority"] = priority

            messagebox.showinfo("Task Updated", "Task updated successfully.")

    def remove_task(self):
        task_index = self.get_task_index("Remove Task")
        if task_index is not None:
            removed_task = self.tasks.pop(task_index)
            messagebox.showinfo("Task Removed", f"Task '{removed_task['description']}' removed.")

    def get_task_index(self, action):
        if not self.tasks:
            messagebox.showwarning("Error", "No tasks available.")
            return None

        task_index = simpledialog.askinteger("Task Selection", f"Enter the number of the task to {action}:", minvalue=1, maxvalue=len(self.tasks))
        if task_index is not None:
            return task_index - 1  # Adjust index to start from 0

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()



