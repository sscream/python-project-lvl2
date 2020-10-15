import os
import json
from typing import TextIO, Union

import yaml


def get_file_data(file_path: Union[str, os.PathLike]) -> dict:
    extension = get_file_extension(os.path.basename(file_path))

    with open(file_path, 'r') as file:

        if extension == 'json':
            return load_json(file)
        elif extension in ['yml', 'yaml']:
            return load_yaml(file)
        else:
            raise ValueError('Unsupported file format.')


def get_file_extension(filename: Union[str, os.PathLike]) -> str:
    return os.path.splitext(filename)[1][1:]


def load_json(file: TextIO) -> dict:
    return json.load(file)


def load_yaml(file: TextIO) -> dict:
    return yaml.safe_load(file)
