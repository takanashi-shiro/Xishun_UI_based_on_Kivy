import pymysql

from config import SQL_config as config


def link():
    con = pymysql.connect(**config)
    return con


def qq_check(qq_number):
    try:
        sql = "select qq_number from UI_user where qq_number = '%s'" % qq_number
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
        print(e)
        return -1


def username_check(username):
    try:
        sql = "select UI_username from UI_user where UI_username = '%s'" % username
        con = link()
        cursor = con.cursor()
        cursor.execute(sql)
        result_username = cursor.fetchone()
        con.close()
        if result_username is None:
            return False
        else:
            return True
    except Exception as e:
        return -1


def get_username(qq_number):
    try:
        sql = "select UI_username from UI_user where qq_number = '%s'" % qq_number
        con = link()
        cursor = con.cursor()
        cursor.execute(sql)
        username = cursor.fetchone()
        con.close()
        if username is None:
            return None
        else:
            return username[0]
    except Exception as e:
        print(e)
        return -1


def get_qq_number(username):
    try:
        sql = "select qq_number from UI_user where UI_username = '%s'" % username
        con = link()
        cursor = con.cursor()
        cursor.execute(sql)
        qq_number = cursor.fetchone()
        con.close()
        if qq_number is None:
            return None
        else:
            return qq_number[0]
    except Exception as e:
        print(e)
        return -1


def get_passwd(UI_username):
    try:
        sql = "select UI_passwd from UI_user where UI_username = '%s'" % UI_username
        con = link()
        cursor = con.cursor()
        cursor.execute(sql)
        passwd = cursor.fetchone()
        con.close()
        if passwd is None:
            return None
        else:
            return passwd[0]
    except Exception as e:
        print(e)
        return -1


def login_check(username_or_qqNumber, pwd):
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
            cursor = con.cursor()
            cursor.execute(sql)
            result_pwd = cursor.fetchone()
            con.close()
        else:
            sql = "select UI_passwd from UI_user where UI_username = '%s'" % username_or_qqNumber
            con = link()
            cursor = con.cursor()
            cursor.execute(sql)
            result_pwd = cursor.fetchone()
            print(result_pwd)
            con.close()
        if result_pwd[0] == pwd:
            if result_QQ:
                return 2
            else:
                return 1
        else:
            return 0
    except Exception as e:
        print(e)
        return -1, username_or_qqNumber


def update_pwd(username, new_pwd, qq_number=None):
    try:
        if qq_number == None:
            sql = "update UI_user set UI_passwd = '%s' where UI_username = '%s'" % (new_pwd, username)
        else:
            sql = "update UI_user set UI_passwd = '%s' where UI_username = '%s' and qq_number = '%s'" % (new_pwd, username,qq_number)
        con = link()
        cursor = con.cursor()
        cursor.execute(sql)
        try:
            con.commit()
            return 1
        except Exception as e:
            con.rollback()
            return 0
    except Exception as e:
        return -1


def insert_user(username, pwd, qq_number):
    sql = "insert into UI_user values('%s','%s','%s')" % (username, pwd, qq_number)
    con = link()
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        con.commit()
    except Exception as e:
        print(e)
        con.rollback()