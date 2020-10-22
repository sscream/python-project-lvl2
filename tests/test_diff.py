import pathlib
import tempfile

import pytest

from gendiff import generate_diff
from gendiff import formatters


FIXTURES_FOLDER = pathlib.Path(__file__).parent.absolute().joinpath('fixtures')


def get_fixture_path(filename, folder=FIXTURES_FOLDER):
    return folder.joinpath(filename)


test_cases = [
    (
        get_fixture_path('file1.json'),
        get_fixture_path('file2.json'),
        get_fixture_path('expected_stylish'),
        formatters.STYLISH,
    ),
    (
        get_fixture_path('file1.yml'),
        get_fixture_path('file2.yml'),
        get_fixture_path('expected_stylish'),
        formatters.STYLISH,
    ),
    (
        get_fixture_path('file1.json'),
        get_fixture_path('file2.yml'),
        get_fixture_path('expected_stylish'),
        formatters.STYLISH,
    ),
    (
        get_fixture_path('file1.json'),
        get_fixture_path('file2.json'),
        get_fixture_path('expected_plain'),
        formatters.PLAIN,
    )
]


@pytest.mark.parametrize(
    'file1_path, file2_path, expected_file_path, formatter', test_cases
)
def test_generate_diff(file1_path, file2_path, expected_file_path, formatter):
    with open(expected_file_path) as expected_file:
        diff = generate_diff(file1_path, file2_path, formatter)
        assert diff == expected_file.read()


def test_generate_diff_invalid_extension():
    tmp = tempfile.NamedTemporaryFile(suffix='.csv', delete=False)

    with pytest.raises(ValueError):
        generate_diff(
            get_fixture_path('file1.json'),
            tmp.name
        )
