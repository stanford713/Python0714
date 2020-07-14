# 撰寫一個 BMI 計算系統
def calcBMI() -> None: #表示沒有回傳值
    h=float(input("你的身高(CM):"))
    w=float(input("你的體重(KG):"))
    bmi=w/((h/100)**2)
    result= "過重" if (bmi>23)  else "過輕" if (bmi<18) else "正常"
    print("身高:%.1f 體重:%.1f BMI:%.2f (%s)" % (h, w, bmi, result))


def menu():
    print("BMI 計算系統 ")
    print("------------")
    print("1.進入系統")
    print("2.離開系統")
    Choose=int(input("請輸入:"))
    if Choose==1:
        print("檢測你的BMI")
        calcBMI()
        print("以上是您的BMI")
    elif Choose==2:
        print("你選擇離開")
    else:
        print("選擇無效")
        menu()

menu()
