# NumPy

NumPy 是 Python 中科学计算的核心库。它提供了一个高性能的多维数组对象，以及用于处理这些数组的工具。

```sh
$ pip3 install numpy
```

## 1. 数组基础

ndarray 对象是用于存放同类型元素的多维数组。ndarray 中的每个元素在内存中都有相同存储大小的区域。

### 1.1. 创建一个数组

```py
In [1]: import numpy as np

# 1D Array (一维数组)
# 从现有的数据创建数组
# 将类数组对象传递给 numpy 的 array() 函数
In [2]: np.array([0, 1, 2, 3, 4])
Out[2]: array([0, 1, 2, 3, 4])

In [3]: np.array((0, 1, 2, 3, 4))
Out[3]: array([0, 1, 2, 3, 4])

In [4]: np.array(range(5))
Out[4]: array([0, 1, 2, 3, 4])

# numpy 提供了一个类似于 range() 的函数创建数字组成的数组
# numpy.arange([start,] stop[, step,], dtype=None)
In [5]: np.arange(5)
Out[5]: array([0, 1, 2, 3, 4])


# 2D Array (多维数组)
In [6]: np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
Out[6]:
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
```

`.ones()` 和 `.zeros()` 填充方式创建数组

```py
# numpy.zeros(shape, dtype=float, order='C')
# 创建指定形状和数据类型的数组, 数组元素以 0 来填充
# shape: 整型或整型的元祖, 如 (2, 3) 或 2
# dtype: 可选, 默认为 numpy.float64
In [2]: np.zeros((3, 4))
Out[2]:
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])

# numpy.ones(shape, dtype=None, order='C')
# 创建指定形状和数据类型的数组, 数组元素以 1 来填充
# shape: 整型或整型的序列, 如 (2, 3) 或 2
# dtype: 可选, 默认为 numpy.float64
In [3]: np.ones((3, 4))
Out[3]:
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
```

### 1.2. 数组属性

```py
In [2]: a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
In [3]: a
Out[3]:
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])

In [4]: type(a)
Out[4]: numpy.ndarray

# 数组的元素类型
In [5]: a.dtype
Out[5]: dtype('int64')

# 数组的形状 (维度)
In [6]: a.shape
Out[6]: (3, 4)  # 该数组有 3 行和 4 列

# 数组元素的总数, 等于 shape 的元素的乘积
In [7]: a.size
Out[7]: 12

# 数组中每个元素的字节大小
In [8]: a.itemsize
Out[8]: 8  # 该数组的元素为 int64 类型, 占 8 个字节
# 数组的轴 (维度) 的个数
In [9]: a.ndim
Out[9]: 2
# 数组中的所有数据消耗掉的字节数
In [10]: a.nbytes
Out[10]: 96
```

### 1.3. 数据类型

常用的数据类型

|   Numpy 类型    |      C 类型      | 描述                                   |
| :-------------: | :--------------: | -------------------------------------- |
|    `np.int8`    |     `int8_t`     | 字节                                   |
|   `np.int16`    |    `int16_t`     | 整数（2 个字节）                       |
|   `np.int32`    |    `int32_t`     | 整数（4 个字节）                       |
|   `np.int64`    |    `int64_t`     | 整数（8 个字节）                       |
|   `np.uint8`    |    `uint8_t`     | 无符号整数（1 个字节）                 |
|   `np.uint16`   |    `uint16_t`    | 无符号整数（2 个字节）                 |
|   `np.uint32`   |    `uint32_t`    | 无符号整数（4 个字节）                 |
|   `np.uint64`   |    `uint64_t`    | 无符号整数（8 个字节）                 |
|  `np.float16`   |                  | 半精度浮点数                           |
|  `np.float32`   |     `float`      |
|  `np.float64`   |     `double`     | 注意这与内置 Python float 的精度相匹配 |
| `np.complex64`  | `float complex`  | 复数，由两个 32 位浮点数表示           |
| `np.complex128` | `double complex` | 注意这与内置 Python 复合体的精度相匹配 |
|    `np.bool`    |      `bool`      | 存储为字节的布尔值（True 或 False）    |

