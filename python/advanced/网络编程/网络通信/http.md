# HTTP 协议

HTTP（HyperText Transfer Protocol 超文本传输协议）

HTTP 是应用层的协议，建立在 TCP 的基础上。

HTTP 负责如何包装数据，而 TCP 负责如何传输数据。


## 1. 消息 Message

HTTP 消息（message）分为请求（Request）和响应（Response）两类

![](images/http-msg-structure.png)

## 2. 请求 Request

由以下几部分组成

- 请求行（Request-line）如 `GET /hello.htm HTTP/1.1`
- 头部（header）
- 空行
- 可选的消息主体（message-body）

### 2.1. 示例

从 `tutorialspoint.com` 上运行的 Web 服务器获取 `hello.htm` 页面

```http
GET /hello.htm HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive
(空行)
```

使用消息主体将表单数据发送到服务器

```http
POST /cgi-bin/process.cgi HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Content-Type: application/x-www-form-urlencoded
Content-Length: (消息主体中的数据的实际长度)
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive
(空行)
licenseID=string&content=string&/paramsXML=string
```

将 XML 数据传递到 Web 服务器

```http
POST /cgi-bin/process.cgi HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Content-Type: text/xml; charset=utf-8
Content-Length: (消息主体中的数据的实际长度)
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive
(空行)
<?xml version="1.0" encoding="utf-8"?>
<string xmlns="http://clearforest.com/">string</string>
```

## 3. 响应 Response

由以下几部分组成：

- 状态行（Status-Line）如 `HTTP/1.1 200 OK`
- 头部（header）
- 空行
- 可选的消息主体（message body）

### 3.1. 示例

```http
HTTP/1.1 200 OK
Date: Sun, 10 Oct 2010 23:26:07 GMT
Server: Apache/2.2.8 (Ubuntu) mod_ssl/2.2.8 OpenSSL/0.9.8g
Last-Modified: Sun, 26 Sep 2010 22:04:35 GMT
ETag: "45b6-834-49130cc1182c0"
Accept-Ranges: bytes
Content-Length: 12
Connection: close
Content-Type: text/html

Hello world!
```

## 4. 方法 Method

- OPTIONS
- **GET**
- HEAD
- **POST**
- PUT
- DELETE
- TRACE
- CONNECT

## 5. 状态码 Status Code

### 5.1. 信息 Informational

1xx

| 状态码 |      状态信息       |   描述   |
| :----: | :-----------------: | :------: |
|  100   |      Continue       |   继续   |
|  101   | Switching Protocols | 切换协议 |

### 5.2. 成功 Success

2xx

| 状态码 |           状态信息            |    描述    |
| :----: | :---------------------------: | :--------: |
|  200   |              OK               |    成功    |
|  201   |            Created            |   已创建   |
|  202   |           Accepted            |   已接受   |
|  203   | Non-Authoritative Information | 非授权信息 |
|  204   |          No Content           |   无内容   |
|  205   |         Reset Content         |  重置内容  |
|  206   |        Partial Content        |  部分内容  |

### 5.3. 重定向 Redirection

3xx

| 状态码 |      状态信息      |     描述     |
| :----: | :----------------: | :----------: |
|  300   |  Multiple Choices  |   多种选择   |
|  301   | Moved Permanently  |   永久移动   |
|  302   |       Found        |   临时移动   |
|  303   |     See Other      | 查看其他位置 |
|  304   |    Not Modified    |    未修改    |
|  305   |     Use Proxy      |   使用代理   |
|  307   | Temporary Redirect |  临时重定向  |

### 5.4. 客户端错误 Client Error

4xx

| 状态码 |            状态信息             |        描述        |
| :----: | :-----------------------------: | :----------------: |
|  400   |           Bad Request           |      错误请求      |
|  401   |          Unauthorized           |       未授权       |
|  403   |            Forbidden            |        禁止        |
|  404   |            Not Found            |       未找到       |
|  405   |       Method Not Allowed        |      方法禁用      |
|  406   |         Not Acceptable          |       不接受       |
|  407   |  Proxy Authentication Required  |    需要代理授权    |
|  408   |         Request Timeout         |      请求超时      |
|  409   |            Conflict             |        冲突        |
|  410   |              Gone               |       已删除       |
|  411   |         Length Required         |    需要有效长度    |
|  412   |       Precondition Failed       |   未满足前提条件   |
|  413   |    Request Entity Too Large     |    请求实体过大    |
|  414   |      Request-URI Too Long       |  请求的 URI 过长   |
|  415   |     Unsupported Media Type      |  不支持的媒体类型  |
|  416   | Requested Range Not Satisfiable | 请求范围不符合要求 |
|  417   |       Expectation Failed        |    未满足期望值    |

### 5.5. 服务器错误 Server Error

5xx

