import kivy
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

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

    def __init__(self, **kwargs):
        super(Main_Screen, self).__init__(**kwargs)
        self.rows = 2

        Home_Title = (Label(
            text="喜顺's Home",
            font_size=50, size_hint=(.5, .5),
            color=[0, .5, 1, 1],
            pos_hint={'right':0.5, 'top': 0.5},
            font_name=ft
        ))
        self.add_widget(Home_Title)

        buttons_layout = Buttons_Layout()
        buttons_layout.bind(size=buttons_layout._update_rect, pos=buttons_layout._update_rect)
        with buttons_layout.canvas.before:
            Color(1, 1, 1, 1)
            buttons_layout.rect = Rectangle(size=buttons_layout.size, pos=buttons_layout.pos)
        btn1 = Button(
            text ='绑定课表信息',
            size_hint=[.2,.2],
            font_name=ft
        )
        buttons_layout.add_widget(btn1)
        btn2 = Button(
            text='绑定电费信息',
            size_hint=[.2,.2],
            font_name=ft
        )
        buttons_layout.add_widget(btn2)
        btn3 = Button(
            text='修改密码',
            size_hint=[.2,.2],
            font_name=ft
        )
        buttons_layout.add_widget(btn3)
        self.add_widget(buttons_layout)