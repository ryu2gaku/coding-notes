# Pandas

```sh
$ pip3 install pandas
```

## 1. 生成对象

```py
# Pandas 的主要数据结构是 Series 与 DataFrame
# ============
# Series    带标签的一维数组
# DataFrame 由多种类型的列构成的二维标签数据结构
#           类似于 Excel、SQL 表或 Series 对象构成的字典
In [1]: import numpy as np
In [2]: import pandas as pd
```

### 1.1. 生成 Series

```py
# Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
# Series 的轴标签统称为`索引`, index 是轴标签列表
# ============
# data 是多维数组时, index 长度必须与 data 长度一致
# 没有指定 index 参数时, 创建数值型索引, 即 [0, ..., len(data) - 1]

# 通过值列表生成 Series
# Pandas 默认自动生成整数索引
In [3]: pd.Series([1, 3, 5, np.nan, 6, 8])
Out[3]:
0    1.0
1    3.0
2    5.0
3    NaN  # Not a Number, 表示缺失数据
4    6.0
5    8.0
dtype: float64

# 提供索引参数
In [4]: pd.Series(np.array([1, 2, 3, 4, 5]), index=list('abcde'))
Out[4]:
a    1
b    2
c    3
d    4
e    5
dtype: int64

# 通过字典生成 Series
In [5]: pd.Series({'b': 1, 'a': 0, 'c': 2})
Out[5]:
b    1
a    0
c    2
dtype: int64

# data 是标量值 (scalar value) 时, 必须提供索引
In [6]: pd.Series(3, index=['a', 'b', 'c'])
Out[6]:
a    3
b    3
c    3
dtype: int64
```

### 1.2. 生成 DataFrame

```py
# DataFrame 分为 index 和 columns
# index 和 columns 比 axis 0 和 axis 1 更直观
# ============
# DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)

# 通过 numpy ndarray 生成 DataFrame
In [3]: pd.DataFrame(np.arange(12).reshape(3, 4))
Out[3]:
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

# 提供行列参数
In [4]: pd.DataFrame(np.arange(12).reshape(3, 4),
                     index=list('abc'),
                     columns=list('ABCD'))
Out[4]:
   A  B   C   D
a  0  1   2   3
b  4  5   6   7
c  8  9  10  11

# 通过字典生成 DataFrame
In [5]: d = {'one': [1., 2., 3., 4.],
             'two': [5., 6., 7., 8.]}
In [6]: pd.DataFrame(d)
Out[6]:
   one  two
0  1.0  5.0
1  2.0  6.0
2  3.0  7.0
3  4.0  8.0

In [7]: d = [{'one': 1., 'two': 2.},
             {'one': 3., 'two': 4.},
             {'one': 5., 'two': 6.}]
In [8]: pd.DataFrame(d)
Out[8]:
   one  two
0  1.0  2.0
1  3.0  4.0
2  5.0  6.0
```

NumPy 的数组只有一种数据类型，而 DataFrame 的列可以有不同数据类型。

```py
In [3]: d = {'A': 1.,
             'B': pd.Timestamp('20130102'),
             'C': pd.Series(1, index=list(range(4)), dtype='float32'),
             'D': np.array([3] * 4, dtype='int32'),
             'E': pd.Categorical(["test", "train", "test", "train"]),
             'F': 'foo'}
In [4]: df = pd.DataFrame(d)
In [5]: df
Out[5]:
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo

In [6]: df.dtypes
Out[6]:
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
```

## 2. 查看数据

### 2.1. Series 查看数据

```py
In [3]: s = pd.Series([1, 3, 5, np.nan, 6, 8])

In [4]: type(s)
Out[4]: pandas.core.series.Series

In [5]: s.index
Out[5]: RangeIndex(start=0, stop=6, step=1)

# Pandas 推荐使用 .array 或 .to_numpy() 替代
In [6]: s.values
Out[6]: array([ 1.,  3.,  5., nan,  6.,  8.])

In [7]: s.dtype
Out[7]: dtype('float64')

In [8]: s.shape
Out[8]: (6,)

In [9]: s.size
Out[9]: 6
```

`head()` 与 `tail()` 用于快速预览 Series 与 DataFrame。

```py
In [3]: long_series = pd.Series(np.random.randn(1000))

# head(n: int = 5)
In [4]: long_series.head(3)
Out[4]:
0   -0.168213
1   -1.586595
2    0.647403
dtype: float64

# tail(n: int = 5)
In [5]: long_series.tail(3)
Out[5]:
997   -1.735564
998    0.106645
999    1.383611
dtype: float64
```

### 2.2. DataFrame 查看数据

