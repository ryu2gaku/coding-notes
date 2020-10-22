## 函数参数的默认值

```js
// ES5
function multiply(a, b) {
  b = typeof b !== 'undefined' ? b : 1
  return a * b
}

// ES6
function multiply(a, b = 1) {
  return a * b
}
```

与解构赋值的默认值结合使用

```js
function fetch(url, { body = '', method = 'GET', headers = {} } = {}) {}
```

利用参数默认值，可以指定某一个参数不得省略，如果省略就抛出一个错误。

```js
function throwIfMissing() {
  throw new Error('Missing parameter')
}
function foo(mustBeProvided = throwIfMissing()) {
  return mustBeProvided
}

foo()
// Error: Missing parameter
```

## rest 参数

用于获取函数的多余参数。rest 参数是数组，`arguments` 对象是类数组。

```js
// arguments 变量的写法
function sortNumbers() {
  return Array.prototype.slice.call(arguments).sort()
}

// rest 参数的写法
const sortNumbers = (...numbers) => numbers.sort()
```

注意，rest 参数之后不能再有其他参数，否则会报错。

## 箭头函数

箭头函数表达式是比函数表达式更短的语法。箭头函数总是匿名的。

```js
// 简单用法
var arr = [1, 2, 3, 4]
arr.map(function(value) {
  return value * value
})
arr.map(value => {
  return value * value
})
arr.map(value => value * value)

var arr = [5, 6, 13, 0, 1, 18, 23]
var sum = arr.reduce((a, b) => a + b) // 66
var even = arr.filter(v => v % 2 == 0) // [6, 0, 18]
var double = arr.map(v => v * 2) // [10, 12, 26, 0, 2, 36, 46]
```

由于大括号被解释为代码块，所以如果箭头函数直接返回一个对象，必须在对象外面加上括号，否则会报错。

```js
var func = () => ({ foo: 1 })
```

箭头函数体内的 `this` 对象，就是定义时所在的对象，而不是使用时所在的对象。`this` 对象的指向是可变的，但是在箭头函数中，它是固定的。

```js
function Person() {
  this.age = 0

  setInterval(() => {
    this.age++
  }, 1000)
}

// ECMAScript 3/5
function Person() {
  var that = this
  that.age = 0

  setInterval(function growUp() {
    that.age++
  }, 1000)
}
```

## 参考

- [函数的扩展 - ECMAScript 6 入门](http://es6.ruanyifeng.com/#docs/function)
