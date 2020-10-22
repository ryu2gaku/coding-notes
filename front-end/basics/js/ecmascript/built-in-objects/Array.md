# Array

## 语法

数组字面量

```js
[element0, element1, ..., elementN]
```

数组构造器

```ts
new Array(...element): Array
new Array(arrayLength: number): Array
```

## 静态方法

▎**Array.isArray**

```ts
Array.isArray(value: any): boolean
```

```js
// Polyfill
if (!Array.isArray) {
  Array.isArray = function(arg) {
    return Object.prototype.toString.call(arg) === '[object Array]'
  }
}
```

## 实例属性

▎Array.prototype.**length** - 获取或设置数组的长度

## 实例方法

### 访问器方法 Accessor Methods

▎Array.prototype.**concat**

```ts
array.concat(...value?): Array<any>

// @参数 value
// 若省略，则返回所调用的已存在数组的浅拷贝（shallow copy）

// 如果某一项为数组，则其内容将添加到数组末尾
// 如果不为数组，则将其作为单个数组元素添加到数组末尾
```

```js
const letters = ['a', 'b', 'c']
const numbers = [1, 2, 3]
letters.concat(numbers) // ["a", "b", "c", 1, 2, 3]
```

▎Array.prototype.**slice** - 提取数组的一部分并返回一个新数组

```ts
array.slice(begin?: number, end?: number): Array<any>

// @参数 begin
// 若省略，则从索引 0 开始
// 若大于数组长度则返回空数组

// @参数 end
// 该索引处不被包含在内
// 若省略或大于数组长度，则一直提取到原数组末尾（arr.length）

// 若如果 start/end 为负，则将其视为 length + start/end
```

```js
;['Banana', 'Orange', 'Lemon', 'Apple', 'Mango'].slice(1, 3)
// ["Orange", "Lemon"]
```

▎Array.prototype.**join** - 将数组的所有元素串联成一个字符串

```ts
array.join(separator?: string): string

// @参数 separator
// 数组的元素间分开的字符串
// 若省略，则数组元素之间用逗号分隔
```

```js
var a = ['Wind', 'Rain', 'Fire']
a.join()      // 'Wind,Rain,Fire'
a.join(', ')  // 'Wind, Rain, Fire'
a.join(' + ') // 'Wind + Rain + Fire'
a.join('')    // 'WindRainFire'
```

```js
// array-like object
function f(a, b, c) {
  var s = Array.prototype.join.call(arguments)
  console.log(s)
}
f(1, 'a', true) // 1,a,true
```

▎Array.prototype.**indexOf** - 返回给定值在数组中的第一个匹配项的索引

```ts
array.indexOf(
  searchElement: any,
  fromIndex: number = 0
): number

// @返回值
// 若未找到则返回 -1
```

```js
var arr = [2, 5, 9]
arr.indexOf(2)     // 0
arr.indexOf(7)     // -1
arr.indexOf(9, 2)  // 2
arr.indexOf(2, -1) // -1
arr.indexOf(2, -3) // 0
```

▎Array.prototype.**lastIndexOf** - 返回给定值在数组中的最后一个匹配项的索引

```ts
array.lastIndexOf(
  searchElement: any, 
  fromIndex: number = array.length - 1
): number

// @参数 fromIndex
// 从此位置开始逆向查找，默认从数组中的最后一个索引处开始

// @返回值
// 若没有找到则返回 -1
```

### 修改器方法 Mutator Methods

> 这些方法会修改数组

▎Array.prototype.**push** - 添加新元素到数组的末尾，并返回该数组的新长度

```ts
array.push(...element: any): number
```

```js
var sports = ['soccer', 'baseball']
var total = sports.push('football', 'swimming')

console.log(sports) // ['soccer', 'baseball', 'football', 'swimming']
console.log(total)  // 4
```

▎Array.prototype.**pop** - 删除数组中的最后一个元素，并返回该元素

```ts
array.pop(): any
```

```js
var myFish = ['angel', 'clown', 'mandarin', 'sturgeon']
var popped = myFish.pop()

console.log(myFish) // ['angel', 'clown', 'mandarin' ]
console.log(popped) // 'sturgeon'
```

▎Array.prototype.**unshift** - 添加新元素到数组的开头，并返回该数组的新长度

```ts
array.unshift(...element: any): number
```

```js
arr = [4, 5, 6]
arr.unshift(1)
arr.unshift(2)
arr.unshift(3)

console.log(arr) // [3, 2, 1, 4, 5, 6]
```

▎Array.prototype.**shift** - 删除数组的第一个元素，并返回该元素

```ts
array.shift(): any
```

▎Array.prototype.**reverse** - 颠倒数组中元素的位置

```ts
array.reverse(): Array<any>
```

▎Array.prototype.**splice** - 从数组中移除元素，如有必要，在所移除元素的位置上插入新元素

```ts
array.splice(
  start: number,
  deleteCount?: number,
  ...item?: any
): Array<any>

// @参数 deleteCount
// 若参数省略或大于等于 array.length - start，\
// 则 start 索引之后的所有元素都会被移除
// 若为 0 或负数，则不移除元素

// @参数 ...item
// 要添加进数组的元素，从 start 索引开始，
// 如不指定，则将只移除数组元素

// @返回值
// 所移除的元素
```

```js
var arr = new Array('1', '2', '3', '4', '5', '6')
arr.splice(2, 2, '100', '101') // ["3", "4"]

console.log(arr) // ["1", "2", "100", "101", "5", "6"]
```

▎Array.prototype.**sort** - 对数组中的元素进行排序，并返回该数组

