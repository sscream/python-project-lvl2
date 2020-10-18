from gendiff import generate_diff, cli


def main():
    args = cli.parse_args()

    result = generate_diff(args.first_file, args.second_file, args.format)

    print(result)
