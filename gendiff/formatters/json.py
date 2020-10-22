import json

from gendiff import tree


def format(diff_data: dict) -> str:
    return json.dumps(prepare_data(diff_data), indent=3)


def prepare_data(diff_data: dict) -> dict:
    result = {}

    for key, (status, value) in sorted(diff_data.items()):
        if status == tree.NESTED:
            result[key] = {
                'status': status,
                'value': prepare_data(value)
            }
        elif status == tree.MODIFIED:
            result[key] = {
                'status': status,
                'old_value': value[0],
                'new_value': value[1]
            }
        else:
            result[key] = {
                'status': status,
                'value': value
            }

    return result
