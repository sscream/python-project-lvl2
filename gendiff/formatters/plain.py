from typing import Any, List

from gendiff import tree


def format(diff: dict) -> str:
    return '\n'.join(render(diff))


def to_str(value: Any) -> str:
    if isinstance(value, dict):
        return '[complex value]'

    if isinstance(value, bool):
        return f'{str(value).lower()}'

    if value is None:
        return 'null'

    return f"'{str(value)}'"


def render(diff_data: dict, path: str = '') -> List[str]:
    result = []

    for key, (status, value) in sorted(diff_data.items()):
        value_path = f'{path}{key}'

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
                f"From {to_str(value[0])} to {to_str(value[1])}"
            )

        if status == tree.NESTED:
            result.extend(
                render(value, f'{value_path}.')
            )

    return result