```py
In [3]: d = {'col1': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
             'col2': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
             'col3': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])}
In [4]: df = pd.DataFrame(d)
In [5]: df
Out[5]:
       col1      col2      col3
a  0.156182  0.965086       NaN
b  1.416048  0.465485  1.344782
c  0.363120  0.652070 -1.499807
d       NaN -1.813154  0.597196

In [6]: type(df)
Out[6]: pandas.core.frame.DataFrame

In [7]: df.index
Out[7]: Index(['a', 'b', 'c', 'd'], dtype='object')

In [8]: df.columns
Out[8]: Index(['col1', 'col2', 'col3'], dtype='object')

# Pandas 推荐使用 .to_numpy() 替代
In [9]: df.values
Out[9]:
array([[ 0.15618163,  0.96508633,         nan],
       [ 1.41604785,  0.46548501,  1.3447821 ],
       [ 0.36311985,  0.65206998, -1.49980662],
       [        nan, -1.81315352,  0.59719639]])

In [10]: df.dtypes
Out[10]:
col1    float64
col2    float64
col3    float64
dtype: object

In [11]: df.shape
Out[11]: (4, 3)

In [12]: df.size
Out[12]: 12

# 转置数据
In [13]: df.T
Out[13]:
             a         b         c         d
col1  0.156182  1.416048  0.363120       NaN
col2  0.965086  0.465485  0.652070 -1.813154
col3       NaN  1.344782 -1.499807  0.597196
```

```py
# head(n: int = 5)
In [14]: df.head(2)
Out[14]:
       col1      col2      col3
a  0.156182  0.965086       NaN
b  1.416048  0.465485  1.344782

# tail(n: int = 5)
In [15]: df.tail(2)
Out[15]:
      col1      col2      col3
c  0.36312  0.652070 -1.499807
d      NaN -1.813154  0.597196
```

快速查看数据的统计摘要

```py
In [16]: df.describe()
Out[16]:
           col1      col2      col3
count  3.000000  4.000000  3.000000  # 计数
mean   0.645116  0.067372  0.147391  # 均值
std    0.675616  1.270516  1.474675  # 标准差
min    0.156182 -1.813154 -1.499807  # 最小值
25%    0.259651 -0.104175 -0.451305
50%    0.363120  0.558777  0.597196
75%    0.889584  0.730324  0.970989
max    1.416048  0.965086  1.344782  # 最大值
```

按轴排序

```py
In [17]: df.sort_index(axis=1, ascending=False)
Out[17]:
       col3      col2      col1
a       NaN  0.965086  0.156182
b  1.344782  0.465485  1.416048
c -1.499807  0.652070  0.363120
d  0.597196 -1.813154       NaN
```

按值排序

```py
In [18]: df.sort_values(by='col2')
Out[18]:
       col1      col2      col3
d       NaN -1.813154  0.597196
b  1.416048  0.465485  1.344782
c  0.363120  0.652070 -1.499807
a  0.156182  0.965086       NaN
```

## 3. 选择数据

### 3.1. Series 选择数据

```py
In [3]: import string
# string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

In [4]: s = pd.Series({string.ascii_uppercase[i]: i for i in range(6)})
In [5]: s
Out[5]:
A    0
B    1
C    2
D    3
E    4
F    5
dtype: int64

# 获取标量值 (scalar value)
In [6]: s['C']  # 通过索引
Out[6]: 2

In [7]: s[2]  # 通过位置
Out[7]: 2

# 切片
In [8]: s['B': 'D']  # 通过索引, 包含右边界
Out[8]:
B    1
C    2
D    3
dtype: int64

In [9]: s[1: 3]  # 通过位置, 不包含右边界
Out[9]:
B    1
C    2
dtype: int64

In [10]: s[['B', 'D']]
Out[10]:
B    1
D    3
dtype: int64

In [11]: s[[1, 3, 5]]
Out[11]:
B    1
D    3
F    5
dtype: int64
```

布尔索引

```py
In [12]: s[s < 3]
Out[12]:
A    0
B    1
C    2
dtype: int64
```

### 3.2. DataFrame 选择数据

```py
In [3]: df = pd.DataFrame(np.arange(24).reshape(6, 4),
                          index=list('abcdef'),
                          columns=list('ABCD'))
In [4]: df
Out[4]:
    A   B   C   D
a   0   1   2   3
b   4   5   6   7
c   8   9  10  11
d  12  13  14  15
e  16  17  18  19
f  20  21  22  23

# 获取单列数据
In [5]: df['C']
Out[5]: # pandas.core.series.Series
a     2
b     6
c    10
d    14
e    18
f    22
Name: C, dtype: int64

# 用 [] 切片行
In [6]: df[2:4]
Out[6]: # pandas.core.frame.DataFrame
    A   B   C   D
c   8   9  10  11
d  12  13  14  15

# 组合写法
In [7]: df[2:5]['D']  # 取第 3~5 行 D 列的数据
Out[7]:
c    11
d    15
e    19
Name: D, dtype: int64
```

