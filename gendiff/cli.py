import argparse

from gendiff import formatters


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Generate diff.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format', type=str,
        help='set format of output',
        default=formatters.STYLISH,
        choices=formatters.AVAILABLE_FORMATTERS
    )

    return parser.parse_args()
