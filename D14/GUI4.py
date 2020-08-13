#現在時間
import tkinter
import datetime
import time
from tkinter import messagebox
def update():
    dt=datetime.datetime.today()
    ans.set(dt)

win=tkinter.Tk()
win.title('Time')
win.geometry('500x200')
ans=tkinter.IntVar()
update()

label=tkinter.Label(win,textvariable=ans)
label.config(font=('Arial',20))#字的樣式大小'fg'字的顏色跟'bg'背景顏色
label.pack()

button1=tkinter.Button(win,text='Update',command=update)
button1.config(font=("Arial", 20))
button1.pack()



win.mainloop()