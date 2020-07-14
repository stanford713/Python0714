#def自帶參數
def printBMI(h,w):
    bmi=w/((h/100)**2)
    print("%.2f" %bmi)

printBMI(170,50)
printBMI(170,75)
