from vk_api.longpoll import VkLongPoll

from vk_api import VkApi, VkUpload


class VK(object):
    __slots__ = ('api', 'longpoll', 'uploader')

    def __init__(self, token):
        session = VkApi(token=token)
        self.api = session.get_api()
        self.uploader = VkUpload(session)
        self.longpoll = VkLongPoll(session)

    def get_chat(self):
        return self.api.messages.getHistory(peer_id=2000000107)
