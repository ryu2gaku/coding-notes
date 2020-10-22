# 跨域

## 同源策略 Same-origin Policy

所谓同源是指两个页面具有相同的协议（protocol）、端口（port，如果有指定）和主机（host）

```sh
http://store.company.com/dir/page.html

http://store.company.com/dir2/other.html
# 同源，只有路径不同
http://store.company.com/dir/inner/another.htm
# 同源，只有路径不同
https://store.company.com/page.html
# 不同源，协议不同，http 与 https
http://store.company.com:81/dir/page.html
# 不同源，端口不同，http:// 默认端口为 80
http://news.company.com/dir/page.html
# 不同源，主机不同
```

同源策略控制了两个不同源之间的交互。

如果非同源，共有三种行为受到限制

- Cookie、LocalStorage 和 IndexDB 无法读取
- DOM 无法获得
- AJAX 请求不能发送

## Document.domain

这种方法只适用于 Cookie 和 iframe 窗口规避同源政策。

### Cookie

只有同源的网页才能共享 Cookie。两个网页二级域名相同，只是三级域名不同，浏览器允许通过设置 `document.domain` 来共享 Cookie。

```js
// A 网页 http://w1.example.com/a.html
// B 网页 http://w2.example.com/b.html
// 只要设置相同的 document.domain，两个网页就可以共享 Cookie
document.domain = 'example.com'

// A 网页通过脚本设置一个 Cookie
document.cookie = 'test1=hello'

// B 网页就可以读到这个 Cookie
var allCookie = document.cookie
```

### iframe

如果两个网页不同源，就无法拿到对方的 DOM。典型的例子是 `iframe` 窗口和 `window.open` 方法打开的窗口，它们与父窗口无法通信。

比如，父窗口运行下面的命令，如果 `iframe` 窗口不是同源，就会报错。

```js
document.getElementById('myIFrame').contentWindow.document
// Uncaught DOMException: Blocked a frame from accessing a cross-origin frame.
```

上面命令中，父窗口想获取子窗口的 DOM，因为跨源导致报错。

反之亦然，子窗口获取主窗口的 DOM 也会报错。

```js
window.parent.document.body
// 报错
```

如果两个窗口二级域名相同，只是三级域名不同，那么设置 `document.domain` 属性，就可以规避同源政策，拿到 DOM。

## JSON with Padding (JSONP)

JSONP 的基本思路是，由于 `<script>` 元素不受同源策略影响，网页通过添加一个 `<script>` 元素，向服务器请求 JSON 数据。服务器收到请求后，将数据放在一个指定名字的回调函数里传回来。

```js
function jsonp_cb(data) {
  console.log(data)
}

function ajax(url) {
  // HTMLScriptElement
  var script = document.createElement('script')
  script.src = url
  document.head.appendChild(script)
}

ajax('http://xxx.com/test.php?callback=jsonp_cb')
// 请求的查询字符串有一个 callback 参数, \
// 用来指定回调函数的名字, \
// 这对于 JSONP 是必需的
```

由 `<script>` 元素请求的脚本，直接作为代码运行。

服务端获得到 callback 传递的函数名 jsonp_cb，返回一段对该函数调用的 js 代码。

```php
<?php
echo $_GET['callback']."({\"name\": \"ryugaku\", \"age\": 23})";
// 返回 jsonp_cb({"name": "ryugaku", "age": 23})
?>
```

## 跨域资源共享 Cross-origin Resource Sharing (CORS)

## 参考

- [浏览器同源政策及其规避方法 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2016/04/same-origin-policy.html)
- [跨域资源共享 CORS 详解 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2016/04/cors.html)
