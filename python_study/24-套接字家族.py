"""
套接字家族（Socket Family）是一个用于网络通信的分类系统，它定义了不同类型的套接字，以适应不同的网络通信场景。在网络编程中，我们使用套接字来建立网络连接、进行数据传输和通信。不同的套接字家族支持不同的网络协议和通信方式。

以下是几个常见的套接字家族：

AF_INET（IPv4）：这是最常见的套接字家族，用于 Internet 协议版本 4（IPv4）的网络通信。它支持使用 IPv4 地址和端口号来建立连接，通常用于 TCP 和 UDP 协议的通信。

AF_INET6（IPv6）：这个套接字家族用于 Internet 协议版本 6（IPv6）的网络通信。与 AF_INET 类似，但支持使用 IPv6 地址和端口号。

AF_UNIX（Unix Domain Socket）：这是一种在同一台机器上进行进程间通信的套接字家族。它不需要 IP 地址和端口号，而是使用文件系统路径来建立连接，常用于实现本地的进程间通信。

AF_NETLINK（Netlink）：这个套接字家族用于 Linux 内核与用户空间程序之间的通信。它提供了一种用于在用户空间和内核空间交换消息的机制。

AF_BLUETOOTH（Bluetooth）：这个套接字家族用于蓝牙设备之间的通信，支持蓝牙协议。

在 Python 中，我们可以通过 socket 模块来创建套接字，并选择特定的套接字家族来实现网络通信。例如，使用 socket.AF_INET 来创建 IPv4 套接字，使用 socket.AF_INET6 来创建 IPv6 套接字，使用 socket.AF_UNIX 来创建 Unix Domain Socket 套接字等。
"""
"""
除了 socket.SOCK_STREAM 用于创建 TCP 套接字外，socket 模块还支持其他类型的套接字用于不同的传输需求。以下是一些常用的套接字类型：

socket.SOCK_DGRAM：这个类型的套接字用于创建 UDP（用户数据报协议）套接字。UDP 是一种无连接、不可靠的传输协议，适用于低延迟和实时性要求较高的场景，但不保证数据的可靠性。
示例代码：

python
Copy code
import socket

# 创建一个 UDP 套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.SOCK_RAW：这个类型的套接字用于创建原始套接字，可以访问网络层数据包，适用于底层网络数据包的处理，但通常需要管理员权限。
示例代码：

python
Copy code
import socket

# 创建一个原始套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
socket.SOCK_SEQPACKET：这个类型的套接字用于创建可靠的数据包传输套接字，每个数据包都有固定的顺序。
示例代码：

python
Copy code
import socket

# 创建一个可靠数据包传输套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_SEQPACKET)
socket.SOCK_RDM：这个类型的套接字提供一种可靠的数据报传输，但不保证数据包的顺序。
示例代码：

python
Copy code
import socket

# 创建一个可靠数据报传输套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_RDM)
需要根据实际需求选择合适的套接字类型。例如，TCP 套接字（socket.SOCK_STREAM）适用于可靠数据传输，UDP 套接字（socket.SOCK_DGRAM）适用于低延迟和实时性要求的场景，而原始套接字（socket.SOCK_RAW）适用于处理底层网络数据包。
"""
