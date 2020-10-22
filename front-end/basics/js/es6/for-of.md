# for...of 语句

```ts
for (variable of iterable) {
  statement
}
```

迭代 `Array`

```js
const iterable = [10, 20, 30]

for (const value of iterable) {
  console.log(value)
}
// 10
// 20
// 30
```

迭代 `String`

```js
const iterable = 'boo'

for (const value of iterable) {
  console.log(value)
}
// "b"
// "o"
// "o"
```

迭代 `Map`

```js
const iterable = new Map([
  ['a', 1],
  ['b', 2],
  ['c', 3],
])

for (const entry of iterable) {
  console.log(entry)
}
// ['a', 1]
// ['b', 2]
// ['c', 3]

for (const [key, value] of iterable) {
  console.log(value)
}
// 1
// 2
// 3
```

迭代 `Set`

```js
const iterable = new Set([1, 1, 2, 2, 3, 3])

for (const value of iterable) {
  console.log(value)
}
// 1
// 2
// 3
```

迭代 `TypedArray`

```js
const iterable = new Uint8Array([0x00, 0xff])

for (const value of iterable) {
  console.log(value)
}
// 0
// 255
```

迭代 `arguments` 对象

```js
;(function() {
  for (const argument of arguments) {
    console.log(argument)
  }
})(1, 2, 3)

// 1
// 2
// 3
```

迭代 DOM 集合

```js
// Note: This will only work in platforms that have
// implemented NodeList.prototype[Symbol.iterator]
const articleParagraphs = document.querySelectorAll('article > p')

for (const paragraph of articleParagraphs) {
  paragraph.classList.add('read')
}
```

迭代生成器

```js
function* fibonacci() {
  // a generator function
  let [prev, curr] = [0, 1]
  while (true) {
    ;[prev, curr] = [curr, prev + curr]
    yield curr
  }
}

for (const n of fibonacci()) {
  console.log(n)
  // truncate the sequence at 1000
  if (n >= 1000) {
    break
  }
}
```

## for...of 和 for...in

- `for...in` 语句以任意顺序迭代对象的可枚举属性
- `for...of` 语句迭代可迭代对象定义的可迭代的值

```js
Object.prototype.objCustom = function() {}
Array.prototype.arrCustom = function() {}

const iterable = [3, 5, 7]
iterable.foo = 'hello'

for (const i in iterable) {
  console.log(i) // logs 0, 1, 2, "foo", "arrCustom", "objCustom"
}
for (const i in iterable) {
  if (iterable.hasOwnProperty(i)) {
    console.log(i) // logs 0, 1, 2, "foo"
  }
}
for (const i of iterable) {
  console.log(i) // logs 3, 5, 7
}
```

## 参考

- [for...of - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
