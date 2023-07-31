from loguru import logger
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

from src import config
from src.services.colors import colors
from src.views.container import Container


class Client(MDApp):
    title = config.APP_TITLE

    def build(self):
        self.__set_window()
        self.__set_colors()
        self.__load_view()

        return Container()

    def __set_colors(self):
        self.theme_cls.colors = colors
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Red'
        logger.debug('colors set')
        return self

    def __set_window(self):
        Window.size = (config.MINIMUM_WIDTH, config.MINIMUM_HEIGHT)
        Window.minimum_width = config.MINIMUM_WIDTH
        Window.minimum_height = config.MINIMUM_HEIGHT
        logger.debug(
            f'window created({config.MINIMUM_WIDTH}, {config.MINIMUM_HEIGHT})'
        )
        return self

    def __load_view(self):
        Builder.load_file(config.KV_FILE_PATH)
        logger.debug(f'kv file loaded from path: {config.KV_FILE_PATH}')
        return self
