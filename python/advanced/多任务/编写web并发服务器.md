# 编写 Web 并发服务器

## 1. 案例 - 多线程版 Web 服务器

```py
import socket
import threading


def request_handler(conn):
    request = conn.recv(1024)

    if not request:
        return

    # 返回 http 格式的数据给浏览器
    response = 'HTTP/1.1 200 OK\r\n'  # 状态行
    response += 'Content-Type: text/html; charset=utf-8\r\n'  # header
    response += '\r\n'  # 空行
    response += '<h1>hello world</h1>'  # 响应体
    conn.send(response.encode())

    conn.close()


if __name__ == '__main__':
    HOST = ''
    PORT = 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(128)
        while True:
            conn, addr = s.accept()
            print(f'客户端 {addr} 连接到服务器')

            t = threading.Thread(target=request_handler, args=(conn,), daemon=True)
            t.start()
```

## 2. 案例 - 多进程版 Web 服务器

```py
import socket
import multiprocessing


def request_handler(conn):
    request = conn.recv(1024)

    if not request:
        return

    # 返回 http 格式的数据给浏览器
    response = 'HTTP/1.1 200 OK\r\n'  # 状态行
    response += 'Content-Type: text/html; charset=utf-8\r\n'  # header
    response += '\r\n'  # 空行
    response += '<h1>hello world</h1>'  # 响应体
    conn.send(response.encode())

    conn.close()


if __name__ == '__main__':
    HOST = ''
    PORT = 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(128)
        while True:
            conn, addr = s.accept()
            print(f'客户端 {addr} 连接到服务器')

            p = multiprocessing.Process(target=request_handler, args=(conn,))
            p.start()

            # 这里需要加入 conn.close(), 否则浏览器的重新加载按钮会一直转圈
            # 原因:
            # 子进程会拷贝主进程的资源
            # 主进程和子进程的 conn 对象对应同一个文件描述符 (file descriptor)
            # 导致引入计数 +2, 所以需要 close() 两次
            conn.close()
```

## 3. 案例 - gevent 版 Web 服务器

```py
import socket
import gevent
from gevent import monkey

monkey.patch_all()


def request_handler(conn):
    request = conn.recv(1024)

    if not request:
        return

    # 返回 http 格式的数据给浏览器
    response = 'HTTP/1.1 200 OK\r\n'  # 状态行
    response += 'Content-Type: text/html; charset=utf-8\r\n'  # header
    response += '\r\n'  # 空行
    response += '<h1>hello world</h1>'  # 响应体
    conn.send(response.encode())

    conn.close()


if __name__ == '__main__':
    HOST = ''
    PORT = 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(128)
        while True:
            conn, addr = s.accept()
            gevent.spawn(request_handler, conn)
            # 主线程没退出, 所以这里不需要加上 g.join()
```

## 4. 单进程・单线程・非阻塞实现并发的原理

```py
import socket

if __name__ == '__main__':
    HOST = ''
    PORT = 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(128)

        # 设置 socket 非阻塞
        s.setblocking(False)

        conn_list = list()

        while True:
            try:
                conn, addr = s.accept()
            except:  # 没有新客户端连接
                pass
            else:  # 有新客户端连接
                conn.setblocking(False)  # 设置 socket 非阻塞
                conn_list.append(conn)

            for c in conn_list:
                try:
                    data = c.recv(1024)
                except:  # 当前客户端没有发送数据
                    pass
                else:
                    if data:  # 当前客户端发送了数据
                        pass
                    else:  # 客户端调用 close 导致接收数据为空
                        # 关闭 conn socket, 并从列表中移除
                        c.close()
                        conn_list.remove(c)
```

## 5. 案例 - 单进程・单线程・非阻塞・长连接实现 Web 服务器

长连接的响应头要包含 `Content-Length` 告诉浏览器传输数据的大小，否则浏览器会一直等待数据。

```py
import socket


def request_handler(conn, request):
    if not request:
        return

    # 返回 http 格式的数据给浏览器
    # 响应体
    response_body = '<h1>hello world</h1>'
    # 响应头
    response_header = 'HTTP/1.1 200 OK\r\n'  # 状态行
    response_header += 'Content-Type: text/html; charset=utf-8\r\n'  # header
    response_header += f'Content-Length: {len(response_body)}\r\n'
    response_header += '\r\n'  # 空行

    response = (response_header + response_body).encode()
    conn.send(response)

    # 长连接, 客户端先关闭时才能关闭
    # conn.close()


if __name__ == '__main__':
    HOST = ''
    PORT = 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(128)

        # 设置 socket 非阻塞
        s.setblocking(False)

        conn_list = list()

        while True:
            try:
                conn, addr = s.accept()
            except:  # 没有新客户端连接
                pass
            else:  # 有新客户端连接
                conn.setblocking(False)  # 设置 socket 非阻塞
                conn_list.append(conn)

            for c in conn_list:
                try:
                    data = c.recv(1024)
                except:  # 当前客户端没有发送数据
                    pass
                else:
                    if data:  # 当前客户端发送了数据
                        request_handler(conn, data)
                    else:  # 客户端调用 close 导致接收数据为空
                        # 关闭 conn socket, 并从列表中移除
                        c.close()
                        conn_list.remove(c)
```
