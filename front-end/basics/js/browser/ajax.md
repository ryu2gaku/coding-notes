# Ajax

Ajax 的全称是 Asynchronous JavaScript and XML，即异步 JavaScript 和 XML。

## XMLHttpRequest

---

<p align="center">XMLHttpRequest ➠ XMLHttpRequestEventTarget ➠ EventTarget</p>

---

构造器

```js
new XMLHttpRequest(): XMLHttpRequest
```

XMLHttpRequest オブジェクトを作成する関数

```js
// Internet Explorer 6 以前では、
//「ActiveX オブジェクト」を利用する必要があります。
function XMLHttpRequestCreate() {
  // XMLHttpRequest オブジェクトを作成
  try {
    return new XMLHttpRequest()
  } catch (e) {}

  // Internet Explorer 6 用
  try {
    return new ActiveXObject('MSXML2.XMLHTTP.6.0')
  } catch (e) {}
  try {
    return new ActiveXObject('MSXML2.XMLHTTP.3.0')
  } catch (e) {}
  try {
    return new ActiveXObject('MSXML2.XMLHTTP')
  } catch (e) {}

  // 未対応
  return null
}
```

### 事件处理程序 Event Handler

▎XMLHttpRequest.**onreadystatechange** - EventHandler - XHR 通信の状態が変化するたびに実行される

```js
const xhr = new XMLHttpRequest(),
  method = 'GET',
  url = 'https://developer.mozilla.org/'

xhr.open(method, url, true)
xhr.onreadystatechange = function() {
  if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
    console.log(xhr.responseText)
  }
}
xhr.send()
```

### 状态

▎XMLHttpRequest.**readyState** - _readonly_ - XHR 通信の状態を取得する

```js
XMLHttpRequest.UNSENT = 0 // open() 方法还未被调用
XMLHttpRequest.OPENED = 1 // open() 方法已被调用
XMLHttpRequest.HEADERS_RECEIVED = 2 // send() 方法已被调用，已获取响应头
XMLHttpRequest.LOADING = 3 // 正在获取响应体
XMLHttpRequest.DONE = 4 // 操作结束
```

### 请求 Request

▎XMLHttpRequest.**open**

```ts
client.open(
  method: ByteString,
  url: USVString,
  async: boolean = true,
  username: USVString | null = null,
  password: USVString | null = null
): void

// @参数 async
// 是否使用异步请求
```

▎XMLHttpRequest.**setRequestHeader** - HTTP リクエストヘッダーの値を設定します

```ts
client.setRequestHeader(
  name: ByteString,
  value: ByteString
): void

// open()の呼び出しの後、send()の呼び出しの前に呼び出さなければなりません
```

▎XMLHttpRequest.**timeout** - 超时时间（ms）

```js
var xhr = new XMLHttpRequest()
xhr.open('GET', '/server', true)

xhr.timeout = 2000 // time in milliseconds

xhr.onload = function() {
  // Request finished. Do processing here.
}
xhr.ontimeout = function(e) {
  // XMLHttpRequest timed out. Do something here.
}
xhr.send(null)
```

▎XMLHttpRequest.**send** - リクエストをサーバーに送信します

```ts
client.send(
  body: Document | BodyInit | null = null
): void

// @参数 body
// 请求体，如果请求类型是 GET 或 HEAD 时则忽略

type BodyInit = Blob | BufferSource | FormData | URLSearchParams | ReadableStream | USVString
```

▎XMLHttpRequest.**upload** - _readonly_ - XMLHttpRequestUpload

```ts
interface XMLHttpRequestUpload
  extends XMLHttpRequestEventTarget
```

▎XMLHttpRequest.**abort** - 停止请求

```ts
client.abort(): void
```

### 响应

▎XMLHttpRequest.**responseURL** - _readonly_

▎XMLHttpRequest.**status** - _readonly_ - 响应的状态码

▎XMLHttpRequest.**statusText** - _readonly_ - 响应的状态文本信息

▎XMLHttpRequest.**getResponseHeader** - 返回指定响应头

```ts
client.getResponseHeader(name: ByteString): ByteString | null
```

