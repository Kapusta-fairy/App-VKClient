from loguru import logger
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

from src import config, kv_files_paths
from services.colors import colors
from src.controllers.send_panel import SendPanel


class Client(MDApp):
    title = config.APP_TITLE

    def build(self):
        self.__set_window().__set_colors().__load_view()
        return SendPanel()

    def __set_window(self):
        minimum_width = config.MINIMUM_WIDTH
        minimum_height = config.MINIMUM_HEIGHT
        Window.size = (minimum_width, minimum_height)
        Window.minimum_width = minimum_width
        Window.minimum_height = minimum_height
        logger.debug(f'window created({minimum_width}, {minimum_height})')
        return self

    def __set_colors(self):
        self.theme_cls.colors = colors
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Red'
        logger.debug('colors set')
        return self

    def __load_view(self):
        [Builder.load_file(path) for path in kv_files_paths]
        logger.debug(f'kv files loaded')
        return self
