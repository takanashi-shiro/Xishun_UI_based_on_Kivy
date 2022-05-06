import kivy

kivy.require('2.1.0')
from kivy.uix.tabbedpanel import *
from kivy.uix.screenmanager import Screen
from .login_screen import Login_Screen
from .course_screen import Course_Screen


kivy.resources.resource_add_path('font/')
ft = kivy.resources.resource_find('DroidSansFallback.ttf')


class My_TabbedPanelHeader(TabbedPanelHeader):
    def on_touch_down(self,touch):
        super(My_TabbedPanelHeader, self).on_touch_down(touch)


class Model_Screen(Screen):
    def __init__(self, **kwargs):
        super(Model_Screen, self).__init__(**kwargs)  # 这里要加super，才能把现有的新初始化方法覆盖掉继承来的旧初始化方法
        x_size, y_size = 900, 1600
        self.size = (x_size, y_size)
        txt_size = y_size / 10 + 5
        self.rows = 1
        tp = TabbedPanel(
            tab_pos='top_left',
            background_color=[10, 10, 10, 10],
            do_default_tab=False,
            tab_height = 40,
        )

        th1 = TabbedPanelHeader(text='home')
        # th1.content = Label(text = 'th1',color = [0,0,0,1])
        th1.content = Login_Screen()
        tp.add_widget(th1)
        # th2 = TabbedPanelHeader(text='about')
        # th2.content = Label(text = 'th2',color = [0,0,0,1])
        # tp.add_widget(th2)

        th3 = TabbedPanelHeader(text='课表',font_name = ft)
        th3.content = Course_Screen()
        tp.add_widget(th3)
        self.add_widget(tp)

