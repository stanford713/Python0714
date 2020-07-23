user={'John':[170,70],'Mary':[160,48]}
names =user.keys()
for name in names:
    h=float(user.get(name)[0])
    w=float(user.get(name)[1])
    bmi=w/((h/100)**2)
    print(name,user.get(name),h,w,('%.2f'%bmi))
