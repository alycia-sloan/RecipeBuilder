import kivy
import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch,OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivy.uix.screenmanager import ScreenManager, Screen,WipeTransition

import recipe_builder as recipe_builder

#kivy.require('2.0.0')

#Builder.load_file("mainmenu.kv")

class MainMenuWindow(Screen):
    pass

class GroceryListWindow(Screen):
    def run_list_builder(self):
        recipe_builder

class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_file("kivy_files\\mainmenu.kv")

    def grocery_builder_app(self):
        print("Test")




if __name__ == "__main__":
    MainApp().run()