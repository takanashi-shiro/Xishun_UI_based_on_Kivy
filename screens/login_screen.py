import kivy

kivy.require('2.1.0')
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label  # 译者注：这里是从kivy.uix.label包中导入Label控件，这里都注意开头字母要大写
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout

kivy.resources.resource_add_path('font/')
ft = kivy.resources.resource_find('DroidSansFallback.ttf')


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

        self.add_widget(Label(
            text='喜顺',
            font_size=50,
            size_hint=(.00, .08),
            color=[0, .5, 1, 1],
            pos_hint={'x': .5, 'y': .8},
            font_name=ft
        ))
        self.add_widget(Label(
            text='可以摆烂的，不止于此',
            font_size=20,
            size_hint=(.00, .08),
            color=[0, 0, 0, .4],
            pos_hint={'x': .5, 'y': .7},
            font_name=ft
        ))

        self.add_widget(Label(
            text='用户名',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .5},
            color=[0, .5, 1, 1],
            font_name=ft
        )
        )
        self.username = TextInput(
            multiline=False,
            size_hint=(.60, .08),
            pos_hint={'x': .25, 'y': .5},
            hint_text='输入用户名/QQ号',
            font_size=self.height*0.3,
            write_tab=False,
            font_name=ft
        )
        self.add_widget(self.username)

        self.add_widget(Label(
            text='密码',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .35},
            color=[0, .5, 1, 1],
            font_name=ft
        )
        )
        self.passwd = TextInput(
            multiline=False,
            size_hint=(.60, .08),
            pos_hint={'x': .25, 'y': .35},
            font_size=self.height*0.3,
            password=True,
            tab_width=0
        )

        def submit(instance):
            username = self.username.text.split()
            passwd = self.passwd.text.split()
            if not username:
                username = self.username.text
            else:
                username = username[0]
            if not passwd:
                passwd = self.passwd.text
            else:
                passwd = passwd[0]
            print('The button <%s> is being pressed' % instance.text)
            print('username = %s\npassword = %s' % (username, passwd))
            if username == '1' and passwd == '1':
                self.manager.current = 'model'
            else:
                popup_layout = RelativeLayout(size=(500, 500))
                popup_layout.add_widget(
                    Label(text='用户名或密码错误', font_name=ft, size_hint=(0, 0), pos_hint={'x': .5, 'y': .8}))
                close_popup_button = Button(text='了解', font_name=ft, size_hint=(.3, .2), pos_hint={'x': .35, 'y': .3})
                popup_layout.add_widget(close_popup_button)
                popup = Popup(title='Error', content=popup_layout, size_hint=(.5, .5))
                popup.open()
                close_popup_button.bind(on_press=popup.dismiss)

        self.passwd.bind(on_text_validate=submit)
        self.add_widget(self.passwd)

        self.login_button = Button(
            text='登录',
            size_hint=(.8, .1),
            pos_hint={'x': .1, 'y': .15},
            font_name=ft
        )

        self.login_button.bind(on_press=submit)
        self.add_widget(self.login_button)

        self.forget_pwd = Label(
            text='[ref=forget_pwd]忘记密码[/ref]',
            size_hint=(.10, .08),
            pos_hint={'x': .25, 'y': .05},
            color=[0, 0, 0, .7],
            font_name=ft,
            markup=True
        )

        def press_forget_pwd(instance, value):
            print('The Label <%s> is being pressed' % value)
            self.manager.current = 'forget_pwd'
            self.manager.transition.direction = 'right'

        self.forget_pwd.bind(on_ref_press=press_forget_pwd)

        self.add_widget(self.forget_pwd)

        self.register = Label(
            text='[ref=register]注册用户[/ref]',
            size_hint=(.10, .08),
            pos_hint={'x': .65, 'y': .05},
            color=[0, 0, 0, .7],
            font_name=ft,
            markup=True
        )

        def press_register(instance, value):
            print('The Label <%s> is being pressed' % value)
            self.manager.current = 'register'

        self.register.bind(on_ref_press=press_register)
        self.add_widget(self.register)
