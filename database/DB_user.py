import mysql.connector
from .DB_config import SQL_config as config

def link():
    con = mysql.connector.connect(**config)
    return con

def login_check(username_or_qqNumber,pwd):
    sql = "select qq_number from UI_user where qq_number = '%s'" % username_or_qqNumber
    con = link()
    cursor = con.cursor(buffered=True)
    cursor.execute(sql)
    result_QQ = cursor.fetchone()
    con.close()
    sql = "select UI_username from UI_user where UI_username = '%s'" % username_or_qqNumber
    con = link()
    cursor = con.cursor(buffered=True)
    cursor.execute(sql)
    result_username = cursor.fetchone()
    con.close()
    flag_exist = (result_QQ is None or result_username is None)
    if not flag_exist:
        return False
    if result_QQ is not None:
        sql = "select UI_passwd from UI_user where qq_number = '%s'" % username_or_qqNumber
        con = link()
        cursor = con.cursor(buffered=True)
        cursor.execute(sql)
        result_pwd = cursor.fetchone()
        con.close()
    else:
        sql = "select UI_passwd from UI_user where UI_username = '%s'" % username_or_qqNumber
        con = link()
        cursor = con.cursor(buffered=True)
        cursor.execute(sql)
        result_pwd = cursor.fetchone()
        con.close()
    if result_pwd == pwd:
        return True
    else:
        return False
