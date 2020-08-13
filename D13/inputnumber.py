def inputnumber():
    try:
        x=int(input("請輸入數字:"))
        print('您輸入的是:',x)
    except Exception as e:
        print('sorry 您輸入錯了,錯誤原因->',e)
        inputnumber()


if __name__=='__main__':
    inputnumber()