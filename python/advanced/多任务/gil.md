# GIL

GIL（global interpreter lock 全局解释器锁）

```sh
# 实时检测并统计进程的属性和状态
$ top         # 默认按 pid(process ID) 排序
$ top -o cpu  # 按 cpu 排序
$ top -o mem  # 按内存排序
```

GIL 并不是 Python 的特性，而是 Python 解释器 CPython 引入的一个概念，是一个历史遗留问题。

每个线程在执行之前都需要先获取 GIL 锁，从而保证同一时刻只有一个线程可以执行代码，也就是说在多线程中，实际上同一时刻只有一个线程在执行。

GIL 最大的问题就是 Python 的多线程程序并不能利用多核 CPU 的优势。

## 线程释放 GIL 锁的情况

1. 在进行耗时的 IO 操作的时候，可释放 GIL 锁
2. 在 Python 3.2 之前使用的是计数方式，可通过 `sys.setcheckinterval` 来调整计数
3. 从 Python 3.2 开始，GIL 使用计时器，执行时间达到阈值后，当前线程释放 GIL 锁，这样对 CPU 密集型程序更加友好，但依然没有解决 GIL 导致的同一时间只能执行一个线程的问题，所以效率依然不尽如人意

```py
"""
1. sys.getswitchinterval()
返回解释器的线程切换时间间隔, 默认 0.005 秒

2. sys.setswitchinterval(interval)
设置解释器的线程切换时间间隔 (单位秒)
"""
```

Python 的多线程在多核 CPU 上，只对于 IO 密集型计算产生正面效果，而当有至少一个 CPU 密集型（计算密集型）线程存在，那么多线程效率会由于 GIL 而大幅下降。

Python 可使用多进程来充分利用多核 CPU 资源。
