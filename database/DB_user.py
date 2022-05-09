import mysql.connector
from config import SQL_config as config

def link():
    con = mysql.connector.connect(**config)
    return con

def qq_check(qq_number):
    try:
        sql = "select qq_number from UI_user where qq_number = '%s'" % qq_number
        con = link()
        cursor = con.cursor(buffered=True)
        cursor.execute(sql)
        result_QQ = cursor.fetchone()
        con.close()
        if result_QQ is None:
            return False
        else:
            return True
    except Exception as e:
        return -1

def username_check(username):
    try:
        sql = "select UI_username from UI_user where UI_username = '%s'" % username
        con = link()
        cursor = con.cursor(buffered=True)
        cursor.execute(sql)
        result_username = cursor.fetchone()
        con.close()
        if result_username is None:
            return False
        else:
            return True
    except Exception as e:
        return -1


def login_check(username_or_qqNumber,pwd):
    try:
        result_QQ = qq_check(username_or_qqNumber)
        result_username = username_check(username_or_qqNumber)
        if result_QQ == -1 or result_username == -1:
            return -1
        flag_exist = result_QQ or result_username
        if not flag_exist:
            return 0
        if result_QQ:
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
            return 1
        else:
            return 0
    except Exception as e:
        return -1

