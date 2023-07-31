from pydantic import BaseSettings


class Settings(BaseSettings):
    KIVY_NO_CONSOLELOG: str = '1'


settings = Settings()
