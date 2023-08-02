from dotenv import load_dotenv
from loguru import logger

from src.config import Config
from src.utils.files import get_kv_files_paths

load_dotenv()

kv_files_paths = get_kv_files_paths()
config = Config()
logger.debug(f'init app success')
