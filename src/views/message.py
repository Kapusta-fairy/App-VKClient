from time import ctime

from kivymd.uix.boxlayout import MDBoxLayout


class Message(MDBoxLayout):
    def __init__(self, message, vk):
        super().__init__()
        name = vk.get_name_by_id(message.get('from_id'))
        date = ctime(message.get('date'))[10:19]
        self.header.text = f'{name} {date}'
        self.text.text = message.get('text')
