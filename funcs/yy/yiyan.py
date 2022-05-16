import requests
import time


def yiyan():
    url = 'https://v1.hitokoto.cn'
    response = requests.get(url)
    res_dict = response.json()
    map = {"a": "动画", "b": "漫画", "c": "游戏", "d": "文学", "e": "原创", "f": "网络",
           "g": "其他", "h": "影视", "i": "诗词", "j": "网易云", "k": "哲学", "l": "抖机灵"}
    source = ''
    if res_dict['from_who'] is not None:
        source += "——" + res_dict['from_who']+" 《"+res_dict['from']+"》"
    else:
        source +="——" +"《"+res_dict['from']+"》"
    types = map[res_dict['type']]
    l = len(res_dict['hitokoto'])
    l2 = len(source)
    returns = ""

    returns += (types+"每日一句：\n『".ljust(3*(l+l2))+"\n"
                + res_dict['hitokoto'].center((l+l2))+"\n\n")
    returns += (source.rjust(2*(l+l2))+"\n" +
                "』".rjust(3*(l+l2))+"\n")
    return returns

if __name__ == "__main__":
    print(yiyan())