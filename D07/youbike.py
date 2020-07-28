import requests
import json
from math import radians, cos, sin, asin, sqrt
#24.990022 121.311989
def borrowfromneartofar(q,youbikes):
    rows=[]
    for youbike in youbikes:
        if int(youbike.get('sbi'))>=q:
            rows.append(youbike)
    dis=[]
    for row in rows:
        print(row.get('sna'), row.get('distance'))
        dis.append(row.get('distance'))
        print(dis)

def printyoubikesbydistance(m,youbikes):#距離目標地點幾公尺內
    for youbike in youbikes:
        if youbike.get('distance')<=m:
            print(youbike.get('sna'), youbike.get('distance'))
def appendDistance(lat,lng,youbikes):
    for youbike in youbikes:
        d = haversine(24.990042, 121.311989, float(youbike.get('lat')), float(youbike.get('lng')))
        youbike.setdefault("distance", d)

def getyoubikes() ->list:
    limit=500
    path='https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json&limit=%d'
    path=path % limit
    data=requests.get(path).text
    dict=json.loads(data)
    youbikes=dict.get('result').get('records')
    return youbikes
def getyoubikesbyname(sna,youbikes=None)->dict:
    if youbikes is None:
        youbikes=getyoubikes()
    for youbike in youbikes:
        if str(youbike.get('sna')).__contains__(sna):
            return youbike
# 透過經緯度計算距離的方法
def haversine(lon1, lat1, lon2, lat2) : # 經度1，緯度1，經度2，緯度2）
    # 轉弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # 半正矢 haversine 公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # 地球平均半徑(公里)
    return c * r * 1000 # 單位公尺
if __name__=="__main__":
    youbikes=getyoubikes()
    youbike=getyoubikesbyname('桃園火車站(前站)')
    d=haversine(24.990042,121.311989,float(youbike.get('lat')),float(youbike.get('lng')))
    print(d,'公尺',type(youbike))
    # 加入距離資訊
    appendDistance(24.990042, 121.311989, youbikes)
    print(youbikes)
    printyoubikesbydistance(500, youbikes)
    print('-------------------------------------')
    borrowfromneartofar(20,youbikes)

