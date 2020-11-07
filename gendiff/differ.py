import os
from typing import Union

from gendiff import (
    get_file_data,
    tree,
    formatters
)


def read_file(file_path: str):
    return open(file_path, 'r')


def get_file_extension(filename: Union[str, os.PathLike]) -> str:
    return os.path.splitext(filename)[1][1:]


def generate_diff(
    file_path1: str, file_path2: str, formatter_name: str = formatters.STYLISH
) -> str:

    file1 = read_file(file_path1)
    file2 = read_file(file_path2)

    data1 = get_file_data(file1, get_file_extension(file_path1))
    data2 = get_file_data(file2, get_file_extension(file_path2))

    file1.close()
    file2.close()

    diff = tree.build_diff(data1, data2)

    formatter = formatters.get_formatter(formatter_name)

    return formatter(diff)
