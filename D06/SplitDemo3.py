data='170,60&160,48'
for row in data.split('&'):
    print(row,type(row))
    h,w=row.split(',')
    print(h,w,type(h),type(w))
    bmi='%.2f'%(float(w)/((float(h)/100)**2))
    print(bmi)