# DNS

DNS（Domain Name System 域名解析系统），主要用来将域名转化为对应的 IP 地址。

DNS 是一台运行在互联网上的服务器。

```
     你的电脑
访问 www.baidu.com
                     ↘↖
        ↓↑                 百度服务器
                      IP 为 183.232.231.172
   DNS 域名解析系统
将域名转换成对应 IP 地址
www.baidu.com 183.232.231.172
```

## 本地 DNS

hosts 是本地的 DNS。DNS 中就是 IP 地址和域名的对应关系表。

hosts 文件是隐藏文件、系统文件、没有扩展名的文件。

hosts 文件路径

- Windows - `C:\Windows\System32\drivers\etc\hosts`
- Linux - `/etc/hosts`，注意 Linux 下修改 hosts 后需要重启网络，命令为 `/etc/init.d/networking restart`
