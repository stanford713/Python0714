def  calc(T,F):
    r=((F-2*T))/2
    c=T-r
    return c,r

c,r=calc(83,240)
print("雞有%d隻 兔子有%d隻 隻數:%d 腳數:%d" %(c,r,c+r,(2*c+4*r)))