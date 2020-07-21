import random
x=0
while x%3==0:
    x=random.randint(1,9)
    print(x)
    if x%2==0:
        break
