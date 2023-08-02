from functools import cache

from vk_api import VkApi
from vk_api.vk_api import VkApiMethod

from src import config


class VK(object):
    __slots__ = 'api', 'peer_id'

    def __init__(self, token):
        self.api: VkApiMethod = VkApi(token=token).get_api()
        self.peer_id = config.VK_CHAT_PEER_ID

    def __iter__(self):
        history: dict = self.api.messages.getHistory(peer_id=self.peer_id)
        for message in history.get('items')[:10]:
            yield message

    @cache
    def get_name_by_id(self, user_id):
        if user := self.api.users.get(user_ids=user_id):
            return f'{user[0].get("first_name")} {user[0].get("last_name")}'

    def send_message(self, text):
        self.api.messages.send(peer_id=self.peer_id, message=text, random_id=0)