```py
# 创建指定元素类型的数组
In [2]: a = np.array([1, 0, 1, 0], dtype=np.bool)
In [3]: a
Out[3]: array([ True, False,  True, False])

# 修改数组的数据类型
In [4]: a.astype(np.int8)
Out[4]: array([1, 0, 1, 0], dtype=int8)

# 修改浮点型的小数位数
In [5]: import random
In [6]: b = np.array([random.random() for i in range(4)])
In [7]: b
Out[7]: array([0.98932547, 0.60339655, 0.34273345, 0.12857327])

In [8]: np.round(b, 2)
Out[8]: array([0.99, 0.6 , 0.34, 0.13])
```

## 2. 数组运算

数组上的算术运算符会应用到元素级别。

### 2.1. 数组与标量之间的运算

```py
In [2]: a = np.array([[1, 2, 3], [4, 5, 6]])

In [3]: a + 1
Out[3]:
array([[2, 3, 4],
       [5, 6, 7]])

In [4]: a * 2
Out[4]:
array([[ 2,  4,  6],
       [ 8, 10, 12]])

# 广播 Broadcasting
# 描述了 NumPy 如何在算术运算期间处理具有不同形状的数组
# 受某些约束的影响, 较小的数组在较大的数组上"广播", 以便它们具有兼容的形状

# 当一个数组和一个标量值在一个操作中组合时，会发生最简单的广播
# 标量会和数组中的每一个元素进行计算
```

### 2.2. 数组间的运算

#### 2.2.1. 相同形状数组间的运算

```py
In [2]: a = np.array([[1, 2, 3], [4, 5, 6]])
In [3]: b = np.array([[0, 2, 4], [6, 8, 10]])

In [4]: a + b
Out[4]:
array([[ 1,  4,  7],
       [10, 13, 16]])

In [6]: a * b
Out[6]:
array([[ 0,  4, 12],
       [24, 40, 60]])
```

#### 2.2.2. 不同形状数组间的运算

```py
In [2]: a = np.array([[1, 2, 3], [4, 5, 6]])
In [3]: b = np.array([[1, 2], [3, 4], [5, 6]])

In [4]: a * b
# ValueError: operands could not be broadcast together with shapes (2,3) (3,2)
```

```py
In [5]: c = np.array([0, 2, 4])  # 1 行 3 列
In [6]: a  # 2 行 3 列
Out[6]:
array([[1, 2, 3],
       [4, 5, 6]])

In [7]: a + c
Out[7]:
array([[ 1,  4,  7],
       [ 4,  7, 10]])


In [8]: d = np.array([[1],[3]])  # 2 行 1 列
In [9]: a  # 2 行 3 列
Out[9]:
array([[1, 2, 3],
       [4, 5, 6]])

In [10]: a + d
Out[10]:
array([[2, 3, 4],
       [7, 8, 9]])

# 广播原则:
# 如果两个数组的后缘维度 (即: 从末尾开始算起的维度) 的轴长相符
# 或其中一方的长度为 1, 则认为它们是广播兼容的.
# 广播会在缺失和 (或) 长度为 1 的轴上进行.

# 可以把维度理解为 shape 所对应的数字个数
# 1. shape 为 (3, 3, 2) 的数组和 (3, 2) 的数组
# 由于从末尾开始算起的维度一样, 可以计算
# 2. shape 为 (3, 3, 2) 的数组和 (3, 1) 或 (1, 2) 或 (1, 1) 或 (1,) 的数组
# 由于从末尾开始算起的维度一样或为 1, 可以计算
# 3. shape 为 (3, 3, 3) 的数组和 (3, 2) 的数组
# 由于从末尾开始算起的维度不同, 不能进行计算
```

