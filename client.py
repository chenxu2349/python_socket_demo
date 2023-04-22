import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("127.0.0.1", 1234))    # 连接服务器
    client.sendall(b"Hello, server!")    # 加b将字符串转字节序列
    data = client.recv(1024)
    print("Received: ", repr(data))    # repr将字节序列转为字符串

