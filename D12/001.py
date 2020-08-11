class Human:
    name=''
    age=0
    sex=''

    def __str__(self) -> str:
        return self.name+','+str(self.age)+','+self.sex


if __name__=='__main__':
    h1=Human()
    h1.name='Stanford'
    h1.age=18
    h1.sex='男'

print(h1)