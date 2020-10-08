import argparse
import json

from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')

    args = parser.parse_args()

    result = generate_diff(args.first_file, args.second_file)

    print(result)
