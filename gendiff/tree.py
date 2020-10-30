import typing


NESTED = 'nested'
UNMODIFIED = 'unmodified'
MODIFIED = 'modified'
REMOVED = 'removed'
ADDED = 'added'


def build_diff(data1: dict, data2: dict) -> typing.Dict[str, dict]:
    result = {}

    for key in data1.keys() - data2.keys():
        result[key] = {'status': REMOVED, 'value': data1[key]}

    for key in data2.keys() - data1.keys():
        result[key] = {'status': ADDED, 'value': data2[key]}

    for key in sorted(data1.keys() & data2.keys()):
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {
                'status': NESTED,
                'value': build_diff(data1[key], data2[key])
            }

        elif data1[key] == data2[key]:
            result[key] = {'status': UNMODIFIED, 'value': data2[key]}
        else:
            result[key] = {
                'status': MODIFIED,
                'value': {
                    'old': data1[key],
                    'new': data2[key]
                }
            }

    return result
