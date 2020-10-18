import os
import json
from typing import Union

import yaml


def get_file_data(file_path: Union[str, os.PathLike]) -> dict:
    extension = get_file_extension(os.path.basename(file_path))

    with open(file_path, 'r') as file:

        if extension == 'json':
            return json.load(file)
        elif extension in {'yml', 'yaml'}:
            return yaml.safe_load(file)
        else:
            raise ValueError('Unsupported file format.')


def get_file_extension(filename: Union[str, os.PathLike]) -> str:
    return os.path.splitext(filename)[1][1:]
