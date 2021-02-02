from request.views import *
from servers.response import *

welcome = Welcome()
currencyUsd = CurrencyUsd()


def get_path(path, request_type):
    if request_type == 'GET':
        get = re.findall("\d+", path)

        paths = [
            ('/', welcome.get()),
            ('/amount', []),
        ]

        if get:
            amount = get[0]
            if path == '/amount/{}'.format(amount):
                response = currencyUsd.get(amount=amount)
                return response.status_code, response.data
            else:
                return HTTP_404_NOT_FOUND, URL_NOT_FOUND
        if any(path in url for url in paths):
            if path == '/':
                return paths[0][1].status_code, paths[0][1].data
            else:
                return HTTP_404_NOT_FOUND, URL_NOT_FOUND
        else:
            return HTTP_404_NOT_FOUND, URL_NOT_FOUND
    else:
        return HTTP_405_METHOD_NOT_ALLOWED, METHOD_NOT_ALLOWED
