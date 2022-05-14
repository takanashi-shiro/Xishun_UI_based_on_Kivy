import kivy
from kivy.graphics import Color, Rectangle

from database.DB_user import get_qq_number
from database.Elc_DB import find_bd
from database.jwxt_DB import user_check, get_cookie
from funcs.do_in_tmp import read_tmp
from funcs.kb.get_kb import get_kb
from funcs.kb.get_week import get_now_week, get_all_week
from funcs.kb.login import login
from widgets.Popup_item import MyPopup
from widgets.course_item import Course_Layout_Title, Course_Layout_Content
from widgets.elc_item import Elc_Info_Label, Elc_Layout
from .elc_screen import Elc_Screen

kivy.require('2.1.0')
from kivy.uix.tabbedpanel import *
from kivy.uix.screenmanager import Screen
from .course_screen import Course_Screen
from .main_screen import Main_Screen

kivy.resources.resource_add_path('font/')
ft = kivy.resources.resource_find('DroidSansFallback.ttf')


class My_TabbedPanelHeader(TabbedPanelHeader):
    def on_touch_down(self, touch):
        super(My_TabbedPanelHeader, self).on_touch_down(touch)


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
        username = read_tmp()
        th1 = TabbedPanelHeader(text='home')
        tp.add_widget(th1)
        th2 = TabbedPanelHeader(text='课表', font_name=ft)
        th1.content = Main_Screen()
        qq_number = get_qq_number(username)
        course_screen = Course_Screen(qq_number)



        def on_move_in2(instance):
            elc_screen.clear_widgets()
            course_screen.first_add()

        th2.bind(on_release=on_move_in2)
        def on_move_in1(instance):
            course_screen.clear_widgets()
        th1.bind(on_release=on_move_in1)
        th2.content = course_screen
        tp.add_widget(th2)
        th3 = TabbedPanelHeader(text='电费查询', font_name=ft)
        elc_screen = Elc_Screen()
        def on_move_in3(instance):
            course_screen.clear_widgets()
            elc_label = Elc_Info_Label()
            if find_bd(qq_number):
                elc_label.update_text(qq_number)
            elc_screen.add_widget(elc_label)
            elc_screen.add_widget(Elc_Layout())

        th3.bind(on_release=on_move_in3)
        th3.content = elc_screen
        tp.add_widget(th3)
        self.add_widget(tp)