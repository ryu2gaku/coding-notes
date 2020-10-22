# Number

构造器

```js
new Number(value): Number
```

如果参数无法被转换为数字，则返回 `NaN`。没有 `new` 运算符，则用于执行类型转换。

在 JavaScript 中，数值是一种基本的数据类型。`Number` 对象是原始数值的包装对象。

```js
typeof new Number('123') // "object"
typeof Number('123')     // "number"
typeof 123               // "number"
```

在必要时，JavaScript 会自动地把原始数值转化成 `Number` 对象

```js
;(31).toString(2) // "11111"
```

## 静态属性

▎**Number.MIN_VALUE** - 最小正数

▎**Number.MAX_VALUE** - 最大正数

▎**Number.NEGATIVE_INFINITY** - 正无穷 `Infinity`

▎**Number.POSITIVE_INFINITY** - 负无穷 `-Infinity`

▎**Number.NaN** - 表示 `Not-A-Number`，相当于 `NaN`

## 静态方法

▎**Number.isNaN**

```ts
Number.isNaN(value: number): boolean
```

```js
Number.isNaN(NaN)        // true
Number.isNaN(Number.NaN) // true
Number.isNaN(0 / 0)      // true
```

以下使用全局 `isNaN` 时会返回 `true`

```js
Number.isNaN('NaN')     // false
Number.isNaN(undefined) // false
Number.isNaN({})        // false
Number.isNaN('blabla')  // false
```

全局 `isNaN` 会把参数转换为 Number 后在执行。`Number.isNaN` 只有参数是 Number 类型，并且等于 `NaN` 时才返回 `true`

```js
// Polyfill
// 因为 NaN 是 JS 中唯一不等于自身的值
Number.isNaN =
  Number.isNaN ||
  function(value) {
    return value !== value
  }
```

▎**Number.isFinite** - 判断给定值是否为有限数

```ts
Number.isFinite(value: number): boolean
```

```js
Number.isFinite(Infinity) // false
Number.isFinite(NaN) // false
Number.isFinite(-Infinity) // false

Number.isFinite(0) // true
Number.isFinite(2e64) // true
```

全局 `isFinite` 会强制将参数转换为 Number。`Number.isFinite` 只有参数是 Number 类型，并且值有限时才返回 `true`

```js
// Polyfill
if (Number.isFinite === undefined)
  Number.isFinite = function(value) {
    return typeof value === 'number' && isFinite(value)
  }
```

▎**Number.isInteger** - 判断参数值是否为一个整数

```ts
Number.isInteger(value: number): boolean
```

```js
// Polyfill
Number.isInteger =
  Number.isInteger ||
  function(value) {
    return (
      typeof value === 'number' &&
      isFinite(value) &&
      Math.floor(value) === value
    )
  }
```

▎**Number.parseInt** - 解析字符串为给定基数的整数

```ts
Number.parseInt(str: string, radix?: number): number

// @参数 radix
// 2～36 之间的整数
```

```js
Number.parseInt === parseInt // true

Number.parseInt('1111011', 2) // 123
Number.parseInt('173', 8)     // 123
Number.parseInt('123', 10)    // 123
Number.parseInt('7b', 16)     // 123
```

▎**Number.parseFloat** - 解析字符串为浮点数

```ts
Number.parseFloat(str: string): number
```

```js
Number.parseFloat === parseFloat // true
```
## 实例方法

▎Number.prototype.**toString** - 返回代表指定 Number 对象的字符串

```ts
number.toString(radix?: number): string

// @参数 radix
// 2～36 之间的整数
```

```js
var value = 123

value.toString(2)  // "1111011"
value.toString(8)  // "173"
value.toString(10) // "123"
value.toString(16) // "7b"
```

▎Number.prototype.**toExponential** - 返回以指数表示法的字符串

```ts
number.toExponential(fractionDigits?: number): string

// @参数 fractionDigits
// 小数位数，默认情况用尽可能多的位数来显示数字
```

```js
var numObj = 77.1234
numObj.toExponential()  // "7.71234e+1"
numObj.toExponential(4) // "7.7123e+1"
numObj.toExponential(2) // "7.71e+1"

;(77.1234).toExponential() // "7.71234e+1"
```

▎Number.prototype.**toFixed** - 返回以小数表示法的字符串

```ts
number.toFixed(digits?: number): string

// @参数 digits
// 小数位数（0～20 之间）
// 若省略，则将其视为 0
```

```js
var numObj = 12345.6789
numObj.toFixed()  // "12346"
numObj.toFixed(1) // "12345.7"
numObj.toFixed(6) // "12345.678900"

;(1.23e20).toFixed(2)  // "123000000000000000000.00"
;(1.23e-10).toFixed(2) // "0.00"
```

▎Number.prototype.**toPrecision** - 把数字格式化为指定的长度


```ts
number.toPrecision(precision?: number): string

// 精确到整数部分时，指数表示
// 没有精确到整数部分时，小数表示
```

```js
var value = 1234.5678
value.toPrecision(1) // "1e+3"
value.toPrecision(3) // "1.23e+3"
value.toPrecision(5) // "1234.6"
value.toPrecision(7) // "1234.568"
```