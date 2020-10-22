# Navigator

Navigator 提供了与浏览器有关的信息。

## API 文档

---

<p align="center">Navigator</p>

---

### NavigatorOnLine

▎NavigatorOnLine.**onLine** - _readonly_ - 浏览器是否连网

```js
if (navigator.onLine) {
  alert('online')
} else {
  alert('offline')
}
```

监听浏览器的联网状态

```js
// 使用 window.ononline 和 window.onoffline 事件
window.addEventListener('offline', function(e) {
  alert('offline')
})
window.addEventListener('online', function(e) {
  alert('online')
})
```

### NavigatorID

▎NavigatorID.**appCodeName** - _readonly_ - 返回 `"Mozilla"`

▎NavigatorID.**appName** - _readonly_ - 返回 `"Netscape"`

▎NavigatorID.**appVersion** - _readonly_ - 返回浏览器的版本

```js
navigator.appVersion
// "5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
```

▎NavigatorID.**platform** - _readonly_ - 浏览器所在的系统平台

```js
navigator.platform // "MacIntel"
```

▎NavigatorID.**product** - _readonly_ - 返回 `"Gecko"`

▎NavigatorID.**productSub** - _readonly_ - 返回 `"20030107"` 或 `"20100101"`

▎NavigatorID.**userAgent** - _readonly_ - 浏览器的用户代理字符串

```js
navigator.userAgent
// "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
```

▎NavigatorID.**vendor** - _readonly_ - 返回 `""` 或 `"Apple Computer, Inc."` 或 `"Google Inc."`

▎NavigatorID.**vendorSub** - _readonly_ - 返回 `""`

### NavigatorLanguage

▎NavigatorLanguage.**language** - _readonly_ - 浏览器的主语言

▎NavigatorLanguage.**languages** - _readonly_

### NavigatorCookies

▎NavigatorCookies.**cookieEnabled** - _readonly_ - cookie 是否启用

### 访问设备地理位置

▎Navigator.**geolocation** - _readonly_ - Geolocation - 允许访问设备位置

## 参考

- [Navigator - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator)