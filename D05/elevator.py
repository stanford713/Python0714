import time
print('有一棟7層大樓的電梯系統,運作如下:')
now=1
while True:
    goal=int(input('你現在在%d樓,請問要去哪樓?\n>>'%now))
    if goal<=0 or goal>=8:
        print("尚未有這些樓層,請輸入1~7樓")
        continue
    if goal==now:
        continue
    if goal>now:
        print('goes up')
        while goal>now:
            print(now)
            now=now+1
            time.sleep(1)
        print(now)
    elif goal<now:
        print('goes down')
        while goal<now:
            print(now)
            now=now-1
            time.sleep(1)
        print(now)






