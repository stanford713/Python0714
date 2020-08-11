class Drink:
    def __init__(self,name,amount,price) -> None:
        self.name=name
        self.amount=amount
        self.price=price

    def __lt__(self, other):
        return (self.price/self.amount) < (other.price/other.amount)

    def __gt__(self, other):
        return (self.price/self.amount) > (other.price/other.amount)

if __name__=='__main__':
    milk=Drink('牛奶',2,80)
    coffee=Drink('咖啡',3,105)
    print(coffee < milk)
    drinkName= coffee.name if coffee < milk else milk.name
    print("便宜的是:",drinkName)
    drinkName = coffee.name if coffee > milk else milk.name
    print("貴的是:",drinkName)