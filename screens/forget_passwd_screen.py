import kivy
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput

kivy.resources.resource_add_path('../font/')
ft = kivy.resources.resource_find('DroidSansFallback.ttf')


class Forget_Pwd_Screen(Screen):
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def __init__(self, **kwargs):
        super(Forget_Pwd_Screen, self).__init__(**kwargs)
        x_size, y_size = 900, 1600
        # self.size_hint = ( None , None )
        self.size = (x_size, y_size)
        txt_size = y_size / 50

        self.bind(size=self._update_rect, pos=self._update_rect)
        with self.canvas.before:
            Color(1, 1, 1, .95)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.add_widget(Label(
            text='喜顺',
            font_size=50,
            size_hint=(.00, .08),
            color=[0, .5, 1, 1],
            pos_hint={'x': .5, 'y': .85},
            font_name=ft
        ))
        self.add_widget(Label(
            text='不管卷成什么样，你随时可以选择摆烂',
            font_size=20,
            size_hint=(.00, .08),
            color=[0, 0, 0, .4],
            pos_hint={'x': .5, 'y': .75},
            font_name=ft
        ))
        self.add_widget(Label(
            text='用户名',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .6},
            color=[0, .5, 1, 1],
            font_name=ft
        )
        )
        username = TextInput(
            multiline=False,
            size_hint=(.60, .08),
            pos_hint={'x': .2, 'y': .6},
            # text='1',
            font_size=txt_size - 10
        )
        self.add_widget(username)

        self.add_widget(Label(
            text='QQ',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .3},
            color=[0, .5, 1, 1],
        )
        )
        QQ = TextInput(
            multiline=False,
            size_hint=(.60, .08),
            pos_hint={'x': .2, 'y': .3},
            font_size=txt_size - 10,
            password=True
        )
        self.add_widget(QQ)

        self.add_widget(Label(
            text='新密码',
            # 新密码
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .45},
            color=[0, .5, 1, 1],
            font_name=ft
        )
        )
        newpasswd = TextInput(
            multiline=False,
            size_hint=(.60, .08),
            pos_hint={'x': .2, 'y': .45},
            font_size=txt_size - 10,
            password=True
        )
        self.add_widget(newpasswd)

        reset_button = Button(
            text='重设密码',
            # 重新设置密码
            size_hint=(.5, .1),
            pos_hint={'x': .25, 'y': .15},
            font_name=ft
        )
        self.add_widget(reset_button)
        self.cols = 2
