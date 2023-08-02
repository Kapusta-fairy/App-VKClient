from loguru import logger

from src.client import Client

if __name__ == '__main__':
    try:
        Client().run()
    except Exception as ex:
        logger.critical(ex)
