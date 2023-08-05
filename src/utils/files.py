import os
import sys
from pathlib import Path


def get_kv_files_paths() -> list:
    kv_files_paths = []
    views = Path(sys.path[0]).joinpath('views')
    for root, dirs, paths in os.walk(views):
        kv_paths = [path for path in paths if(path.endswith('.kv'))]
        [kv_files_paths.append(f'{views}/{kv_path}') for kv_path in kv_paths]
    return kv_files_paths
