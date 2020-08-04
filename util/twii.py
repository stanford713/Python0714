def gettwiilist():
    file=open('BWIBBU_d_ALL_20200804.csv')
    rows=file.readlines()
    list=[]#用來存放整理好的資料
    #your code here
    for row in rows:
        row=row.replace('\n','')
        row =row.replace('\"', '')
        array=row.split(',')
        if len(array)==8 and array[0] !='證券代號':
            dict={} # 存放每一筆紀律
            dict.setdefault("證券代號",array[0])
            dict.setdefault("證券名稱", array[1])
            dict.setdefault("殖利率(%)", float(array[2]) if array[2] !='-' else -1)
            dict.setdefault("股利年度", array[3])
            dict.setdefault("本益比", float(array[4]) if array[4] !='-' else -1)
            dict.setdefault("股價淨值比", array[5] if array[5] !='-' else -1)
            dict.setdefault("財報年季", array[6])
            list.append(dict) #加入到list
    print(list)




