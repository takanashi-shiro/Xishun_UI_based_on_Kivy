import bs4

def get_now_week(session):
    url = 'http://218.75.197.123:83/jsxsd/framework/xsMain_new.jsp?t1=1'
    headers = {
        'Host': '218.75.197.123:83',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://218.75.197.123:83',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://218.75.197.123:83/jsxsd/framework/xsMain.jsp',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive'
    }
    response = session.get(url=url, headers=headers)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    ls = soup.find_all('span',class_='main_text main_color')[0].text
    res = ls[ls.find("第")+1:ls.find("周"):]
    return res

def get_all_week(session):
    url = 'http://218.75.197.123:83/jsxsd/framework/xsMain_new.jsp?t1=1'
    headers = {
        'Host': '218.75.197.123:83',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://218.75.197.123:83',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://218.75.197.123:83/jsxsd/framework/xsMain.jsp',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive'
    }
    response = session.get(url=url, headers=headers)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    res = soup.find_all('div', id='li_showWeek')[0].text
    res=res[res.find('/')+1:]
    res=res[:res.find("周")]
    return res