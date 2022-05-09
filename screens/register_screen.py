import kivy
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from widgets.register_item import Username_TextInput, Passwd_TextInput, QQ_TextInput

kivy.resources.resource_add_path('font/')
ft = kivy.resources.resource_find('DroidSansFallback.ttf')


class Register_Screen(Screen):

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def __init__(self, **kwargs):
        super(Register_Screen, self).__init__(**kwargs)
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
            pos_hint={'x': .08, 'y': .65},
            color=[0, .5, 1, 1],
            font_name=ft
        )
        )
        username = Username_TextInput(
            size_hint=(.60, .08),
            pos_hint={'x': .2, 'y': .65},
            font_size=txt_size - 10,
        )

        self.add_widget(username)

        self.add_widget(Label(
            text='密码',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .5},
            color=[0, .5, 1, 1],
            font_name=ft
        )
        )
        passwd = Passwd_TextInput(
            size_hint=(.60, .08),
            pos_hint={'x': .2, 'y': .5},
            font_size=txt_size - 10,

        )
        self.add_widget(passwd)

        self.add_widget(Label(
            text='QQ',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .35},
            color=[0, .5, 1, 1],
            font_name=ft
        )
        )
        QQ = QQ_TextInput(
            size_hint=(.60, .08),
            pos_hint={'x': .2, 'y': .35},
            font_size=txt_size - 10,
        )
        self.add_widget(QQ)

        register_button = Button(
            text='注册',
            size_hint=(.6, .1),
            # pos_hint={'x': .15, 'y': .15},
            pos_hint={'x':.2,'y':.05},
            font_name=ft
        )

        return_button2 = Button(
            text='<',
            font_size=20,
            size_hint=(.1,.1),
            pos_hint={'x':0,'y':.9},
            color=[0,0,0,1],
            background_color=[1,1,1,.05]
        )
        def on_press_return(instance):
            print('The button [%s] is being pressed' % instance.text)
            self.manager.current = 'login'
            self.manager.transition.direction = 'right'
        return_button2.bind(on_press=on_press_return)
        def on_press_register(instance):
            print('The button [%s] is being pressed' % instance.text)
        register_button.bind(on_press=on_press_register)
        self.add_widget(return_button2)
        self.add_widget(register_button)

        self.add_widget(Label(
            text='验证码',
            # 新密码
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .2},
            color=[0, .5, 1, 1],
            font_name=ft
        ))
        captcha = TextInput(
            multiline=False,
            size_hint=(.30, .08),
            font_size=txt_size - 10,
            pos_hint={'x': .2, 'y': .2}
        )
        self.add_widget(captcha)

        captcha_button = Button(
            size_hint=(.25, .08),
            pos_hint={'x': .55, 'y': .2},
            text='获取验证码',
            font_name=ft,
            disabled_color=[0, 0, 0, .6]
        )

        self.nowsecond = 60

        def on_press_captcha_button(instance):
            print('The button [%s] is being pressed' % instance.text)
            instance.disabled = True
            change_captcha_button(instance)
            event1 = Clock.schedule_interval(lambda dt: change_captcha_button(instance), 1)
            # 用sleep会崩溃，要用kivy的clock
            Clock.schedule_once(lambda dt: captcha_clock_cancel(event1, instance), 61)

        def captcha_clock_cancel(event, instance):
            event.cancel()
            instance.disabled = False
            instance.text = '获取验证码'
            self.nowsecond = 60

        def change_captcha_button(instance):
            instance.text = '已发送,请等待%d秒后重试' % self.nowsecond
            self.nowsecond -= 1

        captcha_button.bind(on_press=on_press_captcha_button)
        self.add_widget(captcha_button)
