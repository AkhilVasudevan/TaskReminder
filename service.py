import json
from datetime import datetime
from datetime import date
import time
from DBHelper import *
from tkinter import messagebox
import tkinter
import easygui

if __name__=="__main__":
    while(True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S").split(' ')
        data=GetTasksByDateTime(now[0],now[1])
        reminders=""
        for item in data:
            reminders=reminders+item[1]
            reminders=reminders+"\n"
            DeleteTask(item[0])
        if(len(data)>0):
            easygui.msgbox(reminders,"Task Reminder")
        time.sleep(60)