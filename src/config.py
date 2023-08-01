from pydantic_settings import BaseSettings


class Config(BaseSettings):
    MINIMUM_WIDTH: int
    MINIMUM_HEIGHT: int

    APP_TITLE: str

    COLOR_BACKGROUND: str
    COLOR_ELEMENTS: str

    VK_TOKEN: str
    VK_CHAT_PEER_ID: int
