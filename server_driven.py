from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO

# ROUTE

ROUTE_PRODUCT = "/product"
ROUTE_LIST = "/list"
ROUTE_COORDINATOR = "/coordinator.js"
ROUTE_LAYOUT = "/layout.xml"

ROUTE_PRODUCT_LIST = ROUTE_PRODUCT + ROUTE_LIST
ROUTE_PRODUCT_LIST_COORDINATOR = ROUTE_PRODUCT_LIST + ROUTE_COORDINATOR
ROUTE_PRODUCT_LIST_LAYOUT = ROUTE_PRODUCT_LIST + ROUTE_LAYOUT

# String

js = '''
var message = function(message, callback) {
            switch (message) {
                case 'initialize':
                callback('initialize', true)
                break;
                case `start`:
                callback('presentViewController')
                break;
            }
        }
'''

xml = '''
<UIStackView
        alignment="center"
        distribution="fillEqually"
        axis="vertical"
        width="100%"
        height="{height}"
        top="{navBarHeight}"
        spacing="0">
        <UIView
            backgroundColor="purple">
            <UIButton
                title="firstproduct"
                top="10"
                left="10"
                tag="0"
                touchUpInside="wasPressedtag:"/>
            <UIImageView
                image="{image0}"
                contentMode="scaleAspectFit"
                width="100"
                height="100"
                top="50"
                left="10"/>
        </UIView>
        <UIView
            backgroundColor="green">
            <UIButton
                title="secondproduct"
                top="10"
                left="10"
                tag="1"
                touchUpInside="wasPressedtag:"/>
            <UIImageView
                image="{image1}"
                width="100"
                height="100"
                top="50"
                left="10"/>
        </UIView>
        <UIView
            backgroundColor="blue">
            <UIButton
                title="thirdproduct"
                top="10"
                left="10"
                tag="2"
                touchUpInside="wasPressedtag:"/>
            <UIImageView
                image="{image2}"
                width="100"
                height="100"
                top="50"
                left="10"/>
        </UIView>
        <UIView
            backgroundColor="yellow">
            <UIButton
                title="thirdproduct"
                top="10"
                left="10"
                tag="3"
                touchUpInside="wasPressedtag:"/>
            <UIImageView
                image="{image3}"
                width="100"
                height="100"
                top="50"
                left="10"/>
        </UIView>
    </UIStackView>
'''

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
        # Extract values from the query string
        path, _, _ = self.path.partition('?')
   
        print('path :' + path)
        print('ROUTE_PRODUCT_LIST_COORDINATOR :' + ROUTE_PRODUCT_LIST_COORDINATOR)

        # Handle the possible request paths
        if path == ROUTE_PRODUCT_LIST_COORDINATOR:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(js)
        elif path == ROUTE_PRODUCT_LIST_LAYOUT:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(xml)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write('Path is Not Found' + path + "=!" + ROUTE_PRODUCT_LIST_COORDINATOR)

if __name__ == '__main__':
    port = 80
    httpd = HTTPServer(('', port), PostHandler)
    print('Listening on :' + str(port))
    httpd.serve_forever()
