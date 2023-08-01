from kivymd.uix.boxlayout import MDBoxLayout

from src import config
from src.services.vk import VK
from src.views.message import Message


class Container(MDBoxLayout):
    __slots__ = 'vk'

    def __init__(self):
        super().__init__()
        self.vk = VK(config.VK_TOKEN)
        self.update()

    def update(self):
        self.clear_widgets([self])
        for message in self.vk:
            self.add_widget(Message(message))
