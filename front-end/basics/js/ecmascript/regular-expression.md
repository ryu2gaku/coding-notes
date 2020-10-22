# 正则表达式

## 1. RegExp

### 1.1. 创建正则表达式

字面量语法

```js
/pattern/afgls;
```

构造器语法

```ts
new RegExp(pattern, flags): RegExp

// @参数
// @pattern: 模式
// @flags: 标志
// 1) g (global): 全局匹配
// 查找所有匹配，而不是在第一个匹配后停止
// 2) i (ignoreCase): 不区分大小写
// 3) m (multiline): 多行
// 开始和结束字符（^ 和 $）工作在多行模式。
// 也就是匹配字符串中每一行的开始和结束由 \n 或 \r 界定，
// 而不只是整个输入字符串的最开始和最末尾处
// 4) s (dotAll): 允许 . 匹配换行符
// 5) u(unicode)
// 6) y(sticky)
```

```js
// 匹配字符串中所有 "at"
var re1 = /at/g;

// 匹配第一个 "bat" 或 "cat"，不区分大小写
var re2 = /[bc]at/i;
// or
var re2 = new RegExp("[bc]at", "i");

// 匹配所有以 "at" 结尾的 3 个字符的组合，不区分大小写
var re3 = /.at/gi;

// 匹配所有 ".at"，不区分大小写
var re4 = /\.at/gi;
```

### 1.2. 实例属性

✦ RegExp.**lastIndex** ✦ 下一次匹配的起始索引

```ts
regExp.lastIndex;
```

> 仅当正则表达式实例使用了 `g` 或 `y` 标志时才设置该属性。

✦ RegExp.prototype.**flags** ✦ 返回当前正则表达式对象的标志组成的字符串

✦ RegExp.prototype.**global** ✦ 是否设置了 `g` 标志

✦ RegExp.prototype.**ignoreCase** ✦ 是否设置了 `i` 标志

✦ RegExp.prototype.**multiline** ✦ 是否设置了 `m` 标志

✦ RegExp.prototype.**source** ✦ 正则表达式对象的模式文本的字符串

```js
var re = /\[bc\]at/i;
re.global; // false
re.ignoreCase; // true
re.multiline; // false
re.lastIndex; // 0
re.source; // "\[bc\]at"
```

### 1.3. 实例方法

✦ RegExp.prototype.**exec** ✦ 在一个指定字符串中执行搜索匹配

```ts
regexp.exec(str): RegExpExecArray

// @返回值
// 包含第一个匹配项信息的数组
// 若匹配失败则返回 null
```

返回值的结构

| 属性／索引    | 描述                         |
| ------------- | ---------------------------- |
| `[0]`         | 整个模式匹配的字符串         |
| `[1]` ~ `[n]` | 与模式中的捕获组匹配的字符串 |
| `index`       | 匹配项在字符串中的位置       |
| `input`       | 应用正则表达式的字符串       |

```js
var re = /quick\s(brown).+?(jumps)/gi;
var result = re.exec("The Quick Brown Fox Jumps Over The Lazy Dog");

// result 对象
// [
//   "Quick Brown Fox Jumps",
//   "Brown",
//   "Jumps",
//   index: 4,
//   input: "The Quick Brown Fox Jumps Over The Lazy Dog"
// ]

// re 对象
// re.lastIndex  => 25
// re.ignoreCase => true
// re.global     => true
// re.multiline  => false
// re.source     => "quick\s(brown).+?(jumps)"
```

✦ RegExp.prototype.**test** ✦

```ts
regexp.test(str): boolean
```

```js
var text = "000-00-0000";
var re = /\d{3}-\d{2}-\d{4}/;
if (re.test(text)) {
  console.log("The pattern was matched.");
}
```

全局匹配的正则表达式使用 `test` 方法

如果正则表达式设置了 `g` 标志，则使用 `test` 会增加正则表达式的 `lastIndex` 属性值（`exec` 同理）

```js
var regex = /foo/g;

// regex.lastIndex is at 0
regex.test("foo"); // true
// regex.lastIndex is now at 3
regex.test("foo"); // false

// regex.lastIndex is at 0
regex.test("barfoo"); // true
// regex.lastIndex is at 6
regex.test("foobar"); //false
```

## 2. 正则表达式模式

### 2.1. 工具网站

