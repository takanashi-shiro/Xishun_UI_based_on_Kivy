import functools

import bs4


# import login


def mycmp(a, b):
    if eval(a['day']) < eval(b['day']):
        return -1
    elif eval(a['day']) > eval(b['day']):
        return 1
    else:
        if eval(a['class'][1:2]) < eval(b['class'][1:2]):
            return -1
        elif eval(a['class'][1:2]) > eval(b['class'][1:2]):
            return 1
        else:
            return 0


def get_sykb(session):
    url = "http://218.75.197.123:83/jsxsd/syjx/toXskb.do"
    headers = {
        'Host': '218.75.197.123:83',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://218.75.197.123:83/jsxsd/framework/xsMain.jsp',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive'
    }
    response = session.get(url=url, headers=headers)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    ls_tmp = soup.find('table', id='tblHead')
    trs = ls_tmp.find_all('tr')
    weeks = '1'
    tmp_dicts_ls = ['name', 'content', 'weeks', 'week_flag', 'day', 'class', 'pos']
    res = []
    for tr in trs:
        for td in tr:
            if td.get('scope') == 'col':
                continue
            if td.get('rowspan') == '6':
                weeks = td.text
                continue
            if td.text != chr(160) and td.text[-2:] != '大节':
                tmp_dict = {}
                tt = 0
                pos = ''
                for i in td:
                    if i.text != '':
                        if tt == 2:
                            pos = i.text[i.text.find('   ') + 3:]
                            tt += 1
                        elif tt == 3:
                            f = i.text.find('节次：') + 3
                            tmp = i.text[0 - len(i.text) + f:-1]
                            day = tmp[0]
                            class_tmp = tmp[1:3] + '-' + tmp[-2:] + '节'
                            tt += 1
                        else:
                            tmp_dict[tmp_dicts_ls[tt]] = i.text
                            tt += 1
                tmp_dict['weeks'] = weeks
                tmp_dict['week_flag'] = '每周'
                tmp_dict['day'] = day
                tmp_dict['class'] = class_tmp
                tmp_dict['pos'] = pos
                tmp_dict['name'] = '[实验课]'+tmp_dict['name']
                res.append(tmp_dict)
    return res


def get_kb(session):
    url = "http://218.75.197.123:83/jsxsd/xskb/xskb_list.do"
    headers = {
        'Host': '218.75.197.123:83',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://218.75.197.123:83/jsxsd/framework/xsMain.jsp',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive'
    }
    response = session.get(url=url, headers=headers)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    #pip install lxml
    ls = soup.find_all('div', class_="kbcontent")
    class_list = []
    tmp_dicts_ls = ['name', 'teacher', 'weeks', 'week_flag', 'day', 'class', 'pos']
    for i in ls:
        if len(i.text) != 1:
            tt = 0
            tmp_dicts = {}
            for j in i:
                if len(j.text) != 0:
                    if j.text == '&nbspP' or j.text == '&nbspO':
                        continue
                    if tt == 2:
                        weeks = j.text[0:j.text.find('(')]
                        week_flag = j.text[j.text.find('(') + 1:j.text.find(')')]
                        if week_flag == '周':
                            week_flag = "每周"
                        day = str(i['id'])[-3:-2:]
                        classtime = j.text[j.text.find('[') + 1:j.text.find(']')]
                        tmp_dicts['weeks'] = weeks
                        tmp_dicts['week_flag'] = week_flag
                        tmp_dicts['day'] = day
                        tmp_dicts['class'] = classtime
                        tt += 4
                    else:
                        if j.text[0] == '-' and j.text[1] == '-':
                            tt = 0
                            continue
                        if j.text[0] == '(':
                            tmp_dicts['name'] += j.text
                            continue
                        tmp_dicts[tmp_dicts_ls[tt]] = j.text
                        tt += 1
                        if tt >= 7:
                            # print(tmp_dicts)
                            class_list.append(tmp_dicts)
                            tmp_dicts = {}
    tmp_ls = get_sykb(session)
    class_list = class_list + tmp_ls
    res = sorted(class_list, key=functools.cmp_to_key(mycmp))

    return res
