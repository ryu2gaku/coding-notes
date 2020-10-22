# 事件处理程序 & 事件侦听器

事件就是用户或浏览器自身执行的某种动作。诸如 click, load 和 mouseover，都是事件的名字。而响应某个事件的函数就叫**事件处理程序**或**事件侦听器**。

事件处理程序（event handler）和事件侦听器（event listener）没有本质区别，仅仅是同一件事的不同术语。

## 事件处理程序 Event Handler

事件处理程序是指通过 `on{eventtype}` 特性或属性注册的函数。

### HTML 级事件处理程序

在 HTML 元素上使用 `on{eventtype}` 命名的特性指定事件处理程序。

```html
<button onclick="return handleClick(event);"></button>
```

### DOM0 级事件处理程序

通过 JavaScript 指定事件处理程序。将一个函数赋值给一个事件处理程序属性。

每个元素（包括 `window` 和 `document`）都有自己的事件处理程序属性，如 `onclick`。将这种属性的值设置为一个函数，就可以指定事件处理程序。

```js
var btn = document.getElementById('myBtn')
btn.onclick = function(event) {
  alert('Clicked!')
}
```

使用 DOM0 级方法指定的事件处理程序被认为是元素的方法。因此，这时候的事件处理程序是在元素的作用域中运行，即程序中的 `this` 引用当前元素。

```js
var btn = document.getElementById('myBtn')
btn.onclick = function(event) {
  alert(this.id) // 'myBtn'
}
```

以这种方式添加的事件处理程序会在事件流的冒泡阶段被处理。

删除通过 DOM0 级方法指定的事件处理程序，只要像下面这样将事件处理程序属性的值设为 `null` 即可。

```js
btn.onclick = null // 删除事件处理程序
```

## EventTarget 接口

DOM 的事件操作都定义在 EventTarget 接口。

`Element`, `Document` 和 `Window` 是最常见的事件目标，其他还有 `XMLHttpRequest`, `AudioNode`, `AudioContext`

### API 文档

---

<p align="center">EventTarget</p>

---

每个 EventTarget 有一个关联的事件侦听器（event listener）列表。事件侦听器将一个回调函数和一个指定事件相关联。事件侦听器由 _type_、_callback_、_capture_ 等字段组成。

▎EventTarget.**addEventListener** - 添加一个事件侦听器

```ts
target.addEventListener(
  type: DOMString,
  callback: EventListener | null,
  capture: boolean = false
): void

// @参数 useCapture
// 为 true 表示在捕获阶段执行回调函数
// 为 false 表示在冒泡阶段执行回调函数
// 无论那种情况都会在目标阶段执行回调函数

interface EventListener {
  handleEvent(event: Event): void
}
```

> 回调函数命名为 `EventListener` 是历史原因，事件侦听器是一个更广的概念。

▎EventTarget.**removeEventListener** - 移除事件目标的事件侦听器列表中具有相同 type、callback 和 capture 的事件侦听器

```ts
target.removeEventListener(
  type: DOMString,
  callback: EventListener | null
  capture: boolean = false
): void
```

▎EventTarget.**dispatchEvent**

```ts
target.dispatchEvent(event: Event): boolean
```

## 事件侦听器 Event Listener

事件侦听器又可称为 DOM2 级事件处理程序

```js
var btn = document.getElementById('myBtn')
btn.addEventListener('click', function {
  alert(this.id)
}, false)
```

与 DOM0 级方法一样，这里添加的事件处理程序也是在其依附的元素的作用域中运行。

使用 DOM2 级方法添加事件处理程序的主要好处是可以添加多个事件处理程序。

```js
var btn = document.getElementById('myBtn')
btn.addEventListener('click', function {
  alert(this.id)
}, false)
btn.addEventListener('click', function {
  alert('Hello world!')
}, false)
```

多个事件处理程序会按照添加它们的顺序触发。

