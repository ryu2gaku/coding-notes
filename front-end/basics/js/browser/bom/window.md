# Window

BOM 的核心对象是 `window`，它表示浏览器的一个实例。

在浏览器中，`window` 对象有双重角色，它既是通过 JavaScript 访问浏览器窗口的一个接口，又是 ECMAScript 规定的 `Global` 对象。这意味着在网页中定义的任何一个对象、变量和函数，都以 `window` 作为其 `Global` 对象。

## 全局作用域

由于 `window` 对象同时扮演着 ECMAScript 中的 `Global` 对象的角色，因此所有在全局作用域中声明的变量、函数都会变成 window 对象的属性和方法。

```js
var age = 29
function sayAge() {
  // 由于 sayAge 存在于全局作用域
  // 因此 this.age 被映射到 window.age
  alert(this.age)
}

alert(window.age) // 29
sayAge() // 29
window.sayAge() // 29
```

抛开全局变量会成为 `window` 对象的属性不谈，定义全局变量与在 `window` 对象上直接定义属性还是有一点差别：全局变量不能通过 `delete` 操作符删除，而直接在 `window` 对象上定义的属性可以。

```js
var age = 29
window.color = 'red'

// 在 IE < 9 时抛出错误，在其他所有浏览器中都返回 false
delete window.age
// 在 IE < 9 时抛出错误，在其他所有浏览器中都返回 true
delete window.color

alert(window.age) // 29
alert(window.color) // undefined
```

上面使用 var 语句添加的 `window` 属性有一个名为 `[[Configurable]]` 的特性，这个特性的值被设置为 `false`，因此这样定义的属性不可以通过 `delete` 操作符删除。

## API 文档

---

<p align="center">Window ➠ EventTarget</p>

---

▎Window.**document** - _readonly_ - Document

▎Window.**location** - _readonly_ - Location

▎Window.**history** - _readonly_ - History

▎Window.**screen** - _readonly_ - Screen

▎Window.**navigator** - _readonly_ - Navigator

### 窗口关系及框架

▎Window.**window** - _readonly_ - WindowProxy

▎Window.**self** - _readonly_ - WindowProxy - 始终指向 `window`

▎Window.**frames** - _readonly_ - WindowProxy

如果页面中包含框架，则每个框架都拥有自己的 `window` 对象，并且保存在 `frames` 集合中。

在 `frames` 集合中，可以通过数值索引（从 0 开始，从左至右，从上到下）或者框架名称来访问相应的 `window` 对象。每个 `window` 对象都有一个 `name` 属性，其中包含框架的名称。

```html
<html>
  <head>
    <title>Frameset Example</title>
  </head>
  <frameset rows="160,*">
    <frame src="frame.htm" name="topFrame">
    <frameset cols="50%,50%">
      <frame src="anotherframe.htm" name="leftFrame">
      <frame src="yetanotherframe.htm" name="rightFrame">
    </frameset>
  </frameset>
</html>
```

以上代码创建了一个框架集，其中一个框架居上，两个框架居下。可以通过 `window.frames[0]` 或 `window.frames["topFrame"]` 或 `top.frames[0]` 来引用上方的框架。

▎Window.**top** - _readonly_ - WindowProxy | null - 当前窗口最顶层的浏览器窗口

▎Window.**parent** - _readonly_ - WindowProxy | null - 当前窗口的父窗口

▎Window.**length** - _readonly_ - 窗口的框架数（`frame` 或 `iframe` 元素）

### 导航和打开窗口

▎Window.**name** - 窗口名

除非最高层窗口是通过 `window.open()` 打开的，否则其 `window` 对象的 `name` 属性不会包含任何值。

▎Window.**stop** - 取消文档加载

```ts
window.stop(): void
```

▎Window.**close** - 关闭窗口

```ts
window.close(): void
```

仅适用于通过 `window.open()` 打开的弹出窗口。

▎Window.**closed** - _readonly_ - 窗口是否已被关闭

▎Window.**opener**

只在弹出窗口中的最外层 `window` 对象中有定义，而且指向调用 `window.open()` 的窗口或框架。

```js
var wroxWin = window.open(
  'http://www.wrox.com/',
  'wroxWindow',
  'height=400,width=400,top=10,left=10,resizable=yes'
)
alert(wroxWin.opener == window) // true
```

