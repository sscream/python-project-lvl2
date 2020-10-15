from .io import get_file_data


def jsonify_value(key: str, value: str, action: str = ' '):
    template = ' {} {}: {}'

    if isinstance(value, bool):
        return template.format(action, key, str(value).lower())

    return template.format(action, key, value)


def generate_diff(file_path1: str, file_path2: str) -> str:
    json1 = get_file_data(file_path1)
    json2 = get_file_data(file_path2)

    json1_keys = set(json1.keys())
    json2_keys = set(json2.keys())

    diff = [
        jsonify_value(key, json1[key])
        for key in json1_keys & json2_keys
        if json1[key] == json2[key]
    ]

    diff.extend([
        jsonify_value(key, json1[key], '-')
        for key in json1_keys - json2_keys
    ])

    diff.extend([
        jsonify_value(key, json2[key], '+')
        for key in json2_keys - json1_keys
    ])

    diff.sort()

    for key in json1_keys & json2_keys:
        if json1[key] != json2[key]:
            diff.append(jsonify_value(key, json1[key], '-'))
            diff.append(jsonify_value(key, json2[key], '+'))

    diff_str = '\n'.join(diff)

    return f'{{\n{diff_str}\n}}'
