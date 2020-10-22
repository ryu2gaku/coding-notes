# TCP

TCP（Transmission Control Protocol 传输控制协议）

## 1. TCP 服务器

```py
import socket

if __name__ == "__main__":
    # 1. 创建一个 TCP/IP socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = ''  # 传入空字符串, 服务器将接受本机所有可用的 IPv4 地址
    PORT = 8000

    # 2. 绑定地址
    tcp_server_socket.bind((HOST, PORT))

    # 3. 使服务器可以接受连接请求
    tcp_server_socket.listen(128)
    # 使用 socket() 创建的 socket 默认是主动的, 使用 listen() 将其变为被动, 来接收别人的连接

    # 4. 阻塞并等待传入连接
    conn, addr = tcp_server_socket.accept()
    # 如果有客户端连接服务器, 会返回一个新的 socket 和客户端进行通信
    # conn 用来和客户端进行通信, 而 tcp_server_socket 只用来授受新的连接请求

    # 5. 收发数据
    message = conn.recv(1024)
    print(f'接收到的数据为: {message.decode()}')

    conn.send('已收到你的信息'.encode())

    # 6. 关闭 socket
    conn.close()
    tcp_server_socket.close()
```

```py
"""
1. socket.listen([backlog])

Enable a server to accept connections.

backlog 指定在拒绝连接之前, 操作系统可以挂起的最大连接数量
"""

"""
2. socket.accept()

Accept a connection.

The socket must be bound to an address and listening for connections.

返回值为 (conn, address) 其中 conn 是一个新的 socket, 用来接收和发送数据
"""

"""
3. socket.recv(bufsize[, flags])

Receive data from the socket.

bufsize 指定要接收的最大数据量

The return value is a bytes object representing the data received.
"""
```

### 1.1. 循环为多个客户端服务

```py
import socket

if __name__ == "__main__":
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = ''
    PORT = 8000

    tcp_server_socket.bind((HOST, PORT))

    tcp_server_socket.listen(128)

    while True:
        conn, addr = tcp_server_socket.accept()
        print(f'客户端 {addr} 连接到服务器')

        while True:
            data = conn.recv(1024)

            # 当接收到数据为空时, 表示客户端已经断开链接
            # 服务器也要断开连接
            if data:
                print(f'接收到客户端信息: {data.decode()}')
            else:
                print(f'客户端 {addr} 断开连接')
                break

        conn.close()

    # 关闭 socket
    tcp_server_socket.close()
```

使用 with 语句实现

```py
import socket

if __name__ == "__main__":
    HOST = ''
    PORT = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(128)

        while True:
            conn, addr = s.accept()
            print(f'客户端 {addr} 连接到服务器')

            with conn:
                while True:
                    data = conn.recv(1024)
                    if data:
                        print(f'接收到客户端信息: {data.decode()}')
                    else:
                        print(f'客户端 {addr} 断开连接')
                        break
```

## 2. TCP 客户端

```py
import socket

if __name__ == "__main__":
    # 1. 创建一个 TCP/IP socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = '127.0.0.1'
    PORT = 8000

    # 2. 连接服务器
    tcp_client_socket.connect((HOST, PORT))

    # 3. 收发数据
    message = input('> ')
    tcp_client_socket.send(message.encode())
    # tcp_client_socket.send(b'hello world')

    # 4. 关闭 socket
    tcp_client_socket.close()
```

```py
"""
1. socket.connect(address)

Connect to a remote socket at `address`.

地址家族 (address family) 为 AF_INET 的 address 格式为 (host, port)
"""

"""
2. socket.send(bytes[, flags])

Send data to the socket.

The socket must be connected to a remote socket.

Returns the number of bytes sent.
"""
```

使用 with 语句实现

```py
import socket

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        message = input('> ')
        s.send(message.encode())
```

## 3. 案例 - 文件下载器

```py
"""
client.py
"""
import socket

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # 将要下载的文件名发送到服务器
        file_name = input('请输入要下载的文件名: ')
        s.send(file_name.encode())

        # 将接收到的数据保存到一个文件中
        # 使用 wb 模式的 open() 来写入二进制数据
        with open('/Users/ryugaku/Desktop/' + file_name, 'wb') as f:
            while True:
                data = s.recv(1024)  # 1024=1k 1024**2=1M 1024**3=1G
                if data:
                    f.write(data)
                else:
                    break
```

```py
"""
server.py
"""
import socket


def send_file_to_client(conn, addr):
    # 接收客户端需要下载对文件名
    file_name = conn.recv(1024).decode()
    print(f'客户端 {addr} 需要下载的文件是: {file_name}')

    # 读取文件内容, 并发送给客户端
    try:
        with open(file_name, 'rb') as f:
            while True:
                content = f.read(1024)
                if content:
                    conn.send(content)
                else:
                    break
    except:
        print(f'文件 {file_name} 下载失败')
    else:
        print(f'文件 {file_name} 下载成功')


if __name__ == '__main__':
    HOST = ''
    PORT = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(128)

        while True:
            conn, addr = s.accept()
            print(f'客户端 {addr} 连接到服务器')
            with conn:
                send_file_to_client(conn, addr)
```