```py
# .loc  按`标签`获取数据
# .iloc 按`位置`获取数据

# 用标签获取一行数据
In [8]: df.loc['d']
Out[8]:
A    12
B    13
C    14
D    15
Name: d, dtype: int64

# 获取标量值
In [9]: df.loc['c', 'B']  # 等效于 df.at['c', 'B'] (快速访问标量)
Out[9]: 9

In [10]: df.loc['c', ['B', 'D']]
Out[10]: # pandas.core.series.Series
B     9
D    11
Name: c, dtype: int64

In [11]: df.loc[['b', 'e'], ['B', 'D']]
Out[11]:
    B   D
b   5   7
e  17  19

In [12]: df.loc['d':, ['B', 'D']]
Out[12]:
    B   D
d  13  15
e  17  19
f  21  23

In [13]: df.loc['c':'e', ['B', 'D']]
Out[13]:
    B   D
c   9  11
d  13  15
e  17  19

# 获取标量值
In [14]: df.iloc[1, 3]  # 等效于 df.iat[1, 3] (快速访问标量)
Out[14]: 7

In [15]: df.iloc[1:3, [1, 3]]
Out[15]:
   B   D
b  5   7
c  9  11
```

布尔索引

```py
# 用单列的值选择数据
In [16]: df[df.A > 18]
Out[16]:
    A   B   C   D
f  20  21  22  23

# 选择满足条件的值
In [17]: df[df > 18]
Out[17]:
      A     B     C     D
a   NaN   NaN   NaN   NaN
b   NaN   NaN   NaN   NaN
c   NaN   NaN   NaN   NaN
d   NaN   NaN   NaN   NaN
e   NaN   NaN   NaN  19.0
f  20.0  21.0  22.0  23.0
```

## 4. 缺失值

Pandas 主要用 `np.nan` 表示缺失数据。 计算时，默认不包含空值。

```py
# isna    检测缺失值
# isnull  是 isna 的别名
# notna   检测非缺失值
# notnull 是 notna 的别名
# dropna  删除所有含缺失值的行
# fillna  填充缺失值

In [3]: df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                           [3, 4, np.nan, 1],
                           [np.nan, np.nan, np.nan, 5],
                           [np.nan, 3, np.nan, 4]],
                          columns=list('ABCD'))
In [4]: df
Out[4]:
     A    B   C  D
0  NaN  2.0 NaN  0
1  3.0  4.0 NaN  1
2  NaN  NaN NaN  5
3  NaN  3.0 NaN  4

In [5]: df.isna()
Out[5]:
       A      B     C      D
0   True  False  True  False
1  False  False  True  False
2   True   True  True  False
3   True  False  True  False

In [6]: df.fillna(0)
Out[6]:
     A    B    C  D
0  0.0  2.0  0.0  0
1  3.0  4.0  0.0  1
2  0.0  0.0  0.0  5
3  0.0  3.0  0.0  4
```

## 5. 运算

### 5.1. 字符串方法

Series 的 `str` 属性包含一组字符串处理功能。

```py
# cat        实现元素级的字符串连接操作, 可指定分隔符
# contains   返回表示各字符串是否含有指定模式的布尔型数组
# count      模式的出现次数
# startswith 相当于对每个元素执行 str.startswith(pat)
# endswith   相当于对每个元素执行 str.endswith(pat)
# findall    计算各字符串的模式列表
# get        获取各元素的第 i 个字符
# join       根据制定的分隔符将 Series 中各元素的字符串连接起来
# len        计算各字符串的长度
# upper      相当于 str.upper
# lower      相当于 str.lower
# capitalize 相当于 str.capitalize
# match      根据指定的正则表达式对各个元素执行 re.match
# pad        在字符串的左边、右边或者左右两边添加空白符
# center     相当于 pad(side='both')
# repeat     重复值. 如 s.str.repeat(3) 相当于对各个字符串执行 `x * 3`
# replace    用指定字符串替换找到的模式
# slice      对 Series 中的各个字符串进行子串截取
# split      根据分隔符或正则表达式对字符串进行拆分
# strip      去除空白符, 包括换行符, 相当于 str.strip
# rstrip     相当于 str.rfind
# lstrip     相当于 str.lstrip

In [3]: s = pd.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])

In [4]: s.str.upper()
Out[4]:
0                 LOWER
1              CAPITALS
2    THIS IS A SENTENCE
3              SWAPCASE
dtype: object
```

