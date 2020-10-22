# String

构造器

```js
new String(value): String
```
没有 `new` 运算符，则用于执行类型转换。

在 JavaScript 中，字符串是一种基本的数据类型。

```js
typeof new String('123') // "object"
typeof String(123)       // "string"
typeof '123'             // "string"
```

## 实例属性

▎String.prototype.**length** - 字符串长度

## 实例方法

▎String.prototype.**indexOf** - 返回子字符串首次出现的位置

```ts
str.indexOf(searchValue: string, fromIndex?: number): number

// @返回值
// 若未找到则返回 -1
```

```js
'Blue Whale'.indexOf('Blue')     // 0
'Blue Whale'.indexOf('Blute')    // -1
'Blue Whale'.indexOf('Whale', 0) // 5
'Blue Whale'.indexOf('Whale', 5) // 5
'Blue Whale'.indexOf('Whale', 7) // -1
'Blue Whale'.indexOf('')         // 0
'Blue Whale'.indexOf('', 9)      // 9
'Blue Whale'.indexOf('', 10)     // 10
'Blue Whale'.indexOf('', 11)     // 10
```

检测是否存在某字符串

```js
'Blue Whale'.indexOf('Blue') !== -1 // true
'Blue Whale'.indexOf('Bloe') !== -1 // false
```

▎String.prototype.**lastIndexOf** - 返回子字符串最后出现的位置

```ts
str.lastIndexOf(searchValue: string, fromIndex?: number): number

// @返回值
// 若未找到则返回 -1
```

```js
'canal'.lastIndexOf('a')     // 3
'canal'.lastIndexOf('a', 2)  // 1
'canal'.lastIndexOf('a', 0)  // -1
'canal'.lastIndexOf('x')     // -1
'canal'.lastIndexOf('c', -5) // 0
'canal'.lastIndexOf('c', 0)  // 0
'canal'.lastIndexOf('')      // 5
'canal'.lastIndexOf('', 2)   // 2
```

▎String.prototype.**slice** - 提取字符串的片段

```ts
str.slice(beginIndex?: number, endIndex?: number): string

// @参数 beginIndex
// 大于或等于字符串长度时返回 ""
// 为负时被看作是 strLength + beginIndex

// @参数 endIndex
// 该索引处的字符不被包含在内
// 省略时一直提取到字符串末尾
// 为负时被看作是 strLength + endSlice
```

```js
var str = 'The morning is upon us.' // 长度为 23
str.slice(1, 8)   // "he morn"
str.slice(4, -2)  // "morning is upon u"
str.slice(12)     // "is upon us."
str.slice(30)     // ""
str.slice(-3)     // 'us.'
str.slice(-3, -1) // 'us'
str.slice(0, -1)  // 'The morning is upon us'
```

▎String.prototype.**substring** - 提取字符串两个索引之间的子串

```ts
str.substring(indexStart: number, indexEnd?: number): string

// @参数 indexEnd
// 该索引处的字符不被包含在内
// 省略时一直提取到字符串末尾

// @返回值
// indexStart 等于 indexEnd 时返回 ""
// indexStart 大于 indexEnd 时的执行效果像两个参数调换了一样

// 任何参数的值小于 0 或大于 length 均被视为 0 或 length
// 任何参数的值为 NaN 均被视为 0
```

```js
var str = 'Mozilla'
str.substring(0, 1)  // "M"
str.substring(1, 0)  // "M"
str.substring(4)     // "lla"
str.substring(4, 7)  // "lla"
str.substring(7, 4)  // "lla"
str.substring(0, 10) // "Mozilla"
```

`substring` 与 `substr` 的区别

```js
// substr 的参数表示开始索引和子字符串长度
var text = 'Mozilla'
text.substring(2, 5) // "zil"
text.substr(2, 3) // "zil"
```

▎String.prototype.**toUpperCase** - 返回字符串大写形式

```ts
str.toUpperCase(): string
```

▎String.prototype.**toLowerCase** - 返回字符串小写形式

```ts
str.toLowerCase(): string
```

▎String.prototype.**charAt** - 返回字符串中指定位置的字符

```ts
str.charAt(index: number = 0): string

// @参数 index
// 介于 0 和 length-1 之间的整数

// @返回值
// 索引超出范围时返回 ""
```

```js
'ABCDE'.charAt(0) // "A"
'ABCDE'.charAt(1) // "B"
'ABCDE'.charAt(2) // "C"
'ABCDE'.charAt(9) // ""
```

▎String.prototype.**valueOf** - 返回 String 对象的原始值

```ts
str.valueOf(): string
```

▎String.prototype.**toString** - 返回表示指定对象的字符串

```ts
str.toString(): string
```

#### 使用正则表达式

▎String.prototype.**split**

