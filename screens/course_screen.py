from kivy.uix.gridlayout import GridLayout
from widgets.course_item import Layout_Title,Layout_Content


class Course_Screen(GridLayout):

    def __init__(self, **kwargs):
        super(Course_Screen, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 1
        self.spacing = 20



