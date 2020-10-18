import typing


NESTED = 'nested'
UNMODIFIED = 'unmodified'
MODIFIED = 'modified'
REMOVED = 'removed'
ADDED = 'added'


def build_diff(data1: dict, data2: dict) -> dict:
    result: typing.Dict[str, tuple] = {}

    for key in data1.keys() - data2.keys():
        result[key] = (REMOVED, data1[key])

    for key in data2.keys() - data1.keys():
        result[key] = (ADDED, data2[key])

    for key in sorted(data1.keys() & data2.keys()):
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = (NESTED, build_diff(data1[key], data2[key]))
        elif data1[key] == data2[key]:
            result[key] = (UNMODIFIED, data2[key])
        else:
            result[key] = (MODIFIED, (data1[key], data2[key]))

    return result
