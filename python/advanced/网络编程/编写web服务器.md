# 编写 Web 服务器

## 1. 案例 - 返回固定页面的 Web 服务器

```py
import socket


def request_handler(conn):
    # 接收浏览器发送过来的请求, 即 http 请求
    request = conn.recv(1024)
    print(request)

    if not request:
        return

    # 返回 http 格式的数据给浏览器
    response = 'HTTP/1.1 200 OK\r\n'  # 状态行
    response += 'Content-Type: text/html; charset=utf-8\r\n'  # header
    response += '\r\n'  # 空行
    response += '<h1>hello world</h1>'  # 响应体
    conn.send(response.encode())


if __name__ == '__main__':
    HOST = ''
    PORT = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(128)
        while True:
            conn, addr = s.accept()
            with conn:
                request_handler(conn)
```

使用 Chrome 访问 `127.0.0.1:8000` 来连接服务器，打印请求内容如下

```py
b'GET / HTTP/1.1\r\nHost: 127.0.0.1:8000\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36\r\nSec-Fetch-Dest: document\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9,ja;q=0.8,zh-TW;q=0.7,zh-HK;q=0.6,en-US;q=0.5,en;q=0.4\r\n\r\n'
```

```http
GET / HTTP/1.1
Host: 127.0.0.1:8000
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36
Sec-Fetch-Dest: document
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,ja;q=0.8,zh-TW;q=0.7,zh-HK;q=0.6,en-US;q=0.5,en;q=0.4
(空行)
(空行)
```

使用 Postman 附带表单数据访问 `127.0.0.1:8000` 来连接服务器，打印请求内容如下

```py
b'POST / HTTP/1.1\r\nContent-Type: application/x-www-form-urlencoded\r\ncache-control: no-cache\r\nPostman-Token: fea8a557-e9b1-496b-91c4-dff4634a3da2\r\nUser-Agent: PostmanRuntime/7.6.0\r\nAccept: */*\r\nHost: 127.0.0.1:8000\r\naccept-encoding: gzip, deflate\r\ncontent-length: 6\r\nConnection: keep-alive\r\n\r\nid=123'
```

```http
POST / HTTP/1.1
Content-Type: application/x-www-form-urlencoded
cache-control: no-cache
Postman-Token: fea8a557-e9b1-496b-91c4-dff4634a3da2
User-Agent: PostmanRuntime/7.6.0
Accept: */*
Host: 127.0.0.1:8000
accept-encoding: gzip, deflate
content-length: 6
Connection: keep-alive

id=123
```

### 1.1. 重新运行时产生的端口占用问题

上例浏览器连接服务器后，直接 `Ctrl-C` 再立刻重新运行程序会抛出异常 `Address already in use`

原因是服务器返回 HTTP 格式的数据给客户端后，在没有等待客户端调用 `close()` 的前提下先调用了 `close()` 断开连接，TCP 断开连接时，主动关闭端最后需要等待 2MSL（TIME-WAIT 状态）

解决办法除了更换端口外，上例代码部分修改如下

```py
if __name__ == '__main__':
    HOST = ''
    PORT = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 绑定前使用, 允许 socket 地址复用
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # setsockopt(level, option, value)
        # 参数 level 是被设置的选项的级别, \
        # 如果想要在套接字级别上设置选项, 就必须把 level 设置为 SOL_SOCKET
        # 参数 option 指定准备设置的选项
        # SO_REUSEADDR, 打开或关闭地址复用功能, \
        # 当 value 不等于 0 时打开, 否则关闭

        s.bind((HOST, PORT))
        s.listen(128)
```

## 2. 案例 - 返回浏览器请求页面的 Web 服务器

```py
import socket
import re


def request_handler(conn):
    # 接收浏览器发送过来的请求, 即 http 请求
    request = conn.recv(1024)

    if not request:
        return

    # 按行分割请求数据
    request_lines = request.decode().splitlines()
    # 提取请求行信息, 格式 GET /index.html HTTP/1.1
    # | [^xyz][^a-c] | 求反: 与不在字符集合中的任何单个字符匹配
    # |       *      | 匹配上一个元素零次或多次
    # |       +      | 匹配上一个元素一次或多次
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
    if ret:
        file_path = ret.group(1)
        if file_path == '/':
            file_path = '/index.html'

    # 返回 http 格式的数据给浏览器
    try:
        with open('public' + file_path, 'rb') as f:
            # 若打开文件成功, 发送文件内容
            html_content = f.read()
            response = 'HTTP/1.1 200 OK\r\n'  # 状态行
            response += '\r\n'  # 空行
            conn.send(response.encode())
            conn.send(html_content)
    except:
        # 若打开文件失败, 发送 404 页面
        response = 'HTTP/1.1 404 Not Found\r\n'
        response += '\r\n'
        response += '<h1>file not found</h1>'
        conn.send(response.encode())


if __name__ == '__main__':
    HOST = ''
    PORT = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(128)
        while True:
            conn, addr = s.accept()
            with conn:
                request_handler(conn)
```

```html
<!-- public/index.html -->
<h1>hello world</h1>
```

## 3. 案例 - 面向对象封装

