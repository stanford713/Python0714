def bread(func):
    print('我是麵包')
    return func
def onion(func):
    print('我是洋蔥')
    return func

@onion  #擺放順序也會有差別
@bread
def Hotdog():
    print('我是熱狗')


if __name__=='__main__':
    Hotdog()
