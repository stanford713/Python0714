import random
import statistics
def gerStat(list):

    list.sort()
    list.__delitem__(0)
    list.__delitem__(0)
    list.__delitem__(len(list)-1)
    list.__delitem__(len(list)-1)
    mean = statistics.mean(list)
    stdev=statistics.stdev(list)
    cv=stdev/mean
    return mean, stdev,cv
a,b=[],[]
for i in range(0,10):
    a.append(random.randint(0,10))
    b.append(random.randint(0,10))
print('a:',a)
print('b:',b)
mean_a,stdev_a,cv_a=gerStat(a)
mean_b,stdev_b,cv_b=gerStat(b)
print(mean_a,stdev_a,cv_a)
print(mean_b,stdev_b,cv_b)
