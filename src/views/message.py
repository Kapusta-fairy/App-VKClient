from time import ctime

from kivymd.uix.boxlayout import MDBoxLayout


class Message(MDBoxLayout):
    def __init__(self, message):
        super().__init__()
        self.owner.text = str(message.get('from_id'))
        self.date.text = ctime(message.get('date'))[10:19]
        self.text.text = message.get('text')
