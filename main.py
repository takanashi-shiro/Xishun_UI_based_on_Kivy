import kivy
from kivy.uix.screenmanager import ScreenManager

kivy.require('2.1.0')
from kivy.app import App  # 译者注：这里就是从kivy.app包里面导入App类
from screens.model_screen import Model_Screen
from screens.login_screen import Login_Screen
from screens.register_screen import Register_Screen
from screens.forget_passwd_screen import Forget_Pwd_Screen


class MyApp(App):
    def build(self):  # 译者注：这里是实现build()方法
        # self.root = root = Login_Screen()
        screen_manager = ScreenManager()
        screen_manager.add_widget(Login_Screen(name='login'))
        screen_manager.add_widget(Model_Screen(name='model'))
        screen_manager.add_widget(Register_Screen(name='register'))
        screen_manager.add_widget(Forget_Pwd_Screen(name='forget_pwd'))
        # screen_manager.current_screen()
        # self.root = root = Model_Screen()
        # root.bind(size=self._update_rect, pos=self._update_rect)
        #
        # with root.canvas.before:
        #     Color(1, 1, 1, .95)
        #     self.rect = Rectangle(size=root.size, pos=root.pos)
        return screen_manager

    # def _update_rect(self, instance, value):
    #     self.rect.pos = instance.pos
    #     self.rect.size = instance.size


if __name__ == '__main__':
    MyApp().run()  # 译者注：这里就是运行了。
