# 动态样式 Dynamic Style

能够把 CSS 样式包含到 HTML 页面中的元素有两个。其中 `<link>` 元素用于包含来自外部的文件，而 `<style>` 元素用于指定嵌入的样式。

与动态脚本类似，所谓动态样式是指在页面刚加载时不存在的样式；动态样式是在页面加载完成后动态添加到页面中的。

以下面这个典型的 `<link>` 元素为例

```html
<link rel="stylesheet" type="text/css" href="styles.css" />
```

使用 DOM 代码可以很容易地动态创建出这个元素

```js
var link = document.createElement('link')
link.rel = 'stylesheet'
link.type = 'text/css'
link.href = 'styles.css'
var head = document.getElementsByTagName('head')[0]
head.appendChild(link)
```

以上代码在所有主流浏览器中都可以正常运行。需要注意的是，必须将 `<link>` 元素添加到 `<head>` 而不是 `<body>` 元素，才能保证在所有浏览器中的行为一致。

整个过程可以用以下函数来表示

```js
function loadStyles(url) {
  var link = document.createElement('link')
  link.rel = 'stylesheet'
  link.type = 'text/css'
  link.href = url
  var head = document.getElementsByTagName('head')[0]
  head.appendChild(link)
}
```

调用这个函数的代码如下

```js
loadStyles('styles.css')
```

另一种定义样式的方式是使用 `<style>` 元素来包含嵌入式 CSS，如下所示

```html
<style>
  body {
    background-color: red;
  }
</style>
```

按照相同的逻辑，下面 DOM 代码应该是有效的

```js
var style = document.createElement('style')
style.type = 'text/css'
style.appendChild(document.createTextNode('body{background-color:red}'))
var head = document.getElementsByTagName('head')[0]
head.appendChild(style)
```

以上代码可以在 Firefox、Safari、Chrome 和 Opera 中运行，在 IE 中则会报错。IE 将 `<style>` 视为一个特殊的，与 `<script>` 类似的节点，不允许访问其子节点。事实上，IE 此时抛出的错误与向 `<script>` 元素添加子节点时抛出的错误相同。

解决 IE 中这个问题的办法，就是访问元素的 `styleSheet` 属性，该属性又有一个 `cssText` 属性，可以接受 CSS 代码，如下面的例子所示

```js
var style = document.createElement('style')
style.type = 'text/css'
try {
  style.appendChild(document.createTextNode('body{background-color:red}'))
} catch (ex) {
  style.styleSheet.cssText = 'body{background-color:red}'
}
var head = document.getElementsByTagName('head')[0]
head.appendChild(style)
```

与动态添加嵌入式脚本类似，重写后的代码使用了 try-catch 语句来捕获 IE 抛出的错误，然后再使用针对 IE 的特殊方式来设置样式。因此，通用的解决方案如下

```js
function loadStyleString(css) {
  var style = document.createElement('style')
  style.type = 'text/css'
  try {
    style.appendChild(document.createTextNode(css))
  } catch (ex) {
    style.styleSheet.cssText = css
  }
  var head = document.getElementsByTagName('head')[0]
  head.appendChild(style)
}
```

调用这个函数的示例如下

```js
loadStyleString('body{background-color:red}')
```
