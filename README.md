import tkinter as tk
from tkinter import messagebox
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task field cannot be empty!")
def remove_task():
    try:
        selected_task = task_list.get(tk.ACTIVE)
        task_list.delete(tk.ACTIVE)
    except:
        messagebox.showwarning("Warning", "Please select a task to remove!")
root = tk.Tk()
root.title("To-Do List")
task_list = tk.Listbox(root, height=10, width=50)
task_list.pack(pady=10)
task_entry = tk.Entry(root, width=40)
task_entry.pack()
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
add_button.pack(pady=5)
remove_button.pack()
root.mainloop()