| 状态码 |          状态信息          |       描述        |
| :----: | :------------------------: | :---------------: |
|  500   |   Internal Server Error    |  服务器内部错误   |
|  501   |      Not Implemented       |     尚未实施      |
|  502   |        Bad Gateway         |     错误网关      |
|  503   |    Service Unavailable     |    服务不可用     |
|  504   |      Gateway Timeout       |     网关超时      |
|  505   | HTTP Version Not Supported | HTTP 版本不受支持 |

## 6. 头字段 Header Field

头字段根据实际用途被分为以下 4 种类型：

- 通用头字段
- 请求头字段
- 响应头字段
- 实体头字段

### 6.1. 通用头字段 General Header Field

|   字段名   |             描述             | 示例                                             |
| :--------: | :--------------------------: | ------------------------------------------------ |
| Connection | 控制网络连接是否保持打开状态 | `Connection: keep-alive` <br>`Connection: close` |
|    Date    |     消息起源的日期和时间     | `Date: Tue, 15 Nov 1994 08:12:31 GMT`            |

### 6.2. 请求头字段 Request Header Field

|     字段名      |                          描述                           | 示例                                                                                                                       |
| :-------------: | :-----------------------------------------------------: | -------------------------------------------------------------------------------------------------------------------------- |
|     Accept      |                   可接受的 MIME 类型                    | `Accept: text/html` <br>`Accept: image/*` <br>`Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8` |
| Accept-Charset  |                     可接受的字符集                      | `Accept-Charset: utf-8` <br>`Accept-Charset: utf-8, iso-8859-1;q=0.5, *;q=0.1`                                             |
| Accept-Encoding |                    可接受的编码方式                     | `Accept-Encoding: gzip, deflate` <br>`Accept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1`                                      |
| Accept-Language |                      可接受的语言                       | `Accept-Language: en-US` <br>`Accept-Language: da, en-gb;q=0.8, en;q=0.7`                                                  |
|     Cookie      | 包含服务器通过 `Set-Cookie` 标题头存储到客户端的 cookie | `Cookie: PHPSESSID=298zf09hf012fh2; csrftoken=u32t4o3tb3gg43; _gat=1;`                                                     |
|      Host       |            服务器的域名及其监听的 TCP 端口号            | `Host: en.wikipedia.org:8080` <br>`Host: en.wikipedia.org`                                                                 |
|     Referer     |          链接到当前所请求页面的来源页面的地址           | `Referer: http://en.wikipedia.org/wiki/Main_Page`                                                                          |
|   User-Agent    |                发起请求的用户代理的信息                 | `User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0`                                         |

> `;q=` 代表优先级，默认值为 1

### 6.3. 响应头字段 Response Header Field

|    字段名     |                                               描述                                               | 示例                                                                                                                                    |
| :-----------: | :----------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------------------------------------------------------- |
| Accept-Ranges | 通告服务器支持部分请求的标识。若存在该头字段，浏览器可能会尝试恢复中断的下载，而不是从头再次开始 | `Accept-Ranges: bytes`                                                                                                                  |
|     ETag      |                                      资源的特定版本的标识符                                      | `ETag: "737060cd8c284d8af7ad3082f209582d"`                                                                                              |
|    Server     |                                            服务器名称                                            | `Server: Apache/2.4.1 (Unix)`                                                                                                           |
|  Set-Cookie   |                                   从服务器向客户端发送 cookie                                    | `Set-Cookie: sessionid=38afes7a8; HttpOnly; Path=/` <br>`Set-Cookie: id=a3fWa; Expires=Wed, 21 Oct 2015 07:28:00 GMT; Secure; HttpOnly` |

### 6.4. 实体头字段 Entity Header Field

|      字段名      |                                             描述                                             | 示例                                                                                           |
| :--------------: | :------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------- |
| Content-Encoding |                                       内容编码压缩类型                                       | `Content-Encoding: gzip`                                                                       |
| Content-Language |                                       内容所使用的语言                                       | `Content-Language: da`                                                                         |
|  Content-Length  |                                        内容的字节长度                                        | `Content-Length: 348`                                                                          |
|   Content-Type   | 内容的 MIME 类型。在响应中告知客户端实际返回数据的类型，在请求中告知服务器实际发送数据的类型 | `Content-Type: application/x-www-form-urlencoded` <br>`Content-Type: text/html; charset=utf-8` |
|  Last-Modified   |                                   内容最后修改的日期和时间                                   | `Last-Modified: Tue, 15 Nov 1994 12:45:26 GMT`                                                 |

## 7. 长连接与短连接

- 在 `HTTP/1.0` 中默认使用的是短连接。浏览器的每次请求都要求建立一次单独的连接，在处理完本次请求后，就自动释放连接。
- 在 `HTTP/1.1` 中默认使用的是长连接。可以在一次连接中处理多个请求，并且多个请求可以重叠进行，不需要等待一个请求结束后再发送下一个请求。服务器会在响应头中加入 `Connection: keep-alive`。

## 参考

- [HTTP 常用的状态码](https://xdwangiflytek.iteye.com/blog/1343395)