```ts
array.sort(compareFunction?): Array<any>

// @参数 compareFunction
// compareFunction(firstEl, secondEl)
```

```js
var numbers = [4, 2, 5, 1, 3]

numbers.sort(function(a, b) {
  return a - b
})
// ES2015
numbers.sort((a, b) => a - b)

console.log(numbers)
// [1, 2, 3, 4, 5]
```

### 迭代方法 Iteration Methods

▎Array.prototype.**forEach** - 为数组中的每个元素调用给定函数

```ts
array.forEach(callback, thisArg?: any): void

// @参数 callback
// callback(currentValue, index?, array?)

// @参数 thisArg
// callback 中的 this 可引用的对象
```

```js
const items = ['item1', 'item2', 'item3']
const copy = []

// before
for (let i = 0; i < items.length; i++) {
  copy.push(items[i])
}
// after
items.forEach(function(item) {
  copy.push(item)
})
```

▎Array.prototype.**map** - 为数组中的每个元素调用给定函数，并返回包含结果的数组

```ts
array.map(callback, thisArg?: any): Array

// @参数 callback
// callback(currentValue, index?, array?)

// @参数 thisArg
// callback 中的 this 可引用的对象
```

```js
var numbers = [1, 4, 9]
var roots = numbers.map(Math.sqrt)
// roots 的值为 [1, 2, 3]
// numbers 的值仍为 [1, 4, 9]
```

▎Array.prototype.**some** - 测试数组中是否至少有一个元素通过了给定函数的测试

```ts
array.some(callback, thisArg?: any): boolean

// 该方法会为数组中的每个元素调用回调函数，\
// 直到回调函数返回 true 或直到到达数组的结尾

// @参数 callback
// callback(element, index?, array?)

// @参数 thisArg
// callback 中的 this 可引用的对象
```

```js
function isBiggerThan10(element, index, array) {
  return element > 10
}

;[2, 5, 8, 1, 4].some(isBiggerThan10)  // false
;[12, 5, 8, 1, 4].some(isBiggerThan10) // true
```

▎Array.prototype.**every** - 测试数组中是否所有元素通过了给定函数的测试

```ts
array.every(callback, thisArg?: any): boolean

// 该方法会为数组中的每个元素调用回调函数，\
// 直到回调函数返回 false 或直到到达数组的结尾

// @参数 callback
// callback(element, index?, array?)

// @参数 thisArg
// callback 中的 this 可引用的对象
```

```js
function isBigEnough(element, index, array) {
  return element >= 10
}

;[12, 5, 8, 130, 44].every(isBigEnough)   // false
;[12, 54, 18, 130, 44].every(isBigEnough) // true
```

▎Array.prototype.**filter** - 返回数组中的满足给定函数过滤的元素组成的数组

```ts
array.filter(callback, thisArg?: any): Array

// 对数组的每个元素调用定义的回调函数，\
// 并返回回调函数为其返回 true 的值的数组

// @参数 callback
// callback(element, index?, array?)

// @参数 thisArg
// callback 中的 this 可引用的对象
```

```js
function isBigEnough(value) {
  return value >= 10
}
var filtered = [12, 5, 8, 130, 44].filter(isBigEnough)
// filtered is [12, 130, 44]
```

▎Array.prototype.**reduce** - 数组的每项执行给定的累加器（reducer）函数，最终累计为一个值

```ts
array.reduce(callback, initialValue?): any

// @参数 callback
// callback(accumulator, currentValue, currentIndex?, sourceArray?)
// + accumulator(acc) 累计器
// + currentValue(cur) 当前值
// + currentIndex(idx) 当前索引
// + sourceArray(src) 源数组

// @参数 initialValue
// 初次调用 callback 时第一个参数的值，\
// 若未提供则将使用数组中的第一个元素

// @返回值
// 函数累计处理的结果
```

```js
;[0, 1, 2, 3, 4].reduce(function(previousValue, currentValue, index, array) {
  return previousValue + currentValue
}) // 10
// ES2015
;[0, 1, 2, 3, 4].reduce(
  (accumulator, currentValue, currentIndex, array) => accumulator + currentValue
)

// 该回调将被调用四次，每次调用中的参数和返回值如下
// -----------------------------------------
// acc | cur | idx |       src       | 返回值
// ----|-----|-----|-----------------| -----
// 0   |  1  |  1  | [0, 1, 2, 3, 4] | 1
// 1   |  2  |  2  | [0, 1, 2, 3, 4] | 3
// 3   |  3  |  3  | [0, 1, 2, 3, 4] | 6
// 6   |  4  |  4  | [0, 1, 2, 3, 4] | 10
```

提供了第二个参数的情况

```js
;[0, 1, 2, 3, 4].reduce((accumulator, currentValue, currentIndex, array) => {
  return accumulator + currentValue
}, 10) // 20

// -----------------------------------------
// acc | cur | idx |       src       | 返回值
// ----|-----|-----|-----------------| -----
// 10  |  0  |  0  | [0, 1, 2, 3, 4] | 10
// 10  |  1  |  1  | [0, 1, 2, 3, 4] | 11
// 11  |  2  |  2  | [0, 1, 2, 3, 4] | 13
// 13  |  3  |  3  | [0, 1, 2, 3, 4] | 16
// 16  |  4  |  4  | [0, 1, 2, 3, 4] | 20
```

▎Array.prototype.**reduceRight** - 与 reduce 的执行方向相反

```js
array.reduceRight(callback, initialValue?): any

// @参数 callback
// callback(accumulator, currentValue, currentIndex?, sourceArray?)
```