# Node

JavaScript 中的所有节点类型都继承自 Node 类型，因此所有节点类型都共享着相同的基本属性和方法。

## API 文档

---

<p align="center">Node ➠ EventTarget</p>

---

▎Node.**nodeType** - _readonly_ - 节点的类型

```js
ELEMENT_NODE = 1 // Element
ATTRIBUTE_NODE = 2 // Attr
TEXT_NODE = 3 // Text
COMMENT_NODE = 8 // Comment
DOCUMENT_NODE = 9 // Document
DOCUMENT_TYPE_NODE = 10 // DocumentType
```

▎Node.**nodeName** - _readonly_

| Interface  |   return value    |
| :--------: | :---------------: |
| `Element`  | `Element.tagName` |
| `Comment`  |   `"#comment"`    |
| `Document` |   `"#document"`   |
|   `Text`   |     `"#text"`     |

▎Node.**nodeValue** - DOMString | null

|      Interface       |     return value     |
| :------------------: | :------------------: |
|   `Text` `Comment`   | `CharacterData.data` |
| `Document` `Element` |        `null`        |

▎Node.**textContent** - DOMString | null

|    Interface     |      return value      |
| :--------------: | :--------------------: |
|    `Document`    |         `null`         |
| `Text` `Comment` |  `CharacterData.data`  |
|    `Element`     | 节点内所有文本节点的值 |

设置该属性，将所有子节点被移除，替换为一个新文本节点。

### 节点关系

▎Node.**ownerDocument** - _readonly_ - Document | null - 此节点所属的顶层 document 对象

▎Node.**parentNode** - _readonly_ - Node | null - 父节点

▎Node.**parentElement** - _readonly_ - Element | null - 父元素

▎Node.**hasChildNodes** - 是否有子节点

```ts
node.hasChildNodes(): boolean
```

▎Node.**childNodes** - _readonly_ - NodeList - 返回即时更新的动态集合

```js
var firstChild = someNode.childNodes[0]
var secondChild = someNode.childNodes.item[1]
var count = someNode.childNodes.length
```

▎Node.**firstChild** - _readonly_ - Node | null - 第一个子节点

```js
someNode.firstChild === someNode.childNodes[0] // true
```

▎Node.**lastChild** - _readonly_ - Node | null - 最后一个子节点

```js
someNode.lastChild === someNode.childNodes[someNode.childNodes.length - 1] // true
```

▎Node.**previousSibling** - _readonly_ - Node | null - 前一个兄弟节点

▎Node.**nextSibling** - _readonly_ - Node | null - 后一个兄弟节点

<br>

▎Node.**contains** - other 是否是该节点的后代

```ts
node.contains(other: Node | null): boolean
```

```js
function isInPage(node) {
  return node === document.body ? false : document.body.contains(node)
}
```

### 操作节点

▎Node.**insertBefore** - 在 child 子节点之前插入 node，返回 node

```ts
node.insertBefore(node: Node, child: Node | null): Node

// 若 child 为 null，node 插入到父元素末尾
```

模拟不存在的 `insertAfter` 方法

```js
// 将 node1 插入到 node2 后面
parentNode.insertBefore(node1, node2.nextSibling)
```

▎Node.**appendChild** - 将 node 添加成当前节点的最后一个子节点，返回 node

```ts
node.appendChild(node: Node): Node
```

▎Node.**replaceChild** - 将子节点 child 替换成 node 节点，返回 child

```ts
node.replaceChild(node: Node, child: Node): Node
```

▎Node.**removeChild** - 移除 child 子节点，返回 child

```ts
node.removeChild(child: Node): Node
```

### 其他方法

▎Node.**cloneNode** - 返回一个节点副本

```ts
node.cloneNode(deep: boolean = false): Node

// @参数 deep
// 是否执行深复制
// ▸ 若 deep 为 false，只复制节点本身，\
// 如果是元素节点，还包括它的特性（attribute）
// ▸ 若 deep 为 true，执行深复制，\
// 也就是复制节点及其整个子节点树
```

## NodeList

NodeList 对象是节点的集合，通常由 `Node.childNodes` 属性和 `document.querySelectorAll()` 方法返回。

▎NodeList.**length** - _readonly_ - 返回集合中的节点个数

▎NodeList.**item** - 返回集合中指定索引的节点

```ts
element = collection.item(index)
element = collection[index]
```
## 参考

- [Node - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Node)