import re

from kivy.uix.textinput import TextInput


class Username_TextInput(TextInput):

    def __init__(self, **kwargs):
        super(Username_TextInput, self).__init__(**kwargs)
        self.multiline = False

    def insert_text(self, substring, from_undo=False):
        pat = re.compile('[^0-9a-zA-Z\w]')
        s = re.sub(pat, '', substring)
        return super().insert_text(s, from_undo=from_undo)


class Passwd_TextInput(TextInput):
    def __init__(self, **kwargs):
        super(Passwd_TextInput, self).__init__(**kwargs)
        self.multiline = False
        self.password = True

    def insert_text(self, substring, from_undo=False):
        pat = re.compile('[^0-9a-zA-Z\w@#!~%$^&()*,./?<>{}]')
        s = re.sub(pat, '', substring)
        return super().insert_text(s, from_undo=from_undo)

class QQ_TextInput(TextInput):
    def __init__(self, **kwargs):
        super(QQ_TextInput, self).__init__(**kwargs)
        self.multiline = False

    def insert_text(self, substring, from_undo=False):
        pat = re.compile('[^0-9]')
        s = re.sub(pat, '', substring)
        return super().insert_text(s, from_undo=from_undo)
