import random as r
#set不可重複數組[1,2,3,4,5]
#list可以重複數組[1,1,2,3,4]
lotto=[]#list
while len(lotto)<5:
    lotto.append(r.randint(1,10))
print(lotto)
lotto2=set()
while len(lotto2)<5:
    lotto2.add(r.randint(1,10))
print(lotto2)