import  tkinter
import  tkinter.ttk as ttk

def ctof():
    c=float(entry1.get())
    f=c*9/5+32
    f_value.set(f)

def ftoc():
    f = float(entry2.get())
    c= (f-32)*5/9
    c_value.set(c)


win = tkinter.Tk()

win.title('溫度轉換')
win.geometry('300x300')
s = ttk.Style()
s.configure('My.TButton', font=('Arial', 10))
#設變數
c_value=tkinter.StringVar()
c_value.set(0)
f_value=tkinter.StringVar()
f_value.set(0)

my_frame=ttk.Frame(win)
my_frame.pack()

label1=ttk.Label(my_frame,text='攝氏:')
label1.config(font=('Arial',15))
label1.pack(side=tkinter.LEFT)
entry1=ttk.Entry(my_frame,textvariable=c_value)
entry1.config(font=('Arial',10))
entry1.pack(side=tkinter.LEFT)
button1=ttk.Button(my_frame,text='轉換',style='My.TButton',command=ctof)
button1.pack(side=tkinter.LEFT)


my_frame1=ttk.Frame(win)
my_frame1.pack()

label2=ttk.Label(my_frame1,text='華氏:')
label2.config(font=('Arial',15))
label2.pack(side=tkinter.LEFT)
entry2=ttk.Entry(my_frame1,textvariable=f_value)
entry2.config(font=('Arial',10))
entry2.pack(side=tkinter.LEFT)
button2=ttk.Button(my_frame1,text='轉換',style='My.TButton',command=ftoc)
button2.pack(side=tkinter.LEFT)





win.mainloop()