## 3. 数组操作

### 3.1. 改变数组的形状

```py
In [2]: a = np.array([[3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9]])
In [3]: a
Out[3]:
array([[3, 4, 5, 6, 7, 8],
       [4, 5, 6, 7, 8, 9]])

In [4]: a.shape
Out[4]: (2, 6)

# ndarray.reshape(shape, order='C')
# 在不更改数据的情况下为数组赋予新的形状
# 等效函数 numpy.reshape(a, newshape, order='C')
In [5]: a.reshape(3,4)
Out[5]:
array([[3, 4, 5, 6],
       [7, 8, 4, 5],
       [6, 7, 8, 9]])

In [6]: a.shape
Out[6]: (2, 6)
```

把数组转化为一维数组

```py
In [7]: a.reshape((12,))
Out[7]: array([3, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 9])

# ndarray.flatten(order='C')
# 返回折叠成一维的数组副本 (展开数组)
In [8]: a.flatten()
Out[8]: array([3, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 9])
```

### 3.2. 转置数组

```py
In [2]: a = np.arange(12).reshape((3, 4))
In [3]: a
Out[3]:
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

In [4]: a.transpose()
Out[4]:
array([[ 0,  4,  8],
       [ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11]])
```

```py
# ndarray.swapaxes(axis1, axis2)
# 互换数组的两个轴
# 等效函数 numpy.swapaxes(a, axis1, axis2)
In [5]: a.swapaxes(1, 0)
Out[5]:
array([[ 0,  4,  8],
       [ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11]])

# 轴 Axis
# 在 NumPy 中轴可以理解为方向, 使用从 0 开始的数字表示
# 对于一维数组只有一个 0 轴
# 对于二维数组有 0 轴和 1 轴
# 对于三维数组有 0 轴、1 轴和 2 轴
```

```py
# ndarray.T
# 转置数组, 与 self.transpose() 相同
In [6]: a.T
Out[6]:
array([[ 0,  4,  8],
       [ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11]])
```

### 3.3. 组合数组

```py
In [2]: a = np.arange(12).reshape((2, 6))
In [3]: b = np.arange(12, 24).reshape((2, 6))

# numpy.hstack(tup)
# 水平 (按列) 顺序堆叠数组 (竖直拼接 Vertical)
In [4]: np.vstack((a, b))
Out[4]:
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23]])

# numpy.vstack(tup)
# 垂直 (行) 按顺序堆叠数组 (水平拼接 Horizontal)
In [5]: np.hstack((a, b))
Out[5]:
array([[ 0,  1,  2,  3,  4,  5, 12, 13, 14, 15, 16, 17],
       [ 6,  7,  8,  9, 10, 11, 18, 19, 20, 21, 22, 23]])
```

## 4. 索引和切片

```py
In [2]: a = np.arange(18).reshape((3, 6))
In [3]: a
Out[3]:
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17]])

# 取一行的值
In [4]: a[1]  # 等同于 a[1, :]
Out[4]: array([ 6,  7,  8,  9, 10, 11])

# 取相邻多行的值
In [5]: a[1:3]  # 等同于 a[1:3, :]
Out[5]:
array([[ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17]])

In [6]: a[:]  # 等同于 a[:, :]
Out[6]:
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17]])

# 取不相邻多行的值
In [7]: a[[0, 2]]  # 等同于 a[[0, 2], :]
Out[7]:
array([[ 0,  1,  2,  3,  4,  5],
       [12, 13, 14, 15, 16, 17]])
```

```py
# 取一列的值
In [8]: a[:, 2]
Out[8]: array([ 2,  8, 14])

# 取相邻多列的值
In [9]: a[:, 2:5]
Out[9]:
array([[ 2,  3,  4],
       [ 8,  9, 10],
       [14, 15, 16]])

# 取不相邻多列的值
In [10]: a[:, [0, 2, 4]]
Out[10]:
array([[ 0,  2,  4],
       [ 6,  8, 10],
       [12, 14, 16]])
```

