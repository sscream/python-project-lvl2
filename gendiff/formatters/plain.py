from typing import Any, List

from gendiff import tree


def format(diff_data: dict) -> str:
    return '\n'.join(get_plain_diff(diff_data))


def to_str(value: Any) -> str:
    if isinstance(value, dict):
        return '[complex value]'

    if value is None:
        return 'null'

    str_value = str(value)

    if isinstance(value, bool):
        return f'{str_value.lower()}'

    if str_value.isnumeric():
        return str_value

    return f"'{str_value}'"


def get_plain_diff(diff_data: dict, path: str = '') -> List[str]:
    result = []

    for key, meta in sorted(diff_data.items()):
        value_path = f'{path}{key}'

        status = meta['status']
        value = meta['value']

        if status == tree.ADDED:
            result.append(
                f"Property '{value_path}' was added "
                f"with value: {to_str(value)}"
            )

        if status == tree.REMOVED:
            result.append(f"Property '{value_path}' was removed")

        if status == tree.MODIFIED:
            result.append(
                f"Property '{value_path}' was updated. "
                f"From {to_str(value['old'])} to {to_str(value['new'])}"
            )

        if status == tree.NESTED:
            result.extend(
                get_plain_diff(value, f'{value_path}.')
            )

    return result
