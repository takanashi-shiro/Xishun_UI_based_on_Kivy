import kivy
from kivy.graphics import Color, Rectangle

from database.DB_user import get_qq_number
from database.Elc_DB import find_bd
from funcs.do_in_tmp import read_tmp
from widgets.elc_item import Elc_Info_Label, Elc_Layout
from widgets.label_item import MyLabel
from widgets.user import User
from .elc_screen import Elc_Screen
from .home_screen import Home_Screen

kivy.require('2.1.0')
from kivy.uix.tabbedpanel import *
from kivy.uix.screenmanager import Screen
from .course_screen import Course_Screen
from .main_screen import Main_Screen

kivy.resources.resource_add_path('font/')
ft = kivy.resources.resource_find('DroidSansFallback.ttf')

class Model_Screen(Screen):
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def __init__(self, **kwargs):
        super(Model_Screen, self).__init__(**kwargs)  # 这里要加super，才能把现有的新初始化方法覆盖掉继承来的旧初始化方法
        self.rows = 1
        self.bind(size=self._update_rect, pos=self._update_rect)
        with self.canvas.before:
            Color(1, 1, 1, .95)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        tp = TabbedPanel(
            tab_pos='top_left',
            background_color=[10, 10, 10, 10],
            do_default_tab=False,
            tab_height=40,
        )
        th = TabbedPanelHeader(text='主页',font_name=ft)
        home_screen = Home_Screen()
        home_screen.add_items()
        th.content = home_screen
        tp.add_widget(th)
        def on_enter(instance):
            self.username = str(read_tmp().split()[0])
            qq_number = get_qq_number(self.username)
            user = User(username=self.username, qq_number=qq_number)
            course_screen = Course_Screen(user)
            th1 = TabbedPanelHeader(text='个人中心',font_name=ft)
            th1.content = Main_Screen(user, self)
            tp.add_widget(th1)
            th2 = TabbedPanelHeader(text='课表', font_name=ft)
            def on_move_in0(instance):
                course_screen.clear_widgets()
                elc_screen.clear_widgets()
                home_screen.add_items()

            th.bind(on_release=on_move_in0)
            def on_move_in1(instance):
                course_screen.clear_widgets()
                elc_screen.clear_widgets()
                home_screen.clear_widgets()

            th1.bind(on_release=on_move_in1)

            def on_move_in2(instance):
                elc_screen.clear_widgets()
                course_screen.first_add(user)
                home_screen.clear_widgets()

            th2.bind(on_release=on_move_in2)

            th2.content = course_screen
            tp.add_widget(th2)
            th3 = TabbedPanelHeader(text='电费查询', font_name=ft)
            elc_screen = Elc_Screen()

            def on_move_in3(instance):
                course_screen.clear_widgets()
                home_screen.clear_widgets()
                elc_label = Elc_Info_Label()
                if find_bd(qq_number):
                    elc_label.update_text(qq_number)
                elc_screen.add_widget(elc_label)
                elc_screen.add_widget(Elc_Layout())

            th3.bind(on_release=on_move_in3)
            th3.content = elc_screen
            tp.add_widget(th3)
            self.add_widget(tp)

        self.bind(on_enter=on_enter)

    def update_username(self,username):
        self.username = username