```py
# 取指定行和列的值
In [11]: a[2, 4]
Out[11]: 16
In [12]: type(a[2, 4])
Out[12]: numpy.int64

# 取相邻多行多列的值
In [13]: a[0:2, 2:4]
Out[13]:
array([[2, 3],
       [8, 9]])

# 注意:
In [14]: a[[0, 2], [3, 4]]  # 取多个不相邻行和列的值
Out[14]: array([ 3, 16])  # 对应 (0, 3) (2, 4) 的点
In [15]: a[[0, 0, 2], [3, 4, 4]]
Out[15]: array([ 3,  4, 16])  # 对应 (0, 3) (0, 4) (2, 4) 的点
```

### 4.1. 数组赋值

```py
In [2]: a = np.arange(24).reshape((4, 6))
In [3]: a
Out[3]:
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23]])

In [4]: a[:, 2:4]
Out[4]:
array([[ 2,  3],
       [ 8,  9],
       [14, 15],
       [20, 21]])

In [5]: a[:, 2:4] = 0
In [6]: a
Out[6]:
array([[ 0,  1,  0,  0,  4,  5],
       [ 6,  7,  0,  0, 10, 11],
       [12, 13,  0,  0, 16, 17],
       [18, 19,  0,  0, 22, 23]])
```

### 4.2. 数组的行列交换

```py
In [2]: a = np.arange(12).reshape((3, 4))
In [3]: a
Out[3]:
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

# 行交换
In [4]: a[[1, 2], :] = a[[2, 1], :]
In [5]: a
Out[5]:
array([[ 0,  1,  2,  3],
       [ 8,  9, 10, 11],
       [ 4,  5,  6,  7]])

# 列交换
In [6]: a[:, [0, 2]] = a[:, [2, 0]]
In [7]: a
Out[7]:
array([[ 2,  1,  0,  3],
       [10,  9,  8, 11],
       [ 6,  5,  4,  7]])
```

### 4.3. 布尔索引

```py
In [2]: a = np.arange(24).reshape((4, 6))
In [3]: a < 10
Out[3]:
array([[ True,  True,  True,  True,  True,  True],
       [ True,  True,  True,  True, False, False],
       [False, False, False, False, False, False],
       [False, False, False, False, False, False]])

# 要求: 把小于 10 的数替换为 0
In [4]: a[a < 10] = 0
In [5]: a
Out[5]:
array([[ 0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23]])
```

### 4.4. 三元运算符

```py
In [2]: a = np.arange(24).reshape((4, 6))

# 要求: 把小于 10 的数替换为 0, 大于 10 的数替换为 10
# numpy.where(condition[, x, y])
In [3]: np.where(a < 10, 0, 10)
Out[3]:
array([[ 0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0, 10, 10],
       [10, 10, 10, 10, 10, 10],
       [10, 10, 10, 10, 10, 10]])
```

### 4.5. 裁剪

```py
In [2]: a = np.arange(24).reshape((4, 6))

# 要求: 把小于 10 的数替换为 10, 大于 18 的数替换为 18
In [3]: a.clip(10, 18)
Out[3]:
array([[10, 10, 10, 10, 10, 10],
       [10, 10, 10, 10, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 18, 18, 18, 18, 18]])
```

## 5. nan 和 inf

```py
# nan: not a num, 表示不是一个数字
# inf: infinity, inf 表示正无穷, -inf 表示负无穷

In [2]: a = np.nan
In [3]: type(a)
Out[3]: float

In [4]: a = np.inf
In [5]: type(a)
Out[5]: float
```

