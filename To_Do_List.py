import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
    except IndexError:
        pass

def update_task():
    try:
        selected_index = listbox.curselection()[0]
        updated_task = entry.get()
        if updated_task:
            listbox.delete(selected_index)
            listbox.insert(selected_index, updated_task)
            entry.delete(0, tk.END)
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

listbox = tk.Listbox(frame, width=40)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

entry = tk.Entry(root, width=30)
entry.pack(padx=10, pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(padx=10, pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(padx=10, pady=5)

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(padx=10, pady=5)

root.mainloop()
