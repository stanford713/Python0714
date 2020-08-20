import tkinter
import tkinter.ttk as ttk
def b1():
    c_value.set(c_value.get()+'1')
def b2():
    c_value.set(c_value.get()+'2')
def b3():
    c_value.set(c_value.get()+'3')
def b4():
    c_value.set(c_value.get()+'4')
def b5():
    c_value.set(c_value.get()+'5')
def b6():
    c_value.set(c_value.get()+'6')
def b7():
    c_value.set(c_value.get()+'7')
def b8():
    c_value.set(c_value.get()+'8')
def b9():
    c_value.set(c_value.get()+'9')
def b0():
    c_value.set(c_value.get()+'0')
def d():
    c_value.set(c_value.get()+'．')
def c():
    c_value.set('')
def backk():
    s=c_value.get()
    c_value.set(s[:len(s)-1])
def di():
    c_value.set(c_value.get()+'/')
def mul():
    c_value.set(c_value.get()+'*')
def m():
    c_value.set(c_value.get()+'-')
def add():
    c_value.set(c_value.get()+'+')
def eq():
    c_value.set('%.2f'%(eval(c_value.get())))

win=tkinter.Tk()
win.title('佈局')
c_value=tkinter.StringVar()
c_value.set('')
s = ttk.Style()
s.configure('My.TButton', font=('Arial', 20))
label=ttk.Label(win,textvariable=c_value,font=('Arial',20))
btn1=ttk.Button(win,text='1',style='My.TButton',command=b1)
btn2=ttk.Button(win,text='2',style='My.TButton',command=b2)
btn3=ttk.Button(win,text='3',style='My.TButton',command=b3)
btn4=ttk.Button(win,text='4',style='My.TButton',command=b4)
btn5=ttk.Button(win,text='5',style='My.TButton',command=b5)
btn6=ttk.Button(win,text='6',style='My.TButton',command=b6)
btn7=ttk.Button(win,text='7',style='My.TButton',command=b7)
btn8=ttk.Button(win,text='8',style='My.TButton',command=b8)
btn9=ttk.Button(win,text='9',style='My.TButton',command=b9)
btn0=ttk.Button(win,text='0',style='My.TButton',command=b0)
cancel=ttk.Button(win,text='C',style='My.TButton',command=c)
back=ttk.Button(win,text='<－',style='My.TButton',command=backk)
divide=ttk.Button(win,text='/',style='My.TButton',command=di)
multi=ttk.Button(win,text='*',style='My.TButton',command=mul)
minus=ttk.Button(win,text='-',style='My.TButton',command=m)
add=ttk.Button(win,text='+',style='My.TButton',command=add)
equal=ttk.Button(win,text='=',style='My.TButton',command=eq)
dot=ttk.Button(win,text='．',style='My.TButton',command=d)



win.rowconfigure((0,1,2,3,4,5),weight=1)#同步放大縮小
win.columnconfigure((0,1,2,3),weight=1)

label.grid(row=0,column=0,columnspan=4,rowspan=1,sticky='EWNS',padx=(20))#sticky='EWNS'填滿
btn1.grid(row=4,column=0,columnspan=1,rowspan=1,sticky='EWNS')
btn2.grid(row=4,column=1,columnspan=1,rowspan=1,sticky='EWNS')
btn3.grid(row=4,column=2,columnspan=1,rowspan=1,sticky='EWNS')
btn4.grid(row=3,column=0,columnspan=1,rowspan=1,sticky='EWNS')
btn5.grid(row=3,column=1,columnspan=1,rowspan=1,sticky='EWNS')
btn6.grid(row=3,column=2,columnspan=1,rowspan=1,sticky='EWNS')
btn7.grid(row=2,column=0,columnspan=1,rowspan=1,sticky='EWNS')
btn8.grid(row=2,column=1,columnspan=1,rowspan=1,sticky='EWNS')
btn9.grid(row=2,column=2,columnspan=1,rowspan=1,sticky='EWNS')
btn0.grid(row=5,column=0,columnspan=1,rowspan=1,sticky='EWNS')
cancel.grid(row=1,column=0,columnspan=2,rowspan=1,sticky='EWNS')
back.grid(row=1,column=2,columnspan=1,rowspan=1,sticky='EWNS')
divide.grid(row=1,column=3,columnspan=1,rowspan=1,sticky='EWNS')
multi.grid(row=2,column=3,columnspan=1,rowspan=1,sticky='EWNS')
minus.grid(row=3,column=3,columnspan=1,rowspan=1,sticky='EWNS')
add.grid(row=4,column=3,columnspan=1,rowspan=2,sticky='EWNS')
equal.grid(row=5,column=2,columnspan=1,rowspan=1,sticky='EWNS')
dot.grid(row=5,column=1,columnspan=1,rowspan=1,sticky='EWNS')

win.mainloop()