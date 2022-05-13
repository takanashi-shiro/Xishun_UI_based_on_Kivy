from .DB_user import link


def insert_jwxt(qq_number, cookie):
    sql = "insert into jwxt values('%s','%s')" % (cookie, qq_number)
    print(sql)
    con = link()
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        con.commit()
    except Exception as e:
        print(e)
        con.rollback()


def user_check(qq_number):
    try:
        sql = "select qq_number from jwxt where qq_number = '%s'" % qq_number
        con = link()
        cursor = con.cursor()
        cursor.execute(sql)
        result_QQ = cursor.fetchone()
        con.close()
        if result_QQ is None:
            return False
        else:
            return True
    except Exception as e:
        return -1

def get_cookie(qq_number):
    try:
        sql = "select cookie from jwxt where qq_number = '%s'" % qq_number
        con = link()
        cursor = con.cursor()
        cursor.execute(sql)
        cookie = cursor.fetchone()
        con.close()
        if cookie is None:
            return False
        else:
            return cookie[0]
    except Exception as e:
        return -1