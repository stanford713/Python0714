import math
x0,y0=10,2
x1,y1=4,30
d=math.sqrt((x0-x1)**2+(y0-y1)**2)
result='a點座標({0},{1})b點座標({2},{3}),直線距離{4:.2f}'.format(x0,y0,x1,y1,d)
print(result)