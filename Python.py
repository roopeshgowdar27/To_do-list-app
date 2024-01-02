import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        list_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        task_index = list_tasks.curselection()[0]
        list_tasks.delete(task_index)
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do List App")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

entry_task = tk.Entry(frame_input, width=35)
entry_task.grid(row=0, column=0)

button_add = tk.Button(frame_input, text="Add Task", width=10, command=add_task)
button_add.grid(row=0, column=1, padx=5)

button_delete = tk.Button(root, text="Delete Task", width=10, command=delete_task)
button_delete.pack(pady=10)

list_tasks = tk.Listbox(root, width=50)
list_tasks.pack()

root.mainloop()
