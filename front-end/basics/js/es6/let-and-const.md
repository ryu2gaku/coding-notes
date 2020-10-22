# let 和 const

## let

`let` 声明 **块级作用域** 变量，而 `var` 声明 **全局作用域** 或 **函数作用域** 变量。

`let` 与 `var` 对比

```js
var a = 1
var b = 2

if (a === 1) {
  var a = 11 // the scope is global
  let b = 22 // the scope is inside the if-block
  console.log(a) // 11
  console.log(b) // 22
}

console.log(a) // 11
console.log(b) // 2
```

注意 `let` 并不会像 `var` 一样在全局对象上创造一个属性

```js
var x = 'global'
let y = 'global'
console.log(window.x) // "global"
console.log(window.y) // undefined
```

`let` 用于 `for` 语句

```js
for (let i = 0; i < 10; i++) {
  console.log(i)
}
console.log(i) // ReferenceError: i is not defined

// var 用来计数的循环变量泄露为全局变量
for (var i = 0; i < 10; i++) {
  console.log(i)
}
console.log(i) // 10
```

### 暂时性死区

`var` 命令会发生“变量提升”现象，即变量可以在声明之前使用，其值为 `undefined`。

```js
console.log(foo) // undefined
var foo = 2
```

在代码块内，使用 `let` 声明变量之前，该变量是不可用的。这在语法上，称为“暂时性死区”（temporal dead zone，简称 TDZ）。

```js
console.log(foo) // ReferenceError
let foo = 2
```

只要块级作用域内存在 `let` 命令，它所声明的变量就“绑定”这个区域，不再受外部的影响。

```js
var tmp = 123

if (true) {
  tmp = 'abc' // ReferenceError
  let tmp
}
```

上面代码中，存在全局变量 `tmp`，但是块级作用域内 `let` 又声明了一个局部变量 `tmp`，导致后者绑定这个块级作用域，所以在 `let` 声明变量前，对 `tmp` 赋值会报错。

### 不允许重复声明

`let` 不允许在相同作用域内，重复声明同一个变量。

```js
{
  let foo
  let foo // SyntaxError
}

{
  let foo
  var foo // SyntaxError
}
```

下例中因为 `var` 会提升到块的顶部，导致隐式重新声明变量。

```js
let x = 1

if (true) {
  var x = 2 // SyntaxError for re-declaration
}
```

## const

`const` 声明一个只读常量，常量需要被初始化，和 `let` 一样是块级作用域。

`const` 命令声明的常量也是不提升，同样存在暂时性死区，只能在声明的位置后面使用，也与 `let` 一样不可重复声明。

```js
// const 只保证常量指向的地址不变，并不保证该地址的数据不变
const foo = {}
foo.prop = 123
console.log(foo.prop) // 123

foo = {} // TypeError: Assignment to constant variable
// 不能把 foo 指向另一个地址，但对象本身是可变的
// 所以依然可以添加新属性
```

## 参考

- [let 和 const 命令 - ECMAScript 6 入门](http://es6.ruanyifeng.com/#docs/let)
- [let - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
