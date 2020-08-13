def inputnumber():
    try:
        x=float(input('請輸入分子:'))
        y=float(input('請輸入分母:'))
        z=x/y

    except ValueError as e:
        print('錯誤類型:',e.__class__.__name__)#內置方法
        print('你輸入的不是數字,請重新輸入')
        inputnumber()
    except ZeroDivisionError as e:
        print('錯誤類型:',e.__class__.__name__)
        print('分母不可=0,程式結束....')
        return
    except Exception as e:
        print('錯誤類型:',e.__class__.__name__)
        print('其他錯誤,程式結束....')
        return
    else:
        print(x, '/', y, '=', z)
    finally:
        print('謝謝使用此程式')


if __name__=='__main__':
    inputnumber()