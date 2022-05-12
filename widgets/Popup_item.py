from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout

from widgets.button_item import MyButton
from widgets.label_item import MyLabel


class MyPopup_Remind(Popup):
    def __init__(self,mytext='提醒', **kwargs):
        super(MyPopup_Remind, self).__init__(**kwargs)
        self.content=MyLabel(text=mytext, size_hint=(1, 1))
        self.title_size = 0
        self.size_hint=(.3,.2)

class MyPopup(Popup):
    def __init__(self,mytext='警告', **kwargs):
        super(MyPopup, self).__init__(**kwargs)
        popup_layout = RelativeLayout(size=(self.width * 0.5, self.height * 0.5))
        popup_layout.add_widget(
            MyLabel(text=mytext, size_hint=(0, 0), pos_hint={'x': .5, 'y': .8}))
        close_popup_button = MyButton(text='了解', size_hint=(.3, .2), pos_hint={'x': .35, 'y': .3})
        popup_layout.add_widget(close_popup_button)
        self.content=popup_layout
        self.title = 'Error'
        self.size_hint=(.5,.5)
        close_popup_button.bind(on_press=self.dismiss)