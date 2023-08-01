import asyncio

from loguru import logger

from src.client import Client

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(Client().async_run(async_lib='asyncio'))
    # except Exception as ex:
    #     logger.critical(ex)
    finally:
        loop.close()
