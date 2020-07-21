import random
def check():
    n=random.randint(1,9)
    print(n)
    return True if n%2 ==0 else False

while check(): #只要他能顯示True OR False 回傳值,就可以當while的條件
    print("Python")