# 事件对象

在触发 DOM 上的某个事件时，会产生一个事件对象 event，这个对象汇总包含着所有与事件有关的信息。

只有在事件处理程序执行期间，event 对象才会存在。一旦事件处理程序执行完成，event 对象就会被销毁。

## Event 接口

---

<p align="center">Event</p>

---

▎Event.**type** - _readonly_ - 被触发的事件的类型

通过一个函数处理多个事件

```js
var btn = document.getElementById('myBtn')
var handler = function(event) {
  switch (event.type) {
    case 'click':
      alert('CLicked')
      break
    case 'mouseover':
      event.target.style.backgroundColor = 'red'
      break
    case 'mouseout':
      event.target.style.backgroundColor = ''
      break
  }
}

btn.onclick = handler
btn.onmouseover = handler
btn.onmouseout = handler
```

▎Event.**target** - _readonly_ - EventTarget | null - 触发事件的对象

▎Event.**currentTarget** - _readonly_ - EventTarget | null - 其事件处理程序当前正在处理事件的那个元素

❐ 比较 `target`, `this` 和 `currentTarget` ❐

在事件处理程序内部，`this` 始终等于 `event.currentTarget` 的值，而 `target` 则只包含事件的实际目标。

如果直接将事件处理程序指定给了目标元素，则 `this`, `currentTarget`, `target` 包含相同的值。

```js
var btn = document.getElementById('myBtn')
btn.onclick = function(event) {
  alert(event.currentTarget === this) // true
  alert(event.target === this) // true
}
```

上例检测了 `currentTarget` 和 `target` 与 `this` 的值。由于 `click` 事件的目标是按钮，因此这三个值是相等的。如果事件处理程序存在于按钮的父节点中（例如 `document.body`），那么这些值是不相同的。

```js
document.body.onclick = function(event) {
  alert(event.currentTarget === document.body) // true
  alert(this === document.body) // true
  alert(event.target === document.getElementById('myBtn')) // true
}
```

单击上例中的按钮时，`this` 和 `currentTarget` 都等于 `document.body`，因为事件处理程序是注册到这个元素上的。然而 `target` 元素却等于按钮元素，因为它是 click 事件真正的目标。由于按钮上并没有注册事件处理程序，结果 click 事件就冒泡到了 `document.body`，在那里事件才得到了处理。

▎Event.**eventPhase** - _readonly_ - 调用事件处理程序的阶段

```js
Event.NONE = 0
Event.CAPTURING_PHASE = 1 // 捕获阶段
Event.AT_TARGET = 2 // 目标阶段
Event.BUBBLING_PHASE = 3 // 冒泡阶段
```

▎Event.**stopPropagation** - 阻止当前事件在事件流的进一步传播

```ts
event.stopPropagation(): void
```

```js
child.addEventListener('click', function(event) {
  event.stopPropagation()
})
parent.addEventListener('click', function(event) {
  // 如果 child 元素被点击，该回调函数不会触发
})
```

▎Event.**stopImmediatePropagation** - 阻止当前事件在事件流的进一步传播，同时阻止剩余的同类事件处理函数执行

```ts
event.stopImmediatePropagation(): void
```

```js
child.addEventListener('click', function(event) {
  event.stopImmediatePropagation()
})
child.addEventListener('click', function(event) {
  // 如果 child 元素被点击，该回调函数不会触发
})
```

▎Event.**trusted** - _readonly_ - 为 true 表示事件是浏览器生成的，为 false 表示事件是由开发人员通过 JavaScript 创建的

▎Event.**bubbles** - _readonly_ - 事件是否冒泡

▎Event.**cancelable** - _readonly_ - 是否可以取消事件的默认行为

▎Event.**preventDefault** - 取消事件的默认行为。只有 `cancelable` 属性为 `true`，才可以使用这个方法

```ts
event.preventDefault(): void
```

链接的默认行为是在被单击时会导航到其 href 特性指定的 URL。通过链接的 onclick 事件处理程序可以取消链接导航这一默认行为。

```js
var link = document.getElementById('myLink')
link.onclick = function(event) {
  event.preventDefault()
}
```

▎Event.**defaultPrevented** - _readonly_ - 是否已经调用了 `preventDefault()`

▎Event.**timeStamp** - _readonly_ - long - 事件的创建时间（ms）

## UIEvent 接口

`MouseEvent`, `TouchEvent`, `FocusEvent`, `KeyboardEvent`, `WheelEvent`, `InputEvent`, `CompositionEvent` 等接口直接或间接继承于 `UIEvent`

---

<p align="center">UIEvent ➠ Event</p>

---

▎UIEvent.**view** - _readonly_ - Window | null - 与事件关联的抽象视图。等同于发生事件的 window 对象

