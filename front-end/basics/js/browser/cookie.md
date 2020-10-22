# Cookie

HTTP 协议是一个是无状态协议，HTTP 协议自身不会对请求和响应之间的通信状态进行保存。

客户端会根据服务器发送的响应头里的 `Set-Cookie` 信息生成 Cookie。当下次客户端再向该服务器发送请求时，会自动在请求中加入 Cookie 值。

服务器发现客户端发送过来的 Cookie 后，会去检查究竟是从哪个客户端发来的连接请求，然后在对比服务器上的记录，最后得到之前的状态信息。

## 语法

读取当前可访问的所有 cookie

```js
allCookies = document.cookie
// allCookies 是一个字符串，\
// 其包含了由分号分隔的所有 cookie 的列表
// 格式 "cookie1=value1; cookie2=value2;"
```

写入一个新 cookie

```js
document.cookie = newCookie
// newCookie 是一个 key=value 形式的字符串
// 使用该方法一次只能设置／更新一个 cookie

// 以下可选的 cookie attribute 值可跟在键值对后，以分号作分隔

// @路径
// ;path=path
// 例如 '/', '/mydir'
// 如未指定，则默认为当前文档位置的路径。

// @域名
// ;domain=domain
// 例如 'example.com', 'subdomain.example.com'
// 如未指定，则默认为当前文档位置的 host 部分。

// @有效期
// ;expires=date-in-GMTString-format
// 如 expires 和 max-age 都未指定，cookie 会在会话结束时到期
// 值的形式参考 Date.prototype.toUTCString()
// 如：Sat, 27 Aug 2016 19:33:32 GMT

// ;max-age=max-age-in-seconds
// 例如 60*60*24*365, 31536000

// @安全
// ;secure
// cookie 只通过 https 协议传输

// ;samesite
// strict - 严格
// lax - 宽松

// cookie 的值字符串可以用 encodeURIComponent() 来保证它不包含任何逗号、分号或空白
// cookie 值中禁止使用这些值
```

## 案例

简单用法

```html
<button onclick="alertCookie()">Show cookies</button>
```

```js
document.cookie = 'name=oeschger'
document.cookie = 'favorite_food=tripe'
function alertCookie() {
  alert(document.cookie)
}
// 显示: name=oeschger; favorite_food=tripe
```

获取名为 test2 的 cookie

```html
<button onclick="alertCookieValue()">Show cookie value</button>
```

```js
document.cookie = 'test1=Hello'
document.cookie = 'test2=World'

var cookieValue = document.cookie.replace(
  /(?:(?:^|.*;\s*)test2\s*\=\s*([^;]*).*$)|^.*$/,
  '$1'
)

function alertCookieValue() {
  alert(cookieValue)
}
// 显示: World
```

## 第三方库

+ [Simple cookie framework](https://github.com/madmurphy/cookies.js) - Simple cookie framework with full Unicode support
+ [js-cookie](https://github.com/js-cookie/js-cookie) -  A simple, lightweight JavaScript API for handling cookies

## 参考

- [Document.cookie - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie)
