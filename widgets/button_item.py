import kivy
from kivy.uix.button import Button
kivy.resources.resource_add_path('font/')
ft = kivy.resources.resource_find('DroidSansFallback.ttf')

class MyButton(Button):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.font_name = ft

class Return_Button(Button):
    def __init__(self, **kwargs):
        super(Return_Button, self).__init__(**kwargs)
        self.text = '<'
        self.font_size = self.height * 0.2
        self.size_hint = (.1, .1)
        self.pos_hint = {'x': 0, 'y': .9}
        self.color = [0, 0, 0, 1]
        self.background_color = [1, 1, 1, .05]

