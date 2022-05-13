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