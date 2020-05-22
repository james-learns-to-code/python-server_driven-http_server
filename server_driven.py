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

jsOpen = '''
var img0 = "https://loveandpop.kr/web/product/medium/20200210/3a741bdb02e4aeeee56651aa1fb12d8c.jpg"
var img1 = "https://loveandpop.kr/web/product/medium/20200211/344df0d9732de6b280017a691e4e2c79.jpg"
var img2 = "https://loveandpop.kr/web/product/medium/20200513/a28ccff77e9d498a4e182e91de75d455.jpg"
var img3 = "https://www.bebeche.com/web/product/medium/20200507/43362e929b0571550a13b98ba504c20e.jpg"
var img4 = "https://www.bebeche.com/web/product/medium/20200221/83b7b2b533c1bbe1f2c49002e6d6f9d1.jpg"
var img5 = "https://www.bebeche.com/web/product/medium/20191115/9647b226232c493c6644ca68cf48aaf2.jpg"

var imgURL0 = 'https://loveandpop.kr/product/detail.html?product_no=3965&cate_no=46&display_group=2'
var imgURL1 = 'https://loveandpop.kr/product/detail.html?product_no=1655&cate_no=46&display_group=2'
var imgURL2 = 'https://loveandpop.kr/product/detail.html?product_no=4714&cate_no=46&display_group=1'
var imgURL3 = 'https://www.bebeche.com/product/2colors-%EB%AF%B9%EC%8A%A4-%EB%9E%A9-%EC%8A%A4%ED%8A%B8%EB%9D%BC%EC%9D%B4%ED%94%84%EA%B0%80%EB%94%94%EA%B1%B4cd/3890/category/138/display/1'
var imgURL4 = 'https://www.bebeche.com/product/3colors-%EC%A1%B4-%ED%94%84%EB%A6%B0%ED%8C%85%EB%B0%95%EC%8A%A4%EB%A7%A8%ED%88%AC%EB%A7%A8mtm/3712/category/138/display/1'
var imgURL5 = 'https://www.bebeche.com/product/%EB%AC%B4%EB%A3%8C%EB%B0%B0%EC%86%A1-3colors-%EB%A8%B8%EB%9E%AD-%EC%88%8F%EC%95%BC%EC%83%81%ED%9B%84%EB%93%9C%EC%9E%90%EC%BC%93jk/3735/category/139/display/1'

var message = function(message, callback, tag) {
    // callback('eventName', 'XML URL', '[IMG URL]')
    switch (message) {
        case 'tapEvent':
            switch (tag) {
                case 1:
                    callback('push', 'http://49.50.172.34/product/list/layout.xml', [img0, img1, img2, img3, img4, img5])
                    break;
                case 2:
                    callback('pop')
                    break;
                case 3:
                    callback('present', 'http://49.50.172.34/product/list/layout.xml')
                    break;
                case 4:
                    callback('dismiss')
                    break;
                case 10:
                    callback('openURL', imgURL0)
                    break;
                case 11:
                    callback('openURL', imgURL1)
                    break;
                case 12:
                    callback('openURL', imgURL2)
                    break;
                case 13:
                    callback('openURL', imgURL3)
                    break;
                case 14:
                    callback('openURL', imgURL4)
                    break;
                case 15:
                    callback('openURL', imgURL5)
                    break;
                default:
                    break;
            }
        default:
            break;
            
    }
}
'''

