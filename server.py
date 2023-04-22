import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:    # 第一个参数表示使用的是IPv4的地址家族，第二个表示使用的是TCP协议
    server.bind(("0.0.0.0", 1234))    # 绑定的网卡IP和端口，全0表示可以使用主机上的任意网卡
    server.listen()    # 开启监听
    client, addr = server.accept()    # 接收来自客户端的连接
    with client:
        print(addr, "connected")

        while True:    # 永真循环，一直监听
            data = client.recv(1024)    # 一次性接受数据的最大长度（字节）
            if not data:
                break
            client.sendall(data)    # 将数据原封不动回传给客户端
