import base64

from kivy.uix.relativelayout import RelativeLayout

from database.DB_user import get_qq_number
from database.jwxt_DB import insert_jwxt
from funcs.kb.login import login
from widgets.Popup_item import MyPopup
from widgets.button_item import MyButton
from widgets.label_item import MyLabel
from widgets.mythread import MyThread
from widgets.textinput_item import Passwd_TextInput, Username_TextInput


class Band_Kb_Screen(RelativeLayout):

    def __init__(self, username, **kwargs):
        super(Band_Kb_Screen, self).__init__(**kwargs)  # 这里要加super，才能把现有的新初始化方法覆盖掉继承来的旧初始化方法

        self.add_widget(MyLabel(
            # font_size = self.height * 0.4,
            text='绑定教务系统账号',
            size_hint=(.00, .08),
            color=[1, 1, 1, 1],
            pos_hint={'x': .5, 'y': .7},
        ))

        self.add_widget(MyLabel(
            text='教务系统账号',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .5},
            color=[0, .5, 1, 1],
        ))

        username_textinput = Username_TextInput(
            size_hint=(.60, .08),
            pos_hint={'x': .25, 'y': .5},
            hint_text='输入教务系统账号（学号）',
            # font_size=self.height * 0.3,
            write_tab=False
        )

        self.add_widget(username_textinput)

        self.add_widget(MyLabel(
            text='教务系统密码',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .35},
            color=[0, .5, 1, 1],
        ))

        passwd_textinput = Passwd_TextInput(
            size_hint=(.60, .08),
            pos_hint={'x': .25, 'y': .35},
            tab_width=0
        )
        self.add_widget(passwd_textinput)

        submit_button = MyButton(
            text='确定',
            size_hint=(.8, .1),
            pos_hint={'x': .1, 'y': .15},
        )

        def submit(instance):
            username_kb = username_textinput.text
            pwd_kb = passwd_textinput.text
            encode_username = base64.b64encode(username_kb.encode("utf-8")).decode('utf-8')
            encode_passwd = base64.b64encode(pwd_kb.encode("utf-8")).decode('utf-8')
            encode = encode_username + "%%%" + encode_passwd
            length = login(encode)[1]
            popup_text = '绑定成功'
            if 1300 < length < 30000:
                popup_text = '账号或密码错误，重试8'
            else:
                t = MyThread(insert_jwxt,(get_qq_number(username),encode))
                t.daemon = True
                t.start()
            popup = MyPopup(popup_text)
            popup.open()

        submit_button.bind(on_press=submit)
        self.add_widget(submit_button)