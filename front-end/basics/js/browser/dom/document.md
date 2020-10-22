# Document

JavaScript 通过 Document 类型表示文档。在浏览器中，`document` 对象是 HTMLDocument（继承自 Document 类型）的一个实例，表示整个 HTML 页面。

## API 文档

---

<p align="center">Document ➠ Node ➠ EventTarget</p>

---

### 文档的子节点

▎Document.**documentElement** - _readonly_ - Element - 该属性始终指向 HTML 页面中的 `<html>` 元素

▎Document.**doctype** - _readonly_ - DocumentType | null

### 文档信息

▎Document.**domain** - 页面的域名

```js
// https://developer.mozilla.org/en-US/docs/Web/API/Document/domain
document.domain // "developer.mozilla.org"
```

由于安全方面的限制，不能将 `domain` 属性设置为 URL 中不包含的域。

```js
// 假设页面来自 p2p.wrox.com 域
document.domain = 'wrox.com' // 成功
document.domain = 'nczonline.net' // 出错
```

浏览器对 domain 属性还有一个限制，即如果域名一开始是“松散的”，那么不能将它再设置为“紧绷的”。

```js
// 假设页面来自 p2p.wrox.com 域
document.domain = 'wrox.com' // 松散的(loose), 成功
document.domain = 'p2p.wrox.com' // 紧绷的(tight), 出错
```

▎Document.**URL** - _readonly_ - 页面完整的 URL

```html
<p id="urlText">
  URL:<br />
  <span id="url">URL goes here</span>
</p>
```

```js
document.getElementById('url').textContent = document.URL
```

▎Document.**referrer** - _readonly_ - 链接到当前页面的那个页面的 URL

### 文档字符集

▎Document.**characterSet** - 文档中实际使用的字符集

```js
document.characterSet // "UTF-8"
```

### 文档状态

▎Document.**readyState** - _readonly_ - 文档的加载状态

- `"loading"` - 文档加载中
- `"interactive"` - 文档完成加载和解析，但子资源（图像，样式表等）仍在加载
- `"complete"` - 文档和所有子资源完成加载

当该属性值发生改变时，触发 `document` 对象的 `readystatechange` 事件。

`DOMContentLoaded` 事件的替代方式

```js
document.onreadystatechange = function() {
  if (document.readyState === 'interactive') {
    initApplication()
  }
}
```

`load` 事件的替代方式

```js
document.onreadystatechange = function() {
  if (document.readyState === 'complete') {
    initApplication()
  }
}
```

### 焦点管理

▎HTMLElement.**focus** - 指定元素获取焦点

```ts
element.focus({ preventScroll: boolean = true })

// @参数 preventScroll
// 浏览器是否应滚动文档，使获取焦点的元素进入视图
```

▎DocumentOrShadowRoot.**activeElement** - _readonly_ - Element | null - 始终会引用 DOM 中当前获得了焦点的元素

元素获得焦点的方式有页面加载、用户输入（通常是通过按 Tab 键）和在代码中调用 `focus()` 方法。

```js
var button = document.getElementById('myButton')
button.focus()
alert(document.activeElement === button) // true
```

默认情况下，文档刚刚加载完成时，`document.activeElement` 中保存的是 `document.body` 元素的引用。文档加载期间，`document.activeElement` 的值为 `null`。

▎Document.**hasFocus** - 文档是否获得了焦点

```ts
document.hasFocus(): boolean
```

```js
var button = document.getElementById('myButton')
button.focus()
alert(document.hasFocus()) // true
```

### DOM 树访问

▎Document.**title** - 文档的标题

▎Document.**body** - 文档的 `body` 元素

▎Document.**head** - _readonly_ - 文档的 `head` 元素

▎Document.**images** - _readonly_ - HTMLCollection - 文档中的 `img` 元素集合

▎Document.**links** - _readonly_ - HTMLCollection - 文档中拥有 `href` 特性的 `a` 或 `area` 元素集合

▎Document.**forms** - _readonly_ - HTMLCollection - 文档中的 `form` 元素集合

▎Document.**scripts** - _readonly_ - HTMLCollection - 文档中的 `script` 元素集合

### 查找元素

▎Document.**getElementById**

```ts
document.getElementById(elementId: DOMString): Element | null
```

> 与 `querySelector`, `querySelectorAll` 等元素查找方法不同，`getElementById` 仅可作为全局 `document` 对象的方法使用，而不可作为 DOM 中元素对象的方法使用。因为 id 值在整个文档中必须保持唯一性，因此不需要一个“局部”版本。

▎Document.**getElementsByTagName**

```ts
document.getElementsByTagName(qualifiedName: DOMString): HTMLCollection

// @参数 qualifiedName
// "*" 匹配所有元素

// @返回值
// 匹配指定标签名的元素集合（实时）
```

▎Document.**getElementsByClassName**

```ts
document.getElementsByClassName(classNames: DOMString): HTMLCollection

// @返回值
// 匹配指定标签名的元素集合（实时）
```

```js
// 获取所有 class 为 'test' 的元素
document.getElementsByClassName('test')
// 获取所有 class 同时包括 'red' 和 'test' 的元素
document.getElementsByClassName('red test')
```

Document.**querySelector**

```ts
document.querySelector(selectors: DOMString): Element | null

// @返回值
// 匹配指定选择器的第一个元素
```

▎Document.**querySelectorAll**

```ts
document.querySelectorAll(selectors: DOMString): NodeList

// @返回值
// 匹配指定选择器的所有元素集合（非实时）
```

### 创建节点

▎Document.**createElement** - 创建一个元素节点

```ts
document.createElement(localName: DOMString): Element
```

▎Document.**createTextNode** - 创建一个文本节点

```ts
document.createTextNode(data: DOMString): Text
```

▎Document.**createComment** - 创建一个注释节点

```ts
document.createComment(data: DOMString): Comment
```

```js
// 创建一个 p 元素
var para = document.createElement('P')
// 创建一个文本节点
var txt = document.createTextNode('这是一个段落')
// 将文本节点添加到 p 元素
para.appendChild(txt)
// 将 p 元素添加到 body 元素
document.body.appendChild(para)
```

### 文档写入

▎Document.**write** - 将给定字符串添加到文档的输入流

```ts
document.write(...text: string)
```

在已关闭（已加载）的文档上调用 `document.write()` 会自动调用 `document.open()`，这将清空文档内容。

▎Document.**writeln** - 将给定字符串添加到文档的输入流，后面跟着一个换行符

```ts
document.writeln(...text: string)
```

## HTMLCollection

▎HTMLCollection.**length** - readonly

▎HTMLCollection.**item** - 返回集合中指定索引的元素

```ts
element = collection.item(index)
element = collection[index]
```

▎HTMLCollection.**namedItem** - 返回集合中具有指定 `id` 或 `name` 属性的第一个元素

```ts
element = collection.namedItem(name)
element = collection[name]
```

## 参考

- [Document - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Document)
