import re

from pip._vendor import requests
from servers.response import *


class Welcome:

    def get(self):
        data = 'Welcome to world'
        return Response(data=data, status=HTTP_200_OK)


class CurrencyUsd:

    def get(self, amount=None):
        if not amount:
            return HTTP_400_BAD_REQUEST, BAD_REQUEST

        url = 'https://www.banki.ru/products/currency/usd/'

        try:
            source = requests.get(url)
            main_text = source.text
            source.raise_for_status()
        except requests.exceptions.Timeout:
            return HTTP_503_SERVICE_UNAVAILABLE, SERVICE_UNAVAILABLE
        except requests.exceptions.TooManyRedirects:
            return HTTP_503_SERVICE_UNAVAILABLE, SERVICE_UNAVAILABLE
        except requests.exceptions.ConnectionError:
            return HTTP_503_SERVICE_UNAVAILABLE, SERVICE_UNAVAILABLE
        except requests.exceptions.RequestException:
            return HTTP_503_SERVICE_UNAVAILABLE, SERVICE_UNAVAILABLE

        currency = re.findall("<div.*class\s*=\s*[\"'].*currency-table__large-text.*[\"']\s*>(.*)<\/div>", main_text)

        if not currency:
            return HTTP_400_BAD_REQUEST, BAD_REQUEST

        currency = float(currency[0].replace('.', '').replace(',', '.'))
        amount = float(amount)

        response = {
            'RUB': currency,
            'AMOUNT_USD': amount,
            'RESULT': currency * amount
        }

        return Response(data=response, status=HTTP_200_OK)
