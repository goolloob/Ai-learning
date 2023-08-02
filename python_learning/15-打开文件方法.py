"""
open() 方法
Python open() 方法用于打开一个文件，并返回文件对象。
在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)
"""
# open(file,mode='r')
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
"""
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符
"""

"""
mode参数
t	文本模式 (默认)。
x	写模式，新建一个文件，如果该文件已存在则会报错。
b	二进制模式。
+	打开一个文件进行更新(可读可写)。
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，
    创建新文件。一般用于非文本文件如图片等。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，
    创建新文件。一般用于非文本文件如图片等。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。
    如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
"""


"""
file.close()
关闭文件。关闭后文件不能再进行读写操作。

file.flush()
刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。

file.fileno()
返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。

file.isatty()
如果文件连接到一个终端设备返回 True,否则返回 False。

file.next()
Python 3 中的 File 对象不支持 next() 方法。
返回文件下一行。

file.read([size])
从文件读取指定的字节数，如果未给定或为负则读取所有。

file.readline([size])
读取整行，包括 "\n" 字符。

file.readlines([sizeint])
读取所有行并返回列表,若给定sizeint>0,返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。

file.seek(offset[, whence])
移动文件读取指针到指定位置

file.tell()
返回文件当前位置。

file.truncate([size])
从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 windows 
系统下的换行代表2个字符大小。

file.write(str)
将字符串写入文件，返回的是写入的字符长度。

file.writelines(sequence)
向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符
"""
# 读
a = open(r'D:\data\Desktop\Ai-learning\python_learning\test', mode='r')
b = a.read()
print(b)
a.close()
# 写（会删除原有内容）
a = open(r'D:\data\Desktop\Ai-learning\python_learning\test', mode='r+')
b = a.read()
print(b)
x = '222'
a.write(x)
b = a.read()
print(b)


# 常用语句
file = r'D:\data\Desktop\Ai-learning\python_learning\test'
with open(file,mode='r') as file:
    pass