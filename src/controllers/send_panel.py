from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout

from src import config
from src.services.vk import VK
from src.controllers.message import Message


class SendPanel(MDBoxLayout):
    __slots__ = 'vk'

    def __init__(self):
        super().__init__()
        self.vk = VK(config.VK_TOKEN)
        self.update()
        Clock.schedule_interval(lambda dt: self.update(), 3)

    def update(self):
        self.clear_widgets(self.children[1:])
        for message in self.vk:
            self.add_widget(Message(message, self.vk), index=3)

    def send(self):
        self.vk.send_message(self.ids.text_input.text)
        self.update()
