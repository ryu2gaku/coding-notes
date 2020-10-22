# Map

```ts
new Map(iterable?): Map
```

## 实例属性

▎Map.prototype.**size** - 返回 Map 对象的成员总数

## 实例方法

### 操作方法

▎Map.prototype.**set**

```ts
map.set(key: any, value: any): Map
```

```js
var myMap = new Map()

// Add new elements to the map
myMap.set('bar', 'foo')
myMap.set(1, 'foobar')

// Update an element in the map
myMap.set('bar', 'baz')
```

因为 `set` 方法返回 Map 对象本身，所以可以链式调用

```js
// Add new elements to the map with chaining.
myMap
  .set('bar', 'foo')
  .set(1, 'foobar')
  .set(2, 'baz')
```

▎Map.prototype.**get**

```ts
map.get(key: any): any
```

```js
var myMap = new Map()
myMap.set('bar', 'foo')

myMap.get('bar') // Returns "foo".
myMap.get('baz') // Returns undefined.
```

▎Map.prototype.**has**

```ts
map.has(key: any): boolean
```

```js
var myMap = new Map()
myMap.set('bar', 'foo')

myMap.has('bar') // returns true
myMap.has('baz') // returns false
```

▎Map.prototype.**delete**

```ts
map.delete(key: any): boolean
```

```js
var myMap = new Map()
myMap.set('bar', 'foo')

myMap.delete('bar')
// Returns true. Successfully removed.
myMap.has('bar')
// Returns false. The "bar" element is no longer present.
```

▎Map.prototype.**clear**

```ts
map.clear(): void
```

```js
var myMap = new Map()
myMap.set('bar', 'baz')
myMap.set(1, 'foo')

myMap.size // 2
myMap.has('bar') // true

myMap.clear()

myMap.size // 0
myMap.has('bar') // false
```

### 遍历方法

▎Map.prototype.**keys**

```ts
map.keys(): IterableIterator
```

```js
var myMap = new Map()
myMap.set('0', 'foo')
myMap.set(1, 'bar')
myMap.set({}, 'baz')

var mapIter = myMap.keys()

console.log(mapIter.next().value) // "0"
console.log(mapIter.next().value) // 1
console.log(mapIter.next().value) // Object
```

▎Map.prototype.**values**

```ts
map.values(): IterableIterator
```

```js
var myMap = new Map()
myMap.set('0', 'foo')
myMap.set(1, 'bar')
myMap.set({}, 'baz')

var mapIter = myMap.values()

console.log(mapIter.next().value) // "foo"
console.log(mapIter.next().value) // "bar"
console.log(mapIter.next().value) // "baz"
```

▎Map.prototype.**entries**

```ts
map.entries(): IterableIterator
```

```js
var myMap = new Map()
myMap.set('0', 'foo')
myMap.set(1, 'bar')
myMap.set({}, 'baz')

var mapIter = myMap.entries()

console.log(mapIter.next().value) // ["0", "foo"]
console.log(mapIter.next().value) // [1, "bar"]
console.log(mapIter.next().value) // [Object, "baz"]
```

▎Map.prototype.**forEach**

```ts
map.forEach(callback: Function, thisArg?: any): void

// @参数 callback
// callback(
//   value: any,
//   key: any,
//   map: Map
// ): void
```

```js
function logMapElements(value, key, map) {
  console.log(`map.get('${key}') = ${value}`)
}
new Map([
  ['foo', 3],
  ['bar', {}],
  ['baz', undefined],
]).forEach(logMapElements)
// logs:
// "map.get('foo') = 3"
// "map.get('bar') = [object Object]"
// "map.get('baz') = undefined"
```

## 参考

- [Set 和 Map 数据结构 - ECMAScript 6 入门](http://es6.ruanyifeng.com/#docs/set-map#Map)
- [Map - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)