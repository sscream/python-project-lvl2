from gendiff import (
    get_file_data,
    tree,
    formatters
)


def generate_diff(
    file_path1: str, file_path2: str, formatter_name: str = formatters.STYLISH
) -> str:

    data1 = get_file_data(file_path1)
    data2 = get_file_data(file_path2)

    diff = tree.build_diff(data1, data2)

    formatter = formatters.get_formatter(formatter_name)

    return formatter(diff)
