class Number:
    n=0

    def __init__(self,n) -> None:
        self.n=n

    def __str__(self) -> str:
        return str(self.n)

    def __add__(self, x):
        self.n=self.n+x

    def __pow__(self, power, modulo=None):
        self.n=self.n**power


if __name__=='__main__':
    n=Number(4)
    n**2
    n+10

    print(n)