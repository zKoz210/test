HTTP_200_OK = 200
HTTP_400_BAD_REQUEST = 400
HTTP_404_NOT_FOUND = 404
HTTP_405_METHOD_NOT_ALLOWED = 405
HTTP_503_SERVICE_UNAVAILABLE = 503

URL_NOT_FOUND = {"error": "URL not found"}
DATA_NOT_FOUND = {"error": "Data not found"}
INVALID_REQUEST = {"error": "Invalid request"}
NOT_IMPLEMENTED = {'error': "Method not implemented"}
METHOD_NOT_ALLOWED = {'error': "Method not allowed"}
SERVICE_UNAVAILABLE = {'error': "Service is currently unavailable"}
BAD_REQUEST = {'error': 'Bad request'}


class Response:

    def __init__(self, status, data=None):
        if data is None:
            data = []
        self.status_code = status
        self.data = data