▎Window.**open** - 打开一个窗口来展示 url

```ts
window.open(
  url: USVString = "",
  target: DOMString = "_blank",
  features: DOMString = ""
): WindowProxy | null

// @参数 target
// 窗口名
// 可以作为 a 和 form 元素上 HTML target 特性的值
// 特殊值 _blank, _self, _parent, _top
// 如果已存在了该名称的窗口，则把 url 加载到这个已存在窗口中，
// 同时返回该窗口，并忽略参数 features

// @参数 features
// 特性之间用逗号分隔
// fullscreen | yes/no | 浏览器窗口是否最大化, 仅限 IE
// width      | number | 新窗口的宽度, 不能小于 100
// height     | number | 新窗口的高度, 不能小于 100
// top        | number | 新窗口的上坐标, 不能为负值
// left       | number | 新窗口的左坐标, 不能为负值
// location   | yes/no | 是否在浏览器窗口中显示地址栏，不同浏览器的默认值不同，
//                       如果设置为 no，地址栏可能会隐藏，也可能会被禁用（取决于浏览器）
// menubar    | yes/no | 是否在浏览器窗口中显示菜单栏, 默认值为 no
// resizable  | yes/no | 是否可以通过拖动浏览器窗口的边框改变其大小，默认值为 no
// scrollbars | yes/no | 如果内容在视口中显示不下, 是否允许滚动，默认值为 no
// status     | yes/no | 是否在浏览器窗口中显示状态栏, 默认值为 no
// toolbar    | yes/no | 是否在浏览器窗口中显示工具栏, 默认值为 no
// titlebar   | yes/no | 是否在浏览器窗口中显示标题栏, 默认值为 yes

// @返回值
// 一个新创建窗口的引用，如果执行失败则返回 null
```

```js
var myWindow = window.open('', '_self')
myWindow.document.write('<p>I replaced the current window.</p>')

var myWindow = window.open('', 'myWindow', 'width=200,height=100')
myWindow.document.write("<p>This is 'myWindow'</p>")
myWindow.opener.document.write('<p>This is the source window!</p>')

window.open('http://www.wrox.com/', 'topFrame')
// 等同于 <a href="http://www.wrox.com/" target="topFrame"></a>
```

检测弹出窗口是否被屏蔽

```js
var blocked = false

try {
  var wroxWin = window.open('http://www.wrox.com/', '_blank')
  if (wroxWin == null) {
    blocked = true
  }
} catch (error) {
  blocked = true
}

if (blocked) {
  alert('The popup was blocked!')
}
```

### 窗口位置

▎Window.**screenX** - _readonly_ - 窗口相对于屏幕的水平坐标

▎Window.**screenY** - _readonly_ - 窗口相对于屏幕的垂直坐标

以下代码可以跨浏览器取得窗口左边和上边的位置

```js
var leftPos =
  typeof window.screenLeft == 'number' ? window.screenLeft : window.screenX
var topPos =
  typeof window.screenTop == 'number' ? window.screenTop : window.screenY
```

上例运用二元操作符首先确定 `screenLeft` 和 `screenTop` 属性是否存在，如果存在（在 IE、Safari、Opera 和 Chrome 中）则取得这两个属性的值。如果不存在（在 Firefox 中）则取得 `screenX` 和 `screenY` 的值。

▎Window.**moveTo** - ウィンドウを指定座標に移動します

```ts
window.moveTo(x: long, y: long): void
```

```js
// 把窗口移动到坐上角
function origin() {
  window.moveTo(0, 0)
}
```

▎Window.**moveBy** - 指定された量だけ現在のウィンドウを移動します

```ts
window.moveBy(x: long, y: long): void
```

不能移动非 `window.open()` 创建的窗口或标签页。当一个窗口内包含复数的标签页时，不能移动窗口。

### 窗口大小

▎Window.**innerWidth** - _readonly_ - 视口宽度（包括滚动条）

▎Window.**innerHeight** - _readonly_ - 视口高度（包括滚动条）

▎Window.**outerWidth** - _readonly_ - 窗口宽度

▎Window.**outerHeight** - _readonly_ - 窗口高度

▎Window.**resizeTo** - 动态调整窗口的大小

