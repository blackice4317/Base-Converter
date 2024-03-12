from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager

Window.size = (360, 640)


class HomeScreen(Screen):
    pass


class BaseTwoConvertion(Screen):
    def binary_convert(self):
        if self.ids.Number.text == '':
            close_button = MDFlatButton(text='Close', on_release=self.close_func)
            self.dialog = MDDialog(title='Message', text='Enter Number', buttons=[close_button])
            self.dialog.open()

        else:
            number = int(self.ids.Number.text)
            store_remainder = ''
            while number > 0:
                remainder = number % 2
                store_remainder = str(remainder) + store_remainder
                number = number // 2
            self.ids.Answer.text = str(store_remainder)
        self.ids.Number.text = ""

    def binary_to_decimal(self):
        if self.ids.Number.text == '':
            close_button = MDFlatButton(text='Close', on_release=self.close_func)
            self.dialog = MDDialog(title='Message', text='Enter Number', buttons=[close_button])
            self.dialog.open()
        else:
            binary = self.ids.Number.text
            decimal = int(binary, 2)

            self.ids.Answer.text = str(decimal)
        self.ids.Number.text = ""

    def reset(self):
        self.ids.Answer.text = "0"

    def close_func(self):
        self.dialog.dismiss()

    pass


class BaseEightConverter(Screen):
    def decimal_to_octal(self):
        if self.ids.Number.text == '':
            close_button = MDFlatButton(text='Close', on_release=self.close_func)
            self.dialog = MDDialog(title='Message', text='Enter Number', buttons=[close_button])
            self.dialog.open()

        else:
            store = int(self.ids.Number.text)
            decimal = oct(store)
            self.ids.Answer.text = str(decimal)[2:]
        self.ids.Number.text = ""

    def octal_to_decimal(self):
        if self.ids.Number.text == '':
            close_button = MDFlatButton(text='Close', on_release=self.close_func)
            self.dialog = MDDialog(title='Message', text='Enter Number', buttons=[close_button])
            self.dialog.open()
        else:
            octal = self.ids.Number.text
            decimal = int(octal, 8)

            self.ids.Answer.text = str(decimal)
        self.ids.Number.text = ""

    def reset(self):
        self.ids.Answer.text = "0"

    def close_func(self):
        self.dialog.dismiss()

    pass


class BaseSixteenConverter(Screen):
    def decimal_to_hexa(self):
        if self.ids.Number.text == '':
            close_button = MDFlatButton(text='Close', on_release=self.close_func)
            self.dialog = MDDialog(title='Message', text='Enter Number', buttons=[close_button])
            self.dialog.open()

        else:
            store = int(self.ids.Number.text)
            decimal = hex(store)
            self.ids.Answer.text = str(decimal)[2:]
        self.ids.Number.text = ""

    def hexa_to_decimal(self):
        if self.ids.Number.text == '':
            close_button = MDFlatButton(text='Close', on_release=self.close_func)
            self.dialog = MDDialog(title='Message', text='Enter Number', buttons=[close_button])
            self.dialog.open()
        else:
            hexa = self.ids.Number.text
            decimal = int(hexa, 16)

            self.ids.Answer.text = str(decimal)
        self.ids.Number.text = ""

    def reset(self):
        self.ids.Answer.text = "0"

    def close_func(self):
        self.dialog.dismiss()

    pass


class Menu(Screen):
    def button_change2(self):
        self.ids.base2.source = "Assets/BaseTwo_pressed.jpg"

    def button_change_back2(self):
        self.ids.base2.source = "Assets/BaseTwo.jpg"

    def button_change8(self):
        self.ids.base8.source = "Assets/BaseEight_pressed.jpg"

    def button_change_back8(self):
        self.ids.base8.source = "Assets/BaseEight.jpg"

    def button_change16(self):
        self.ids.base16.source = "Assets/BaseSixteen_pressed.jpg"

    def button_change_back16(self):
        self.ids.base16.source = "Assets/BaseSixteen.jpg"
    pass


class NumberConverter(MDApp):
    def build(self):
        self.icon = "Assets/logo.png"
        self.theme_cls.primary_palette = "Teal"
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("HomeScreen.kv"))
        screen_manager.add_widget(Builder.load_file("BaseTwoConvertion.kv"))
        screen_manager.add_widget(Builder.load_file("BaseEightConverter.kv"))
        screen_manager.add_widget(Builder.load_file("BaseSixteenConverter.kv"))
        screen_manager.add_widget(Builder.load_file("Menu.kv"))
        return screen_manager


LabelBase.register(name='Big',
                   fn_regular='big_noodle_titling.ttf')
LabelBase.register(name='Glasket',
                   fn_regular='glasket500.otf')
LabelBase.register(name='eraser',
                   fn_regular='EraserDust.ttf')
LabelBase.register(name='broken',
                   fn_regular='KGBrokenVesselsSketch.ttf')
NumberConverter().run()
