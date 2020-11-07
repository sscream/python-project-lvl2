import json
from io import TextIOWrapper

import yaml


def get_file_data(file: TextIOWrapper, extension: str) -> dict:
    if extension == 'json':
        return json.load(file)
    elif extension in {'yml', 'yaml'}:
        return yaml.safe_load(file)
    else:
        raise ValueError('Unsupported extension.')
