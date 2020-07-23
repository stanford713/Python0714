#字典資料格式
fruits={'orange':20,'apple':10,'watermelon':30}
#利用get(放入KEY值)得到value
print('orange 幾元',fruits.get('orange'))
print('apple 幾元',fruits.get('apple'))
print('watermelon 幾元',fruits.get('watermelon'))
print(fruits)
#setdefault(Key值,預設值(若找不到此元素))
print('banana 幾元',fruits.setdefault('banana',100))
print(fruits)
#取得所有的key值
names=fruits.keys()
print(names, type(names))
#取得所有的value值
value=fruits.values()
print(value,type(value),sum(value))