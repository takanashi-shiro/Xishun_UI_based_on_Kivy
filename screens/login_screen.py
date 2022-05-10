from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout

from widgets.Popup_item import MyPopup
from widgets.button_item import MyButton
from widgets.do_in_tmp import write_in_tmp
from widgets.label_item import MyLabel
from database.DB_user import login_check, get_username
from widgets.textinput_item import Username_TextInput,Passwd_TextInput


class Login_Screen(Screen):

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def __init__(self, **kwargs):
        super(Login_Screen, self).__init__(**kwargs)  # 这里要加super，才能把现有的新初始化方法覆盖掉继承来的旧初始化方法
        self.bind(size=self._update_rect, pos=self._update_rect)
        with self.canvas.before:
            Color(1, 1, 1, .95)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.add_widget(MyLabel(
            text='喜顺',
            font_size=50,
            size_hint=(.00, .08),
            color=[0, .5, 1, 1],
            pos_hint={'x': .5, 'y': .8},
        ))
        self.add_widget(MyLabel(
            text='可以摆烂的，不止于此',
            font_size=20,
            size_hint=(.00, .08),
            color=[0, 0, 0, .4],
            pos_hint={'x': .5, 'y': .7},
        ))

        self.add_widget(MyLabel(
            text='用户名',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .5},
            color=[0, .5, 1, 1],
        ))
        username_textinput = Username_TextInput(
            size_hint=(.60, .08),
            pos_hint={'x': .25, 'y': .5},
            hint_text='输入用户名/QQ号',
            font_size=self.height*0.3,
            write_tab=False
        )
        self.add_widget(username_textinput)

        self.add_widget(MyLabel(
            text='密码',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .35},
            color=[0, .5, 1, 1],
        ))
        passwd_textinput = Passwd_TextInput(
            size_hint=(.60, .08),
            pos_hint={'x': .25, 'y': .35},
            font_size=self.height*0.3,
            tab_width=0
        )

        def submit(instance):
            username = username_textinput.text.split()
            passwd = passwd_textinput.text.split()
            if not username:
                username = username_textinput.text
            else:
                username = username[0]
            if not passwd:
                passwd = passwd_textinput.text
            else:
                passwd = passwd[0]
            print('The button <%s> is being pressed' % instance.text)
            print('username = %s\npassword = %s' % (username, passwd))
            status = login_check(username,passwd)
            if status == 1 or status == 2:
                if status == 1:
                    write_in_tmp(username)
                else:
                    write_in_tmp(get_username(username))
                self.manager.current = 'model'
            else:
                popup_text = '用户名或密码错误'
                if status == -1:
                    popup_text = '服务器开小差了~稍后试试吧'
                popup=MyPopup(popup_text)
                popup.open()
                # close_popup_button.bind(on_press=popup.dismiss)

        passwd_textinput.bind(on_text_validate=submit)
        self.add_widget(passwd_textinput)

        self.login_button = MyButton(
            text='登录',
            size_hint=(.8, .1),
            pos_hint={'x': .1, 'y': .15},
        )

        self.login_button.bind(on_press=submit)
        self.add_widget(self.login_button)

        self.forget_pwd = MyLabel(
            text='[ref=forget_pwd]忘记密码[/ref]',
            size_hint=(.10, .08),
            pos_hint={'x': .25, 'y': .05},
            color=[0, 0, 0, .7],
            markup=True
        )

        def press_forget_pwd(instance, value):
            print('The Label <%s> is being pressed' % value)
            self.manager.current = 'forget_pwd'
            self.manager.transition.direction = 'right'

        self.forget_pwd.bind(on_ref_press=press_forget_pwd)

        self.add_widget(self.forget_pwd)

        self.register = MyLabel(
            text='[ref=register]注册用户[/ref]',
            size_hint=(.10, .08),
            pos_hint={'x': .65, 'y': .05},
            color=[0, 0, 0, .7],
            markup=True
        )

        def press_register(instance, value):
            print('The Label <%s> is being pressed' % value)
            self.manager.current = 'register'

        self.register.bind(on_ref_press=press_register)
        self.add_widget(self.register)
