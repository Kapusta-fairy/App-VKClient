from dotenv import load_dotenv
from loguru import logger

from src.config import Config

load_dotenv()
config = Config()
logger.debug(f'config: {config}')
