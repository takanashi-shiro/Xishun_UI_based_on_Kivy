from kivy.uix.gridlayout import GridLayout


class Elc_Screen(GridLayout):
    def __init__(self, **kwargs):
        super(Elc_Screen, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 1