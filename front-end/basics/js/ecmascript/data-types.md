# 数据类型

最新的 ECMAScript 标准定义了 7 种数据类型

- 6 种原始类型【primitive】
  - **Boolean**
  - **Null**
  - **Undefined**
  - **Number**
  - **String**
  - **Symbol**（ES6 新定义）
- **Object**

## 原始值

**除 Object 以外的所有类型的值都是不可变的**。

例如，不同于 C 语言，JavaScript 中字符串的值是不可变的，JavaScript 中对字符串的操作返回了一个新字符串，原始字符串并没有被改变。

## Boolean 类型

有两个字面值 `true` 和 `false`。

```js
// Boolean()
var message = "hello world!";
var messageAsBoolean = Boolean(message);
```

| 数据类型 | 转换为 `true` 的值 | 转换为 `false` 的值 |
| :------: | :----------------: | :-----------------: |
| `Boolean` | `true` | `false` |
| `String` | 任何非空字符串 | `""` |
| `Number` | 任何非零数字值（包括无穷大） | `0` 和 `NaN` |
| `Object` | 任何对象 | `null` |
| `Undefined` | []() | `undefined` |

## Null 类型

Null 型は値が `null` の 1 種類しかありません。

```js
typeof null;        // "object" (not "null" for legacy reasons)
typeof undefined;   // "undefined"

null === undefined; // false
null == undefined;  // true
null === null;      // true
null == null;       // true
```

## Undefined 类型

没有被赋值的变量的值为 `undefined`。

```js
var message;
alert(message); // "undefined"
alert(age);     // ReferenceError: age is not defined

// 对未初始化和未声明的变量执行 typeof 操作符都返回 undefined 值。
var message;
alert(typeof message); // "undefined"
alert(typeof age);     // "undefined"
```

## Number 类型

- 整数
  - 十进制【Decimal】
  - 八进制【Octal】- 前缀 `0o` 或 `0O`
  - 十六进制【Hexadecimal】- 前缀 `0x` 或 `0X`
  - 二进制【Binary】- 前缀 `0b` 或 `0B`
- 浮点数
  - 语法 `[digits][.digits][(E|e)[(+|-)]digits]`

## String 类型

```js
"string text";
"string text";

var str1 = "123";
var str2 = "123";
console.log(str1 === str2); // true
```

> JavaScript 中，`String`、`Boolean` 和 `Number` 的原始值和对象是有区别的。调用 `valueOf()` 方法可返回对象的原始值。
