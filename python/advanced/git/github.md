# GitHub 使用

## 1. 创建仓库

❶ 注册 GitHub 账户，登录后点击 <kbd>New respository</kbd>。

❷ 在新页面中输入项目的名称，勾选 <kbd>Initialize this repository with a README</kbd>，点击 <kbd>Create respository</kbd>。

❸ 添加成功后，转到文件列表页面。

## 2. 添加 SSH 账户

❶ 点击账户头像后的下拉三角，选择 <kbd>Settings</kbd>。

如果某台机器需要与 GitHub 上的仓库交互，那么就要把这台机器的 SSH 公钥添加到这个 GitHub 账户上。

点击左侧 <kbd>SSH and GPG keys</kbd>，之后点击 <kbd>New SSH Key</kbd> 添加 SSH 公钥。

❷ 在 Ubuntu 的命令行中，回到用户的主目录下，编辑文件 `.gitconfig` 修改某台机器的 Git 配置。

```sh
$ vi .gitconfig
```

❸ 修改为注册 GitHub 时的邮箱，填写用户名。

❹ 使用如下命令生成 SSH 公钥。

```sh
# ssh-keygen -t rsa -C '邮箱地址'
# -t：指定要创建的密钥类型
# -C：添加注释
$ ssh-keygen -t rsa -C '251131698@qq.com'
```

❺ 进入主目录下的 `.ssh` 文件夹，查看公钥内容并复制此内容。

```sh
$ cd .ssh/
$ ls
id_rsa		id_rsa.pub
# 公钥为 id_rsa.pub
# 私钥为 id_rsa

$ cat id_rsa.pub
```

❻ 回到浏览器中，填写标题粘贴公钥，点击 <kbd>Add SSH Key</kbd>。

## 3. 克隆项目

❶ 在浏览器中点击进入 GitHub 首页，在进入项目仓库的页面。

❷ 复制 Git 地址

```sh
# Clone with HTTPS
https://github.com/ryu2gaku/git-test.git

# Clone with SSH
git@github.com:ryu2gaku/git-test.git
```

❸ 在命令行中复制仓库中的内容

```sh
# git clone [url]
# 下载一个项目和它的整个代码历史

$ git clone git@github.com:ryu2gaku/git-test.git
Cloning into 'git-test'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
```

## 4. 上传分支

❶ 项目克隆到本地之后，执行如下命令创建新分支 smart。

```sh
$ cd git-test/

$ git checkout -b smart
Switched to a new branch 'smart'

$ git branch
  master
* smart
```

❷ 创建一个 code.txt 并提交一个版本。

```sh
$ touch code.txt

$ vi code.txt

$ git add code.txt

$ git commit -m '版本1'
[smart 2114cbe] 版本1
 1 file changed, 1 insertion(+)
 create mode 100644 code.txt
```

❸ 推送分支，就是把该分支上的所有本地提交推送到远程库，推送时要指定本地分支，这样 git 就会把该分支推送到远程库对应的远程分支上。

```sh
# git push [remote] [branch]
# 上传本地指定分支到远程仓库

$ git push origin smart  # git push origin 分支名称
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 287 bytes | 287.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote:
remote: Create a pull request for 'smart' on GitHub by visiting:
remote:      https://github.com/ryu2gaku/git-test/pull/new/smart
remote:
To github.com:ryu2gaku/git-test.git
 * [new branch]      smart -> smart
```

❹ 再去 GitHub 网站上查看分支页面。

## 5. 将本地分跟踪服务器分支

```sh
# git branch --set-upstream-to=origin/远程分支名称 本地分支名称

$ git branch --set-upstream-to=origin/smart smart
Branch 'smart' set up to track remote branch 'smart' from 'origin'.
# 分支 smart 设置为跟踪来自 origin 的远程分支 smart

$ git status
On branch smart  # 位于分支 smart
Your branch is up to date with 'origin/smart'.
# 您的分支与上游分支 'origin/smart' 一致

nothing to commit, working tree clean
# 无文件要提交，干净的工作区
```

```sh
$ vi code.txt

$ git add code.txt

$ git commit -m ' 版本2'
[smart 7e1e4b8]  版本2
 1 file changed, 1 insertion(+)

$ git status
On branch smart  # 位于分支 smart
Your branch is ahead of 'origin/smart' by 1 commit.
# 您的分支领先 origin/smart 共 1 个提交
  (use "git push" to publish your local commits)
  # 使用 git push 来发布您的本地提交

nothing to commit, working tree clean
# 无文件要提交, 干净的工作区
```

```sh
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 298 bytes | 298.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To github.com:ryu2gaku/git-test.git
   2114cbe..7e1e4b8  smart -> smart

$ git status
On branch smart
Your branch is up to date with 'origin/smart'.

nothing to commit, working tree clean
```

## 6. 从远程分支上拉取代码

```sh
# git pull [remote] [branch]
# 取回远程仓库的变化, 并与本地分支合并

$ git pull origin smart  # git pull origin 分支名称
From github.com:ryu2gaku/git-test
 * branch            smart      -> FETCH_HEAD
Already up to date.
```

## 7. 工作中使用 Git

项目经理

❶ 项目经理搭建项目的框架。

❷ 搭建完项目框架之后，项目经理把项目框架代码放到服务器。

普通员工

❶ 在自己的电脑上生成 SSH 公钥，然后把公钥给项目经理，项目经理把它添加到服务器上面。

❷ 项目经理会给每个组员项目代码的地址，组员把代码下载到自己的电脑上。

❸ 创建本地的分支 dev，在 dev 分支中进行每天的开发。

❹ 每一个员工开发完自己的代码之后，都需要将代码发布到远程的 dev 分支上。

```sh
master # 保存发布的项目代码, v1.0 v2.0 ...
dev    # 保存开发过程中的代码
```
