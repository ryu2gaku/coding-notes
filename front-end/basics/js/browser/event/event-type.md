# 事件类型

## 资源事件

▎**load** - 当页面完全加载后在 `window` 上面触发，当所有框架都加载完毕时在框架集上面触发，当图像加载完毕时在 `<img>` 元素上面触发，或者当嵌入的内容加载完毕时在 `<object>` 元素上面触发

❐ 当页面完全加载后（包括所有图像、JavaScript 文件、CSS 文件等外部资源）就会触发 `window` 上面的 `load` 事件。

```js
window.addEventListener('load', event => {
  console.log('page is fully loaded.')
})
window.onload = event => {
  console.log('page is fully loaded.')
}
```

另一种指定 `onload` 事件处理程序的方式是为 `<body>` 元素添加一个 `onload` 特性。

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Load Event Example</title>
  </head>
  <body onload="alert('Loaded!')"></body>
</html>
```

一般来说，在 `window` 上面发生的任何事件都可以在 `<body>` 元素中通过相应的特性来指定，因为在 HTML 中无法访问 `window` 元素。实际上，这只是为了保证向后兼容的一种权宜之计，但所有浏览器都能很好地支持这种方式。建议尽可能使用 JavaScript 方式。

❐ 图像上面也可以触发 `load` 事件，无论是在 HTML 中的图像元素还是在 DOM 中的图像元素。

```html
<img src="smile.gif" onload="alert('Image loaded.')" />
```

```js
var image = document.getElementById('myImage')
image.addEventListener('load', function(event) {
  alert(event.target.src)
})
```

在创建新的 `<img>` 元素时，可以为其指定一个事件处理程序，以便图片加载完毕后给出提示。此时，最重要的是要在指定 `src` 属性之前先指定事件。

```js
// 首先为 window 指定了 onload 事件处理程序
// 因为想向 DOM 中添加一个新元素，必须确定页面已经加载完毕
// 如果在页面加载完毕前操作 document.body 会导致错误
window.addEventListener('load', function() {
  var image = document.createElement('img')
  image.addEventListener('load', function(event) {
    alert(event.target.src)
  })
  document.body.appendChild(image)
  // 需要格外注意：新图像元素不一定要从添加到文档后才开始下载，\
  // 只要设置了 src 属性就会开始下载
  image.src = 'smile.gif'
})
```

▎**DOMContentLoaded** - 页面形成完整的 DOM 树之后就会触发，不理会图像、样式表等其他资源是否已经下载完毕（HTML5 事件）

```js
document.addEventListener('DOMContentLoaded', event => {
  console.log('DOM fully loaded and parsed.')
})
```

▎**beforeunload** - 浏览器卸载页面之前触发（HTML5 事件）

当前页面不会直接关闭，而是会触发一个确认对话框，询问用户是否真的要离开该页面。

```js
window.addEventListener('beforeunload', event => {
  // Cancel the event as stated by the standard.
  event.preventDefault()
  // Chrome requires returnValue to be set.
  event.returnValue = ''
})
```

▎**unload** - 当页面完全卸载后在 `window` 上面触发，当所有框架都卸载后在框架集上面触发，或者当嵌入的内容卸载完毕后在 `<object>` 元素上面触发

▎**abort** - 在用户停止下载过程时，如果嵌入的内容没有加载完，则在 `<object>` 元素上面触发

▎**error** - 当发生 JavaScript 错误时在 `window` 上面触发，当无法加载图片时在 `<img>` 元素上面触发，当无法加载嵌入内容时在 `<object>` 元素上面触发，或者当有一或多个框架无法加载时在框架集上面触发

## 视图事件

▎**resize** - 当窗口或框架的大小变化时在 `window` 或框架上面触发

这个事件在 `window` 上面触发，因此可以通过 JavaScript 或者 `<body>` 元素中的 `onresize` 特性来指定事件处理程序。

```js
window.addEventListener('resize', function(event) {
  alert('Resize.')
})
```

浏览器窗口最小化或最大化时也会触发 `resize` 事件。

▎**scroll** - 当用户滚动带滚动条的元素中的内容时，在该元素上面触发。`<body>` 元素中包含所加载页面的滚动条

```js
// 在混杂模式下，可以通过 <body> 元素的 ScrollLeft 和 scrollTop 来监控到这一变化
// 在标准模式下，除了 Safari 之外的所有浏览器都会通过 <html> 元素来反映这一变化，\
// Safari 仍然基于 <body> 跟踪滚动位置
window.addEventListener('scroll', function(event) {
  // document.compatMode - 当前文档的渲染模式是混杂模式还是标准模式
  // "BackCompat" - 文档处于混杂模式（quirks mode）
  // "CSS1Compat"
  if (document.compatMode == 'CSS1Compat') {
    alert(document.documentElement.scrollTop)
  } else {
    alert(document.body.scrollTop)
  }
})
// 由于 Safari 3.1 之前的版本不支持 document.compatMode，\
// 因此旧版本的浏览器会满足第二个条件
```

## 焦点事件 Focus Event

当元素获得或失去焦点时触发。

▎**focus** - 在元素获得焦点时触发，不会冒泡

▎**blur** - 在元素失去焦点时触发，不会冒泡

```html
<form id="form">
  <input type="text" placeholder="text input" />
  <input type="password" placeholder="password" />
