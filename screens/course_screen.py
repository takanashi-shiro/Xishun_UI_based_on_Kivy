from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout

from database.jwxt_DB import user_check, get_cookie
from funcs.kb.get_kb import get_kb
from funcs.kb.get_week import get_now_week, get_all_week
from funcs.kb.login import login
from widgets.Popup_item import MyPopup
from widgets.button_item import MyButton
from widgets.course_item import Course_Layout_Content, Course_Layout_Title, Course_Drop_List


class Course_Screen(GridLayout):

    def __init__(self,user, **kwargs):
        super(Course_Screen, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 1
        self.spacing = 20
        self.course_ls = []
        self.week = '1'
        self.all_week = '20'
        self.count_in2 = 0
        self.layout_content = Course_Layout_Content(size_hint=[1, .9])
        self.drop_list = Course_Drop_List(self.week,height=self.height / 2, size_hint=(.3, 1))

        self.dropdown = DropDown()
        for index in range(int(self.all_week) + 1):
            if index == 0: continue
            btn = MyButton(text='第%d周' % index, size_hint_y=None, height=self.height * 0.8)
            def on_press_child(btn1):
                self.dropdown.select(btn1.text)
                week = btn1.text
                self.week = week[1:-1]
                self.refresh(self.week)

            btn.bind(on_release=on_press_child)
            self.dropdown.add_widget(btn)
        self.drop_list.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.drop_list, 'text', x))
        self.pre_week_button = MyButton(text='<', size_hint=(.17, 1))
        self.next_week_button = MyButton(text='>', size_hint=(.17, 1))
        def on_press_pre_week(btn):
            if 1 <= int(self.week) - 1 <= int(self.all_week):
                self.week = str(int(self.week) - 1)
                self.drop_list.change_week(self.week)
                self.refresh(self.week,user)
        def on_press_next_week(btn):
            if 1 <= int(self.week) + 1 <= int(self.all_week):
                self.week = str(int(self.week) + 1)
                self.drop_list.change_week(self.week)
                self.refresh(self.week,user)
        self.pre_week_button.bind(on_release=on_press_pre_week)
        self.next_week_button.bind(on_release=on_press_next_week)
        self.course_layout_title = Course_Layout_Title(self.drop_list,self.pre_week_button,self.next_week_button, size_hint=[1, .1])




    def first_add(self,user):
        qq_number = user.get_qq_number()
        self.layout_content = Course_Layout_Content(size_hint=[1, .9])
        if user.get_class_ls() is not None:
            self.layout_content.add_items(class_ls=user.get_class_ls(), week=self.week)
            self.drop_list.change_week(self.week)
            self.update_title()
            self.add_widget(self.course_layout_title)
            self.add_widget(self.layout_content)
            return
        check1 = user_check(qq_number)
        popup_text = ''
        if check1 in [False, -1]:
            if check1 is False:
                popup_text = '账号未绑定课表，请先绑定吧'
            else:
                popup_text = '网络出现错误，请稍后试试?'
            self.layout_content.add_items()
        else:
            if self.count_in2 == 0:
                if user.get_encode() == '':
                    encode = get_cookie(qq_number)
                    user.set_encode(encode=encode)
                else:
                    encode = user.get_encode()
                session = login(encode)
                if session[1] < 1300:
                    popup_text = '网络出现错误，请稍后再点一下试试?'
                elif session[1] > 30000:
                    course_ls = get_kb(session[0])
                    self.week = get_now_week(session[0])
                    self.all_week = get_all_week(session[0])
                    self.count_in2 = 1
                    self.layout_content.add_items(class_ls=course_ls, week=self.week)
                    user.set_class_ls(course_ls)
            else:
                self.layout_content.add_items(class_ls=user.get_class_ls(), week=self.week)
        if self.count_in2 == 0:
            popup = MyPopup(popup_text)
            popup.open()
        self.drop_list.change_week(self.week)
        self.update_title()
        self.add_widget(self.course_layout_title)
        self.add_widget(self.layout_content)

    def update_title(self):
        self.course_layout_title.clear_widgets()
        self.course_layout_title = Course_Layout_Title(self.drop_list,self.pre_week_button,self.next_week_button, size_hint=[1, .05])
    def refresh(self,week,user):
        self.layout_content.clear_widgets()
        self.layout_content.add_items(class_ls=user.get_class_ls(), week=week)
