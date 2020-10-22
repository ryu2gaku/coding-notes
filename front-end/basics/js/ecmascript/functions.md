# 函数

- 参数为原始类型，值传递
- 参数为对象类型（非原始类型），引用传递

## 函数声明和函数表达式

函数声明（Function Declaration）

```js
// function 函数名([参数列表]) { 函数体 }
function funcDeclaration() {
  return 'A function declaration'
}
```

函数表达式（Function Expression）

```js
// function [函数名]([参数列表]) { 函数体 }
var funcExpression = function() {
  return 'A function expression'
}
```

## 函数提升 Function Hoisting

- 变量声明提升：通过 `var` 声明的变量在代码执行之前被 js 引擎提升到了当前作用域的顶部。
- 函数声明提升：通过函数声明的方式（非函数表达式）声明的函数在代码执行之前被 js 引擎提升到了当前作用域的顶部。**用表达式定义的函数不能提升**。

## 立即执行函数表达式

```js
// IIFE(Immediately Invoked Function Expressions)
;(function() {
  // code in here
})()
```

## arguments

`arguments` 对象是一个类数组对象，代表当前所执行的函数的参数。

可以在函数内部通过使用 `arguments` 对象来获取函数的所有参数。

## 闭包 Closure

闭包是 JavaScript 中最强大的特性之一。

JavaScript 允许函数嵌套，并且内部函数可以访问定义在外部函数中的所有变量和函数（以及外部函数能访问的所有变量和函数）。但是外部函数却不能够访问定义在内部函数中的变量和函数。这给内部函数的变量提供了一定的安全性。

当内部函数生存周期大于外部函数时，由于内部函数可以访问外部函数的作用域，定义在外部函数的变量和函数的生存周期就会大于外部函数本身。当内部函数以某一种方式被任何一个外部函数外的作用域访问时，一个闭包就产生了。

> A closure is a function having access to the parent scope, even after the parent function has closed.

```js
var add = (function() {
  var counter = 0
  return fucntion() {
    return counter += 1;
  }
})()

add()
add()
add()
// the counter is now 3
```

## 全局函数

▎**isFinite()**

▎**isNaN()**

▎**parseFloat()**

▎**parseInt()**

▎**encodeURI()**

```ts
encodeURI(URI): string

// encodeURI escapes all characters except:
// A-Z a-z 0-9 ; , / ? : @ & = + $ - _ . ! ~ * ' ( ) #

// 不对 URI 具有特殊含义的字符（保留字符）进行编码
'http://username:password@www.example.com:80/path/to/file.php?foo=316&bar=this+has+spaces#anchor'
```

```js
var set1 = ';,/?:@&=+$#' // 予約文字（Reserved Characters）
var set2 = "-_.!~*'()"   // 予約されていない記号（Unreserved Marks）
var set3 = 'ABC abc 123' // 英数字 + 空白

encodeURI(set1) // ";,/?:@&=+$#"
encodeURI(set2) // "-_.!~*'()"
encodeURI(set3) // "ABC%20abc%20123" (空白は %20 にエンコードされる)

encodeURIComponent(set1) // "%3B%2C%2F%3F%3A%40%26%3D%2B%24%23"
encodeURIComponent(set2) // "-_.!~*'()"
encodeURIComponent(set3) // "ABC%20abc%20123"
```

▎**encodeURIComponent()**

```ts
encodeURIComponent(str): string

// encodeURIComponent escapes all characters except:
// A-Z a-z 0-9 - _ . ! ~ * ' ( )
```

```js
var set1 = ';,/?:@&=+$'  // Reserved Characters
var set2 = "-_.!~*'()"   // Unescaped Characters
var set3 = '#'           // Number Sign
var set4 = 'ABC abc 123' // Alphanumeric Characters + Space

encodeURI(set1) // ";,/?:@&=+$"
encodeURI(set2) // "-_.!~*'()"
encodeURI(set3) // "#"
encodeURI(set4) // "ABC%20abc%20123"

encodeURIComponent(set1) // "%3B%2C%2F%3F%3A%40%26%3D%2B%24"
encodeURIComponent(set2) // "-_.!~*'()"
encodeURIComponent(set3) // "%23"
encodeURIComponent(set4) // "ABC%20abc%20123"
```

▎**decodeURI()**

▎**decodeURIComponent()**
