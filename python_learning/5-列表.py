"""
序列是 Python 中最基本的数据结构。
序列中的每个值都有对应的位置值,称之为索引,第一个索引是0,第二个索引是1,依此类推。
Python 有 6 个序列的内置类型，但最常见的是列表和元组。
列表都可以进行的操作包括索引，切片，加，乘，检查成员。
此外,Python 已经内置确定序列的长度以及确定最大和最小的元素的方法。
列表是最常用的 Python 数据类型，它可以作为一个方括号内的逗号分隔值出现。
列表的数据项不需要具有相同的类型
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
"""

import operator

# 访问列表中的值
a = ['hello', 'apple', 'start']
print(a[0])
print(a[1])
print(a[2])

# 更新列表append()
a.append('sss')
print(a)  # ['hello', 'apple', 'start', 'sss']

# 删除列表内元素del
del a[2]
print(a)  # ['hello', 'apple', 'sss']

# 列表相加
b = ['find', 'append', 'del']
print(a+b)  # ['hello', 'apple', 'sss', 'find', 'append', 'del']

# 列表比较
# 列表比较需要operator模块
# import operator
a = [1, 2]
b = [1, 3]
c = [1, 2]
print(operator.eq(a, b))  # False
print(operator.eq(b, c))  # False
print(operator.eq(a, c))  # True

# 获取列表元素个数len()
print(len(a))  # 2

# 获取列表最大值max()
print(max(a))  # 2

# 获取列表最小值min()
print(min(a))  # 1

a.append('123')  # 在末尾添加对象
a.count(1)  # 统计某个元素在列表内出现的次数
a.extend(b[0:1])  # 在列表末尾一次性追加另一个序列中的多个值
a.index(2)  # 从列表中找出第一个匹配的索引的位置
a.insert(2, 'aaa')  # 在对相处插入元素
a.pop(-2)  # 移除列表中的元素,并且返回该元素的值
a.remove('aaa')  # 移除列表中某个值的第一个匹配项
a.reverse()  # 反向列表中的元素
a.clear()  # 清空列表
a.copy()  # 复制列表

a = [5, 4, 2, 8, 1]
a.sort()  # sort() 排序-升序
a.sort(reverse=True)  # 降序
print(a)  # [1, 2, 4, 5, 8]
c = sorted(a)  # sorted()返回新的列表
print(a, c)
