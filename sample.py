from kivy.app import App
from kivy.uix.label import Label

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

# /System/Library/Fonts

resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT, 'ヒラギノ角ゴシック W1.ttc')


class TextApp(App):
    def build(self):
        return Label(text='こんにちはこんばんは')


TextApp().run()