jsMove = '''
var img0 = "https://loveandpop.kr/web/product/medium/20200210/3a741bdb02e4aeeee56651aa1fb12d8c.jpg"
var img1 = "https://loveandpop.kr/web/product/medium/20200211/344df0d9732de6b280017a691e4e2c79.jpg"
var img2 = "https://loveandpop.kr/web/product/medium/20200513/a28ccff77e9d498a4e182e91de75d455.jpg"
var img3 = "https://www.bebeche.com/web/product/medium/20200507/43362e929b0571550a13b98ba504c20e.jpg"
var img4 = "https://www.bebeche.com/web/product/medium/20200221/83b7b2b533c1bbe1f2c49002e6d6f9d1.jpg"
var img5 = "https://www.bebeche.com/web/product/medium/20191115/9647b226232c493c6644ca68cf48aaf2.jpg"

var imgURL0 = 'https://loveandpop.kr/product/detail.html?product_no=3965&cate_no=46&display_group=2'
var imgURL1 = 'https://loveandpop.kr/product/detail.html?product_no=1655&cate_no=46&display_group=2'
var imgURL2 = 'https://loveandpop.kr/product/detail.html?product_no=4714&cate_no=46&display_group=1'
var imgURL3 = 'https://www.bebeche.com/product/2colors-%EB%AF%B9%EC%8A%A4-%EB%9E%A9-%EC%8A%A4%ED%8A%B8%EB%9D%BC%EC%9D%B4%ED%94%84%EA%B0%80%EB%94%94%EA%B1%B4cd/3890/category/138/display/1'
var imgURL4 = 'https://www.bebeche.com/product/3colors-%EC%A1%B4-%ED%94%84%EB%A6%B0%ED%8C%85%EB%B0%95%EC%8A%A4%EB%A7%A8%ED%88%AC%EB%A7%A8mtm/3712/category/138/display/1'
var imgURL5 = 'https://www.bebeche.com/product/%EB%AC%B4%EB%A3%8C%EB%B0%B0%EC%86%A1-3colors-%EB%A8%B8%EB%9E%AD-%EC%88%8F%EC%95%BC%EC%83%81%ED%9B%84%EB%93%9C%EC%9E%90%EC%BC%93jk/3735/category/139/display/1'

var message = function(message, callback, tag) {
    // callback('eventName', 'XML URL', '[IMG URL]')
    switch (message) {
        case 'tapEvent':
            switch (tag) {
                case 1:
                    callback('push', 'http://49.50.172.34/product/list/layout.xml', [img0, img1, img2, img3, img4, img5])
                    break;
                case 2:
                    callback('pop')
                    break;
                case 3:
                    callback('present', 'http://49.50.172.34/product/list/layout.xml')
                    break;
                case 4:
                    callback('dismiss')
                    break;
                case 10:
                    callback('moveURL', imgURL0)
                    break;
                case 11:
                    callback('moveURL', imgURL1)
                    break;
                case 12:
                    callback('moveURL', imgURL2)
                    break;
                case 13:
                    callback('moveURL', imgURL3)
                    break;
                case 14:
                    callback('moveURL', imgURL4)
                    break;
                case 15:
                    callback('moveURL', imgURL5)
                    break;
                default:
                    break;
            }
        default:
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
            backgroundColor="white">
            <UIImageView
                image="{image0}"
                width="100"
                height="100"
                top="10"
                left="20" />
            <UIButton
                title="주카 체크남방"
                titleColor="black"
                top="20"
                left="135"
                tag="10"
                touchUpInside="wasPressedtag:"/>
            <UILabel
                text="박시한 핏으로 편안하게 코디할수 있어요."
                textColor="gray"
                font="11"
                left="135"
                top="50" />
            <UILabel
                text="19,500원"
                left="135"
                font="bold"
                top="80" />
        </UIView>
        <UIView
            backgroundColor="white">
            <UIView
                backgroundColor="gray"
                width="95%"
                center.x="50%"
                height="1"/>
            <UIImageView
                image="{image1}"
                width="100"
                height="100"
                top="10"
                left="20"/>
            <UIButton
                title="하리 셔츠"
                titleColor="black"
                top="20"
                left="135"
                tag="11"
                touchUpInside="wasPressedtag:"/>
            <UILabel
                text="둥근카라가 매력적인 워싱 셔츠에요."
                textColor="gray"
                font="11"
                left="135"
                top="50" />
            <UILabel
                text="28,500원"
                left="135"
                font="bold"
                top="80"/>
        </UIView>
        <UIView
            backgroundColor="white">
            <UIView
                backgroundColor="gray"
                width="95%"
                center.x="50%"
                height="1"/>
            <UIImageView
                image="{image2}"
                width="100"
                height="100"
                top="10"
                left="20"/>
            <UIButton
                title="린넨꽃나시"
                titleColor="black"
                top="20"
                left="135"
                tag="12"
                touchUpInside="wasPressedtag:"/>
            <UILabel
                text="잔꽃무늬라 은은하게 포인트 코디할수 있어요!"
                textColor="gray"
                font="11"
                left="135"
                top="50"/>
            <UILabel
                text="13,000원"
                left="135"
                font="bold"
                top="80"/>
        </UIView>
        <UIView
            backgroundColor="white">
            <UIView
                backgroundColor="gray"
                width="95%"
                center.x="50%"
                height="1"/>
            <UIImageView
                image="{image3}"
                width="100"
                height="100"
                top="10"
                left="20"/>
            <UIButton
                title="믹스 랩 스트라이프가디건cd"
                titleColor="black"
                top="20"
                left="135"
                tag="13"
                touchUpInside="wasPressedtag:"/>
            <UILabel
                text="전체적으로 들어간 스트라이프 패턴으로 캐주얼한 무드를 연출해주었어요"
                font="11"
                textColor="gray"
                left="135"
                numberOfLines="0"
                right="20"
                top="50"/>
            <UILabel
                text="35,000원"
                left="135"
                font="bold"
                top="80"/>
        </UIView>
        <UIView
            backgroundColor="white">
            <UIView
                backgroundColor="gray"
                width="95%"
                center.x="50%"
                height="1"/>
            <UIImageView
                image="{image4}"
                width="100"
                height="100"
                top="10"
                left="20"/>
            <UIButton
                title="존 프린팅박스맨투맨mtm"
                titleColor="black"
                top="20"
                left="135"
                tag="14"
                touchUpInside="wasPressedtag:"/>
            <UILabel
                text="캐주얼한 무드의 박스핏맨투맨"
                font="11"
                textColor="gray"
                left="135"
                top="50"/>
            <UILabel
                text="28,000원"
                font="bold"
                left="135"
                top="80"/>
        </UIView>
        <UIView
            backgroundColor="white">
            <UIView
                backgroundColor="gray"
                width="95%"
                center.x="50%"
                height="1"/>
            <UIImageView
                image="{image5}"
                width="100"
                height="100"
                top="10"
                left="20"/>
            <UIButton
                title="머랭 숏야상후드자켓jk"
                titleColor="black"
                top="20"
                left="135"
                tag="15"
                touchUpInside="wasPressedtag:"/>
            <UILabel
                text="숏한 기장감에 후드 디테일로 캐주얼하면서 발랄한 무드를 연출해주었어요"
                font="11"
                numberOfLines="0"
                textColor="gray"
                left="135"
                right="20"
                top="50"/>
            <UILabel
                text="65,000원"
                font="bold"
                left="135"
                top="80"/>
        </UIView>
    </UIStackView>
'''

isMove = False

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
            global isMove
            js = jsMove if isMove == True else jsOpen
            self.wfile.write(bytes(js, 'utf-8'))
            isMove = False if isMove == True else True
        elif path == ROUTE_PRODUCT_LIST_LAYOUT:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(xml, 'utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Path is Not Found')

if __name__ == '__main__':
    port = 80
    httpd = HTTPServer(('', port), PostHandler)
    print('Listening on :' + str(port))
    httpd.serve_forever()
