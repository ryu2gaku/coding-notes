# Function

构造器

```ts
new Function (...arg, functionBody: string): Function

// @参数 ...arg
// "x", "theValue" 或 "A, B"
```

```js
var adder = new Function('a', 'b', 'return a + b')
adder(2, 6)
```

## 实例方法

▎Function.prototype.**bind** - 创建一个新函数。该新函数在被调用时，会将 `this` 设为给定值

```ts
func.bind(thisArg, ...arg?: any): Function

// 对于给定函数，创建具有与原始函数相同的主体的绑定函数。
// 在绑定函数中，this 将解析为传入的对象
// 绑定函数具有指定的初始参数
```

创建绑定函数 Bound Function

```js
this.x = 9 // 在浏览器中，this 指向全局的 `window` 对象
var module = {
  x: 81,
  getX: function() {
    return this.x
  },
}

module.getX() // 81

var retrieveX = module.getX
retrieveX()
// 返回 9 - 因为函数是在全局作用域中调用的

// 创建一个新函数，把 `this` 绑定到 module 对象
// 新手可能会将全局变量 x 与 module 的属性 x 混淆
var boundGetX = retrieveX.bind(module)
boundGetX() // 81
```

给绑定函数预设初始参数

当绑定函数被调用时，初始参数会被插入到参数列表的开始位置，函数传递的参数会跟在它们后面。

```js
function list() {
  return Array.prototype.slice.call(arguments)
}
list(1, 2, 3) // [1, 2, 3]

// Create a function with a preset leading argument
var leadingThirtysevenList = list.bind(null, 37)
leadingThirtysevenList() // [37]
leadingThirtysevenList(1, 2, 3) // [37, 1, 2, 3]
```

```js
function addArguments(arg1, arg2) {
  return arg1 + arg2
}
addArguments(1, 2) // 3

// Create a function with a preset first argument.
var addThirtySeven = addArguments.bind(null, 37)
addThirtySeven(5)
// 37 + 5 = 42
addThirtySeven(5, 10)
// 37 + 5 = 42，第二个参数被忽略
```

创建 shortcut

```js
var slice = Array.prototype.slice
slice.apply(arguments)

var unboundSlice = Array.prototype.slice
var slice = Function.prototype.apply.bind(unboundSlice)
slice(arguments)
```

▎Function.prototype.**call** - 用给定 `this` 值以及单独提供的参数调用一个函数

```ts
func.call(thisArg, ...arg?: any): any

// @返回值
// 使用调用者提供的 this 值和参数调用该函数的返回值
```

使用 `call` 来链接对象的构造器，类似于 Java

```js
function Product(name, price) {
  this.name = name
  this.price = price
}
function Food(name, price) {
  Product.call(this, name, price)
  this.category = 'food'
}
function Toy(name, price) {
  Product.call(this, name, price)
  this.category = 'toy'
}

var cheese = new Food('feta', 5)
var fun = new Toy('robot', 40)
```

使用 `call` 方法调用匿名函数

```js
var animals = [
  { species: 'Lion', name: 'King' },
  { species: 'Whale', name: 'Fail' },
]
for (var i = 0; i < animals.length; i++) {
  ;(function(i) {
    this.print = function() {
      console.log('#' + i + ' ' + this.species + ': ' + this.name)
    }
    this.print()
  }.call(animals[i], i))
}
// #0 Lion: King
// #1 Whale: Fail
```

▎Function.prototype.**apply** - 用给定 `this` 值以及数组或类数组对象提供的参数调用一个函数

```ts
func.apply(thisArg, argsArray?: any): any
```

```js
var numbers = [5, 6, 2, 3, 7]

Math.max.apply(null, numbers) // 7
Math.min.apply(null, numbers) // 2
```