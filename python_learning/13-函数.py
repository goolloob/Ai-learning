"""
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
函数能提高应用的模块性,和代码的重复利用率。你已经知道Python提供了许多内建函数,比如print()。
但你也可以自己创建函数，这被叫做用户自定义函数

你可以定义一个由自己想要功能的函数，以下是简单的规则：
    函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
    任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号 : 起始，并且缩进。
    return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。
"""


print("普通函数")
# 普通函数


def sum(a, b):
    if a > b:
        return a
    else:
        return b
# #调用


x = sum(a=5, b=4)  # 着用也属于关键字参数,还可以在定义函数时，使用默认参数直接在函数上定义其参数内容
print(x)


print("函数调用")
# 函数之间的调用


def kfc(a, b):
    if a > b:
        return a
    else:
        return b


def zbb(a, b, c):
    x = kfc(a, b)
    if x > c:
        print(x)
    else:
        print(c)


zbb(5, 4, 10)
"""
上述列子,在其zbb中调用函数kfc,因其kfc使用return返回值,而不是print输出值所以其函数有值.
"""


print("不定长函数单*号")


def ckl(a, *values):  # 单个*号会以元组的方式传入其中
    print("输出内容:", end="")
    print(a, end=",")
    for i in values:
        print(i, end=",")
        print()


ckl(123, 4, 5, 6, 7)

print("不定长函数双**号")


def cpp(a, **values):  # 双**号会以字典形式传入其中
    print(a, values)


cpp(1, x=1, name='noah')  # 1 {'x': 1, 'name': 'noah'}


print("结合使用")


def coo(*args, **kwargs):  # 其可以包括所有
    print(args, kwargs)


coo(1, 2, 3, p=1, name='noah')  # (1, 2, 3) {'p': 1, 'name': 'noah'}
