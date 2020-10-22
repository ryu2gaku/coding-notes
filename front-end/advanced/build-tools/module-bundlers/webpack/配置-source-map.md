# 配置 source map

```js
module.exports =  {
  mode: 'production',
  // 会产生 .map 文件
  devtool: 'source-map',
  // ...
})
```

简单说，source map 就是一个信息文件，里面储存着位置信息。也就是说，转换后的代码的每一个位置，所对应的转换前的位置。

有了它，出错的时候，除错工具将直接显示原始代码，而不是转换后的代码。这无疑给开发者带来了很大方便。

## 参考

- [Devtool | webpack](https://webpack.js.org/configuration/devtool/)
- [JavaScript Source Map 详解 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2013/01/javascript_source_map.html)
