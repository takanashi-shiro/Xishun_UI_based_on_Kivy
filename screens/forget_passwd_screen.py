from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput

from database.DB_user import update_pwd, username_check, get_username
from widgets.Popup_item import MyPopup_Remind, MyPopup
from widgets.button_item import Return_Button, MyButton
from widgets.captcha_create import Captcha_Create
from widgets.label_item import MyLabel
from widgets.mythread import MyThread
from widgets.send_mail import Send_Msg
from widgets.textinput_item import Username_TextInput, Passwd_TextInput, QQ_TextInput


class Forget_Pwd_Screen(Screen):
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def __init__(self, **kwargs):
        super(Forget_Pwd_Screen, self).__init__(**kwargs)

        self.bind(size=self._update_rect, pos=self._update_rect)
        with self.canvas.before:
            Color(1, 1, 1, .95)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.add_widget(MyLabel(
            text='喜顺',
            font_size=50,
            size_hint=(.00, .08),
            color=[0, .5, 1, 1],
            pos_hint={'x': .5, 'y': .85},
        ))
        self.add_widget(MyLabel(
            text='卷到失去了摆烂的记忆，我们帮你找回',
            font_size=20,
            size_hint=(.00, .08),
            color=[0, 0, 0, .4],
            pos_hint={'x': .5, 'y': .75},
        ))
        self.add_widget(MyLabel(
            text='用户名',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .65},
            color=[0, .5, 1, 1],
        )
        )
        username = Username_TextInput(
            size_hint=(.60, .08),
            pos_hint={'x': .2, 'y': .65},
        )
        self.add_widget(username)

        self.add_widget(MyLabel(
            text='新密码',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .5},
            color=[0, .5, 1, 1],
        )
        )
        newpasswd = Passwd_TextInput(
            size_hint=(.60, .08),
            pos_hint={'x': .2, 'y': .5},
        )
        self.add_widget(newpasswd)

        self.add_widget(MyLabel(
            text='QQ',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .35},
            color=[0, .5, 1, 1],
        ))
        QQ = QQ_TextInput(
            size_hint=(.60, .08),
            pos_hint={'x': .2, 'y': .35},
        )
        self.add_widget(QQ)

        self.add_widget(MyLabel(
            text='验证码',
            # 新密码
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .2},
            color=[0, .5, 1, 1],
        )
        )
        captcha = Username_TextInput(
            size_hint=(.30, .08),
            pos_hint={'x': .2, 'y': .2}
        )
        self.add_widget(captcha)

        captcha_button = MyButton(
            size_hint=(.25, .08),
            pos_hint={'x': .55, 'y': .2},
            text='获取验证码',
            disabled_color=[0, 0, 0, .6]
        )

        self.nowsecond = 60
        self.captcha_str = ''
        def on_press_captcha_button(instance):
            print('The button [%s] is being pressed' % instance.text)
            if 5 < len(QQ.text) < 13:
                self.captcha_str = Captcha_Create()
                instance.disabled = True
                change_captcha_button(instance)
                event1 = Clock.schedule_interval(lambda dt: change_captcha_button(instance), 1)
                # 用sleep会崩溃，要用kivy的clock
                Clock.schedule_once(lambda dt: captcha_clock_cancel(event1, instance), 61)
                popup = MyPopup_Remind('验证码已发送~')
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 2)
                t = MyThread(Send_Msg, ([QQ.text + "@qq.com"], '喜顺Bot的验证码来咯', self.captcha_str))
                t.daemon = True
                t.start()
            else:
                popup = MyPopup('输入的QQ号不合法，重新输入吧')
                popup.open()

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

        reset_button = MyButton(
            text='重设密码',
            size_hint=(.5, .1),
            pos_hint={'x': .25, 'y': .05},
        )

        def on_press_reset(instance):
            print('The button [%s] is being pressed' % instance.text)
            popup_text='密码重设成功,请返回登录8'
            if not 5 <= len(username.text) <= 15:
                popup_text='用户名长度应在5~15位'
            elif not username_check(username.text):
                popup_text='用户名不存在'
            elif not username.text == get_username(QQ.text):
                popup_text='用户名和QQ不匹配'
            elif not 6 <= len(newpasswd.text) <= 18:
                popup_text = '密码长度应在6~18位'
            elif not (self.captcha_str == captcha.text):
                popup_text = '验证码不正确'
            popup_register = MyPopup(popup_text)
            if popup_text == '密码重设成功,请返回登录8':
                popup_register.title_size = 0
                print(username.text,newpasswd.text,QQ.text)
                t = MyThread(update_pwd,(username.text,newpasswd.text,QQ.text))
                t.daemon = True
                t.start()
            popup_register.open()
            self.manager.current= 'login'
            self.manager.transition.direction = 'right'

        reset_button.bind(on_press=on_press_reset)
        self.add_widget(reset_button)
        return_button = Return_Button()

        def on_press_return(instance):
            print('The button [%s] is being pressed' % instance.text)
            self.manager.current = 'login'
            self.manager.transition.direction = 'left'

        return_button.bind(on_press=on_press_return)
        self.add_widget(return_button)
