# @Author   : takanashi-shiro
# @QQ       : 764806602
# @Wechat   : Ender_White
# @Software : Pycharm
# @Time     : 2022/05/06 - 2022/05/14





import kivy
from kivy import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

kivy.require('2.1.0')
from kivy.app import App  # 译者注：这里就是从kivy.app包里面导入App类
from screens.model_screen import Model_Screen
from screens.login_screen import Login_Screen
from screens.register_screen import Register_Screen
from screens.forget_passwd_screen import Forget_Pwd_Screen


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Login_Screen(name='login'))
        screen_manager.add_widget(Model_Screen(name='model'))
        screen_manager.add_widget(Register_Screen(name='register'))
        screen_manager.add_widget(Forget_Pwd_Screen(name='forget_pwd'))
        return screen_manager


if __name__ == '__main__':
    Config.set('graphics', 'borderless', 0)
    Config.set('graphics', 'window_state', 'maximized')
    Config.write()
    MyApp().run()
