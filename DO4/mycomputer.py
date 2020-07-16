def add(x,y):
    result=x+y
    return result

def info():
    print("本城市是由Python所撰寫")
    return

def checkgender(id):
    gender=id[1] #抓id的第()個的字元 利用中括號
    if gender =='1':
        print("男生")
        return
    if gender =='2':
        print("女生")
        return

checkgender('a128925443')