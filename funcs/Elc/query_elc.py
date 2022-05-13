import requests

from funcs.Elc.choose_building import choose_building
from funcs.Elc.choose_room import choose_room


def query_elc(id):
    url = 'http://h5cloud.17wanxiao.com:8080/CloudPayment/user/getRoomState.do?payProId=1567&schoolcode=786&businesstype=2&roomverify='+id
    response = requests.get(url=url)
    dicts = response.json()
    res = '寝室号：'+dicts['description']+'\n剩余电量：'+dicts['quantity']+'度\n'
    return res,str(dicts['quantity'])

def get_elc(building, room):
    building = int(building) - 1
    search = str(choose_building()[1][building])
    room_id = str(choose_room(search)[1][choose_room(search)[0].index(room)])
    elc = eval(query_elc(room_id)[1])
    return elc