import json
from http.server import BaseHTTPRequestHandler
from request.routes import get_path


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
        )
        self.respond(status_code, response)

    def handle_http(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        content = json.dumps(data)
        return bytes(content, 'UTF-8')

    def respond(self, status_code, data=None):
        response = self.handle_http(status_code, data)
        self.wfile.write(response)