```ts
window.resizeTo(x: long, y: long): void

// @参数 x
// 新しい outerWidth を表す整数値（ピクセル値）
//（スクロールバー、タイトルバー等を含む）

// @参数 y
// 新しい outerHeight を表す整数値（ピクセル値）
// （スクロールバー、タイトルバー等を含む）
```

```js
// 将窗口设置为整个屏幕的 1/4 大小（面积）
function quarter() {
  window.resizeTo(window.screen.availWidth / 2, window.screen.availHeight / 2)
}
```

▎Window.**resizeBy** - 現在のウィンドウを特定の量だけリサイズします

```ts
window.resizeBy(x: long, y: long): void
```

不能调整非 `window.open()` 创建的窗口或标签页的大小。当一个窗口内包含复数的标签页时，不能调整窗口的大小。

### 视口滑动

▎Window.**scrollX** - _readonly_ - 文档在水平方向已滚动的像素值

▎Window.**pageXOffset** - _readonly_ - 等同于 `scrollX`

▎Window.**scrollY** - _readonly_ - 文档在垂直方向已滚动的像素值

▎Window.**pageYOffset** - _readonly_ - 等同于 `scrollY`

▎Window.**scroll** - ウィンドウを文書内の特定の位置までスクロールします

```ts
window.scroll(options: ScrollToOptions = {}): void

window.scroll(x: double, y: double): void

// ScrollToOptions 字典
// options.top
// options.left
// options.behavior = auto | smooth
```

効果としては、 `window.scrollTo()` もこのメソッドと同じです。

▎Window.**scrollTo** - 文書内の特定の座標までスクロールします

```ts
window.scrollTo(options: ScrollToOptions = {}): void

window.scrollTo(x: double, y: double): void
```

```js
window.scrollTo(0, 1000)

// 使用 options
window.scrollTo({
  top: 100,
  left: 100,
  behavior: 'smooth',
})
```

この関数は、効果としては、`window.scroll()` と同じです。

▎Window.**scrollBy** - 指定された量だけウィンドウ内の文書をスクロールします

```ts
window.scrollBy(options: ScrollToOptions = {}): void

window.scrollBy(x: double, y: double): void
```

```js
// scroll down one page
window.scrollBy(0, window.innerHeight)
// scroll up
window.scrollBy(0, -window.innerHeight)

// 使用 options
window.scrollBy({
  top: 100,
  left: 100,
  behavior: 'smooth',
})
```

`window.scrollBy()` 滚动指定的距离，而 `window.scroll()` 滚动至文档中的绝对位置。

### 定时器

▎Window.**setTimeout** - 在执行代码前需要等待多少毫秒

```ts
handle = self.setTimeout(handler, timeout?, ...arguments)

handle = self.setTimeout(code, timeout?)

// @参数 handler
// 定时器到期后要执行的函数

// @参数 timeout
// 默认值 0

// @参数 arguments
// 附加参数，定时器到期后传递给 handler 指定的函数
```

▎Window.**clearTimeout**

```ts
self.clearTimeout(handle)
```

```js
var timeoutID

function delayedAlert() {
  timeoutID = window.setTimeout(window.alert, 2000, 'That was really slow!')
}
function clearAlert() {
  window.clearTimeout(timeoutID)
}
```

▎Window.**setInterval**

```ts
handle = self.setInterval(handler , timeout?, ...arguments?)

handle = self.setInterval(code , timeout?)
```

▎Window.**clearInterval**

```ts
self.clearInterval(handle)
```

### 系统对话框

▎Window.**alert** - 显示带有一段消息和一个确认按钮的警告框

```ts
window.alert(): void
window.alert(message: DOMString): void
```

▎Window.**confirm** - 显示一个带有指定消息以及确认和取消按钮的对话框

```ts
window.confirm(message: DOMString = ""): boolean

// @返回值
// 点击确定返回 true，点击取消返回 false
```

```js
if (confirm('Are you sure?')) {
  alert("I'm so glad you're sure!")
} else {
  alert("I'm sorry to hear you're not sure.")
}
```

▎Window.**prompt** - 显示可提示用户输入的对话框

```ts
window.prompt(
  message: DOMString = "",
  default: DOMString = ""
): DOMString | null

// @返回值
// 点击确定返回用户输入值，点击取消返回 null
```

```js
var result = prompt('What is your name?', '')
if (result !== null) {
  alert('Welcome, ' + result)
}
```

## 参考

- [Window - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window)
