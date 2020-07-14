Name=(input('請輸入名字:'))
h=(float(input('請輸入身高:')))
w=(float(input('請輸入體重:')))
bmi=w/((h/100)**2)
result='正常'if 18<bmi<=23 else'過高'if bmi>23 else'過低'

print('%s的身高是幾%5.1fcm體重是%5.1fkg,bmi結果為%5.2f(%s)'%(Name,h,w,bmi,result))