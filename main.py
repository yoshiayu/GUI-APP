# -*- config: utf-8 -*-
from random import randint
from kivy.resources import resource_add_path
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.config import Config
from numpy import source
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT, 'ヒラギノ角ゴシック W1.ttc')

resource_add_path('./image')


class ImageWidget(Widget):
    source = StringProperty('./image/0001.jpg')

    def __init__(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
        pass

    def buttonStarted(self):
        self.source = './image/0001.jpg'

    def buttonRandom(self):
        self.source = f'000{randint(1,9)}.jpg'


class CarApp(App):
    def __init__(self, **kwargs):
        super(CarApp, self).__init__(**kwargs)
        self.title = 'WRX STI画像表示'


if __name__ == '__main__':
    CarApp().run()
