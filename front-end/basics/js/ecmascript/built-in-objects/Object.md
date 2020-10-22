# Object

构造器

```ts
new Object(value): Object

// 为给定的值创建一个对象包装
// 如果给定值是 null 或 undefined，创建并返回一个空对象，\
// 否则，返回一个与给定值对应类型的对象
// 如果给定值已是对象，则返回该值
```

对象初始化器（initialiser）或对象字面量（literal）

```js
{"键值对1", "键值对2", ..."键值对N"}

var obj = { a: "foo", b: 42, c: {} }
```

访问对象的属性

- 点符号表示法 `object.property`
- 括号表示法 `object["property"]`

## 构造器属性

▎**Object.prototype** - 表示对象 Object 的原型对象

可以为所有 Object 类型的对象添加属性

## 构造器方法

▎**Object.defineProperty** - 在对象上定义或修改一个属性，并返回该对象

```ts
Object.defineProperty(
  obj: any,
  prop,
  descriptor: propertyDescriptor
): object

// @属性 prop
// 被定义或修改的属性名称

// @参数 descriptor
// 被定义或修改的属性的描述符
```

❐ 属性描述符 ❐

对象里目前存在的属性描述符有两种主要形式：**数据描述符**（data descriptor）和**存取描述符**（accessor descriptor）

描述符必须是两种形式之一，不能同时是两者。

❐ 两类皆具有的键值（必须）

- `configurable` - 表示对象的属性是否可以被删除，以及除 `writable` 特性外的其他特性是否可以被修改，默认 `false`。
- `enumerable` - 属性是否可枚举，默认 `false`

如果一个属性的 `configurable` 为 `false`，那么 `writable` 标志符也仅仅只能修改为 `false`。

❐ 数据描述符键值（可选）

- `value` - 属性的值，默认 `undefined`
- `writable` - 为 `true` 时，该属性关联的值才能被改变，默认 `false`

❐ 存取描述符键值（可选）

- `get` - 给属性提供 getter 的方法，默认 `undefined`
- `set` - 给属性提供 setter 的方法，默认 `undefined`

Configurable 特性（attribute）

```js
var o = {}
Object.defineProperty(o, 'a', {
  get() {
    return 1
  },
  configurable: false,
})

Object.defineProperty(o, 'a', { configurable: true }) // throws a TypeError
Object.defineProperty(o, 'a', { enumerable: true }) // throws a TypeError
Object.defineProperty(o, 'a', { set() {} }) // throws a TypeError
Object.defineProperty(o, 'a', {
  get() {
    return 1
  },
}) // throws a TypeError
Object.defineProperty(o, 'a', { value: 12 }) // throws a TypeError

console.log(o.a) // logs 1
delete o.a // 何も起きません
console.log(o.a) // logs 1

// 如果 o.a 的 configurable 特性为 true，\
// 则不会抛出任何错误，并且该属性将在最后被删除
```

使用点表示法和使用 `Object.defineProperty` 为对象的属性赋值时，数据描述符中的特性默认值是不同的

```js
var o = {}
o.a = 1
// 等同于
Object.defineProperty(o, 'a', {
  value: 1,
  writable: true,
  configurable: true,
  enumerable: true,
})

// 另一方面
Object.defineProperty(o, 'a', { value: 1 })
// 等同于
Object.defineProperty(o, 'a', {
  value: 1,
  writable: false,
  configurable: false,
  enumerable: false,
})
```

自定义 setter 和 getter，下例展示如何实现一个自归档对象

```js
function Archiver() {
  var temperature = null
  var archive = []

  Object.defineProperty(this, 'temperature', {
    get() {
      console.log('get!')
      return temperature
    },
    set(value) {
      temperature = value
      archive.push({ val: temperature })
    },
  })

  this.getArchive = function() {
    return archive
  }
}

var arc = new Archiver()
arc.temperature // 'get!'
arc.temperature = 11
arc.temperature = 13
arc.getArchive() // [{ val: 11 }, { val: 13 }]
```

▎**Object.defineProperties** - 在对象上定义或修改一个或多个属性，并返回该对象

