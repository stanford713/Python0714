def calc(x=1,y=2)->int:
    return x+y
def calc2(x=None,y=None)->int:
    if x==None:
        print('使用者沒帶X值')
        return  0
    if y is None:#can use is to replace the ==
        print('使用者沒帶y值')
        return 0
    return x+y


if __name__=='__main__':
    sum=calc(10,20)
    print(sum)
    sum=calc()
    print(sum)
    sum=calc(7)#為X的數
    print(sum)
    sum=calc(y=7)
    print(sum)
    sum=calc2(3,1)
    print(sum)