```ts
str.split(
  separator: string | RegExp,
  limit?: number
): Array<string>

// @参数 separator
// 标识用于分隔字符串的字符(s)

// @参数 limit
// 返回数组的最大长度

// @返回值
// 将字符串分割为若干子字符串而组成的数组
```

```js
'A=B=CD=E'.split('=')    // ["A", "B", "CD", "E"]
'A=B=CD=E'.split('=', 2) // ["A", "B"]
'A==B=CD====E'.split('=')
// ["A", "", "B", "CD", "", "", "", "E"]
'A==B=CD====E'.split(/[=]+/)
// ["A", "B", "CD", "E"]
```

若 separator 参数是一个包含捕获组的正则表达式，则其匹配结果将会包含在返回的数组中

```js
'Hello 1 word. Sentence number 2.'.split(/(\d)/)
// ["Hello ", "1", " word. Sentence number ", "2", "."]
'Hello 1 word. Sentence number 2.'.split(/\d/)
// ["Hello ", " word. Sentence number ", "."]
```

▎String.prototype.**search**

```ts
str.search(pattern: RegExp): number

// @参数 pattern
// 如果传入一个非 RegExp 对象，则会使用 new RegExp() 隐式地将其转换为 RegExp

// @返回值
// 第一个子字符串匹配项的位置
// 若失败则返回 -1
```

```js
'ABCDEFGH'.search('B') // 1
```

> 如果想要知道字符串中是否存在某个模式以及它在字符串中的索引时，可使用 `search`方法。
> 
> 如果只想知道它是否存在时，则使用正则表达式的 `test` 方法。
> 
> 如果需要了解更多匹配信息时，可使用 `match`方法（执行速度较慢），类似于正则表达式的 `exec` 方法。

▎String.prototype.**match** - 将字符串与正则表达式匹配

```ts
string.match(pattern: RegExp): RegExpMatchArray

// @参数 pattern
// 如果传入一个非 RegExp 对象，则会使用 new RegExp() 隐式地将其转换为 RegExp

// @返回值
// 包含该搜索结果的数组
```

正则表达式包含 `g` 标志，返回一个包含所有匹配结果的数组。如果没有匹配到，则返回 `null`。

```js
var str = "The rain in SPAIN stays mainly in the plain"

str.match(/ain/gi)) // ["ain", "AIN", "ain", "ain"]
```

正则表达式没有 `g` 标志，返回一个数组。

| 属性 | 描述 |
| ---- | ---- |
| `[0]` | 匹配结果 |
| `[1]` ~ `[n]` | 括号中的分组捕获 |
| `index` | 匹配结果的位置 |
| `input` | 原始字符串 |


```js
var str = "The rain in SPAIN stays mainly in the plain"

str.match(/ain/i)
// [ "ain",
//   index: 5, 
//   input: "The rain in SPAIN stays mainly in the plain" ]
str.match(/(a)(i)(n)/i)
// [ "ain",
//   "a",
//   "i",
//   "n",
//   index: 5,
//   input: "The rain in SPAIN stays mainly in the plain" ]
```

▎String.prototype.**replace**

```ts
str.replace(
  pattern: string | RegExp,
  replacement: string | Function
): string
```

在进行全局的搜索替换时，正则表达式需包含 g 标志。

```js
var str = 'AB===CD==E=='
str.replace(/[=]+/, '+')  // "AB+CD==E=="
str.replace(/[=]+/g, '+') // "AB+CD+E+"
```

指定字符串作为 replacement 参数，替换字符串可以包含以下特殊的替换模式：

| 模式 | 描述 |
| ---- | ---- |
| `$$` | 插入 `$` |
| `$&` | 插入匹配的子串 |
| `$` | 插入当前匹配的子串左边的内容 |
| `$'` | 插入当前匹配的子串右边的内容 |
| `$1` ~ `$n` | 插入第 n 个括号匹配的字符串 |

```js
// 交换字符串中的两个单词的位置
var re = /(\w+)\s(\w+)/
var str = 'John Smith'
var newStr = str.replace(re, '$2 $1')
console.log(newStr) // Smith John
```

指定函数作为 replacement 参数，函数的返回值会作为替换字符串，函数的参数如下：

| 参数 | 描述 |
| ------ | ---- |
| `match` | 匹配的子串
| `p1` ~ `pn` | 代表第 n 个括号匹配的字符串
| `offset` | 匹配到的子字符串在原字符串中的偏移
| `string` | 被匹配的原字符串

```js
var str = 'ABCDEFG'
var newStr = str.replace(/c(d)e/i, function(match, p1, offset, string) {
  console.log(match) // CDE
  console.log(p1) // D
  console.log(offset) // 2
  console.log(string) // ABCDEFG
  return '@@@'
})
console.log(newStr) // AB@@@FG
```