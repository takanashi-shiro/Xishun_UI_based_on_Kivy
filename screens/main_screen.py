import kivy
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

from screens.band_elc_screen import Band_Elc_Screen
from screens.band_kb_screen import Band_Kb_Screen
from screens.change_pwd_screen import Change_Pwd_Screen
from funcs.do_in_tmp import read_tmp, clean_tmp
from widgets.button_item import MyButton
from widgets.label_item import MyLabel

kivy.resources.resource_add_path('font/')
ft = kivy.resources.resource_find('DroidSansFallback.ttf')

class Buttons_Layout(GridLayout):

    def __init__(self, **kwargs):
        super(Buttons_Layout, self).__init__(**kwargs)
        self.rows = 3
        self.padding = [150,60]
        self.spacing = [10,0]

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class Main_Screen(GridLayout):
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def __init__(self,user,model, **kwargs):
        super(Main_Screen, self).__init__(**kwargs)
        self.rows = 2
        Home_Title = (MyLabel(
            text="个人中心",
            font_size=50, size_hint=(.5, .5),
            color=[0, .5, 1, 1],
            pos_hint={'right':0.5, 'top': 0.5},
        ))
        self.add_widget(Home_Title)

        buttons_layout = Buttons_Layout()
        buttons_layout.bind(size=buttons_layout._update_rect, pos=buttons_layout._update_rect)
        with buttons_layout.canvas.before:
            Color(1, 1, 1, 1)
            buttons_layout.rect = Rectangle(size=buttons_layout.size, pos=buttons_layout.pos)
        btn1 = MyButton(
            text ='绑定课表信息',
            size_hint=[.2,.2]
        )
        username = user.get_username()
        def press_band_kb(instance):
            print('The button <%s> is being pressed' % instance.text)
            print(username)
            popup_band_kb = Popup()
            popup_band_kb.content = Band_Kb_Screen(user)
            popup_band_kb.title = 'Band_KB'
            popup_band_kb.font_name = ft
            popup_band_kb.size_hint = (.8, .8)
            popup_band_kb.open()


        btn1.bind(on_press=press_band_kb)
        buttons_layout.add_widget(btn1)
        btn2 = MyButton(
            text='绑定电费信息',
            size_hint=[.2,.2]
        )
        def press_band_elc(instance):
            print('The button <%s> is being pressed' % instance.text)
            print(username)
            popup_band_elc = Popup()
            popup_band_elc.content = Band_Elc_Screen(user)
            popup_band_elc.title = 'Band_Elc'
            popup_band_elc.font_name = ft
            popup_band_elc.size_hint = (.8, .8)
            popup_band_elc.open()
        btn2.bind(on_press=press_band_elc)
        buttons_layout.add_widget(btn2)
        btn3 = MyButton(
            text='修改密码',
            size_hint=[.2,.2]
        )
        def press_change_pwd(instance):
            print('The button <%s> is being pressed' % instance.text)
            username = str(read_tmp().split()[0])
            print(username)
            popup_change_pwd = Popup()
            popup_change_pwd.content = Change_Pwd_Screen(username=username)
            popup_change_pwd.title = 'Change_Password'
            popup_change_pwd.font_name = ft
            popup_change_pwd.size_hint = (.5, .8)
            popup_change_pwd.open()
        btn3.bind(on_press=press_change_pwd)
        buttons_layout.add_widget(btn3)
        btn4 = MyButton(text='退出登录',size_hint=(.2,.2))
        def press_exit(instance):
            clean_tmp()
            model.manager.current = 'login'
        btn4.bind(on_press=press_exit)
        buttons_layout.add_widget(btn4)
        self.add_widget(buttons_layout)