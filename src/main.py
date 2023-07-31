from src.views.container import Container

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


class Client(MDApp):
    title = 'Клиент для вк'

    def build(self):
        Window.size = (420, 360)
        Window.minimum_width = 420
        Window.minimum_height = 260

        Builder.load_file('views/main.kv')
        self.theme_cls.primary_palette = "Gray"

        return Container()


if __name__ == '__main__':
    Client().run()
