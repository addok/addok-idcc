from .utils import Search


def register_http_endpoint(api):
    api.add_route('/search', Search())
