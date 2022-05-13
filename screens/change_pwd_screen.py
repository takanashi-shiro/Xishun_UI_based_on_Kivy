from kivy.uix.relativelayout import RelativeLayout

from database.DB_user import update_pwd, get_passwd
from widgets.Popup_item import MyPopup
from widgets.button_item import MyButton
from widgets.label_item import MyLabel
from widgets.textinput_item import Passwd_TextInput


class Change_Pwd_Screen(RelativeLayout):

    def __init__(self, username, **kwargs):
        super(Change_Pwd_Screen, self).__init__(**kwargs)  # 这里要加super，才能把现有的新初始化方法覆盖掉继承来的旧初始化方法

        self.add_widget(MyLabel(
            # font_size = self.height * 0.4,
            text='修改密码',
            size_hint=(.00, .08),
            color=[1, 1, 1, 1],
            pos_hint={'x': .5, 'y': .7},
        ))

        self.add_widget(MyLabel(
            text='原密码',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .5},
            color=[0, .5, 1, 1],
        ))

        passwd_textinput = Passwd_TextInput(
            size_hint=(.60, .08),
            pos_hint={'x': .25, 'y': .5},
            hint_text='输入原密码',
            # font_size=self.height * 0.3,
            write_tab=False
        )

        self.add_widget(passwd_textinput)

        self.add_widget(MyLabel(
            text='新密码',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .35},
            color=[0, .5, 1, 1],
        ))

        new_passwd_textinput = Passwd_TextInput(
            size_hint=(.60, .08),
            pos_hint={'x': .25, 'y': .35},
            # font_size=self.height * 0.3,
            tab_width=0
        )
        self.add_widget(new_passwd_textinput)

        def submit(instance):
            passwd = passwd_textinput.text
            new_passwd = new_passwd_textinput.text
            print('The button <%s> is being pressed' % instance.text)
            if passwd != get_passwd(username):
                popup_text = '原密码错误'
                popup_change_pwd_child = MyPopup(popup_text)
                popup_change_pwd_child.open()
            elif not 6 <= len(new_passwd) <= 18:
                popup_text = '密码长度应在6~18位'
                popup_change_pwd_child = MyPopup(popup_text)
                popup_change_pwd_child.open()
            else:
                flag = update_pwd(username=username, new_pwd=new_passwd)
                if flag != 1:
                    popup_change_pwd_child = MyPopup('服务器开小差了，稍后试试8')
                    popup_change_pwd_child.open()
                else:
                    popup_change_pwd_child = MyPopup('修改密码成功！')
                    popup_change_pwd_child.open()

        passwd_textinput.bind(on_text_validate=submit)

        yes_button = MyButton(
            text='确定',
            size_hint=(.8, .1),
            pos_hint={'x': .1, 'y': .15},
        )

        yes_button.bind(on_press=submit)
        self.add_widget(yes_button)
