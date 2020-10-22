# Location

Location 提供了与当前窗口中加载的文档有关的信息，还提供了一些导航功能。

`location` 对象是很特别的一个对象，因为它即是 `window` 对象的属性，也是 `document` 对象的属性。`document.location` 和 `window.location` 引用的是同一个对象。

## API 文档

---

<p align="center">Location</p>

---

### URL 解析

▎Location.**hash** - URL 的片段（fragment）部分，以 `#` 开头

▎Location.**host** - 服务器名称和端口号（如果有）

▎Location.**hostname** - 不带端口号的服务器名称

▎Location.**href** - 当前加载页面的完整的 URL

▎Location.**pathname** - URL 的路径名，以 `/` 开头

▎Location.**port** - URL 的端口号

▎Location.**protocol** - URL 的协议

▎Location.**search** - URL 的查询部分，以 `?` 开头

### 位置操作

▎Location.**assign** - 导航到给定 URL，并在浏览器的历史记录中生成一条记录

```ts
location.assign(url: USVString): void
```

```js
document.location.assign('http://www.wrox.com')
```

如果将 `location.href` 或 `window.location` 设置为一个 URL 值，也会以该值调用 `assign()` 方法。

```js
// 导航到一个新页面的三种方式
window.location.assign('http://www.wrox.com')
window.location = 'http://www.wrox.com'
window.location.href = 'http://www.wrox.com'
```

上面的方法中，最常用的是设置 `location.href` 属性。另外，修改 `location` 对象的其他属性也可以改变当前加载的页面。

```js
// 假设初始 URL 为 http://www.wrox.com/WileyCDA/

// 将 URL 修改为 http://www.wrox.com/WileyCDA/#section1
location.hash = '#section1'

// 将 URL 修改为 http://www.wrox.com/WileyCDA/?q=javascript
location.search = '?q=javascript'

// 将 URL 修改为 http://www.yahoo.com/WileyCDA/
location.hostname = 'www.yahoo.com'

// 将 URL 修改为 http://www.wrox.com/mydir
location.pathname = 'mydir'

// 将 URL 修改为 http://www.wrox.com:8080/WileyCDA/
location.port = 8080
```

每次修改 `location` 的属性（`hash` 除外）页面都会以新 URL 重新加载。

▎Location.**replace** - 从会话历史中移除当前页面，并导航到给定 URL

```ts
location.replace(url: USVString): void
```

▎Location.**reload** - 重新加载当前页面

```ts
location.reload(): void
```
## 参考

- [Location - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Location)