```py
import socket
import re


class WebServer:
    def __init__(self):
        HOST = ''
        PORT = 8000

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(128)

        self.server_socket = server_socket

    def start(self):
        """启动 Web 服务器"""
        while True:
            conn, addr = self.server_socket.accept()
            with conn:
                self.request_handler(conn)

    def request_handler(self, conn):
        request = conn.recv(1024)

        if not request:
            return

        request_lines = request.decode().splitlines()
        ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
        if ret:
            file_path = ret.group(1)
            if file_path == '/':
                file_path = '/index.html'

        try:
            with open('public' + file_path, 'rb') as f:
                html_content = f.read()
                response = 'HTTP/1.1 200 OK\r\n'
                response += '\r\n'
                conn.send(response.encode())
                conn.send(html_content)
        except:
            response = 'HTTP/1.1 404 Not Found\r\n'
            response += '\r\n'
            response += '<h1>file not found</h1>'
            conn.send(response.encode())


if __name__ == '__main__':
    web_server = WebServer()
    web_server.start()
```

## 4. 案例 - 基础框架构建

逻辑关系

```
****************           *******************
   webServer                     app 模块
****************           *******************
   __init__                application(request)
    start()      request     处理并拼接响应报文
request_handler()  ↗↙
 调用 app 模块处理    response
```

目录结构

```
.
├── application
│   ├── __init__.py
│   └── app.py
├── public
│   ├── index.html
│   └── *.html
└── webserver.py
```

代码实现

```py
"""
webserver.py
"""
import socket
from application import app


class WebServer:
    def __init__(self):
        HOST = ''
        PORT = 8000

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(128)

        self.server_socket = server_socket

    def start(self):
        """启动 Web 服务器"""
        while True:
            conn, addr = self.server_socket.accept()
            with conn:
                self.request_handler(conn)

    def request_handler(self, conn):
        request = conn.recv(1024)

        if not request:
            return

        response = app.application('public', request)
        conn.send(response)


if __name__ == '__main__':
    web_server = WebServer()
    web_server.start()
```

```py
"""
application/app.py
"""
import re


def parse_request(request):
    """解析请求报文, 返回浏览器请求资源路径"""
    request_lines = request.decode().splitlines()
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
    if ret:
        file_path = ret.group(1)
        if file_path == '/':
            file_path = '/index.html'
        return file_path


def application(current_dir, request):
    file_path = parse_request(request)
    resource_path = current_dir + file_path

    try:
        with open(resource_path, 'rb') as f:
            html_content = f.read()
            response = 'HTTP/1.1 200 OK\r\n'
            response += '\r\n'
            return response.encode() + html_content
    except:
        response = 'HTTP/1.1 404 Not Found\r\n'
        response += '\r\n'
        response += '<h1>file not found</h1>'
        return response.encode()
```

## 5. 案例 - 基础框架构建 升级版

逻辑关系

```
****************           *******************
   webServer                     app 模块
****************           *******************
   __init__                application(request)
    start()      request  处理并调用模块拼接响应报文
request_handler()  ↗↙    status, body ↓↑ response
 调用 app 模块处理    response
                           *******************
                                utils 模块
                           *******************
                      create_http_response(status, body)
                       根据提供的状态和内容拼接 http 响应报文
```

目录结构

```
.
├── application
│   ├── __init__.py
│   ├── app.py
│   └── utils.py
├── public
│   ├── index.html
│   └── *.html
└── webserver.py
```

代码实现，其中 webserver.py 文件内容如上例

```py
"""
application/app.py
"""
import re
from application import utils


def parse_request(request):
    """解析请求报文, 返回浏览器请求资源路径"""
    request_lines = request.decode().splitlines()
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
    if ret:
        file_path = ret.group(1)
        if file_path == '/':
            file_path = '/index.html'
        return file_path


def application(current_dir, request):
    file_path = parse_request(request)
    resource_path = current_dir + file_path

    try:
        with open(resource_path, 'rb') as f:
            html_content = f.read()
            response = utils.create_http_response('200 OK', html_content)
    except:
        error_content = '<h1>file not found</h1>'.encode()
        response = utils.create_http_response('404 Not Found', error_content)

    return response
```

```py
"""
application/utils.py
"""
def create_http_response(status, body):
    response = f'HTTP/1.1 {status}\r\n'
    response += '\r\n'
    response = response.encode() + body
    return response
```

## 6. 案例 - 使用终端启动 Web 服务器

启动格式

```sh
$ python3 webserver.py 8000
# webserver.py 为 web 服务器文件
# 8000 为 web 服务器对外服务端口
```

代码实现，其中 application 目录下的 app.py 和 utils.py 文件内容如上例

```py
"""
webserver.py
"""
import socket
from application import app
import sys


class WebServer:
    def __init__(self, port):
        HOST = ''

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, port))
        server_socket.listen(128)

        self.server_socket = server_socket

    def start(self):
        """启动 Web 服务器"""
        while True:
            conn, addr = self.server_socket.accept()
            with conn:
                self.request_handler(conn)

    def request_handler(self, conn):
        request = conn.recv(1024)

        if not request:
            return

        response = app.application('public', request)
        conn.send(response)


def main():
    # 获取运行 python 文件时的命令行参数
    params = sys.argv

    if len(params) != 2:
        print('启动失败, 参数格式错误! 正确格式应为 python3 webserver.py 8000')
        return

    # ['webserver.py', '8000']
    if not params[1].isdigit():
        print('启动失败, 端口号不是一个纯数字')
        return

    port = int(params[1])

    web_server = WebServer(port)
    web_server.start()


if __name__ == '__main__':
    main()
```