</form>
```

```js
const form = document.getElementById('form')
form.addEventListener(
  'focus',
  event => {
    event.target.style.background = 'pink'
  },
  true
)
form.addEventListener(
  'blur',
  event => {
    event.target.style.background = ''
  },
  true
)
```

▎**focusin** - 在元素获得焦点时触发，会冒泡

▎**focusout** - 在元素失去焦点时触发，会冒泡

```js
const form = document.getElementById('form')
form.addEventListener('focusin', event => {
  event.target.style.background = 'pink'
})
form.addEventListener('focusout', event => {
  event.target.style.background = ''
})
```

❐ 当焦点从页面中的一个元素移动到另一个元素，会依次触发下列事件：

- `focusout` 在失去焦点的元素上触发
- `focusin` 在获得焦点的元素上触发
- `blur` 在失去焦点的元素上触发
- `focus` 在获得焦点的元素上触发

## 表单事件 Form Event

▎**reset** - 表单重置，用于 `form`

▎**submit** - 表单提交，用于 `form`

▎**select** - 当用户选择文本框（`<input>` 或 `<textarea>`）中的一或多个字符时触发

```html
<input value="Try selecting some text in this element." />
<p id="log"></p>
```

```js
function logSelection(event) {
  const log = document.getElementById('log')
  const selection = event.target.value.substring(
    event.target.selectionStart,
    event.target.selectionEnd
  )
  log.textContent = `You selected: ${selection}`
}

const input = document.querySelector('input')
input.addEventListener('select', logSelection)
```

▎**change** - `input`, `select`, `textarea` 元素已完成更改

- `input:text`, `textarea` - 元素失去焦点时
- `input:radio`, `input:checkbox` - `checked` 状态改变时

▎**input** - `input`, `select`, `textarea` 元素的 `value` 改变（HTML5 事件）

```html
<input placeholder="Enter some text" name="name" />
<p id="values"></p>
```

```js
const input = document.querySelector('input')
const log = document.getElementById('values')

input.addEventListener('input', updateValue)

function updateValue(e) {
  log.textContent = e.target.value
}
```

## 鼠标事件 Mouse Event

当用户通过鼠标在页面上执行操作时触发。

▎**click** - 在用户单击主鼠标按钮（一般是左边的按钮）或者按下回车键时触发

▎**dblclick** - 在用户双击主鼠标按钮（一般是左边的按钮）时触发

`click` 和 `dblclick` 事件对象的 `detail` 属性表示当前点击数。

▎**mousemove** - 当鼠标指针在元素内部移动时重复地触发。不能通过键盘触发这个事件

▎**mousedown** - 在用户按下了任意鼠标按钮时触发。不能通过键盘触发这个事件

▎**mouseup** - 在用户释放鼠标按钮时触发。不能通过键盘触发这个事件

`mouseup` 和 `mousedown` 事件对象的 `detail` 属性是 1 加上当前点击数。

▎**mouseover** - 当鼠标指针位于一个元素外部，然后用户将其首次移入另一个元素边界之内时触发。不能通过键盘触发这个事件

▎**mouseout** - 在鼠标执行位于一个元素上方，然后用户将其移入另一个元素时触发。有一入的另一个元素可能位于前一个元素的外部，也可能时这个元素的子元素。不能通过键盘触发这个事件

▎**contextmenu** - 点击鼠标右键请求上下文菜单（HTML5 事件）

```html
<p id="noContextMenu">The context menu has been disabled on this paragraph.</p>
<p>But it has not been disabled on this one.</p>
```

```js
noContext = document.getElementById('noContextMenu')

noContext.addEventListener('contextmenu', e => {
  e.preventDefault()
})
```

▎**mouseenter** - 在鼠标光标从元素外部首次移动到元素范围之内时触发。不会冒泡，而且在光标移动到后代元素上不会触发

▎**mouseleave** - 在位于元素上方的鼠标光标移动到元素范围之外时触发。不会冒泡，而且在光标移动到后代元素上不会触发

页面上的所有元素都支持鼠标事件。除了 `mouseenter` 和 `mouseleave`，所有鼠标事件都会冒泡，也可以被取消，而取消鼠标事件将会影响浏览器的默认行为。

❐ `mousedown`, `mouseup`, `click`, `dbclick` 事件的触发顺序：

- `mousedown`
- `mouseup`
- `click`
- `mousedown`
- `mouseup`
- `click`
- `dbclick`

## 滚轮事件 Wheel Event

当使用鼠标滚轮（或类似设备）时触发。

▎**mousewheel** - 用户通过鼠标滚轮与页面交互、在垂直方向上滚动页面时（无论向上还是向下）触发

## 键盘事件 Keyboard Event

当用户通过键盘在页面上执行操作时触发。

▎**keyup** - 当用户释放键盘上的键时触发

▎**keydown** - 当用户按下键盘上的任意键时触发，而且如果按住不放的话，会重复触发此事件

▎**keypress** - _Deprecated_ - 当用户按下键盘上的字符键时触发，而且如果按住不放的话，会重复触发此事件

所有键盘事件都会冒泡，也可以被取消。

## Hash Change Event

▎**hashchange** - 当 URL 中 # 符号后面的部分更改时触发（HTML5 事件）

```js
window.addEventListener('hashchange', function(event) {
  alert('Old URL: ' + event.oldURL + '\nNew URL: ' + event.newURL)
})
```

## 参考

- [Event reference | MDN](https://developer.mozilla.org/en-US/docs/Web/Events)