▎UIEvent.**detail** - _readonly_ - long - 与事件相关的细节信息，取决于事件的类型

- 对于 `click` 或 `dblclick` 事件，`UIEvent.detail` 是当前点击数
- 对于 `mousedown` 或 `mouseup` 事件，`UIEvent.detail` 是当前点击数加 1
- 对所有的其它 `UIEvent` 对象，`UIEvent.detail` 总是 0

## MouseEvent 接口

`WheelEvent` 和 `DragEvent` 接口继承于 `MouseEvent`

---

<p align="center">MouseEvent ➠ UIEvent ➠ Event</p>

---

▎MouseEvent.**screenX** - _readonly_ - 鼠标指针相对于屏幕坐标系的水平坐标

▎MouseEvent.**screenY** - _readonly_ - 鼠标指针相对于屏幕坐标系的垂直坐标

▎MouseEvent.**clientX** - _readonly_ - 鼠标指针相对于视口的水平坐标

▎MouseEvent.**clientY** - _readonly_ - 鼠标指针相对于视口的垂直坐标

```html
<p>Move your mouse to see its position.</p>
<p id="screen-log"></p>
```

```js
let screenLog = document.querySelector('#screen-log')
document.addEventListener('mousemove', logKey)

function logKey(e) {
  screenLog.innerText = `
      Screen X/Y: ${e.screenX}, ${e.screenY}
      Client X/Y: ${e.clientX}, ${e.clientY}`
}
```

▎MouseEvent.**ctrlKey** - _readonly_ - 是否按下了 <kbd>control</kbd> 键

▎MouseEvent.**shiftKey** - _readonly_ - 是否按下了 <kbd>shift</kbd> 键

▎MouseEvent.**altKey** - _readonly_ - 是否按下了 <kbd>alt</kbd> 键

▎MouseEvent.**metaKey** - _readonly_ - 是否按下了 <kbd>meta</kbd> 键

```html
<p>Click anywhere to test the <code>shiftKey</code> property.</p>
<p id="log"></p>
```

```js
let log = document.querySelector('#log')
document.addEventListener('click', logKey)

function logKey(e) {
  log.textContent = `The shift key is pressed: ${e.shiftKey}`
}
```

▎MouseEvent.**relatedTarget** - _readonly_ - EventTarget | null

| 事件名       | `target`               | `relatedTarget`        |
| ------------ | ---------------------- | ---------------------- |
| `mouseenter` | 指针进入的 EventTarget | 指针离开的 EventTarget |
| `mouseleave` | 指针离开的 EventTarget | 指针进入的 EventTarget |
| `mouseout`   | 指针离开的 EventTarget | 指针进入的 EventTarget |
| `mouseover`  | 指针进入的 EventTarget | 指针离开的 EventTarget |
| `dragenter`  | 指针进入的 EventTarget | 指针离开的 EventTarget |
| `dragexit`   | 指针离开的 EventTarget | 指针进入的 EventTarget |

▎MouseEvent.**button** - _readonly_ - short - 哪个鼠标按钮被按下

- 0 - 主按键被按下，通常指鼠标左键
- 1 - 辅助按键被按下，通常指鼠标滚轮
- 2 - 次按键被按下，通常指鼠标右键

## KeyboardEvent 接口

---

<p align="center">KeyboardEvent ➠ UIEvent ➠ Event</p>

---

▎KeyboardEvent.**ctrlKey** - _readonly_ - 事件触发时，是否按下了 <kbd>Ctrl</kbd> 键

▎KeyboardEvent.**shiftKey** - _readonly_ - 事件触发时，是否按下了 <kbd>Shift</kbd> 键

▎KeyboardEvent.**altKey** - _readonly_ - 事件触发时，是否按下了 <kbd>Alt</kbd> 键

▎KeyboardEvent.**metaKey** - _readonly_ - 事件触发时，是否按下了 <kbd>Meta</kbd> 键

## FocusEvent 接口

---

<p align="center">FocusEvent ➠ UIEvent ➠ Event</p>

---

▎FocusEvent.**relatedTarget** - _readonly_ - EventTarget | null

| 事件名   | `target`               | `relatedTarget`                    |
| -------- | ---------------------- | ---------------------------------- |
| blur     | 失去焦点的 EventTarget | 获取焦点的 EventTarget（如果存在） |
| focus    | 获取焦点的 EventTarget | 失去焦点的 EventTarget（如果存在） |
| focusin  | 获取焦点的 EventTarget | 失去焦点的 EventTarget（如果存在） |
| focusout | 失去焦点的 EventTarget | 获取焦点的 EventTarget（如果存在） |

和鼠标事件 `MouseEvent.relatedTarget` 相似

## 参考

- [Event - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Event)
