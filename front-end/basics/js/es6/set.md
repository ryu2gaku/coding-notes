# Set

```ts
new Set(iterable?: Iterable): Set
```

Set 集合中的值是唯一的，它只会出现一次。

## 实例属性

▎Set.prototype.**size** - 返回 Set 对象的成员总数

## 实例方法

### 操作方法

▎Set.prototype.**add** - 添加指定值到 Set 对象的尾部，并返回该 Set 对象

```ts
set.add(value: any): Set

// 不能添加重复的值
```

```js
var mySet = new Set()

mySet.add(1)
mySet.add(5).add('some text') // 可以链式调用

console.log(mySet)
// Set [1, 5, "some text"]
```

▎Set.prototype.**delete** - 删除 Set 对象中的指定值，返回布尔值表示删除是否成功

```ts
set.delete(value: any): boolean
```

```js
var mySet = new Set()
mySet.add('foo')

mySet.delete('bar') // Returns false. No "bar" element found to be deleted.
mySet.delete('foo') // Returns true.  Successfully removed.

mySet.has('foo') // Returns false. The "foo" element is no longer present.
```

▎Set.prototype.**has**

```ts
set.has(value: any): boolean
```

▎Set.prototype.**clear** - 清除所有成员

```ts
set.clear(): void
```

### 遍历方法

▎Set.prototype.**keys** - 与 `values` 方法相同

```ts
set.keys(): Iterator
```

▎Set.prototype.**values**

```ts
set.values(): Iterator

// @返回值
// 包含 Set 对象中的按插入顺序排列的所有元素的值
```

```js
var mySet = new Set()
mySet.add('foo')
mySet.add('bar')
mySet.add('baz')

var setIter = mySet.values()

console.log(setIter.next().value) // "foo"
console.log(setIter.next().value) // "bar"
console.log(setIter.next().value) // "baz"
```

▎Set.prototype.**entries**

```ts
set.entries(): Iterator
```

```js
var mySet = new Set()
mySet.add('foobar')
mySet.add(1)
mySet.add('baz')

var setIter = mySet.entries()

console.log(setIter.next().value) // ["foobar", "foobar"]
console.log(setIter.next().value) // [1, 1]
console.log(setIter.next().value) // ["baz", "baz"]
```

▎Set.prototype.**forEach**

```ts
set.forEach(callback: Function, thisArg?: any): void

// @参数 callback
// callback(
//   value: any,
//   key: any,
//   set: Set
// ): void
```

```js
function logSetElements(value1, value2, set) {
  console.log('s[' + value1 + '] = ' + value2)
}

new Set(['foo', 'bar', undefined]).forEach(logSetElements)

// logs:
// "s[foo] = foo"
// "s[bar] = bar"
// "s[undefined] = undefined"
```

## 参考

- [Set 和 Map 数据结构 - ECMAScript 6 入门](http://es6.ruanyifeng.com/#docs/set-map)
- [Set - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
