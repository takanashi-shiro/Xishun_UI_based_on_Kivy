import functools

import requests


def mycmp(a, b):
    if len(a['name']) > len(b['name']):
        if a['name'] < b['name']:
            return -1
        elif a['name'] > b['name']:
            return 1
        else:
            return 0
    elif len(a['name']) < len(b['name']):
        if a['name'] < b['name']:
            return 1
        elif a['name'] > b['name']:
            return -1
        else:
            return 0
    else:
        return 0
    # return a['name'] < b['name']


def choose_building():
    url = 'http://h5cloud.17wanxiao.com:8080/CloudPayment/user/getRoom.do?payProId=1567&schoolcode=786&optype=2&areaid=4&buildid=0&unitid=0&levelid=0&businesstype=2'
    response = requests.get(url=url)
    dicts = response.json()
    buildings = dicts['roomlist']
    tmp = sorted(buildings, key=functools.cmp_to_key(mycmp))
    namelist = []
    idlist = []
    for i in tmp:
        if i['name'].find('学生') != -1:
            namelist.append(i['name'])
            idlist.append(i['id'])
    res = [namelist, idlist]
    return res
