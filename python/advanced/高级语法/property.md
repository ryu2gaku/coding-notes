# property 属性

## 1. 使用装饰器实现

```py
class Person:
    def __init__(self, name):
        self._name = name

    # getter 方法
    @property
    def name(self):
        print('Getting name')
        return self._name

    # setter 方法
    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    # deleter 方法
    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name


if __name__ == '__main__':
    p = Person('Adam')
    print('The name is:', p.name)  # 执行 @property 修饰的 name 方法

    p.name = 'John'  # 执行 @name.setter 修饰的 name 方法

    del p.name  # 执行 @name.deleter 修饰的 name 方法

# 结果:
# Getting name
# The name is: Adam
# Setting name to John
# Deleting name
```

## 2. 使用 property 函数实现

```py
class Person:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print('Getting name')
        return self._name

    def setName(self, value):
        print('Setting name to ' + value)
        self._name = value

    def delName(self):
        print('Deleting name')
        del self._name

    # Set property to use getName, setName
    # and delName methods
    name = property(getName, setName, delName, 'Name property')


if __name__ == '__main__':
    p = Person('Adam')
    print(p.name)

    p.name = 'John'

    del p.name

# 结果:
# Getting name
# Adam
# Setting name to John
# Deleting name
```

```py
"""
property(fget=None, fset=None, fdel=None, doc=None)
"""
```
