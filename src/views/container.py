from kivymd.uix.boxlayout import MDBoxLayout

from src import config
from src.services.vk import VK


class Message(MDBoxLayout):
    def __init__(self, content):
        super().__init__()
        self.content.text = content


class Container(MDBoxLayout):
    __slots__ = ('vk',)

    def __init__(self):
        super().__init__()
        self.vk = VK(config.VK_TOKEN)
        msg = self.vk.get_chat().get('items')
        for i in msg:
            new_message = Message(i.get('text'))
            self.add_widget(new_message, index=3)
