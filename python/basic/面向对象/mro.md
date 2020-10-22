# MRO

MRO（Method Resolution Order 方法解析顺序）

对于支持继承的编程语言来说，其方法（属性）可能定义在当前类，也可能来自于基类，所以在方法调用时就需要对当前类和基类进行搜索以确定方法所在的位置，而搜索的顺序就是所谓的 MRO。

对于只支持单继承的语言来说，MRO 一般比较简单，而对于 Python 这种支持多继承的语言来说，MRO 就复杂很多。Python 2.3 以后采用了 C3 方法来确定方法解析顺序。

通过类的 `__mro__` 属性可以直接获取类的 MRO

```py
class A(object):
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.__mro__)  # D → B → C → A → object

# 结果:
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```