```ts
Object.defineProperties(
  obj: any,
  props: PropertyDescriptorMap
): object
```

```js
var obj = {}
Object.defineProperties(obj, {
  prop1: {
    value: true,
    writable: true,
  },
  prop2: {
    value: 'Hello',
    writable: false,
  },
})
```

▎**Object.getOwnPropertyDescriptor** - 返回给定对象上一个自有属性对应的属性描述符

```ts
Object.getOwnPropertyDescriptor(obj, prop): PropertyDescriptor
```

```js
var o = {
  get foo() {
    return 17
  },
}
Object.getOwnPropertyDescriptor(o, 'foo')
// {
//   set: undefined,
//   enumerable: true,
//   configurable: true,
//   get: ƒ
//  }

o = { bar: 42 }
Object.getOwnPropertyDescriptor(o, 'bar')
// {
//   value: 42,
//   writable: true,
//   enumerable: true,
//   configurable: true
// }
```

▎**Object.getOwnPropertyDescriptors**

```ts
Object.getOwnPropertyDescriptors(obj): PropertyDescriptorMap
```

▎**Object.create** - 创建一个拥有指定原型和若干个指定属性的对象

```ts
Object.create(
  proto: object,
  props: PropertyDescriptorMap
): object

// @参数 proto
// 新创建对象的原型

// @参数 props
// 包含一个或多个属性描述符
```

```js
var o

// create an object with null as prototype
o = Object.create(null)

o = {}
// 等同于
o = Object.create(Object.prototype)

function Constructor() {}
o = new Constructor()
// 等同于
o = Object.create(Constructor.prototype)
// 若在 Constructor 函数中有一些初始化代码
// Object.create 不能执行这些代码
```

```js
var o = Object.create(Object.prototype, {
  foo: {
    writable: true,
    configurable: true,
    value: 'hello',
  },
  bar: {
    configurable: false,
    get: function() {
      return 10
    },
    set: function(value) {
      console.log('Setting `o.bar` to', value)
    },
    // ES2015 写法
    // get() { return 10 },
    // set(value) {
    //   console.log('Setting `o.bar` to', value)
    // }
  },
})
```

▎**Object.getPrototypeOf** - 返回指定对象的原型（即内部 `[[Prototype]]` 属性的值）

```ts
Object.getPrototypeOf(obj): object
```

```js
var proto = {}
var obj = Object.create(proto)
Object.getPrototypeOf(obj) === proto // true
```

```js
Object.getPrototypeOf(new String()) === String.prototype // true
```

### 枚举对象属性

▎**Object.keys** - 返回一个由给定对象的所有**可枚举自身属性**的属性名组成的数组

```ts
Object.keys(obj): Array<string>
```

```js
Object.keys(['a', 'b', 'c']) // ["0", "1", "2"]
Object.keys({ 100: 'a', 2: 'b', 7: 'c' }) // ["2", "7", "100"]
```

> 数组中属性名的排列顺序和使用 `for-in` 循环遍历该对象时返回的顺序一致。
> 
> 两者的主要区别是 `for-in` 还会遍历出一个对象从其原型链上继承到的可枚举属性。

▎**Object.getOwnPropertyNames** - 返回一个由指定对象的**所有自身属性**的属性名（包括不可枚举属性）组成的数组

```ts
Object.getOwnPropertyNames(obj): Array<string>
```

```js
Object.getOwnPropertyNames(['a', 'b', 'c']).sort()
// ["0", "1", "2", "length"]
```

| 方法或语句 | 自身可枚举属性 | 自身不可枚举属性 | 非自身可枚举属性 |
| ---- | :----: | :----: | :----: |
| `for-in` | ✓ | ✗ | ✓ |
| `Object.keys` | ✓ | ✗ | ✗ |
| `Object.getOwnPropertyNames` | ✓ | ✓ | ✗ |

#### 防篡改对象

▎**Object.preventExtensions** - 让对象变的不可扩展，也就是永远不能再添加新的属性

```ts
Object.preventExtensions(obj): object
```

