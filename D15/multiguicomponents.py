import  tkinter
import  tkinter.ttk as ttk

win = tkinter.Tk()

win.title('GUI元件視窗')
win.geometry('300x300')


#GUI元件配置
#標籤 label
my_label=ttk.Label(win,text='我是標籤')
my_label.pack()
#按鈕Button
my_buttun=ttk.Button(win,text='我是按鈕')
my_buttun.pack()#PACK放置元件
#按鈕checkbutton
my_checkbutton=ttk.Checkbutton(win,text='我同意')
my_checkbutton.pack()

#窗框Frame
my_frame=ttk.Frame(win)
my_frame.pack()

#按鈕radiobutton
m_radiobutton=ttk.Radiobutton(my_frame,text="男",value=1)
f_radiobutton=ttk.Radiobutton(my_frame,text="女",value=2)
m_radiobutton.pack(side=tkinter.LEFT)
f_radiobutton.pack(side=tkinter.LEFT)
#輸入框
my_entry=ttk.Entry(win)
my_entry.pack()
#下拉選單
values=['Python','Java','C+']
my_combobox=ttk.Combobox(win,value=values)
my_combobox.pack()


win.mainloop()