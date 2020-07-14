from DBHelper import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
import json
from tkinter import messagebox
#from tkcalendar import Calendar,DateEntry
import sys
from functools import partial

def getAbout():
    with open('config.json') as f:
        data = json.load(f)
    return data

def UpdateForm():
    pass

def Create(task_name,hh,mm,dt,mn,yr):
    try:
        alert_date="{:04d}-{:02d}-{:02d}".format(int(yr.get()),int(mn.get()),int(dt.get()))
        alert_time="{:02d}:{:02d}:00".format(int(hh.get()),int(mm.get()))
        if (InsertTask(task_name.get(),alert_date,alert_time)):
            messagebox.showinfo("Task Reminder", "Reminder for the task has been created.")
        else:
            message.showerror("Create Reminder","Reminder for the task has not been created.")
    except:
        messagebox.showerror("Create Reminder",sys.exc_info())
    
def Update():
    return "done"

def Delete():
    return "done"

def SubmitComment():
    messagebox.showinfo("Task Reminder", "Your suggestion has been sent to developer.")


if __name__=="__main__":
    try:
        root = tk.Tk()
        all_tasks=GetAllTasks()
        root.title("Task Reminder")
        root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='./Image/icon.png'))
        root.resizable(0,0)
        task_name=tk.StringVar()
        hh=tk.StringVar()
        mm=tk.StringVar()
        dt=tk.StringVar()
        mn=tk.StringVar()
        yr=tk.StringVar()
        tabControl = ttk.Notebook(root)
        #home tab
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text ='Home')
        ttk.Label(tab1,text="Task Name").grid(column=0,row=0,padx=5,pady=5)
        ttk.Label(tab1,text="Reminder Date").grid(column=1,row=0,padx=5,pady=5)
        ttk.Label(tab1,text="Reminder Time").grid(column=2,row=0,padx=20,pady=5)
        i=1
        for task in all_tasks:
            ttk.Label(tab1,text=task[1]).grid(column=0,row=i,padx=5,pady=5)
            ttk.Label(tab1,text=task[2]).grid(column=1,row=i,padx=5,pady=5)
            ttk.Label(tab1,text=task[3]).grid(column=2,row=i,padx=20,pady=5)
            i=i+1
        #create task tab
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text ='Create Task')
        ttk.Label(tab2,  text ="*Indicates mandatory fields").grid(column = 1,row = 0, padx = 30, pady = 5)
        ttk.Label(tab2,  text ="Task Name*").grid(column = 0,row = 2, padx = 30, pady = 5)
        task_names=tk.Entry(tab2,width=25,textvariable=task_name).grid(column = 1,row = 2, padx = 30, pady = 5)

        ttk.Label(tab2,  text ="Reminder Date(DD:MM:YYYY)*").grid(column = 0,row = 6, padx = 30, pady = 5)
        #alarm_date = DateEntry(tab2, width=20).grid(column = 1,row = 6, padx = 30, pady = 5)
        day=tk.Spinbox(tab2, from_=1, to=31,width=10,textvariable=dt).grid(column = 1,row = 6, padx = 30, pady = 5)
        month=tk.Spinbox(tab2, from_=1, to=12,width=10,textvariable=mn).grid(column = 2,row = 6, padx = 30, pady = 5)
        year=tk.Spinbox(tab2, from_=2020, to=2030, width=10,textvariable=yr).grid(column = 3,row = 6, padx = 30, pady = 5)
        ttk.Label(tab2,  text ="Reminder Time(HH:MM)*").grid(column = 0,row = 7, padx = 30, pady = 5)
        hour=tk.Spinbox(tab2, from_=0, to=23,width=10,textvariable=hh).grid(column = 1,row = 7, padx = 30, pady = 5)
        minutes=tk.Spinbox(tab2, from_=0, to=59,width=10,textvariable=mm).grid(column = 2,row = 7, padx = 30, pady = 5)
        Create = partial(Create, task_name,hh,mm,dt,mn,yr) 
        Button(tab2, text ="Create", command = Create).grid(column = 1,row = 9, padx = 30, pady = 5)
        #about tab
        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text ='About')
        about=getAbout()
        ttk.Label(tab3,  text ="Welcome to Task Reminder").grid(column = 1,row = 0, padx = 50, pady = 5)
        ttk.Label(tab3,  text ="Version : "+about['Version']).grid(column = 1,row = 2, padx = 50, pady = 5)
        ttk.Label(tab3,  text ="Developed By "+about['Developed_by']).grid(column = 1,row = 4, padx = 50, pady = 5)
        ttk.Label(tab3,  text =about['Made_in']).grid(column = 1,row = 6, padx = 50, pady = 5)
        tabControl.pack(expand = 1, fill ="both")
        root.mainloop()
    except:
        messagebox.showerror("Task Reminder", sys.exc_info())