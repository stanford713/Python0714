import random as r
m,M=0,100
ans=(r.randint(1,99))
amount=5
while amount>0:
    amount -=1 #amount每猜一次扣一次
    guess=int(input("在%d~%d輸入一個數字:"%(m,M)))
    if guess<=m or guess>=M:
        print("輸入錯誤")
        continue

    if guess>ans:
            M=guess
    elif guess<ans:
            m=guess
    else:
        print("恭喜你答對了")
        break
    if amount==0:
        print("GG了,答案",str(ans))
        break






