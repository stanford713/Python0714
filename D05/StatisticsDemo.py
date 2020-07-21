import statistics
import random

score = []
for i in range(0,10):
    score.append(random.randint(0,10))
#排序
score.sort()
print(score)
#移除最小的兩個元素
#__delitem__(0)移除指定位置的元素
score.__delitem__(0)
score.__delitem__(0)
score.__delitem__(len(score)-1)
score.__delitem__(len(score)-1)
print(score)

mean=statistics.mean(score)
print('平均:',mean)
stdev=statistics.stdev(score)
print('標準差:',stdev)
cv=stdev/mean
print('變異係數:',cv)