from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def _set_response(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self.index()
        else:
            self.unknown()

    def index(self):
        self._set_response(200)
        self.wfile.write("INDEX page\nnewline".encode('utf-8'))

    def unknown(self):
        self._set_response(404)
        self.wfile.write("Page {} NOT FOUND".format(self.path).encode('utf-8'))


server_address = ('127.0.0.1', 8080)
httpd = HTTPServer(server_address, Handler)
print("Serving HTTP ")
httpd.serve_forever()