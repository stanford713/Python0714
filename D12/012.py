class JPY:
    def __get__(self, instance, owner):
        return instance.TW/0.28
    def __set__(self, instance, value):
        instance.TW=value*0.28
class USD:
    def __get__(self, instance, owner):
        return instance.TW/30.5
    def __set__(self, instance, value):
        instance.TW=value*30.5
class Exchange:
    usd=USD()
    jpy=JPY()
    def __init__(self,money) -> None:
        self.TW=money



if __name__=='__main__':
    ex=Exchange(10000)
    print(ex.usd)
    print(ex.jpy)
    ex.jpy=4500
    print(ex.TW)
    ex.usd=1000000
    print(ex.TW)