```js
var client = new XMLHttpRequest()
client.open('GET', 'unicorns-are-awesome.txt', true)
client.send()
client.onreadystatechange = function() {
  if (this.readyState == this.HEADERS_RECEIVED) {
    print(client.getResponseHeader('Content-Type'))
  }
}
// text/plain; charset=UTF-8
```

▎XMLHttpRequest.**getAllResponseHeaders** - 返回所有的响应头

```ts
client.getAllResponseHeaders(): ByteString

// 返回以 CRLF 分割的字符串，如果没有收到任何响应则返回 null，如果发生网络错误则返回 ""
// CRLF: CR(Carriage Return, 回车) LF(Line Feed, 换行)
```

```js
var client = new XMLHttpRequest()
client.open('GET', 'narwhals-too.txt', true)
client.send()
client.onreadystatechange = function() {
  if (this.readyState == this.HEADERS_RECEIVED) {
    print(this.getAllResponseHeaders())
  }
}
```

▎XMLHttpRequest.**overrideMimeType** - 重写响应 MIME 类型，必须在 `send` 之前设置

```ts
client.overrideMimeType(mime: DOMString): void
```

```js
// Interpret the received data as plain text

req = new XMLHttpRequest()
req.overrideMimeType('text/plain')
req.addEventListener('load', callback, false)
req.open('get', url)
req.send()
```

▎XMLHttpRequest.**responseType** - XMLHttpRequestResponseType

```ts
enum XMLHttpRequestResponseType {
  '',
  'arraybuffer',
  'blob',
  'document',
  'json',
  'text',
}
```

▎XMLHttpRequest.**response** - _readonly_

▎XMLHttpRequest.**responseText** - _readonly_

▎XMLHttpRequest.**responseXML** - _readonly_ - Document | null

## XMLHttpRequestEventTarget

---

<p align="center">XMLHttpRequestEventTarget ➠ EventTarget</p>

---

### Event Handler

▎XMLHttpRequestEventTarget.**onloadstart** - EventHandler - XHR 通信を開始したときに実行される

▎XMLHttpRequestEventTarget.**onprogress** - EventHandler - 受信中に繰り返し実行される

▎XMLHttpRequestEventTarget.**onabort** - EventHandler - XHR 通信を中止すると実行される

▎XMLHttpRequestEventTarget.**onerror** - EventHandler - XHR 送信が失敗したときに実行される（失敗時のみ）

▎XMLHttpRequestEventTarget.**onload** - EventHandler - XHR 送信が成功したときに実行される（成功時のみ）

▎XMLHttpRequestEventTarget.**ontimeout** - EventHandler - タイムアウトエラー発生時に実行される

▎XMLHttpRequestEventTarget.**onloadend** - EventHandler - XHR 通信が完了したときに実行される（成功失敗に関係無く）

`error`、`abort`、`timeout` 或 `load` 事件之一被触发后

```js
var xmlhttp = new XMLHttpRequest(),
  method = 'GET',
  url = 'https://developer.mozilla.org/'

xmlhttp.open(method, url, true)
xmlhttp.onprogress = function() {
  //do something
}
xmlhttp.onerror = function() {
  console.log('** An error occurred during the transaction')
}
xmlhttp.onload = function() {
  // Do something with the retrieved data (found in xmlhttp.response)
}
xmlhttp.send()
```

`readystatechange` 事件对应 `Event` 接口，而以上事件均对应 `ProgressEvent` 接口。

## ProgressEvent

---

<p align="center"> ProgressEvent ➠ Event</p>

---

▎ProgressEvent.**lengthComputable** - _readonly_ - boolean

▎ProgressEvent.**loaded** - _readonly_ - 已经传输的字节

▎ProgressEvent.**total** - _readonly_ - 需要传输的总字节

```js
var progressBar = document.getElementById('p'),
  client = new XMLHttpRequest()
client.open('GET', 'magical-unicorns')
client.onprogress = function(pe) {
  if (pe.lengthComputable) {
    progressBar.max = pe.total
    progressBar.value = pe.loaded
  }
}
client.onloadend = function(pe) {
  progressBar.value = pe.loaded
}
client.send()
```

## 参考

- [XMLHttpRequest Standard | Living Standard](https://xhr.spec.whatwg.org/)
- [XMLHttpRequest - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)
- [XMLHttpRequest について | JavaScript プログラミング講座](http://hakuhin.jp/js/xmlhttprequest.html)
