from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO

class PostHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(body)
        self.wfile.write(response.getvalue())

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

if __name__ == '__main__':
    port = 80
    httpd = HTTPServer(('', port), PostHandler)
    print('Listening on :' + str(port))
    httpd.serve_forever()