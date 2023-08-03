# 面向对象
"""
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
方法:类中定义的函数。
类变量:类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员:类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写:如果从父类继承的方法不能满足子类的需求,可以对其进行改写,这个过程叫方法的覆盖(override),也称为方法的重写。
局部变量:定义在方法中的变量,只作用于当前实例的类。
实例变量:在类的声明中,属性是用变量来表示的,这种变量就称为实例变量,实例变量就是一个用 self 修饰的变量。
继承:即一个派生类(derived class)继承基类(base class)的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如,有这样一个设计:一个Dog类型的对象派生自Animal类,这是模拟"是一个(is-a)"关系(例图,Dog是一个Animal)。
实例化:创建一个类的实例,类的具体对象。
对象:通过类定义的数据结构实例。对象包括两个数据成员(类变量和实例变量)和方法。
"""

# 用法1 -简单用法
# class OPK:
#     a = 123
#     def abc(self):
#         return  456
    
# x = OPK()
# print(x.a)
# print(x.abc())

# 用法2 __init__方法
"""
_init__ 方法是Python中的一个特殊方法,也称为构造函数。
当创建类的实例(对象)时,__init__ 方法会被自动调用，用于初始化对象的属性。
在类中定义 __init__ 方法时，第一个参数通常是 self,它表示正在创建的实例对象本身。
接着，你可以在 __init__ 方法中定义其他参数，用于初始化对象的属性。
这些参数在创建对象时传递给 __init__ 方法
"""
# class Myclass:
#     def __init__(self,name):
#         self.name = name

#     def print_name(self):
#         print(self.name)

# x = Myclass('noah')
# x.print_name()


# # 用法3 # 私有属性 __work为私有属性
# class Myclass:
#     name = 'noah'
#     age = 18
#     __work = 'sack' # 外部无法访问
#     def __init__(self):
#         self.name = Myclass.name
#         self.age = Myclass.age
#         self.__work = Myclass.__work

#     def say_self(self):
#         print(self.name,self.age,self.__work)


# x = Myclass()
# x.say_self()


# 用法4 类的继承
# 子类（派生类 DerivedClassName）会继承父类（基类 BaseClassName）的属性和方法
# class A:
#     def foo(self):
#         print('A')

# class B(A):
#     def foo(self):
#         print('B')
#         super().foo()  # 调用父类的方法 B-A

# class C(A):
#     def foo(self):
#         print('C')
#         super().foo()  # 调用父类的方法 C-A

# class D(B,C):
#     def foo(self):
#         print('D')
#         super().foo()  # 调用父类的方法 D-B,C

# x = D()
# x.foo()
"""
super()函数:一个内置函数,在Python中用于调用父类的方法。
它提供了一种简单的方式，让子类能够调用继承的父类方法，从而实现方法的继承和重用。
在多继承的情况下,super() 函数特别有用，
因为它能够按照 Method Resolution Order (MRO) 的顺序找到下一个类，并调用该类的方法，确保了方法调用的顺序是符合预期的
#
MRO概念:
MRO(Method Resolution Order)是指在多继承的情况下,Python 解释器决定调用方法的顺序。
当一个类继承自多个父类时,可能会出现方法名重复的情况,MRO 用于解决这种命名冲突，确定方法调用的顺序。

Python 使用 C3 线性化算法来计算 MRO,该算法通过一系列规则来确定方法解析的顺序，以保证合理的继承顺序。以下是 C3 线性化算法的几个关键规则：
    1.线性化的第一个原则是从左到右扫描所有父类，保持原来的顺序。这意味着在类定义中，继承的第一个类会先于后面的类进行搜索。
    2.如果有多个父类，且它们都没有基类，那么它们的顺序不会改变。
    3.如果有多个父类，且它们都有相同的基类，那么基类只会出现在 MRO 中的第一个位置。
    4.如果有多个父类，且它们之间存在复杂的继承关系,Python 会根据 C3 算法来计算 MRO。

为了更好地理解 MRO,可以使用 super() 函数来调用父类的方法。super() 函数按照 MRO 的顺序找到下一个类，并调用该类的方法。这样确保了在多继承的情况下，方法调用的顺序是符合预期的
"""


"""
类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方
"""