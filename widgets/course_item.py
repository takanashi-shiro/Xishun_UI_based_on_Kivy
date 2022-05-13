import kivy
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

kivy.resources.resource_add_path('font/')
ft = kivy.resources.resource_find('DroidSansFallback.ttf')


class Course_Class_Item(Button):

    def __init__(self, **kwargs):
        super(Course_Class_Item, self).__init__(**kwargs)
        self.background_normal = "''"
        self.background_color = [1, 1, 1, .6]
        self.color = [0, 0, 0, 1]
        self.disabled_color = [0, 0, 0, 1]
        self.size_hint = [.3, .2]
        self.font_name = ft
        # self.padding = [3, 3]
        self.text_size = self.width,None




class Course_Info_Item(Label):

    def __init__(self, **kwargs):
        super(Course_Info_Item, self).__init__(**kwargs)
        self.size_hint = [.3, .1]
        self.color = [1, 1, 1, 1]
        self.font_name = ft
        self.bold = True
        self.outline_color = [0, 0, 0, 1]

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = (instance.width, instance.height)


class Course_Drop_List(Button):
    def __init__(self, **kwargs):
        super(Course_Drop_List, self).__init__(**kwargs)
        self.text = '周数'
        self.size_hint_y = None
        self.font_name = ft
        dropdown = DropDown()
        for index in range(21):
            if index == 0: continue
            btn = Button(text='第%d周' % index, size_hint_y=None, height=self.height * 0.8, font_name=ft)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        self.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self, 'text', x))
        # runTouchApp(self)


class Layout_Content(GridLayout):

    course_list = []
    def __init__(self, **kwargs):
        super(Layout_Content, self).__init__(**kwargs)
        self.cols = 8
        self.rows = 6
        self.padding = 20
        self.spacing = 3


    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    def add_items(self):
        for i in range(6):
            t = '+'
            nowcourse = '%s'%['1-2', '3-4', '5-6', '7-8', '9-10'][i - 1]
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
                    course_info = {
                        'name': 'python程序设计',
                        'content': '',
                        'pos': '计通楼512'
                    }
                    if course_info['content'] == '':
                        t = '%s %s' % (course_info['name'], course_info['pos'])
                    else:
                        t = '%s %s %s' % (course_info['name'], course_info['content'], course_info['pos'])
                    item = Course_Class_Item(text=t)
               # 周 j+1 第 i 节
               #  t = '周 %d 第 %d 节'%(j,i)
                self.add_widget(item)



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
                self.add_widget(Course_Drop_List(height=self.height / 2, size_hint=(.3, 1)))
            elif i == 1:
                self.add_widget(pre_week_button)
            elif i == 3:
                self.add_widget(next_week_button)
            else:
                self.add_widget(Label())

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
