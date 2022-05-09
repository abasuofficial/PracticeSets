from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout

class WindowManager(ScreenManager):
    pass

class About(Screen):
    pass

class DecodeMenu(Screen):
    pass

class EncodeMenu(Screen):
    pass

class MainMenu(Screen):
    pass

class MyGridGUIK(Screen):
    pass

kv = Builder.load_file("cryptostego.kv")

class CryptoStego(App):
    def build(self):
        return kv


if __name__=="__main__":
    CryptoStego().run()