users=[{'n':'John','h':170,'w':60},{'n':'Mary','h':160,'w':48}]
for user in users:
    print(user)
    h=user.get("h")
    w=user.get('w')
    bmi='%.2f'%(w/((h/100)**2))
    print(user,bmi)

