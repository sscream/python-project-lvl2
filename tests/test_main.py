import pathlib

import pytest

from gendiff import generate_diff


FIXTURES_FOLDER = pathlib.Path(__file__).parent.absolute().joinpath('fixtures')


def get_fixture_path(filename, folder=FIXTURES_FOLDER):
    return folder.joinpath(filename)


test_cases = [
    (
        get_fixture_path('flat_file1.json'),
        get_fixture_path('flat_file2.json'),
        get_fixture_path('flat_expected'),
    ),
]


@pytest.mark.parametrize(
    'file1_path, file2_path, expected_file_path', test_cases
)
def test_generate_diff(file1_path, file2_path, expected_file_path):
    with open(expected_file_path) as expected_file:
        assert generate_diff(file1_path, file2_path) == expected_file.read()