```js
var obj1 = {}
var obj2 = Object.preventExtensions(obj)
obj1 === obj2 // true
```

▎**Object.seal** - 密封对象

```ts
Object.seal(obj): object

// @返回值
// 被密封的对象
```

▎**Object.freeze** - 冻结对象


```ts
Object.freeze(obj): object

// @返回值
// 被冻结的对象
```

▎**Object.isExtensible** - 判断一个对象是否是可扩展的

```ts
Object.isExtensible(obj): boolean
```

```js
var empty = {}
Object.isExtensible(empty) // true
Object.preventExtensions(empty)
Object.isExtensible(empty) // false

// 密封
var sealed = Object.seal({})
Object.isExtensible(sealed) // false

// 冻结
var frozen = Object.freeze({})
Object.isExtensible(frozen) // false
```

> `Object.preventExtensions` 方法只能阻止一个对象不能再添加新的自身属性，仍然可以为该对象的原型添加属性



▎**Object.isSealed** - 判断一个对象是否是密封的

```ts
Object.isSealed(obj): boolean
```

+ 使对象不可扩展（non-extensible）
+ 为对象的所有属性将 `configurable` 特性设置为 `false`

▎**Object.isFrozen** - 判断一个对象是否被冻结

```ts
Object.isFrozen(obj): boolean
```

+ 使对象不可扩展（non-extensible）
+ 为对象的所有属性将 `configurable` 特性设置为 `false`
+ 为对象的所有数据属性将 `writable` 特性设置为 `false`

不可扩展、密封和冻结三种方法的比较

| 方法 | 对象已设置为不可扩展的 | 为每个属性将 `configurable` 设置为 `false` | 为每个属性将 `writable` 设置为 `false` |
| ---- | :----: | :----: | :----: |
| `Object.preventExtensions` | ✓ | ✗ | ✗ |
| `Object.seal` | ✓ | ✓ | ✗ |
| `Object.freeze` | ✓ | ✓ | ✓ |

如果满足下表中标记的所有条件，则以下方法返回 `true`

| 方法 | 对象是否可扩展 | 为所有属性将 `configurable` 设置为 `false` | 为所有数据属性将 `writable` 设置为 `false` |
| ---- | :----: | :----: | :----: |
| `Object.isExtensible()` | ✓ | ✗ | ✗ |
| `Object.isSealed()` | ✗ | ✓ | ✗ |
| `Object.isFrozen()` | ✗ | ✓ | ✓ |

## 实例属性

▎Object.prototype.**constructor** - 指定用于创建对象的函数

```js
var o = {}
o.constructor === Object // true
var a = []
a.constructor === Array // true
var n = new Number(23)
n.constructor === Number // true

function Tree(name) {
  this.name = name
}
var tree = new Tree('桂花树')
tree.constructor === Tree // true
```

## 实例方法

▎Object.prototype.**hasOwnProperty** - 判断某个对象是否含有指定的自身属性

```ts
obj.hasOwnProperty(prop): boolean
```

```js
var o = new Object()
o.hasOwnProperty('prop') // false
// 自身属性
o.prop = 'exists'
o.hasOwnProperty('prop') // true
// 继承属性
o.hasOwnProperty('toString') // false
o.hasOwnProperty('hasOwnProperty') // false
```

> 和 `in` 运算符不同，该方法会忽略掉那些从原型链上继承到的属性。

▎Object.prototype.**isPrototypeOf** - 测试一个对象是否存在于另一个对象的原型链上

```ts
obj.isPrototypeOf(obj): boolean
```

▎Object.prototype.**propertyIsEnumerable** - 判断指定的属性名是否是当前对象可枚举的自身属性

```ts
obj.propertyIsEnumerable(prop): boolean
```

▎Object.prototype.**valueOf** - 返回该对象的原始值

```ts
obj.valueOf(): primitiveValue
```

▎Object.prototype.**toString** - 返回一个代表该对象的字符串

```ts
obj.toString(): string
```

```js
console.log(Object.prototype.toString.call(Math)) // [object Math]
```