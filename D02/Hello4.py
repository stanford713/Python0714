#資料轉換

x=input('請輸入一個數字X:')
y=input('請輸入一個數字y:')
print(x,y)
sum=x+y
print(sum)
#觀察x,y的資料型態
print(x,type(x),y,type(y))
#皆為字串
#所以要透過int() 來進行字串轉換數字的程序
sum=int(x)+int(y)
print(sum)