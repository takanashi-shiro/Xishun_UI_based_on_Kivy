import kivy
from kivy.uix import dropdown
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.app import App


kivy.resources.resource_add_path('../font/')
ft = kivy.resources.resource_find('DroidSansFallback.ttf')


class Drop_List(App):
    def __init__(self, **kwargs):
        super(Drop_List, self).__init__(**kwargs)
    dropdown = DropDown()
    for index in range(21):
        if index == 0: continue
        btn = Button(text='第%d周' % index, size_hint_y=None, height=44,font_name=ft)
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)
    mainbutton = Button(text='周数', size_hint=(None, None),font_name=ft)
    mainbutton.bind(on_release=dropdown.open)
    dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
    runTouchApp(mainbutton)

class MyApp(App):
    def build(self):
        self.root = root =Drop_List()
        return root
if __name__ == '__main__':
    MyApp().run()