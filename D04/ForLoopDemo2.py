def getSum(score):
    sum = 0
    for i in range(0, len(score)):
        sum += score[i]  # 從sum一開始 開始累加
    return sum
def getAvg(score):
    sum=getSum(score)
    avg = sum / len(score)
    return avg



#主程式
score=[100,93,80,74,66,50,40]#數組 0 1 2 3 4 ....代表 100 90 80 70 60....
for i in range(0,len(score)):#len可以得知數組的元素個數
    print(score[i])

sum=getSum(score)
print("總分:%d"%sum)

avg=getAvg(score)
print("平均:%.2f"%avg)