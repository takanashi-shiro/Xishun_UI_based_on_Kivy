from kivy.uix.relativelayout import RelativeLayout

from database.DB_user import get_qq_number
from database.Elc_DB import insert
from funcs.Elc.query_elc import get_elc
from widgets.Popup_item import MyPopup
from widgets.button_item import MyButton
from widgets.label_item import MyLabel
from widgets.mythread import MyThread
from widgets.textinput_item import digital_TextInput


class Band_Elc_Screen(RelativeLayout):

    def __init__(self, username, **kwargs):
        super(Band_Elc_Screen, self).__init__(**kwargs)
        self.add_widget(MyLabel(
            text='绑定电费信息',
            size_hint=(.00, .08),
            color=[1, 1, 1, 1],
            pos_hint={'x': .5, 'y': .7},
        ))

        self.add_widget(MyLabel(
            text='宿舍栋',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .5},
            color=[0, .5, 1, 1],
        ))

        building_textinput = digital_TextInput(
            size_hint=(.60, .08),
            pos_hint={'x': .25, 'y': .5},
            hint_text='南苑14栋填14',
            write_tab=False
        )

        self.add_widget(building_textinput)

        self.add_widget(MyLabel(
            text='房间号',
            size_hint=(.10, .08),
            pos_hint={'x': .08, 'y': .35},
            color=[0, .5, 1, 1],
        ))

        room_textinput = digital_TextInput(
            size_hint=(.60, .08),
            pos_hint={'x': .25, 'y': .35},
            hint_text='612',
            tab_width=0
        )
        self.add_widget(room_textinput)

        submit_button = MyButton(
            text='确定',
            size_hint=(.8, .1),
            pos_hint={'x': .1, 'y': .15},
        )
        def submit(instance):
            building = building_textinput.text
            room = room_textinput.text
            popup_text = '绑定成功'
            try:
                elc = get_elc(building,room)
                print(elc)
                popup = MyPopup(popup_text)
                t = MyThread(insert,(get_qq_number(username),building,room,elc))
                t.daemon = True
                t.start()
            except:
                popup_text = '绑定失败，检测一下输入的数据?'
                popup = MyPopup(popup_text)
            popup.open()
        submit_button.bind(on_press=submit)
        self.add_widget(submit_button)





