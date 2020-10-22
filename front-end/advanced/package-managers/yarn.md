# Yarn

> 官网 https://yarnpkg.com/en/

## 1. 安装

```sh
# 通过 Homebrew 安装 Yarn
$ brew install yarn

# 检测 Yarn 是否安装成功
$ yarn --version

# 升级
$ brew upgrade yarn
```

## 2. 使用方法

初始化一个新项目

```sh
$ yarn init
```

添加依赖包

```sh
$ yarn add [package]
$ yarn add [package]@[version]
$ yarn add [package]@[tag]
```

将依赖项添加到不同依赖项类别中

```sh
$ yarn add [package] --dev
$ yarn add [package] --peer
$ yarn add [package] --optional
```

升级依赖包

```sh
$ yarn upgrade [package]
$ yarn upgrade [package]@[version]
$ yarn upgrade [package]@[tag]
```

移除依赖包

```sh
$ yarn remove [package]
```

安装项目的全部依赖

```sh
$ yarn
# 或者
$ yarn install
```

## 3. 换源

```sh
# 查看 yarn 当前的 registry 地址
$ yarn config get registry
https://registry.yarnpkg.com

# 永久更换
$ yarn config set https://registry.npm.taobao.org/
```

## 4. CLI 命令

▎**yarn add** - 安装一个包（以及任何它依赖的包）

```sh
$ yarn add package-name # 安装 "latest" 版本
$ yarn add package-name@1.2.3
$ yarn add package-name@tag

$ yarn global add <package...>
# 会安装一个或多个包至 dependencies
# = npm install [package] --save
$ yarn add <package...>  --dev
# 使用 --dev 或 -D 会安装一个或多个包至 devDependencies
# = npm install [package] --save-dev
```

> 大多数人仅仅只使用 `dependencies` 和 `devDependencies` 类型的依赖

▎**yarn bin** - 显示 yarn 的 bin 目录的位置

▎**yarn cache**

```sh
# Yarn 将每个包存储在你的文件系统-用户目录-全局缓存中
$ yarn cache list [--pattern]
# 列出已缓存的每个包
$ yarn cache list --pattern <pattern>

$ yarn cache list --pattern gulp
$ yarn cache list --pattern "gulp|grunt"
$ yarn cache list --pattern "gulp-(match|newer)"

$ yarn cache dir
# 打印出当前的 yarn 全局缓存的位置

$ yarn cache clean [<module_name...>]
# 清除全局缓存
```

▎**yarn global** - 在你的操作系统上全局安装包

```sh
$ yarn global <add/bin/list/remove/upgrade>
```

▎**yarn help** - 显示帮助信息

▎**yarn info** - 显示一个包的信息

```sh
$ yarn info <package> [<field>]

$ yarn info react
$ yarn info react --json

# 选择特定字段
$ yarn info react description
```

▎**yarn init** - 交互式创建或更新 `package.json` 文件

```sh
# 生成一个使用默认值的 package.json
$ yarn init --yes
$ yarn init -y
```

▎**yarn list** - 列出已安装的包

```sh
$ yarn list
# 列出当前工作文件夹所有的依赖

$ yarn list [--depth] [--pattern]
# 层级是从 0 起算的
$ yarn list --depth=0
$ yarn list --pattern gulp
$ yarn list --pattern "gulp|grunt"
$ yarn list --pattern "gulp|grunt" --depth=1
```

▎**yarn remove**

```sh
$ yarn remove <package...>

$ yarn remove foo
# 会从 dependencies 里移除名为 foo 的包
# 同时会更新 package.json 和 yarn.lock 文件

$ yarn remove [package] [--flag]
# 使用与 yarn install 命令相同的 flag
```

▎**yarn run** - 运行一个定义好的包脚本

```js
// package.json
{
  "name": "my-package",
  "scripts": {
    "build": "babel src -d lib",
    "test": "jest"
  }
}
```

```sh
$ yarn run [script] [<args>]

$ yarn run test
# 执行 package.json 中名为 "test" 的脚本
$ yarn run test -o --watch
# 可以在脚本名称后放置要传递给脚本的额外参数
# 会执行 jest -o --watch
```

▎**yarn self-update** - 更新 Yarn 到最新版
