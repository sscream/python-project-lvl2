import json

from gendiff import tree


def format(diff_data: dict) -> str:
    return json.dumps(prepare_data(diff_data), indent=3)


def prepare_data(diff_data: dict) -> dict:
    result = {}

    for key, meta in sorted(diff_data.items()):
        status = meta['status']
        value = meta['value']

        if status == tree.NESTED:
            result[key] = {
                'status': status,
                'value': prepare_data(value)
            }
        elif status == tree.MODIFIED:
            result[key] = {
                'status': status,
                'old_value': value['old'],
                'new_value': value['new']
            }
        else:
            result[key] = {
                'status': status,
                'value': value
            }

    return result
