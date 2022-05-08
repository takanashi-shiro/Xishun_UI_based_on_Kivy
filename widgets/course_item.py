import kivy
from kivy.properties import ReferenceListProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
kivy.resources.resource_add_path('../font/')
ft = kivy.resources.resource_find('DroidSansFallback.ttf')


class Course_Class_Item(Button):

    def __init__(self, **kwargs):
        super(Course_Class_Item, self).__init__(**kwargs)
        self.background_normal="''"
        self.background_color = [1, 1, 1, .6]
        self.color = [0,0,0,1]
        self.disabled_color = [0,0,0,1]
        self.size_hint = [.3, .2]
        self.font_name = ft
        self.padding = [3,3]


class Course_Info_Item(Label):

    def __init__(self, **kwargs):
        super(Course_Info_Item, self).__init__(**kwargs)
        self.size_hint = [.3, .1]
        self.color = [1,1,1,1]
        self.font_name = ft
        self.bold = True
        self.outline_color = [0, 0, 0,1]

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = (instance.width,instance.height)

class Course_Drop_List(Button):
    def __init__(self, **kwargs):
        super(Course_Drop_List, self).__init__(**kwargs)
        self.text = '周数'
        self.size_hint_y = None
        self.font_name = ft
        dropdown = DropDown()
        for index in range(21):
            if index == 0: continue
            btn = Button(text='第%d周' % index, size_hint_y=None, height=self.height*0.8, font_name=ft)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        self.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self, 'text', x))
        # runTouchApp(self)
