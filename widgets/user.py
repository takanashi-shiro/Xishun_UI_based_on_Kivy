import base64

from database.DB_user import get_qq_number


class User:

    def __init__(self, username='', qq_number='', **kwargs):
        self.username = username
        if qq_number != '':
            self.qq_number = qq_number
        else:
            self.qq_number = get_qq_number(username)
        self.encode = ''
        self.room_id= ''
        self.class_ls = None

    def get_username(self):
        return self.username
    def get_qq_number(self):
        return self.qq_number
    def get_encode(self):
        return self.encode
    def set_encode(self,username_kb='',pwd_kb='',encode = ''):
        if encode != '':
            self.encode = encode
            return
        encode_username = base64.b64encode(username_kb.encode("utf-8")).decode('utf-8')
        encode_passwd = base64.b64encode(pwd_kb.encode("utf-8")).decode('utf-8')
        self.encode = encode_username + "%%%" + encode_passwd
    def get_room_id(self):
        return self.room_id
    def set_room_id(self,room_id):
        self.room_id = room_id
    def get_class_ls(self):
        return self.class_ls
    def set_class_ls(self,class_ls):
        self.class_ls = class_ls