通过 `addEventListener` 添加的事件处理程序只能使用 `removeEventListener` 来移除。移除时传入的参数需要与添加时的参数相同，这意味着通过 `addEventListener` 添加的匿名函数将无法移除。

```js
var btn = document.getElementById('myBtn')
btn.addEventListener('click', function {
  alert(this.id)
}, false)

btn.removeEventListener('click', function { // 没有用
  alert(this.id)
}, false)
```

```js
var btn = document.getElementById('myBtn')
var handler = function() {
  alert(this.id)
}
btn.addEventListener('click', handler, false)

btn.removeEventListener('click', handler, false) // 有效
```

## IE 事件处理程序（了解）

IE 实现了与 DOM 中类似的两个方法 `attachEvent` 和 `detachEvent`。这两个方法接受相同的两个参数：事件处理程序名称与事件处理程序函数。

> `attachEvent` 和 `detachEvent` 这两个方法已在 IE11 中被移除

由于 IE8 及更早版本只支持事件冒泡，所以通过 `attachEvent` 添加的事件处理程序都会被添加到冒泡阶段。

```ts
var btn = document.getElementById('myBtn')
btn.attachEvent('onclick', function {
  alert('Clicked!')
})

// 注意 attachEvent 的第一个参数是 "onclick"
// 而非 DOM 的 addEventListener 方法中的 "click"
```

在 IE 中使用 `attachEvent` 与使用 DOM0 级方法的主要区别在于事件处理程序的作用域。在使用 DOM0 级方法的情况下，事件处理程序会在其所属元素的作用域内运行。在使用 `attachEvent` 方法的情况下，事件处理程序会在全局作用域中运行，因此 `this` 等于 `window`。

```js
var btn = document.getElementById('myBtn')
btn.attachEvent('onclick', function {
  alert(this === window) // true
})
```

与 `addEventListener` 类似，`attachEvent` 也可以用来为一个元素添加多个事件处理程序。

```js
var btn = document.getElementById('myBtn')
btn.attachEvent('onclick', function {
  alert('Clicked!')
})
btn.attachEvent('onclick', function {
  alert('Hello world!')
})
```

与 DOM 方法不同的是，这些事件处理程序不是以添加它们的顺序执行，而是以相反的顺序被触发。

使用 `attachEvent` 添加的事件处理程序可以通过 `detachEvent` 来移除，条件是必须提供相同的参数。与 DOM 方法一样，这也意味着添加的匿名函数将不能被移除。

不过只要能将对相同函数的引用传给 `detachEvent`，就可以移除相应的事件处理程序。

```js
var btn = document.getElementById('myBtn')
var handler = function() {
  alert('Clicked')
}
btn.attachEvent('onclick', handler)

btn.detachEvent('onclick', handler)
```

## 跨浏览器的事件处理程序（了解）

```js
var EventUtil = {
  addHandler: function(element, type, handler) {
    if (element.addEventListener) {
      // DOM2 级方法
      element.addEventListener(type, handler, false)
    } else if (element.attachEvent) {
      // 兼容 IE8 及更早版本
      element.attachEvent('on' + type, handler)
    } else {
      // DOM0 级方法
      // 在现代浏览器中，应该不会执行这里的代码
      element['on' + type] = handler
    }
  },
  removeHandler: function(element, type, handler) {
    if (element.removeEventListener) {
      element.removeEventListener(type, handler, false)
    } else if (element.detachEvent) {
      element.detachEvent('on' + type, handler)
    } else {
      element['on' + type] = null
    }
  },
}
```

```js
var btn = document.getElementById('myBtn')
var handler = function() {
  alert('Clicked')
}

EventUtil.addHandler(btn, 'click', handler)

EventUtil.removeHandler(btn, 'click', handler)
```

## 参考

- [DOM onevent handlers - Developer guides | MDN](https://developer.mozilla.org/en-US/docs/Web/Guide/Events/Event_handlers)
- [EventTarget - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget)
