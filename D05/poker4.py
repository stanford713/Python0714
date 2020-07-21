import random
import time
def getScore(p):
    if p=='A':
        return 1
    elif p=='J'or p=='Q' or p=='K':
        return 0.5
    else:
        return p

poker=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']*4
random.shuffle(poker)#亂序
#餘額
balance=100;
while True:
#下注
    bet=int(input('請下注,(不可超過%d):'%balance))
    #牌局開始發一張
    p1=poker.pop()#組數裡最尾端的數據
    sum=getScore(p1)
    print('已拿:',p1,'總分:',sum)


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
            #不執行裡面的CODE

    #PC拿牌
    p2=poker.pop()
    sum2=getScore(p2)
    print('PC已拿:',p2,'總分:',sum2)

    count_pc=0;
    while True:
        take=False
        time.sleep(2)#延遲兩秒
        if sum2>=9:
            break
        elif sum2<7:
           take=True
        elif sum2==7 or sum2==7.5:
            amount=poker.count('A')+poker.count(2)+poker.count(3)
            if amount>=10:
               take=True
        elif sum2==8 or sum2==8.5:
            amount = poker.count('A') + poker.count(2)
            if amount>=7:
               take=True
        if take:
            p = poker.pop()
            sum2 = sum2 + getScore(p)
            print('PC再拿:', p, '總分:', sum2)
        if sum2>10.5:
            print("PC爆了")
            break
        else:
            count_pc+=1
            if count_pc==5:
                print('PC 過五關, 超強的~~~')
                break
    #勝負比較
    #sum,count
    #sum2,count_pc
    if count==5 and sum<=10.5:
        balance+=bet
        continue
    if (sum<=10.5) and (sum2>10.5):
        balance+=bet
        continue
    if (sum<=10.5 and sum2<=10.5) and(sum>sum2):
        balance+=bet
        continue
    if (sum > 10.5 and sum2 > 10.5) or (sum == sum2):
         print('和局, 最新餘額:', balance)
    continue  # 進入下一局