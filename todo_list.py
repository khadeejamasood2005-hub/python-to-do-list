import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"
tasks = []

def load_tasks():
    global tasks
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                tasks = json.load(file)
        except:
            tasks = []
    else:
        tasks = []
    update_list()

def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def update_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        if task["completed"]:
            task_list.insert(tk.END, "✔ " + task["name"])
        else:
            task_list.insert(tk.END, task["name"])

def add_task():
    name = entry.get().strip()
    if name:
        tasks.append({"name": name, "completed": False})
        entry.delete(0, tk.END)
        save_tasks()
        update_list()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected = task_list.curselection()
    if selected:
        tasks.pop(selected[0])
        save_tasks()
        update_list()
    else:
        messagebox.showwarning("Warning", "Select a task to delete.")

def complete_task():
    selected = task_list.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = not tasks[index]["completed"]
        save_tasks()
        update_list()
    else:
        messagebox.showwarning("Warning", "Select a task to mark.")

def clear_all():
    if tasks:
        answer = messagebox.askyesno(
            "Confirm",
            "Are you sure you want to delete all tasks?"
        )
        if answer:
            tasks.clear()
            save_tasks()
            update_list()

root = tk.Tk()
root.title("To-Do List")
root.geometry("450x550")
root.resizable(False, False)
root.configure(bg="#eaf2f8")

title = tk.Label(
    root,
    text="MY TO-DO LIST",
    font=("Arial", 22, "bold"),
    bg="#eaf2f8",
    fg="#154360"
)
title.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14), width=28)
entry.pack(pady=10)

add_button = tk.Button(
    root,
    text="ADD TASK",
    command=add_task,
    font=("Arial", 11, "bold"),
    bg="#2874a6",
    fg="white",
    width=18
)
add_button.pack(pady=5)

task_list = tk.Listbox(
    root,
    font=("Arial", 13),
    width=35,
    height=12,
    selectmode=tk.SINGLE
)
task_list.pack(pady=15)

complete_button = tk.Button(
    root,
    text="MARK COMPLETED / UNDO",
    command=complete_task,
    font=("Arial", 10, "bold"),
    bg="#239b56",
    fg="white",
    width=25
)
complete_button.pack(pady=5)

delete_button = tk.Button(
    root,
    text="DELETE SELECTED",
    command=delete_task,
    font=("Arial", 10, "bold"),
    bg="#c0392b",
    fg="white",
    width=25
)
delete_button.pack(pady=5)

clear_button = tk.Button(
    root,
    text="CLEAR ALL TASKS",
    command=clear_all,
    font=("Arial", 10),
    bg="#d5d8dc",
    width=25
)
clear_button.pack(pady=5)

load_tasks()

root.mainloop()