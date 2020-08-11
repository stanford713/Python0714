class BMI:
    h=0 #公有變數
    w=0 #公有變數
    __bmi=0 #私有變數

    def calcBMI(self):
        self.__bmi=self.w/((self.h/100)**2)
    def getBMI(self):
        return self.__bmi

if __name__ == '__main__':
    b=BMI
    b.h=170
    b.w=75
    b.calcBMI() #計算BMI
    print(b.getBMI())