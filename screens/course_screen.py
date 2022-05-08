from kivy.uix.gridlayout import GridLayout
from widgets.course_item import Course_Class_Item, Course_Drop_List, Course_Info_Item
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle


class Layout_Content(GridLayout):
    def __init__(self, **kwargs):
        super(Layout_Content, self).__init__(**kwargs)
        self.cols = 8
        self.rows = 6
        self.padding = 20
        self.spacing = 3
        # self.bind(size=self._update_rect, pos=self._update_rect)
        # with self.canvas.before:
        #     Color(.95, .95, .95, 1)
        #     self.rect = Rectangle(size=self.size, pos=self.pos)
        for i in range(6):
            t = '+'
            for j in range(8):
                if i == 0:
                    if j != 0:
                        t = '周%s' % (['一', '二', '三', '四', '五', '六', '日'][j - 1])
                    else:
                        t = ''

                    item = Course_Info_Item(text=t, size_hint=[.3, .1])
                    item.bind(size=item._update_rect, pos=item._update_rect)
                    with item.canvas.before:
                        Color(0, .5, 1, .5)
                        item.rect = Rectangle(size=item.size, pos=item.pos)
                elif j == 0:
                    if i != 0:
                        t = '第%s节' % (['1~2', '3~4', '5~6', '7~8', '9~10'][i - 1])
                    else:
                        t = ''
                    item = Course_Info_Item(text=t, size_hint=[.1, .3])
                    item.bind(size=item._update_rect, pos=item._update_rect)
                    with item.canvas.before:
                        Color(0, .5, 1, .5)
                        item.rect = Rectangle(size=item.size, pos=item.pos)
                else:
                    item = Course_Class_Item(text=t)
                t = '+'
                self.add_widget(item)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class Layout_Title(GridLayout):

    def __init__(self, **kwargs):
        super(Layout_Title, self).__init__(**kwargs)
        self.cols = 5
        self.spacing = 20
        self.padding = 7
        self.bind(size=self._update_rect, pos=self._update_rect)
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        pre_week_button = Button(text='<', size_hint=(.17, 1))
        next_week_button = Button(text='>', size_hint=(.17, 1))
        for i in range(5):
            if i == 2:
                self.add_widget(Course_Drop_List(height=self.height/2,size_hint=(.3, 1)))
            elif i == 1:
                self.add_widget(pre_week_button)
            elif i == 3:
                self.add_widget(next_week_button)
            else:
                self.add_widget(Label())

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class Course_Screen(GridLayout):

    def __init__(self, **kwargs):
        super(Course_Screen, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 1
        self.spacing = 20
        layout_title = Layout_Title(size_hint=[1,.05])
        self.add_widget(layout_title)
        # self.add_widget(Label(text='13',size_hint=[1,1],color=[0,0,0,1]))
        layout_content = Layout_Content(size_hint=[1,.95])
        self.add_widget(layout_content)

