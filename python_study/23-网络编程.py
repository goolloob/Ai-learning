# 网络编程需要使用到socket模块
import socket
"""
Socket又称"套接字"，应用程序通常通过"套接字"向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯
"""


# 服务端
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 套接字家族
    server_socket.bind(
        ("localhost",
         12345))  # 绑定地址（host,port）到套接字， 在AF_INET下,以元组（host,port）的形式表示地址
    server_socket.listen(
        1)  # 开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了

    print("服务器已启动，等待连接...")
    conn, addr = server_socket.accept()  # 被动接受TCP客户端连接,(阻塞式)等待连接的到来
    """
    s.recvfrom()	接收UDP数据,与recv()类似,但返回值是(data,address)。其中data是包含接收数据的字符串,address是发送数据的套接字地址。
    s.sendto()	发送UDP数据,将数据发送到套接字,address是形式为(ipaddr,port)的元组，指定远程地址。返回值是发送的字节数
    """
    print(f"已连接客户端：{addr}")

    while True:
        data = conn.recv(
            1024
        )  # 接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。
        if not data:
            break
        print(f"接收到数据：{data.decode()}")

    conn.close()  # 关闭套接字
    server_socket.close()


if __name__ == "__main__":
    server()
