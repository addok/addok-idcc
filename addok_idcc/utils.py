from addok.config import config


def format_result(result):
    return {field['key']: getattr(result, field['key'])
            for field in config.FIELDS}


def make_labels(helper, result):
    if not result.labels:
        result.labels = result._rawattr(config.NAME_FIELD)[:]
        result.labels.append(result.code)
