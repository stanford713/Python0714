import tkinter
from tkinter import  ttk
import sqlite3

win=tkinter.Tk()
win.title('資料庫')


tree=ttk.Treeview(win,columns=['1','2'],show='headings')
tree.heading('1',text='id')
tree.heading('2',text='name')

tree.column('1',width=100,anchor='center')
tree.column('2',width=100,anchor='center')
#資料匯入
conn=sqlite3.connect('student.db')
cursor=conn.cursor()
cursor.execute('select id,name from student')
for row in cursor.fetchall():
    data1=[row[0],row[1]]
    tree.insert('','end',value=row)
tree.grid()

tree.pack()
win.mainloop()