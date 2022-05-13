import kivy
from kivy.graphics import Color, Rectangle

from widgets.course_item import Layout_Title, Layout_Content

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
        th2 = TabbedPanelHeader(text='课表', font_name=ft)
        th1.content = Main_Screen()
        course_screen = Course_Screen()
        def on_move_in2(instance):
            course_layout_title = Layout_Title(size_hint=[1, .05])
            course_screen.add_widget(course_layout_title)
            layout_content = Layout_Content(size_hint=[1, .95])
            layout_content.add_items()
            course_screen.add_widget(layout_content)
        th2.bind(on_release=on_move_in2)
        def on_move_in1(instance):
            course_screen.clear_widgets()
        th1.bind(on_release=on_move_in1)
        th2.content = course_screen
        tp.add_widget(th2)
        self.add_widget(tp)