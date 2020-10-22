## Promise

Promise 对象有三种状态：

- `pending`（搁置）初始状态
- `fulfilled`（实现）表示操作成功完成
- `rejected`（拒绝）表示操作失败

构造器

```ts
new Promise(
  executor: (
    resolve: (value?: any) => void, // resolve 解决
    reject: (reason?: any) => void
  ) => void
): Promise

// @参数 executor
// 用于初始化 promise 的回调函数
// 在构造器返回新对象前执行 executor

// 内部属性 [[PromiseStatus]] 和 [[PromiseValue]]
```
`resolve` 函数的作用是将 promise 的状态从 `pending` 变为 `fulfilled`，在异步操作成功时调用，并将异步操作的结果，作为参数传递出去。

`reject` 函数的作用是将 promise 的状态从 `pending` 变为 `rejected`，在异步操作失败时调用，并将异步操作报出的错误，作为参数传递出去。

promise 的状态一旦发生改变，就会一直保持不会再有任何变化。

## 实例方法

> 由于 `Promise.prototype.then` 和 `Promise.prototype.catch` 方法都返回 Promise，它们可以被链式调用。

▎Promise.prototype.**then**

```ts
promise.then(
  onFulfilled?: (value: any) => any, 
  onRejected?: (reason: any) => any
): Promise

// @参数 onFulfilled
// 当 promise 为 fulfilled 状态时执行

// @参数 onRejected
// 当 promise 为 rejected 状态时执行

// then 方法的处理函数会异步调用
```

使用 `then` 方法

```js
new Promise((resolve, reject) => {
  resolve('Success!')
  // or
  // reject(new Error("Error!"))
}).then(
  value => {
    console.log(value) // Success!
  },
  reason => {
    console.error(reason) // Error!
  }
)
```

`then` 方法的处理函数的返回值会被包装成 resolved promise 作为该方法的返回值（处理函数不返回任何值时，则会包装 `undefined`）。

如果处理函数返回 fulfilled promise，则会将其值包装成新的 fulfilled promise 作为该方法的返回值。

```js
var p = new Promise((resolve, reject) => {
  resolve(1)
})

p.then(value => {
  console.log(value)
  return value + 1
}).then(value => {
  console.log(value + ' - A synchronous value works')
})

p.then(value => {
  console.log(value)
})

// 1                             VM58:6
// 1                             VM58:13
// 2 - A synchronous value works VM58:9
```

`then` 方法的处理函数中抛出错误会被包装成 rejected promise 作为该方法的返回值。

如果处理函数返回 rejected promise，则会将其值包装成新的 rejected promise 作为该方法的返回值。

```js
Promise.resolve()
  .then(() => {
    // Makes .then() return a rejected promise
    throw new Error('Oh no!')
  })
  .then(
    () => {
      console.log('Not called.')
    },
    error => {
      console.error('onRejected function called: ' + error.message)
    }
  )
```

▎Promise.prototype.**catch**

```ts
promise.catch(
  onRejected?: (reason: any) => any
): Promise

// @参数 onRejected
// 当 Promise 对象为 rejected 状态时执行

// 只处理 rejected 的情况，\
// 等同于 Promise.prototype.then(undefined, onRejected)
```

## 静态方法

▎**Promise.resolve** - Creates a new resolved promise for the provided value.

```ts
Promise.resolve(value: any): Promise
```

```js
Promise.resolve('Success').then(
  value => {
    console.log(value) // "Success"
  },
  value => {
    // not called
  }
)
```

▎**Promise.reject** - Creates a new rejected promise for the provided reason.

```ts
Promise.reject(reason: any): Promise
```

```js
Promise.reject(new Error('fail')).then(
  () => {
    // not called
  },
  error => {
    console.error(error) // Stacktrace
  }
)
```

▎**Promise.all** - Wait for all promises to be resolved, or for any to be rejected.

Creates a Promise that is resolved with an array of results when all of the provided Promises resolve, or rejected when any Promise is rejected.

