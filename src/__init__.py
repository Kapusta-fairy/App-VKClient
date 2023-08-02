import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from loguru import logger

from src.config import Config

load_dotenv()

kv_files_paths = []
views = Path(sys.path[0]).joinpath('views')
for root, dirs, paths in os.walk(views):
    kv_paths = [path for path in paths if(path.endswith('.kv'))]
    [kv_files_paths.append(f'{views}/{kv_path}') for kv_path in kv_paths]

config = Config()
logger.debug(f'init app success')
