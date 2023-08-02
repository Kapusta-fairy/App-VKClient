from time import ctime

from kivymd.uix.boxlayout import MDBoxLayout


class Message(MDBoxLayout):
    def __init__(self, message, vk):
        super().__init__()
        self.header.text = self.__create_header(message, vk)
        self.text.text = message.get('text')

    @staticmethod
    def __create_header(message, vk):
        name = vk.get_name_by_id(message.get('from_id'))
        date = ctime(message.get('date'))[10:19]
        return f'{name} {date}'
