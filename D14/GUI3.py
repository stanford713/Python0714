import tkinter

def add():
    n=ans.get()
    n=n+1
    ans.set(n)
def sub():
    n=ans.get()
    n=n-1
    ans.set(n)
win =tkinter.Tk()
win.title('My add')
win.geometry('300x300')#視窗大小

ans=tkinter.IntVar()
ans.set(0)
label=tkinter.Label(win,textvariable=ans)
label.config(font=('Arial',40),fg='Red')#字的樣式大小字的顏色跟背景顏色
label.pack()

button1=tkinter.Button(win,text="add",command=add)
button1.config(font=('Arial',40))
button1.pack(side=tkinter.RIGHT)

button2=tkinter.Button(win,text="sub",command=sub)
button2.config(font=('Arial',40))
button2.pack(side=tkinter.LEFT)




win.mainloop()