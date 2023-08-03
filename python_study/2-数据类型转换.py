"""
python中数据类型转换分为两种:
    隐式类型转换-自动完成
    显式类型转换-需要使用类型函数进行转换
"""
# 隐式类型转换
a = 1
b = 1.2
c = a + b
print('a的类型:', type(a))
print('b的类型:', type(b))
print('c的类型:', type(c))
print('c的结果:', c)
"""
结果:
    a的类型: <class 'int'>
    b的类型: <class 'float'>
    c的类型: <class 'float'>
    c的结果: 2.2
"""
# 显式类型转换
a = 1
b = "3"
# 错误代码 c = a + b
# 正确代码
c = a + int(b)
# 使用函数int将其字符串类型转换为整数类型
