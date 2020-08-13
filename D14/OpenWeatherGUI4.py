#現在時間
import tkinter
import datetime
import requests
import json


def update():
    path='https://api.openweathermap.org/data/2.5/weather?q=Taoyuan,TW&appid=7dd73f7d891388504a1b85da5e069163'
    ow=json.loads(requests.get(path).text)
    weathermain=ow['weather'][0]['main']
    temp=ow['main']['temp']-273.15
    feel_like = ow['main']['feels_like']-273.15
    humidity = ow['main']['humidity']
    ans.set('%s\n氣溫: %.2f°C \n體感:%.2f°C\n濕度:%.2f'%(weathermain,temp,feel_like,humidity))

win=tkinter.Tk()
win.title('The weather of Taoyuan')
win.geometry('500x200')
ans=tkinter.IntVar()
label=tkinter.Label(win,textvariable=ans)
label.config(font=('Arial',20))#字的樣式大小'fg'字的顏色跟'bg'背景顏色
label.pack()
button1=tkinter.Button(win,text='Update',command=update)
button1.config(font=("Arial", 20))
button1.pack()





win.mainloop()