from vk_api import VkApi
from vk_api.vk_api import VkApiMethod

from src import config


class VK(object):
    __slots__ = 'api'

    def __init__(self, token):
        self.api: VkApiMethod = VkApi(token=token).get_api()

    def __iter__(self):
        history: dict = self.api.messages.getHistory(
            peer_id=config.VK_CHAT_PEER_ID
        )
        for message in history.get('items')[:10]:
            yield message
