from addok.config import config
from addok.http.base import Search as BaseSearch


def filter_documents(docs):
    for doc in docs:
        # Those means "no IDCC".
        if doc['code'] in ['9999', '9998']:
            continue
        yield doc


def format_result(result):
    return {field['key']: getattr(result, field['key'])
            for field in config.FIELDS}


def make_labels(helper, result):
    if not result.labels:
        result.labels = result._rawattr(config.NAME_FIELD)[:]
        result.labels.append(result.code)


class Search(BaseSearch):

    def render(self, req, resp, results, query=None, limit=None, **kwargs):
        data = {
            'results': [r.format() for r in results],
            'query': query,
            'limit': limit,
        }
        self.json(req, resp, data)
