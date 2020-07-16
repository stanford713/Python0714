report='台積電每股315.5元,可賣出4000股,目前我的庫存有6000股'
#求賣出後的庫存總值
total=float(report[5:10])*(float(report[28:32])-float(report[15:19]))
print(total)
print(10+2)
