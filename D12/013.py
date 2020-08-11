class Foo:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y

    def __str__(self) -> str:
        return "x: %d y: %d"%(self.x,self.y)
class Bar:
    def __call__(self,x,y ):
        self.x=x
        self.y=y
    def __str__(self) -> str:
        return "x: %d y: %d"%(self.x,self.y)





if __name__=="__main__":
    foo= Foo(10,20) #呼叫 init
    print(foo)
    bar=Bar() #呼叫init
    bar(10,20) #呼叫call
    print(bar)
