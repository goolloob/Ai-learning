# 列表推导式
a = [1, 2, 3, 4, 5]
b = []
[b.append(i) for i in a if i % 2]
print(b)

"""
解
    b.append(i) 将for i in a if i % 2得到的数据添加到b这个空列表当中
"""
# 其余推导式和列表推导式大致相同
