from tkinter import *  #2
import random

root = Tk()
root.title('Add / Remove Tasks')
root.geometry("500x600")
root.config(bg='teal')

def random_color():
    r = random.randint(0, 100)
    g = random.randint(0, 100)
    b = random.randint(0, 100)
    return f'#{r:02x}{g:02x}{b:02x}'

def bg_color():
    root.config(bg=random_color())

Button(root, text='Change Background Color', command=bg_color, bg='purple', fg='black' ).pack()

#----Task----Add/Remove--
task_nr = 0
Label(root, text='Enter a Task',bg ='teal', fg='white').pack()
task_entry= Entry(root)
task_entry.pack()
Label(root, text='  ',bg ='teal', fg='white').pack()
task_listbox = Listbox(root, selectmode=MULTIPLE)
task_listbox.pack()

def add_task():
    global task_nr
    task_nr += 1
    if task_nr > 1000:
        task_nr = 1
    task = task_entry.get()
    task_listbox.insert(END, f'Task number {task_nr}:> {task}')
    task_entry.delete(0,END)
    root.config(bg='lightgreen')

def remove_task():
    tasks = task_listbox.curselection()
    for tsk in tasks[::-1]:  # works better if more than one selection
        task_listbox.delete(tsk)
    root.config(bg='Yellow')


Button(root, text='Add Task', command=add_task, bg='green', fg='black' ).pack()
Button(root, text='Remove Task', command=remove_task, bg='purple', fg='black' ).pack()

root.mainloop()