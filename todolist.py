import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    task_list.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and pack widgets
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
clear_button.pack()

task_list = tk.Listbox(root, width=100)
task_list.pack()

root.mainloop()