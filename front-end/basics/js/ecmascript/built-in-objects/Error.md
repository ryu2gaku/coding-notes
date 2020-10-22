# Error

构造器

```ts
new Error(message: string, fileName?, lineNumber?): Error

// @参数 message
// 错误描述信息

// 以下参数非标准
// @参数 fileName
// 默认是调用 Error 构造器代码所在的文件的名字

// @参数 lineNumber
// 默认是调用 Error 构造器代码所在的文件的行号
```

```js
// this:
const x = Error('I was created using a function call!')
​​​​// has the same functionality as this:
const y = new Error('I was constructed via the "new" keyword!')
```

# 案例

使用 `throw` 关键字来抛出创建的 `Error` 对象，使用 `try...catch` 结构来处理异常

```js
try {
  throw new Error('Whoops!')
} catch (e) {
  console.error(e.name + ': ' + e.message)
}
```

处理一个特定错误

```js
try {
  foo.bar()
} catch (e) {
  if (e instanceof EvalError) {
    console.error(e.name + ': ' + e.message)
  } else if (e instanceof RangeError) {
    console.error(e.name + ': ' + e.message)
  }
  // ... etc
}
```

## Error 类型

- EvalError
- InternalError
- RangeError
- ReferenceError
- SyntaxError
- TypeError
- URIError
