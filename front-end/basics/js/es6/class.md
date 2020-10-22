# 类

```js
// ECMAScript 5
function Point(x, y) {
  this.x = x
  this.y = y
}
Point.prototype.toString = function() {
  return '(' + this.x + ', ' + this.y + ')'
}

// ECMAScript 6
class Point {
  constructor(x, y) {
    this.x = x
    this.y = y
  }
  toString() {
    return '(' + this.x + ', ' + this.y + ')'
  }
}
```

## 定义类

### 类声明

```js
class Rectangle {
  constructor(height, width) {
    this.height = height
    this.width = width
  }
}
```

**类声明** 和 **函数声明** 不同的一点是，函数声明存在提升现象，而类声明不会。也就是说你必须先声明类，然后才能使用它。

```js
var p = new Rectangle() // ReferenceError
class Rectangle {}
```

### 类表达式

```js
// 匿名的
var Polygon /*多边形*/ = class {
  constructor(height, width) {
    this.height = height
    this.width = width
  }
}

// 命名的
var Polygon = class Polygon {
  constructor(height, width) {
    this.height = height
    this.width = width
  }
}
```

类表达式和类声明一样也不会有提升的现象。

## 类的主体

类声明和类表达式的主体都在严格模式下执行。

### 构造器

构造器方法是一个特殊的方法，用于创建和初始化该类的对象。一个类只能拥有一个名为 `constructor` 的方法。

```js
constructor([arguments]) {}
```

### 原型方法

```js
class Rectangle {
  // constructor
  constructor(height, width) {
    this.height = height
    this.width = width
  }
  // Getter
  get area() {
    return this.calcArea()
  }
  // Method
  calcArea() {
    return this.height * this.width
  }
}
const square = new Rectangle(10, 10)
console.log(square.area) // 100
```

### 静态方法

`static` 关键字用来定义类的静态方法。

静态方法是指那些不需要对类进行实例化，使用类名就可以直接访问的方法，需要注意的是静态方法不能被实例化的对象调用。静态方法经常用来作为工具函数。

```js
class Point {
  constructor(x, y) {
    this.x = x
    this.y = y
  }
  static distance(a, b) {
    var dx = a.x - b.x
    var dy = a.y - b.y
    return Math.sqrt(dx * dx + dy * dy)
  }
}

var p1 = new Point(5, 5)
var p2 = new Point(10, 10)
console.log(Point.distance(p1, p2)) // 7.0710678118654755
```

## 子类

`extends` 关键字可以用在类声明或者类表达式中来创建一个继承了某个类的子类。

```js
class ChildClass extends ParentClass {}
```

```js
class Animal {
  constructor(name) {
    this.name = name
  }
  speak() {
    console.log(this.name + ' makes a noise.')
  }
}
class Dog extends Animal {
  // 调用超类构造函数，并传入 name 参数
  constructor(name) {
    super(name)
  }
  speak() {
    console.log(this.name + ' barks.')
  }
}

let d = new Dog('Mitzie')
d.speak() // Mitzie barks.
```

若子类中存在构造函数，则在使用 `this` 之前需要调用 `super()`

可以扩展传统的基于函数的“类”

```js
function Animal(name) {
  this.name = name
}
Animal.prototype.speak = function() {
  console.log(this.name + ' makes a noise.')
}

class Dog extends Animal {
  speak() {
    console.log(this.name + ' barks.')
  }
}

var d = new Dog('Mitzie')
d.speak() // Mitzie barks.
```

## 使用 super 调用超类

`super` 关键字用于调用超类的相应方法

```js
class Cat {
  constructor(name) {
    this.name = name
  }
  speak() {
    console.log(`${this.name} makes a noise.`)
  }
}
class Lion extends Cat {
  speak() {
    super.speak()
    console.log(`${this.name} roars.`)
  }
}

let l = new Lion('Fuzzy')
l.speak()
// Fuzzy makes a noise.
// Fuzzy roars.
```

## 参考

- [Classes - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
