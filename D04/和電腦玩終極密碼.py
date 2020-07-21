import random as r
m,M=0,100
ans=(r.randint(0,100))
amount=5
while amount>0:
    amount -=1 #amount每猜一次扣一次
    guess=int(input("在%d~%d輸入一個數字:"%(m,M)))

    if guess<=m or guess>=M:
        print("輸入錯誤")
        continue
    if guess==ans:
        print('你贏了,答案:',str(ans))
        break
    else:
        if guess>ans:
            M=guess
        elif guess<ans:
            m=guess
    pc = r.randint(m + 1, M - 1)
    print('在%d~%d輸入一個數字,電腦猜%d'%(m,M,pc))
    if pc==ans:
        print('電腦贏了,答案:',str(ans))
        break
    else:
        if pc > ans:
            M = pc
        elif pc < ans:
            m = pc
    if amount==0:
        print("GG了,答案",str(ans))