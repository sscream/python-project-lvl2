import importlib
from typing import Callable

FORMATTER_FUNCTION = 'format'

(STYLISH, PLAIN, JSON) = AVAILABLE_FORMATTERS = ('stylish', 'plain', 'json')


def get_formatter(format_name: str) -> Callable[[dict], str]:
    if format_name not in AVAILABLE_FORMATTERS:
        raise ValueError('Unsupported format.')

    formatter_module = importlib.import_module(f'.{format_name}', __name__)

    return getattr(formatter_module, FORMATTER_FUNCTION)
