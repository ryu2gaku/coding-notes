# 运算符

▎**delete** - 删除一个对象的属性

语法 `delete object.property` 或 `delete object['property']`

▎**in** - 指定属性是否存在于指定对象中

语法 `prop in object`（`prop` 表示属性名的字符串，或数组索引的数字）

▎**instanceof** - 一个对象在其原型链中是否存在一个构造函数的 prototype 属性

语法 `object instanceof constructor`

```js
// object のプロトタイプチェイン(prototype chain)で \
// constructor.prototype の存在を確認します
function C() {}

var o = new C()
o instanceof C // true
// 因为 Object.getPrototypeOf(o) === C.prototype
o instanceof Object // true
// 因为 Object.prototype.isPrototypeOf(o) 返回 true

C.prototype = {}
o instanceof C // false
```

▎**typeof** - 返回一个字符串，表示未经计算的操作数的类型

语法 `typeof operand` 和 `typeof (operand)`

可能的返回值：

|  Type  | Result |
| ------ | ------ |
| Undefined | `"undefined"` |
| Boolean | `"boolean"` |
| Number | `"number"` |
| String | `"string"` |
| Symbol | `"symbol"` |
| Function 对象 | `"function"` |
| Null 或任何其他对象 | `"object"` |

```js
// Numbers
typeof Infinity === 'number'
typeof NaN === 'number' // 尽管是 "Not-A-Number"
typeof Number('1') === 'number'

// Strings
typeof '' === 'string'
typeof `template literal` === 'string'
typeof String(1) === 'string'

// Booleans
typeof true === 'boolean'
typeof false === 'boolean'
typeof Boolean(1) === 'boolean'

// Undefined
typeof undefined === 'undefined'
typeof declaredButUndefinedVariable === 'undefined'
typeof undeclaredVariable === 'undefined'

// Objects
typeof { a: 1 } === 'object'
typeof [1, 2, 4] === 'object'

typeof new Date() === 'object'
typeof /regex/ === 'object'

typeof new Boolean(true) === 'object'
typeof new Number(1) === 'object'
typeof new String('abc') === 'object'

// Functions
typeof function() {} === 'function'
typeof class C {} === 'function'
```

▎**void** - 指定一个表达式无返回值

语法 `void expression` 和 `void (expression)`

▎**new** - 创建一个对象实例

语法 `new constructor[([arguments])]`

当代码 `new Foo()` 被执行：

- 一个新对象被创建，它继承自 `Foo.prototype`。
- 构造函数 `Foo` 被以指定参数调用，同时 `this` 会被指定为这个新对象。`new Foo` 等同于 `new Foo()`，只能用在不传递任何参数的情况。
- 如果构造函数返回了一个对象，那么这个对象会成为整个 `new` 表达式的结果。如果构造函数没有返回对象，那么 `new` 表达式的结果为步骤一创建的对象。一般情况下构造函数不返回任何值，不过用户如果想覆盖这个返回值，可以自己选择返回一个普通对象来覆盖。
