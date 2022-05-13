import kivy
from kivy.uix.relativelayout import RelativeLayout

from database.Elc_DB import ser_by_qq
from funcs.Elc.choose_building import choose_building
from funcs.Elc.choose_room import choose_room
from funcs.Elc.query_elc import query_elc
from widgets.Popup_item import MyPopup
from widgets.button_item import MyButton
from widgets.label_item import MyLabel
from widgets.textinput_item import digital_TextInput

kivy.resources.resource_add_path('font/')
ft = kivy.resources.resource_find('DroidSansFallback.ttf')

class Elc_Info_Label(MyLabel):

    def __init__(self, **kwargs):
        super(Elc_Info_Label, self).__init__(**kwargs)
        self.font_name=ft
        self.text = '还没有绑定电费信息哦'
        self.color = [0,0,0,1]

    def update_text(self,qq_number):
        res = ser_by_qq(qq_number)
        res = '寝室号：%s\n剩余电量: %s 度\n剩余金额: %s 元\n距离上次查询已经过去了%s天%s小时%s分钟%s秒\n与上次查询相比用了: %s 度\n花费金额为 %s 元\n' % (
            res['room'], res['elc'], res['remain_money'], res['days'], res['hour'], res['minutes'], res['seconds'],
            res['used_elc'], res['used_money'])
        self.text = res


class Elc_Layout(RelativeLayout):
    def __init__(self, **kwargs):
        super(Elc_Layout, self).__init__(**kwargs)
        self.add_widget(MyLabel(
            text='宿舍栋',
            size_hint=(.10, .1),
            pos_hint={'x': .08, 'y': .8},
            color=[0, .5, 1, 1],
        ))

        building_textinput = digital_TextInput(
            size_hint=(.60, .1),
            pos_hint={'x': .25, 'y': .8},
            hint_text='南苑14栋填14',
            write_tab=False
        )

        self.add_widget(building_textinput)

        self.add_widget(MyLabel(
            text='房间号',
            size_hint=(.10, .1),
            pos_hint={'x': .08, 'y': .6},
            color=[0, .5, 1, 1],
        ))

        room_textinput = digital_TextInput(
            size_hint=(.60, .1),
            pos_hint={'x': .25, 'y': .6},
            hint_text='612',
            tab_width=0
        )
        self.add_widget(room_textinput)

        submit_button = MyButton(
            text='确定',
            size_hint=(.6, .2),
            pos_hint={'x': .2, 'y': .2},
        )
        def submit(instance):
            building = building_textinput.text
            room = room_textinput.text
            try:
                building_tmp = int(building) - 1
                search = str(choose_building()[1][building_tmp])
                ls = choose_room(search)
                room_id = str(ls[1][ls[0].index(room)])
                res = query_elc(room_id)
                popup_text = '%s 栋 %s 宿舍\n'%(building,room) + res[0]
                popup = MyPopup(popup_text)
            except:
                popup_text = '查询失败，检测一下输入的数据?'
                popup = MyPopup(popup_text)
            popup.open()
        submit_button.bind(on_press=submit)
        self.add_widget(submit_button)