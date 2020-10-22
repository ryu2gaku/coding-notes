# DevServer

## webpack-dev-server

> [webpack-dev-server 仓库](https://github.com/webpack/webpack-dev-server) - Serves a webpack app. Updates the browser on changes.

### 安装

The `webpack-dev-server` provides you with a simple web server and the ability to use live reloading.

```sh
$ npm install webpack-dev-server --save-dev
```

`webpack-dev-server` doesn't write any output files after compiling. Instead, it keeps bundle files in memory and serves them as if they were real files mounted at the server's root path.

### 用法

❐ 使用 CLI

```sh
$ node_modules/.bin/webpack-dev-server
# or
$ npx webpack-dev-server
```

❐ 使用 npm 脚本

```js
// package.json
"scripts": {
  "start:dev": "webpack-dev-server"
}
```

并在终端中运行以下命令

```sh
$ npm run start:dev
```

## 开发环境配置

```js
var path = require('path')

module.exports = {
  //...
  devServer: {
    contentBase: path.join(__dirname, 'dist'),
    compress: true,
    port: 9000,
  },
}
```

当服务器启动时，在解析模块列表之前会有一条消息：

```
http://localhost:9000/
webpack output is served from /build/
Content not from webpack is served from /path/to/dist/
```

### devServer 配置选项

```js
module.exports = {
  // ...
  devServer: {
    // Tell the server where to serve content from.
    // 默认情况下，使用当前工作目录作为提供内容的目录
    // To disable contentBase set it to false.
    //
    // CLI 用法: webpack-dev-server --content-base /path/to/content/dir
    contentBase: path.join(__dirname, 'public'),
    // 从多个目录提供内容
    contentBase: [
      path.join(__dirname, 'public'),
      path.join(__dirname, 'assets'),
    ],

    // Enable gzip compression(压缩) for everything served.
    //
    // CLI 用法: webpack-dev-server --compress
    compress: true,

    // 指定要监听请求的端口号
    //
    // CLI 用法: webpack-dev-server --port 8080
    port: 8080,

    // 告诉 dev-server 在服务器启动后打开浏览器
    //
    // CLI 用法: webpack-dev-server --open
    open: true,

    // 指定使用一个 host
    // 如果希望服务器可从外部访问，指定为 '0.0.0.0'
    //
    // CLI 用法: webpack-dev-server --host 0.0.0.0
    //
    // default: 'localhost'
    host: '0.0.0.0',

    // 被作为索引文件的文件名
    index: 'index.html',

    // 启用 webpack 的热模块替换（Hot Module Replacement）功能
    //
    // 必须有 webpack.HotModuleReplacementPlugin 才能完全启用 HMR。
    // 如果使用 --hot 选项启动 webpack 或 webpack-dev-server，则该插件会被自动添加，
    // 因此可能不需要将其添加到 webpack.config.js 中。
    hot: true,

    // dev-server 仅在获得请求时才编译 bundle
    // 这意味着 webpack 不会监听任何文件变动。
    //
    // CLI 用法: webpack-dev-server --lazy
    lazy: true,
  },
}
```

## 参考

- [DevServer | webpack](https://webpack.js.org/configuration/dev-server/)
