# 转译 ES6 语法

## babel-loader

> [babel-loader 仓库](https://github.com/babel/babel-loader) - Babel loader for webpack

### 安装

加载 ES2015+ 代码，然后使用 Babel 转译为 ES5。

```sh
$ npm install -D babel-loader @babel/core @babel/preset-env webpack
```

### 简单用法

```js
module: {
  rules: [
    {
      test: /\.m?js$/,
      exclude: /(node_modules|bower_components)/,
      use: {
        loader: 'babel-loader',
        options: { presets: ['@babel/preset-env'] },
      },
    },
  ]
}
```

## 参考

- [Babel · The compiler for next generation JavaScript](https://babeljs.io/)
- [Babel 中文网 · Babel - 下一代 JavaScript 语法的编译器](https://www.babeljs.cn/)