- [RegExr](http://www.regexr.com/)
- [Regexper](https://regexper.com/)

### 2.2. 字符类 Character Classes

| 字符              | 描述                                          |
| ----------------- | --------------------------------------------- |
| `.`               | 通配符：与除换行符之外的任意单个字符匹配      |
| `\d`              | 与任何十进制数字匹配，等价于 `[0-9]`          |
| `\D`              | 等价于 `[^0-9]`                               |
| `\w`              | 匹配字母、数字、下划线，等价于 `[A-Za-z0-9_]` |
| `\W`              | 等价于 `[^A-Za-z0-9_]`                        |
| `\s`              | 与任何空白字符匹配                            |
| `\S`              | 与任何非空白字符匹配                          |
| `\t`              | 与制表符匹配                                  |
| `\r`              | 与回车符匹配                                  |
| `\n`              | 与换行符匹配                                  |
| `\v`              | 与垂直制表符匹配                              |
| `\f`              | 与换页符匹配                                  |
| `[\b]`            | 与退格键匹配（不要与 `\b` 混淆）              |
| `[\u4e00-\u9fa5]` | 与中文字符匹配                                |

```js
/a*/; // 匹配零个或多个 "a"
/a\*/; // 匹配 "a*"
```

### 2.3. 字符集合 Character Sets

| 字符              | 描述                                                    |
| ----------------- | ------------------------------------------------------- |
| `[xyz]` `[a-c]`   | 匹配字符集合中的任何单个字符，可使用 `'-'` 指定字符范围 |
| `[^xyz]` `[^a-c]` | 求反：与不在字符集合中的任何单个字符匹配                |

```js
/[ae]/; // 匹配 "gray" 中的 "a", "lane" 中的 "a", "e"
/[^aei]/; // 匹配 "reign" 中的 "r", "g", "n
```

### 2.4. 交替 Alternation

<table>
  <tr><th>字符</th><th>描述</th></tr>
  <tr>
    <td><code>|</code></td>
    <td>匹配以竖线 <code>|</code> 字符分隔的任何一个元素</td>
  </tr>
</table>

```js
/th(e|is|at)/;
// 匹配 "this is the day." 中的 "the", "this"
```

### 2.5. 边界 Boundaries

| 字符 | 描述                                                         |
| ---- | ------------------------------------------------------------ |
| `^`  | 匹配字符串的开始位置。如果设置了多行，也匹配换行符之后的位置 |
| `$`  | 匹配字符串的结束位置。如果设置了多行，也匹配换行符之前的位置 |

```js
/^\d{3}/  // 匹配 "901-333-" 中的 "901"
/-\d{3}$/ // 匹配 "-901-333" 中的 "-333"
```

| 字符 | 描述                                         |
| ---- | -------------------------------------------- |
| `\b` | 匹配必须出现在 `\w` 和 `\W` 字符之间的边界上 |
| `\B` | 匹配不得出现在 `\b` 边界上                   |

```js
/\b\w+\s\w+\b/
// 匹配 "them theme them them" 中的 "them theme", "them them"
/\Bend\w*\b/
// 匹配 "end sends endure lender" 中的 "ends", "ender"
```

### 2.6. 分组和反向引用 Grouping and back references

| 字符           | 描述                                                |
| -------------- | --------------------------------------------------- |
| `(子表达式)`   | 捕获匹配的子表达式并将其分配到一个从 1 开始的序号中 |
| `(?:子表达式)` | 定义非捕获组                                        |
| `\数值`        | 匹配编号子表达式的值                                |

```js
/(\w)\1/
// 匹配 "seek" 中的 "ee"
/Write(?:Line)?/
// 匹配 "Console.WriteLine()" 中的 "WriteLine"
```

### 2.7. 数量词 Quantifiers

| 字符    | 描述                                   |
| ------- | -------------------------------------- |
| `*`     | 匹配上一个元素零次或多次               |
| `+`     | 匹配上一个元素一次或多次               |
| `?`     | 匹配上一个元素零次或一次               |
| `{n,m}` | 匹配上一个元素至少 n 次，但不多于 m 次 |
| `{n,}`  | 匹配上一个元素至少 n 次                |
| `{n}`   | 匹配上一个元素恰好 n 次                |

```js
/\d*\.\d/;
// 匹配 ".0", "19.9", "219.9"
/'be+' /;
// 匹配 "been" 中的 "bee", "bent" 中的 "be"
/"rai?n"/;
// 匹配 "ran", "rain"
/',d{3}' /;
// 匹配 "1,043.6" 中的 ",043", "9,876,543,210" 中的 ",876", ",543", ",210"
/"\d{3,5}"/;
// 匹配 "193024" 中的 "19302"
```

在 `* ? + {}` 后面紧跟 `?` 表示非贪婪匹配（最小可能匹配），默认是贪婪匹配。

```js
/<.*>/  // 匹配 "<foo> <bar>" 中的 "<foo> <bar>"
/<.*?>/ // 匹配 "<foo> <bar>" 中的 "<foo>"
/\w+/   // 匹配 "abc" 中的 "abc"
/\w+?/  // 匹配 "abc" 中的 "a"
```

### 2.8. 断言 Assertions

| 字符           | 描述                 |
| -------------- | -------------------- |
| `(?=子表达式)` | 零宽度正预测先行断言 |
| `(?!子表达式)` | 零宽度负预测先行断言 |

```js
/\w+(?=\.)/     // 匹配 "He is. The dog ran. The sun is out." 中的 "is", "ran", "out"
/\b(?!un)\w+\b/ // 匹配 "unsure sure unity used" 中的 "sure", "used"
```

## 3. 参考

- [正则表达式 - JavaScript | MDN](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions)
- [正则表达式语言 - 快速参考 | Microsoft Docs](https://docs.microsoft.com/zh-cn/dotnet/standard/base-types/regular-expression-language-quick-reference)
