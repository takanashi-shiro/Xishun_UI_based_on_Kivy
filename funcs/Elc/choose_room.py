import requests


def choose_room(id):
    url = 'http://h5cloud.17wanxiao.com:8080/CloudPayment/user/getRoom.do?payProId=1567&schoolcode=786&optype=4&areaid=4&buildid='+id+'&unitid=0&levelid=-1&businesstype=2'
    response = requests.get(url=url)
    dicts = response.json()
    roomlist=dicts['roomlist']
    idlist = []
    namelist = []
    for i in roomlist:
        idlist.append(i['id'])
        namelist.append(i['name'])
    res = [namelist, idlist]
    return res