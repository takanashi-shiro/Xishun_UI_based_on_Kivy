import kivy
from kivy.graphics import Color, Rectangle

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
        th1 = TabbedPanelHeader(text='home')
        tp.add_widget(th1)
        th3 = TabbedPanelHeader(text='课表', font_name=ft)
        th1.content = Main_Screen()
        th3.content = Course_Screen()
        def on_move_in(instance):
            print("moved in %s" % instance.text)
        th3.bind(on_release=on_move_in)
        tp.add_widget(th3)
        self.add_widget(tp)