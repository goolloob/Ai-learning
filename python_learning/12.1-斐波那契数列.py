"""
波那契数列的前两个数字是0和1,之后的每个数字都是前面两个数字的和
"""
import time


def numbers():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


x = numbers()
while True:
    print(next(x))
    time.sleep(1)