```py
In [5]: df = pd.DataFrame(np.random.randn(3, 2),
                          columns=[' Column A ', ' Column B '],
                          index=range(3))
In [6]: df
Out[6]:
    Column A    Column B
0   -0.268409    1.609117
1    1.062621    0.966755
2   -0.397396   -0.023987

# df.columns 是 Index 对象, 可以使用 .str 访问器
In [7]: df.columns.str.strip()
Out[7]: Index(['Column A', 'Column B'], dtype='object')

In [8]: df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
In [9]: df
Out[9]:
   column_a  column_b
0 -0.268409  1.609117
1  1.062621  0.966755
2 -0.397396 -0.023987
```

### 5.2. 统计

```py
# max      最大值
# min      最小值
# mean     均值
# ptp      极差
# median   中位数
# std      标准差
# var      方差
# cov      协方差
# sem      标准误差
# mode     众数
# skem     样本偏度
# kurt     样本蜂度
# quantile 四分位数
# count    非空值数目
# describe 描述统计
# mad      平均绝对离差
```

## 6. 合并 Merge

### 6.1. 结合 Concat

```py
In [3]: s1 = pd.Series(['a', 'b'])
In [4]: s2 = pd.Series(['c', 'd'])

In [5]: pd.concat([s1, s2])
Out[5]: # pandas.core.series.Series
0    a
1    b
0    c
1    d
dtype: object
```

```py
In [3]: df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
In [4]: df1
Out[4]:
  letter  number
0      a       1
1      b       2

In [5]: df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
In [6]: df2
Out[6]:
  letter  number
0      c       3
1      d       4

In [7]: pd.concat([df1, df2])
Out[7]: # pandas.core.frame.DataFrame
  letter  number
0      a       1
1      b       2
0      c       3
1      d       4
```

### 6.2. 连接 join

SQL 风格的合并

```py
In [3]: left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
In [4]: left
Out[4]:
   key  lval
0  foo     1
1  foo     2

In [5]: right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
In [6]: right
Out[6]:
   key  rval
0  foo     4
1  foo     5

In [7]: pd.merge(left, right, on='key')
Out[7]:
   key  lval  rval
0  foo     1     4
1  foo     1     5
2  foo     2     4
3  foo     2     5
```

```py
In [3]: left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
In [4]: left
Out[4]:
   key  lval
0  foo     1
1  bar     2

In [5]: right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
In [6]: right
Out[6]:
   key  rval
0  foo     4
1  bar     5

In [7]: pd.merge(left, right, on='key')
Out[7]:
   key  lval  rval
0  foo     1     4
1  bar     2     5
```

### 6.3. 追加 Append

为 DataFrame 追加行

```py
In [3]: df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
In [4]: df1
Out[4]:
   A  B
0  1  2
1  3  4

In [5]: df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
In [6]: df2
Out[6]:
   A  B
0  5  6
1  7  8

In [7]: df1.append(df2)
Out[7]:
   A  B
0  1  2
1  3  4
0  5  6
1  7  8
```

## 7. 分组 Grouping

```py
In [3]: df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                                 'foo', 'bar', 'foo', 'foo'],
                           'B': ['one', 'one', 'two', 'three',
                                 'two', 'two', 'one', 'three'],
                           'C': np.random.randn(8),
                           'D': np.random.randn(8)})
In [4]: df
Out[4]:
     A      B         C         D
0  foo    one  1.237254  0.850269
1  bar    one -0.753975 -0.805385
2  foo    two  0.011511  1.316811
3  bar  three  1.701065 -0.751763
4  foo    two -1.895226 -0.818049
5  bar    two  3.093597 -0.309560
6  foo    one  0.987922  0.856264
7  foo  three -0.676863 -1.590671

# 计算每组的汇总数据
In [5]: df.groupby('A').sum()
Out[5]:
            C         D
A
bar  4.040687 -1.866708
foo -0.335403  0.614623

In [6]: df.groupby(['A', 'B']).sum()
Out[6]:
                  C         D
A   B
bar one   -0.753975 -0.805385
    three  1.701065 -0.751763
    two    3.093597 -0.309560
foo one    2.225176  1.706532
    three -0.676863 -1.590671
    two   -1.883716  0.498762
```

## 8. 输入和输出

```py
# 写入 CSV 文件
df.to_csv('foo.csv')

# 读取 CSV 文件数据
pd.read_csv('foo.csv')
```
