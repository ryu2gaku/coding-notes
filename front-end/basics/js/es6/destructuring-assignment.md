# 解构赋值 Destructuring Assignment

## 数组解构 Array Destructuring

### 基本用法

```js
var foo = ['one', 'two', 'three']

var [one, two, three] = foo
console.log(one) // "one"
console.log(two) // "two"
console.log(three) // "three"
```

```js
var a, b
;[a, b] = [1, 2]
console.log(a) // 1
console.log(b) // 2
```

### 默认值

从数组中提取的值是 `undefined` 时使用

```js
var a, b
;[a = 5, b = 7] = [1]
console.log(a) // 1
console.log(b) // 7
```

### 交换变量

```js
var a = 1
var b = 3

;[a, b] = [b, a]
console.log(a) // 3
console.log(b) // 1
```

### 解析从函数返回的数组

```js
function f() {
  return [1, 2]
}

var a, b
;[a, b] = f()
console.log(a) // 1
console.log(b) // 2
```

### 忽略某些返回值

```js
function f() {
  return [1, 2, 3]
}

var [a, , b] = f()
console.log(a) // 1
console.log(b) // 3
```

## 将数组剩余部分赋值给一个变量

```js
var [a, ...b] = [1, 2, 3]
console.log(a) // 1
console.log(b) // [2, 3]
```

```js
var [a, ...b] = [1, 2, 3]
// a = 1, b = [2, 3]

var [a, ...b,] = [1, 2, 3]
// SyntaxError: rest element may not have a trailing comma
```

## 对象解构 Object Destructuring

对象的解构与数组有一个重要的不同。数组的元素是按次序排列的，变量的取值由它的位置决定。而对象的属性没有次序，变量必须与属性同名，才能取到正确的值。

### 基本用法

```js
var o = { p: 42, q: true }
var { p, q } = o

console.log(p) // 42
console.log(q) // true
```

实际上对象的解构赋值是下面形式的简写

```js
let { foo, bar } = { foo: 'aaa', bar: 'bbb' }
let { foo: foo, bar: bar } = { foo: 'aaa', bar: 'bbb' }
```

已声明的变量用于解构赋值，需要将解构赋值语句放在 `()` 里

```js
var a, b
;({ a, b } = { a: 1, b: 2 })
```

因为 JS 引擎会将 `{}` 理解成一个代码块，从而发生语法错误。只有不将大括号写在行首，避免 JS 将其解释为代码块，才能解决这个问题。

对象的解构赋值，可以很方便地将现有对象的方法，赋值到某个变量。

```js
const { log, sin, cos } = Math

const { log } = console
log('hello') // hello
```

### 赋值给新的变量名

如果变量名与属性名不一致

```js
var o = { p: 42, q: true }
var { p: foo, q: bar } = o

console.log(foo) // 42
console.log(bar) // true
```

### 默认值

```js
var { a = 10, b = 5 } = { a: 3 }

console.log(a) // 3
console.log(b) // 5
```

### 赋值给新的变量名并提供默认值

```js
var { a: aa = 10, b: bb = 5 } = { a: 3 }

console.log(aa) // 3
console.log(bb) // 5
```

### 函数参数的解构赋值

```js
var user = {
  id: 42,
  displayName: 'jdoe',
  fullName: {
    firstName: 'John',
    lastName: 'Doe',
  },
}

function userId({ id }) {
  return id
}

function whois({ displayName, fullName: { firstName: name } }) {
  return `${displayName} is ${name}`
}

console.log(userId(user)) // 42
console.log(whois(user)) // "jdoe is John"
```

```js
// ES5 版本
function drawES5Chart(options) {
  options = options === undefined ? {} : options
  var size = options.size === undefined ? 'big' : options.size
  var cords = options.cords === undefined ? { x: 0, y: 0 } : options.cords
  var radius = options.radius === undefined ? 25 : options.radius
  console.log(size, cords, radius)
  // now finally do some chart drawing
}

// ES2015 版本
function drawES2015Chart({
  size = 'big',
  cords = { x: 0, y: 0 },
  radius = 25,
} = {}) {
  console.log(size, cords, radius)
  // do some chart drawing
}

drawES2015Chart({
  cords: { x: 18, y: 30 },
  radius: 30,
})
```

## 参考

- [变量的解构赋值 - ECMAScript 6 入门](http://es6.ruanyifeng.com/#docs/destructuring)
- [Destructuring assignment - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)
