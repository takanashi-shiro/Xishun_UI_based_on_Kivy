from kivy.uix.gridlayout import GridLayout
from widgets.course_item import Layout_Title,Layout_Content


class Course_Screen(GridLayout):

    def __init__(self, **kwargs):
        super(Course_Screen, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 1
        self.spacing = 20
        layout_title = Layout_Title(size_hint=[1,.05])
        self.add_widget(layout_title)
        layout_content = Layout_Content(size_hint=[1,.95])
        self.add_widget(layout_content)

