# 动态脚本 Dynamic Script

使用 `<script>` 元素可以向页面中插入 JavaScript 代码，一种方式是通过其 src 特性包含外部文件，另一种方式就是用这个元素本身来包含代码。

动态脚本指定是在页面加载时不存在，但将来的某一时刻通过修改 DOM 动态添加的脚本。跟操作 HTML 元素一样，创建动态脚本也有两种方式：插入外部文件和直接插入 JavaScript 代码。

动态加载的外部 JavaScript 文件能够立即运行，比如下面的 `<script>` 元素

```html
<script type="text/javascript" src="client.js"></script>
```

创建这个节点的 DOM 代码如下

```js
var script = document.createElement('script')
script.type = 'text/javascript'
script.src = client
document.body.appendChild(script)
```

在执行最后一行代码把 `<script>` 元素添加到页面中之前，是不会下载外部文件的。也可以把 `<script>` 元素添加到 `<head>` 元素中，效果相同。

整个过程可以使用下面的函数来封装：

```js
function loadScript(url) {
  var script = document.createElement('script')
  script.type = 'text/javascript'
  script.src = url
  document.body.appendChild(script)
}
```

然后就可以调用这个函数来加载外部的 JavaScript 文件了

```js
loadScript('client.js')
```

另一种指定 JavaScript 代码的方式是行内方式，如下例所示：

```html
<script type="text/javascript">
  function sayHi() {
    alert('hi')
  }
</script>
```

从逻辑上讲，下面的 DOM 代码是有效的

```js
var script = document.createElement('script')
script.type = 'text/javascript'
script.appendChild(document.createTextNode("function sayHi(){alert('hi');}"))
document.body.appendChild(script)
```

在 Firefox、Safari、Chrome 和 Opera 中，这些 DOM 代码可以正常运行。但在 IE 中，则会导致错误。IE 将 `<script>` 设为一个特殊的元素，不允许 DOM 访问其子节点。不过，可以使用 `<script>` 元素的 `text` 属性来指定 JavaScript 代码。

```js
var script = document.createElement('script')
script.type = 'text/javascript'
script.text = "function sayHi(){alert('hi');}"
document.body.appendChild(script)
```

经过这样修改之后的代码可以在 IE、Firefox、Opera 和 Safari 3 及之后版本中运行。Safari 3.0  之前的版本虽然不能正确地支持 `text` 属性，但却允许使用文本节点技术来指定代码。如果需要兼容早期版本的 Safari，可以使用下列代码

```js
var script = document.createElement('script')
script.type = 'text/javascript'
var code = "function sayHi(){alert('hi');}"
try {
  script.appendChild(document.createTextNode(code))
} catch (ex) {
  script.text = code
}
document.body.appendChild(script)
```

这里，首先尝试标准的 DOM 文本节点方法，因为除了 IE（在 IE 中会导致抛出错误），所有浏览器都支持这种方式。如果这行代码抛出了错误，那就说明是 IE，于是就必须使用 `text` 属性了。

整个过程可以用以下函数来封装

```js
function loadScriptString(code) {
  var script = document.createElement('script')
  script.type = 'text/javascript'
  try {
    script.appendChild(document.createTextNode(code))
  } catch (ex) {
    script.text = code
  }
  document.body.appendChild(script)
}
```

下面是调用这个函数的示例

```js
loadScriptString("function sayHi(){alert('hi');}")
```

以这种方式加载的代码会在全局作用域中执行，而且当脚本执行后将立即可用。实际上，这样执行代码与在全局作用域中把相同的字符串传递给 `evea()` 是一样的。