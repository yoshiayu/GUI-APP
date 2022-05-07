from kivy.app import App

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

# /System/Library/Fonts

resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT, 'ヒラギノ角ゴシック W1.ttc')


class TestApp(App):
    pass


if __name__ == '__main__':
    TestApp().run()