```py
# nan 的注意点:
# 两个 nan 是不相等的, 利用该特性可判断数组中 nan 的个数
# 通过 np.isnan() 来判断一个数字是否为 nan
# nan 和任何值计算都为 nan

In [6]: np.nan == np.nan
Out[6]: False
In [7]: np.nan != np.nan
Out[7]: True

In [8]: a = np.array([1.,2., np.nan])
In [9]: a
Out[9]: array([ 1.,  2., nan])

In [10]: np.count_nonzero(a!=a)
Out[10]: 1

In [11]: a[np.isnan(a)] = 0
In [12]: a
Out[12]: array([1., 2., 0.])
```

## 6. 其他函数

### 6.1. 常用统计函数

```py
# a.sum(axis=None)        求和
# a.mean(axis=None)       均值
# np.median(a, axis=None) 中值
# a.max(axis=None)        最大值
# a.min(axis=None)        最小值
# np.ptp(a, axis=None)    极值, 即最大值和最小值之差
# a.std(axis=None)        标准差
# 标准差是一组数据平均值分散程度的度量
# 一个较大的标准差, 代表大部分数值和其平均值之间差异较大
# 反映出数据的波动稳定情况, 越大表示波动越大, 越不稳定

# 默认返回多维数组的全部的统计结果
# 如果指定 axis 则返回当前轴上的结果

In [2]: a = np.arange(24).reshape((4, 6))
In [3]: a
Out[3]:
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23]])

In [4]: a.sum()
Out[4]: 276
In [5]: a.sum(axis=0)
Out[5]: array([36, 40, 44, 48, 52, 56])

In [6]: a.mean(axis=0)
Out[6]: array([ 9., 10., 11., 12., 13., 14.])

In [7]: np.median(a, axis=0)
Out[7]: array([ 9., 10., 11., 12., 13., 14.])

In [8]: np.ptp(a, axis=0)
Out[8]: array([18, 18, 18, 18, 18, 18])

In [9]: a.std(axis=0)
Out[9]:
array([6.70820393, 6.70820393, 6.70820393, 6.70820393, 6.70820393,
       6.70820393])
```

### 6.2. 获取最大值与最小值的位置

```py
In [2]: a = np.array([[23, 43, 22, 54],[33, 23, 12, 43], [32, 45, 19, 32]])
In [3]: a
Out[3]:
array([[23, 43, 22, 54],
       [33, 23, 12, 43],
       [32, 45, 19, 32]])

In [4]: np.argmax(a, axis=0)
Out[4]: array([1, 2, 0, 0])

In [5]: np.argmin(a, axis=1)
Out[5]: array([2, 2, 2])
```

### 6.3. 生成随机数

```py
# 均匀分布: 在相同的大小范围内出现概率是等可能的
# 正态分布: 两头低, 中间高, 左右对称

# randint(low, high=None, size=None, dtype='l')
# 从给定上下限范围选取随机整数
In [2]: np.random.randint(10, 20, (4, 5))
Out[2]:
array([[14, 11, 11, 12, 16],
       [16, 17, 19, 17, 19],
       [13, 14, 19, 11, 19],
       [12, 10, 16, 18, 10]])

# uniform(low=0.0, high=1.0, size=None)
In [3]: np.random.uniform(10.0, 20.0, (4, 5))
Out[3]:
array([[13.60704378, 18.43866637, 16.61086231, 18.30592073, 19.78982919],
       [15.11705496, 18.6006465 , 16.96606247, 10.51237268, 14.72752745],
       [14.76394781, 18.35361479, 11.68502295, 16.22043458, 16.21609135],
       [15.9000023 , 18.36715859, 12.6160217 , 14.04518069, 10.54534131]])

# numpy.random.randn(d0, d1, ..., dn)
# 从标准正态分布中返回一个或多个样本值
# d0, d1, ..., dn 表示数组的维度
In [4]: np.random.randn(3, 4)
Out[4]:
array([[-1.46334641, -0.48617305,  1.20677918,  0.90723804],
       [ 0.13122095,  0.48174309, -1.2758391 , -0.58008203],
       [-0.2912542 , -0.25295982, -0.6291548 ,  0.65200138]])
```
