from util.MyCalc import bmi
import util.MyCalc
import util.MyCalc as m
from util.MyCalc import bmi#可以直接用BMI 不用再強調
if __name__ =='__main__':
    a=10
    b=10
    w=60
    h=170
    print(util.MyCalc.sub(a,b))
    print(m.add(a,b))
    print(bmi(170,75))