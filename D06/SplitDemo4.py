data='orange=10,apple=30,berry=20'
#將字串變成字典格式
fruits=dict(item.split('=')for item in data.split(','))
#先看for迴圈找出item
#然後再去多次split
print(fruits)
print(fruits.get('apple'),type(fruits.get('apple')))
