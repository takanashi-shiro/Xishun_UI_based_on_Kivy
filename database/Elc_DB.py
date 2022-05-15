import datetime

from funcs.Elc.query_elc import get_elc
from .DB_user import link

elc_unit_price = 0.6

def find_bd(qq_number):
    sql = "select qq_number from query_elc where qq_number = '%s'" % qq_number
    con = link()
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    con.close()
    if len(result) != 0:
        return True
    else:
        return False


def insert(qq_number, building, room, elc):
    today_time = str(datetime.datetime.now()).split('.')[0]
    today_time = datetime.datetime.strptime(today_time, '%Y-%m-%d %H:%M:%S')
    flag = 1
    if find_bd(qq_number):
        sql = "update query_elc set building = %d,room = %d,elc_now=%f,elc_now=%f,now_time='%s',pre_time='%s' where qq_number = '%s'" % (
        int(building), int(room), elc, elc, today_time, today_time,qq_number)
        flag = 2
    else:
        sql = "insert into query_elc values('%s',%d,%d,%f,%f,'%s','%s')" % (
        qq_number, int(building), int(room), elc, elc, today_time, today_time)
    con = link()
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        con.commit()
        res = "%s 绑定 %s 栋 %s 成功!" % (qq_number, building, room)
        print(res)
        con.close()
        return flag
    except Exception as e:
        print(e)
        con.rollback()
        con.close()
        return 0


def update(qq_number, building, room, elc, time):
    sql = "update query_elc set elc_pre = %f,pre_time = '%s' where qq_number = '%s' " % (elc, time, qq_number)
    con = link()
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        con.commit()
        res = "更新%s栋%s 成功\n" % (building, room)
        print(res)
        con.close()
        return 1
    except Exception as e:
        print(e)
        con.rollback()
        res = '更新失败，请重试！'
        con.close()
        return 0


def ser_by_qq(qq_number):
    today_time = str(datetime.datetime.now()).split('.')[0]
    today_time = datetime.datetime.strptime(today_time, '%Y-%m-%d %H:%M:%S')
    sql = "select building,room,elc_pre,pre_time from query_elc where qq_number = '%s'" % qq_number
    print(sql)
    con = link()
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        con.close()
        elc_pre = result[2]
        pre_time = result[3]
        days = '0'
        interval_time = str(today_time - pre_time).split(',')
        if len(interval_time) == 2:
            days = interval_time[0].replace(' days', '')
            days = days.replace(' day', '')
            tmp = datetime.datetime.strptime(interval_time[1].strip(), '%H:%M:%S')
            hours = str(tmp.hour)
            minutes = str(tmp.minute)
            seconds = str(tmp.second)
        else:
            tmp = datetime.datetime.strptime(interval_time[0].strip(), '%H:%M:%S')
            hours = str(tmp.hour)
            minutes = str(tmp.minute)
            seconds = str(tmp.second)
        elc = get_elc(str(result[0]), str(result[1]))[0]
        print(elc)
        print(elc_pre)
        update(qq_number, result[0], result[1], elc, today_time)
        res = {
            'room':result[1],
            'elc':str(elc),
            'remain_money':'{:.2f}'.format(elc * elc_unit_price),
            'days':days,
            'hour':hours,
            'minutes':minutes,
            'seconds':seconds,
            'used_elc':'{:.2f}'.format(elc_pre-elc),
            'used_money':'{:.2f}'.format((elc_pre-elc+0.000001) * elc_unit_price)
        }
        return res
    except Exception as e:
        print(e)
        res = None
        con.close()
        return res
