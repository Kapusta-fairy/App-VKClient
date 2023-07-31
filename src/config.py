from pydantic_settings import BaseSettings


class Config(BaseSettings):
    KIVY_NO_CONSOLELOG: str
    KV_FILE_PATH: str

    MINIMUM_WIDTH: int
    MINIMUM_HEIGHT: int

    APP_TITLE: str

    COLOR_BACKGROUND: str
    COLOR_ELEMENTS: str
