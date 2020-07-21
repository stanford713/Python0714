import random
def getScore(p):
    if p=='A':
        return 1
    elif p=='J'or p=='Q' or p=='K':
        return 0.5
    else:
        return p

poker=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']*4
random.shuffle(poker)#亂序
#牌局開始發兩張
print(poker)
p1=poker.pop()#組數裡最尾端的數據

sum=getScore(p1)
print('已拿:',p1,'總分:',sum)
print('剩餘:',poker)

#繼續拿牌
count=0;
while True:
    ask=input('是否要拿牌(y/n)?')
    if ask=='y':
        p=poker.pop()
        sum=sum+getScore(p)
        print('再拿:', p, '總分:', sum)
        if sum>10.5:
            print('總分:',sum,'boom')
            break
        else:
            count+=1
        if count==5:
            print('恭喜過五關',sum,'次數',count)
    else:
        break
