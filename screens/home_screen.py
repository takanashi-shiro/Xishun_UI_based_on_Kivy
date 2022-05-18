from kivy.uix.gridlayout import GridLayout

from funcs.yy.yiyan import yiyan
from widgets.label_item import MyLabel


class Home_Screen(GridLayout):
    def __init__(self, **kwargs):
        super(Home_Screen, self).__init__(**kwargs)
        self.rows = 2

    def add_items(self):
        Home_Title = (MyLabel(
            text="喜顺's Home",
            font_size=50, size_hint=(.5, .5),
            color=[0, .5, 1, 1],
            pos_hint={'right': 0.5, 'top': 0.5},
        ))
        self.add_widget(Home_Title)
        Home_Content = (MyLabel(
            text=yiyan(),
            font_size=30, size_hint=(.5, .5),
            color=[0, .5, 1, 1],
            pos_hint={'right': 0.5, 'top': 0.5},
        ))
        self.add_widget(Home_Content)

    def clear(self):
        self.clear_widgets()
