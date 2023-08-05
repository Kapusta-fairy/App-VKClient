from time import ctime

from kivymd.uix.boxlayout import MDBoxLayout

from services.vk import VK


class Message(MDBoxLayout):
    def __init__(self, message: dict, vk: VK):
        super().__init__()
        self.header.text: str = self.__create_header(message, vk)
        self.text.text: str = message.get('text')

    @staticmethod
    def __create_header(message: dict, vk: VK) -> str:
        name: str = vk.get_name_by_id(message.get('from_id'))
        date: str = ctime(message.get('date'))[10:19]
        return f'{name} {date}'