```ts
Promise.all(values: Iterable): Promise
```

```js
var p1 = Promise.resolve(3)
var p2 = 1337
var p3 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('foo')
  }, 2000)
})

Promise.all([p1, p2, p3]).then(values => {
  console.log(values) // [3, 1337, "foo"]
})
```

▎**Promise.race** - Wait until any of the promises is resolved or rejected.

Creates a Promise that is resolved or rejected when any of the provided Promises are resolved or rejected.

```ts
Promise.race(values: Iterable): Promise
```

```js
var p1 = new Promise((resolve, reject) => {
  setTimeout(() => resolve('one'), 500)
})
var p2 = new Promise((resolve, reject) => {
  setTimeout(() => resolve('two'), 100)
})

Promise.race([p1, p2]).then(value => {
  console.log(value) // "two"
  // Both fulfill, but p2 is faster
})
```

```js
var p3 = new Promise((resolve, reject) => {
  setTimeout(() => resolve('three'), 100)
})
var p4 = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error('four')), 500)
})

Promise.race([p3, p4]).then(
  value => {
    console.log(value) // "three"
    // p3 is faster, so it fulfills
  },
  reason => {
    // Not called
  }
)
```

```js
var p5 = new Promise((resolve, reject) => {
  setTimeout(() => resolve('five'), 500)
})
var p6 = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error('six')), 100)
})

Promise.race([p5, p6]).then(
  value => {
    // Not called
  },
  error => {
    console.log(error.message) // "six"
    // p6 is faster, so it rejects
  }
)
```

## 案例

要使函数具有 promise 功能，只需使其返回一个 promise 即可

```js
function myAsyncFunction(url) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest()
    xhr.open('GET', url)
    xhr.onload = () => resolve(xhr.responseText)
    xhr.onerror = () => reject(xhr.statusText)
    xhr.send()
  })
}
```

### 使用 Promise 和 XMLHttpRequest 加载图像

```js
function imgLoad(url) {
  // Create new promise with the Promise() constructor;
  // This has as its argument a function
  // with two parameters, resolve and reject
  return new Promise(function(resolve, reject) {
    // Standard XHR to load an image
    var request = new XMLHttpRequest()
    request.open('GET', url)
    request.responseType = 'blob'
    // When the request loads, check whether it was successful
    request.onload = function() {
      if (request.status === 200) {
        // If successful, resolve the promise by passing back the request response
        resolve(request.response)
      } else {
        // If it fails, reject the promise with a error message
        reject(
          Error(
            "Image didn't load successfully; error code:" + request.statusText
          )
        )
      }
    }
    request.onerror = function() {
      // Also deal with the case when the entire request fails to begin with
      // This is probably a network error, so reject the promise with an appropriate message
      reject(Error('There was a network error.'))
    }
    // Send the request
    request.send()
  })
}
// Get a reference to the body element, and create a new image object
var body = document.querySelector('body')
var myImage = new Image()
// Call the function with the URL we want to load, but then chain the
// promise then() method on to the end of it. This contains two callbacks
imgLoad('myLittleVader.jpg').then(
  function(response) {
    // The first runs when the promise resolves, with the request.response
    // specified within the resolve() method.
    var imageURL = window.URL.createObjectURL(response)
    myImage.src = imageURL
    body.appendChild(myImage)
    // The second runs when the promise
    // is rejected, and logs the Error specified with the reject() method.
  },
  function(Error) {
    console.log(Error)
  }
)
```

## 参考

- [Promise 对象 - ECMAScript 6 入门](http://es6.ruanyifeng.com/#docs/promise)
- [Promise について](http://hakuhin.jp/js/promise.html)
- [Promise - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [Promises](https://www.promisejs.org/)
- [Promise polyfill](https://github.com/stefanpenner/es6-promise)
- [JavaScript Promise迷你书（中文版）](http://liubin.org/promises-book/)