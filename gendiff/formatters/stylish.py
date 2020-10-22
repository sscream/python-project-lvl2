from typing import Any

from gendiff import tree


def render(diff_data: dict, depth: int = 1) -> str:
    lines = []

    def store(symbol: str, value: Any):
        lines.append(
            f'{indent(depth)}{symbol} {key}: {to_str(value, depth)}'
        )

    for key, (status, value) in sorted(diff_data.items()):
        if status == tree.UNMODIFIED:
            store(' ', value)

        if status == tree.MODIFIED:
            old, new = value
            store('-', old)
            store('+', new)

        if status == tree.REMOVED:
            store('-', value)

        if status == tree.ADDED:
            store('+', value)

        if status == tree.NESTED:
            lines.append(
                f'{indent(depth)}  {key}: '
                f'{{\n{render(value, depth + 2)}\n{indent(depth + 1)}}}'
            )

    return '\n'.join(lines)


def to_str(value: Any, depth: int) -> str:
    if value is None:
        return 'null'

    if isinstance(value, bool):
        return str(value).lower()

    if not isinstance(value, dict):
        return value

    result = f'\n{indent(depth + 3)}'.join(
        [f'{k}: {to_str(v, depth + 2)}' for k, v in value.items()])

    return f'{{\n{indent(depth + 3)}{result}\n{indent(depth + 1)}}}'


def indent(depth: int) -> str:
    return '  ' * depth


def format(diff_data: dict) -> str:
    return f'{{\n{render(diff_data)}\n}}'
