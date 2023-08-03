import socket


def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))
    # s.connect_ex()	connect()函数的扩展版本,出错时返回出错码,而不是抛出异常

    while True:
        message = input("请输入要发送的消息（输入 'exit' 结束）: ")
        if message == "exit":
            break
        client_socket.send(message.encode(
        ))  # 发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小

    client_socket.close()


if __name__ == "__main__":
    client()
