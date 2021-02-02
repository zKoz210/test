import time
from http.server import HTTPServer

from servers.server import MyHandler

HOST = "0.0.0.0"
PORT = 3000


def createServer():
    httpd = HTTPServer((HOST, PORT), MyHandler)
    print(time.asctime(), 'Start server %s:%s' % (HOST, PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    print(time.asctime(), 'Stop Server - %s:%s' % (HOST, PORT))


createServer()
